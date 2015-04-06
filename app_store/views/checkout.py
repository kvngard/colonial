from app_store.views.index import calculate_total, sort_items, reserve_percent
from app_store.storeforms import Address_Form, Credit_Card_Form
from django.contrib.auth.decorators import login_required
from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from app_store.cart import get_cart
import app_base.models as mod
from . import templater
import datetime

@view_function
@login_required(redirect_field_name='/app_store/')
def process_request(request):

    params = {}

    total = calculate_total(request)

    address_form = Address_Form()
    credit_card_form = Credit_Card_Form()
    params['total'] = total

    if request.method == 'POST':

        address_form = Address_Form(request.POST)
        credit_card_form = Credit_Card_Form(request.POST, total=total, user=request.user)

        if address_form.is_valid() and credit_card_form.is_valid():
            a = address_form.save()
            t = create_transaction(request, credit_card_form.resp, total, a)
            return HttpResponseRedirect('/app_store/checkout.receipt/{}'.format(t.id))


    params['address_form'] = address_form
    params['credit_card_form'] = credit_card_form

    return templater.render_to_response(request, 'checkout.html', params)


@view_function
@login_required(redirect_field_name='/app_store/')
def receipt(request):

    params = {}
    t = mod.Transaction.objects.get(id=request.urlparams[0])
    paid = sum([ p.amount for p in t.payment_set.all() ])

    params['t'] = t
    params['paid'] = paid

    emailbody = templater.render(request, 'receipt_email.html', params)
    print(request.user.email)
    print(send_mail(
        'Colonial Heritage Foundation - Receipt',
        emailbody,
        'chfsite@gmail.com',
        [request.user.email],
        html_message=emailbody,
        fail_silently=False
    ))

    return templater.render_to_response(request, 'receipt.html', params)


def create_transaction(request, response, amount, address):

    cart = get_cart(request)

    t = mod.Transaction()
    t.ships_to = address
    t.customer = request.user
    t.save()

    p = mod.Payment()
    p.amount = amount
    p.transaction = t
    p.charge_id = response['ID']
    p.save()

    for r in cart.rentals.values():
        r.transaction = t
        r.save()

        i = mod.Store_Item.objects.get(id=r.rental_item.id)
        i.quantity_on_hand -= 1
        i.save()

    for s in cart.sales.values():
        s.transaction = t
        s.save()

        i = mod.Store_Item.objects.get(id=s.sale_item.id)
        i.quantity_on_hand -= s.quantity
        i.save()

    del request.session['shopping_cart']

    return t