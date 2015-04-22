from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from app_store.cart import get_cart, save_cart
from django.db.models import Q
import app_base.models as mod
from decimal import Decimal
from . import templater

reserve_percent = Decimal('0.20')
checkout_percent = Decimal('0.80')


def get_items(items=None):
    '''
        method for getting items
    '''

    if items is None:
        try:
            items = mod.Store_Item.objects.all().order_by('name')
        except mod.Store_Item.DoesNotExist:
            return HttpResponseRedirect('/')

    return items


def sort_items(items):
    '''
        method for sorting items
    '''
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

    cart = get_cart(request)

    return cart.get_checkout_total()


@view_function
def process_request(request):
    '''
        Default method for displaying all of the items in the store.
    '''
    params = {}

    items = get_items()
    items = sort_items(items)

    params['items'] = items

    return templater.render_to_response(request, 'default_display.html', params)


@view_function
def search(request):
    '''
        method for searching
    '''
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


@view_function
def filter(request):
    '''
        method for filtering
    '''
    params = {}
    items = []
    custom = request.REQUEST.get('c')
    sales = request.REQUEST.get('s')
    rentals = request.REQUEST.get('r')

    # The boolean values are strange because the checkboxes pass lower-case
    # boolean strings.

    if custom == 'false' and sales == 'false' and rentals == 'false':
        params['items'] = sort_items(get_items())
    else:
        if custom == 'true':
            items.extend(list(mod.Custom_Item.objects.all()))
        if sales == 'true':
            items.extend(list(mod.Sale_Item.objects.all()))
        if rentals == 'true':
            items.extend(list(mod.Rental_Item.objects.all()))

        print(items)
        params['items'] = sort_items(items)

    return templater.render_to_response(request, 'search_display.html', params)


@view_function
def show_cart(request):
    '''
        method for showing the cart
    '''
    params = {}
    cart = get_cart(request)

    params['rentals'] = cart.rentals
    params['sales'] = cart.sales
    params['total'] = calculate_total(request)

    return templater.render_to_response(request, 'cart.html', params)


@view_function
def show_mobile_cart(request):
    '''
        method for showing cart
    '''
    params = {}
    cart = get_cart(request)

    params['rentals'] = cart.rentals
    params['sales'] = cart.sales
    params['total'] = calculate_total(request)

    return templater.render_to_response(request, 'cart_mobile.html', params)


@view_function
def add_to_cart(request):
    '''
        method for adding to cart
    '''
    item_id = request.REQUEST.get('i')
    duration = request.REQUEST.get('d')
    quantity = request.REQUEST.get('q')
    mobile = request.REQUEST.get('m')

    if quantity is 'quantity' or quantity is '':
        quantity = 1

    item = mod.Item.cast(mod.Store_Item.objects.get(id=item_id))

    cart = get_cart(request)
    cart.add_to_cart(item, duration=duration, quantity=quantity)

    save_cart(request, cart)

    if mobile == 'mobile':
        return show_mobile_cart(request)

    return show_cart(request)


@view_function
def delete_from_cart(request):
    '''
        method for deleting from cart
    '''
    cart = get_cart(request)
    item_id = int(request.REQUEST.get('i'))

    cart.delete_from_cart(item_id)

    save_cart(request, cart)

    return show_cart(request)
