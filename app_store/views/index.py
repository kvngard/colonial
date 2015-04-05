from django.contrib.auth.decorators import login_required
from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from django.db.models import Q
import app_base.models as mod
from decimal import Decimal
from . import templater

reserve_percent = Decimal('0.20')
checkout_percent = Decimal('0.80')


def get_items():

    try:
        items = mod.Store_Item.objects.all().order_by('name')
    except mod.Store_Item.DoesNotExist:
        return HttpResponseRedirect('/')

    return items


def sort_items(items):

    sorted_items = []

    for item in items:
        try:
            item = mod.Rental_Item.objects.get(
                id=item.id, quantity_on_hand__gt=0)
        except mod.Rental_Item.DoesNotExist:
            try:
                item = mod.Custom_Item.objects.get(id=item.id)
            except mod.Custom_Item.DoesNotExist:
                try:
                    item = mod.Sale_Item.objects.get(
                        id=item.id, quantity_on_hand__gt=0)
                except mod.Sale_Item.DoesNotExist:
                    continue
        sorted_items.append(item)

    return sorted_items


def calculate_total(request):

    cart = request.session['shopping_cart']

    items = mod.Store_Item.objects.filter(id__in=cart.keys())
    items = sort_items(items)

    total = 0

    for item in items:

        if item.__class__.__name__ is "Sale_Item" or item.__class__.__name__ is "Custom_Item":
            total += round(cart[str(item.id)]['quantity'] * item.price, 2)
        elif item.__class__.__name__ is "Rental_Item":
            total += round(cart[str(item.id)]['duration'] * item.price_per_day * reserve_percent, 2)

    return total


@view_function
def process_request(request):
    params = {}

    items = get_items()
    items = sort_items(items)

    params['items'] = items

    return templater.render_to_response(request, 'default_display.html', params)


@view_function
def search(request):
    params = {}
    search_parameter = request.REQUEST.get('p')

    try:
        items = get_items().filter(
            Q(name__icontains=search_parameter) |
            Q(description__icontains=search_parameter))
    except mod.Store_Item.DoesNotExist:
        return HttpResponseRedirect('/')

    items = sort_items(items)
    params['items'] = items

    return templater.render_to_response(request, 'search_display.html', params)


def check_and_intialize_cart(request):
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}
    return


@view_function
def show_cart(request, items=None):
    params = {}
    check_and_intialize_cart(request)
    cart = request.session['shopping_cart']

    items = mod.Store_Item.objects.filter(
            id__in=cart.keys())
    items = sort_items(items)

    rentals = [ i for i in items if i.__class__.__name__ is "Rental_Item" ]
    sales = [ i for i in items if i.__class__.__name__ is "Sale_Item"
                                  or i.__class__.__name__ is "Custom_Item" ]

    params['rentals'] = rentals
    params['sales'] = sales
    params['total'] = calculate_total(request)
    params['cart'] = cart
    params['reserve_percent'] = reserve_percent
    params['checkout_percent'] = checkout_percent

    return templater.render_to_response(request, 'cart.html', params)


@view_function
def add_to_cart(request):
    item_id = request.REQUEST.get('i')
    duration = request.REQUEST.get('d')
    quantity = request.REQUEST.get('q')

    if quantity is None:
        quantity = 1

    # If there is no shopping_cart session variable, make it!
    check_and_intialize_cart(request)

    cart = request.session['shopping_cart']

    if item_id in cart.keys():
        cart[item_id]['quantity'] = int(cart[item_id]) + int(quantity)
    else:
        cart[item_id] = {}
        cart[item_id]['quantity'] = int(quantity)

    if duration != '':
        cart[item_id]['duration'] = int(duration)

    # Save session variable changes
    request.session.modified = True

    items = mod.Store_Item.objects.filter(id__in=cart.keys())

    return show_cart(request, items)


@view_function
def delete_from_cart(request):

    params = {}
    cart = request.session['shopping_cart']
    item_id = request.REQUEST.get('i')

    del cart[str(item_id)]
    request.session.modified = True

    return show_cart(request)

