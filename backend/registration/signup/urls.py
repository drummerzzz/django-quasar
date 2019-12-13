from django.urls import path
from signup.views.custom import ThemeChoiceView, CustomizeView, PlanChoiceView, CreateAccountView
from signup.views.simple import SimplePlanChoiceView, SimpleCreateAccountView

app_name = "signup"

urlpatterns = [
    #Simple
    path('simple/plan-choice/', SimplePlanChoiceView.as_view(), name="simple_plan_choice"),
    path('simple/create/', SimpleCreateAccountView.as_view(), name="simple_create_account"),
    #Custom
    path('theme-choice/', ThemeChoiceView.as_view(), name="theme_choice"),
    path('customize/', CustomizeView.as_view(), name="customize"),
    path('plan-choice/', PlanChoiceView.as_view(), name="plan_choice"),
    path('create/', CreateAccountView.as_view(), name="create_account"),
   
]
