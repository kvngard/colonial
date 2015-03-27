from django.contrib.auth.decorators import login_required
from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from app_store.storeforms import CheckoutForm
from django.db.models import Q
import app_base.models as mod
from . import templater


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
            item = mod.Rentable_Article.objects.get(id=item.id, quantity_on_hand__gt=0)
        except mod.Rentable_Article.DoesNotExist:
            try:
                item = mod.Custom_Product.objects.get(id=item.id)
            except mod.Custom_Product.DoesNotExist:
                try:
                    item = mod.Sale_Product.objects.get(id=item.id, quantity_on_hand__gt=0)
                except mod.Sale_Product.DoesNotExist:
                    continue
        sorted_items.append(item)

    return sorted_items


def check_and_intialize_cart(request):
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}
    return


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
        items = get_items().filter(Q(name__icontains=search_parameter) | Q(description__icontains=search_parameter))
    except mod.Store_Item.DoesNotExist:
        return HttpResponseRedirect('/')

    items = sort_items(items)
    params['items'] = items

    return templater.render_to_response(request, 'search_display.html', params)


@view_function
def show_cart(request, items=None):
    params = {}
    check_and_intialize_cart(request)

    if items is None:
        items = mod.Store_Item.objects.filter(
            id__in=request.session['shopping_cart'].keys())

    items = sort_items(items)
    params['items'] = items
    params['cart'] = request.session['shopping_cart']

    return templater.render_to_response(request, 'cart.html', params)


@view_function
def add_to_cart(request):
    params = {}
    item_id = request.REQUEST.get('i')
    quantity = request.REQUEST.get('q')    

    # If there is no shopping_cart session variable, make it!
    check_and_intialize_cart(request)    

    if item_id in request.session['shopping_cart'].keys():
        request.session['shopping_cart'][item_id] = int(
            request.session['shopping_cart'][item_id]) + int(quantity)
    else:
        request.session['shopping_cart'][item_id] = int(quantity)

    # Save session variable changes
    request.session.modified = True

    items = mod.Store_Item.objects.filter(
        id__in=request.session['shopping_cart'].keys())

    return show_cart(request, items)


@view_function
def delete_from_cart(request):

    params = {}
    item_id = request.REQUEST.get('i')

    print(str(item_id))
    del request.session['shopping_cart'][str(item_id)]
    # Save session variable changes
    request.session.modified = True

    params['items'] = mod.Sale_Product.objects.filter(
        id__in=request.session['shopping_cart'].keys())
    params['cart'] = request.session['shopping_cart']

    return templater.render_to_response(request, 'cart.html', params)


@view_function
@login_required(redirect_field_name='/app_store/')
def checkout(request):

    params = {}
    params['form'] = CheckoutForm()

    params['items'] = mod.Sale_Product.objects.filter(
        id__in=request.session['shopping_cart'].keys())
    params['cart'] = request.session['shopping_cart']

    total = 0
    for item in params['items']:
        total += params['cart'][str(item.id)] * item.price
    params['total'] = total

    return templater.render_to_response(request, 'checkout.html', params)