from django import template
from decimal import Decimal
from descontos.cupom_helper import inteiro_to_decimal, aplicar_desconto

register = template.Library()


@register.simple_tag
def get_price(plan, installments=False, cupom=None):
    price = plan.amount_cents
    if plan.installments > 1 and installments:
        price = plan.installments_amount_cents / plan.installments

    if cupom:
        price = aplicar_desconto(price, cupom)
    price = inteiro_to_decimal(price)
    return "R$ {}".format(price).replace('.', ',')


@register.simple_tag
def get_price_publication(plan, cupom=None):
    price = plan.amount_cents
    if cupom: 
        price = aplicar_desconto(price, cupom)
    price = (inteiro_to_decimal(price) / plan.number_publications / plan.interval) * 100
    price = inteiro_to_decimal(price)
    return "R$ {}".format(price).replace('.', ',')
