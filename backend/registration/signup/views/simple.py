from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from posts.models import Theme, Color, ColorfulPost, Post
from payments.models import Plan
from descontos.cupom_helper import cupom_exists
from users.forms import PreCustomerForm, CustomerForm, SimpleSignupForm
from users.models import Customer
from payments.iugu_helper import create_account_iugu
from posts.tasks import create_free_post


# class SimpleThemeChoiceView(TemplateView):
#     template_name = "signup/theme_choices.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         self.request.session['theme'] = None
#         customer = self.request.session.get('customer', None)
#         if not customer:
#             self.request.session['customer'] = None
#         context["themes"] = Theme.objects.all()
#         return context


# class SimpleCustomizeView(View):
#     template_name = "signup/customize.html"

#     def dispatch(self, request, *args, **kwargs):
#         theme = self.request.GET.get('theme', None)
#         color = self.request.GET.get('color', None)
#         self.customer = self.request.session.get('customer', None)
#         self.customer = Customer.objects.filter(pk=self.customer)
#         if self.customer.exists():
#             self.customer = self.customer.first()

#         self.color = Color.objects.filter(hexadecimal=color)
#         if self.color.exists():
#             self.color = self.color.first()
#         else:
#             color = request.session.get('color', None)
#             self.color = Color.objects.filter(hexadecimal=color).first() 

#         self.theme = Theme.objects.filter(name=theme)
#         if self.theme.exists():
#             self.theme = self.theme.first()
#             self.request.session['theme'] = theme
#             return super().dispatch(request, *args, **kwargs)
#         return redirect(reverse_lazy('signup:theme_choice'))

#     def get(self, request, *args, **kwargs):
#         context = {}
#         context["colors"] = Color.objects.all()
#         if not self.color:
#             self.color = context["colors"].first()
#         context["color"] = self.color
#         self.request.session['color'] = self.color.hexadecimal
#         free_post = self.theme.free_post
#         posts = ColorfulPost.objects.filter(
#             post_origin__theme=self.theme, color=self.color
#         ).select_related()
#         context['posts'] = posts
#         context['post_free'] = posts.filter(
#             post_origin__pk=free_post.pk).first()
#         context['form'] = PreCustomerForm()
#         context['theme'] = self.theme.name
#         context['form'] = PreCustomerForm()
#         if self.customer:
#             context['customer'] = self.customer
#         footer_error = request.GET.get("error", None)
#         if footer_error == "invalid-size":
#             context['footer_error'] = True
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):

#         color = request.POST.get('color', None)
#         customer = request.session.get('customer', None)
#         if color:
#             color = Color.objects.filter(hexadecimal=color).first()
#         else:
#             color = Color.objects.first()
#         if customer:
#             customer = Customer.objects.filter(pk=customer).first()
#             form = PreCustomerForm(
#                 request.POST, request.FILES, instance=customer)
#         else:
#             form = PreCustomerForm(request.POST, request.FILES)

#         url = reverse_lazy('signup:customize') + \
#             "?theme={}".format(self.theme.name) + "&color={}".format(color.hexadecimal)

#         if form.is_valid():
#             customer = form.save(commit=False)
#             customer.theme = self.theme
#             customer.color = color
#             customer.is_active = False
#             customer.save()
#             request.session['customer'] = customer.pk
#             next_tap = request.POST.get('next', None)
#             if next_tap in "True": 
#                 return redirect(reverse_lazy('signup:plan_choice'))
#         else:
#             url = url + "&error=invalid-size"

#         return redirect(url)


class SimplePlanChoiceView(View):
    template_name = "signup/plan_choice.html"
    context = {}

    def dispatch(self, request, *args, **kwargs):
        self.random = request.GET.get('random', "True")
        if not self.random in ["True", "False"]:
            self.random = True
        code = request.GET.get('cupom', None)
        if code:
            context_cupom = cupom_exists(code)
            cupom = context_cupom['result']
            msg = context_cupom['msg']
            if cupom:
                self.context['code'] = cupom.codigo
                self.context["msg"] = msg
                self.context['cupom'] = cupom
            elif code and not cupom:
                self.context['code'] = code
                self.context["msg"] = msg
            else:
                self.context['code'] = ""
        self.context['simple_url'] = reverse_lazy('signup:simple_plan_choice')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        plans = Plan.objects.filter(random=self.random)
        self.context['plans30'] = plans.filter(
            number_publications=30).order_by('amount_cents')
        self.context['plans15'] = plans.filter(
            number_publications=15).order_by('amount_cents')
        self.context['random'] = str(self.random)
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        customer = request.session.get('customer', None)
        code = request.POST.get('cupom', None)
        plan = request.POST.get('plan', None)
        plan = Plan.objects.filter(pk=plan).first()
        if plan:
            if not customer:
                customer = Customer.objects.create(
                    plan=plan.identifier,
                    is_active=False,
                    cupom_code=code
                )
                request.session['customer'] = customer.pk
            else:
                customer = Customer.objects.filter(pk=customer).first()
            if customer:
                customer.plan = plan.identifier
                customer.cupom_code = code
                customer.save()
                request.session['customer'] = customer.pk
                return redirect(reverse_lazy('signup:simple_create_account'))
        return redirect(reverse_lazy('signup:simple_plan_choice'))


class SimpleCreateAccountView(View):
    template_name = "signup/create_account.html"
    context = {}

    def dispatch(self, request, *args, **kwargs):      
        self.customer = self.request.session.get('customer', None)
        if self.customer is None:
            return redirect(reverse_lazy('signup:simple_plan_choice'))
        self.customer = Customer.objects.filter(pk=self.customer).first()
        self.context['simple_url'] = True
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.context['form'] = SimpleSignupForm()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = SimpleSignupForm(request.POST, instance=self.customer)
        if form.is_valid():
            customer = form.save(commit=False)
            password = request.POST['password2']
            customer.set_password(password)
            customer.is_active = True
            customer.iugu_account_id = create_account_iugu(customer)
            customer.save()
            user = authenticate(
                request, username=customer.email, password=password)
            auth_login(request, user)
            request.session['customer'] = None
            # if customer.has_preferences_defined() and not customer.free_post_used:
                # create_free_post.delay(customer.pk)
            if customer.plan_status is None:
                return redirect(reverse_lazy('dashboard:payment'))
            return redirect(reverse_lazy('users:redirect'))
        self.context['form'] = form
        return render(request, self.template_name, self.context)
