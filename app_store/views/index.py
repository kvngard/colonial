from django.contrib.auth.decorators import login_required
from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from app_store.storeforms import CheckoutForm
import app_base.models as mod
from . import templater


@view_function
def process_request(request):
    params = {}
    try:
        items = mod.Sale_Product.objects.all()
    except mod.Sale_Product.DoesNotExist:
        return HttpResponseRedirect('/')

    params['items'] = items

    return templater.render_to_response(request, 'store.html', params)


@view_function
def search(request):
    params = {}
    search_parameter = request.REQUEST.get('p')

    try:
        items = mod.Sale_Product.objects.filter(
            name__icontains=search_parameter)
    except mod.Sale_Product.DoesNotExist:
        return HttpResponseRedirect('/')

    params['items'] = items

    return templater.render_to_response(request, 'storefront.html', params)


@view_function
def add_to_cart(request):
    params = {}
    item_id = request.REQUEST.get('i')
    quantity = request.REQUEST.get('q')

    if item_id is None:
        params['items'] = mod.Sale_Product.objects.filter(
            id__in=request.session['shopping_cart'].keys())
        params['cart'] = request.session['shopping_cart']
        return templater.render_to_response(request, 'cart.html', params)

    try:
        mod.Sale_Product.objects.get(id=item_id)
    except mod.Item.DoesNotExist:
        params['message'] = '404'
        return templater.render_to_response(request, 'default.html', params)

    # If there is no shopping_cart session variable, make it!
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}

    if item_id in request.session['shopping_cart'].keys():
        request.session['shopping_cart'][item_id] = int(
            request.session['shopping_cart'][item_id]) + int(quantity)
    else:
        request.session['shopping_cart'][item_id] = int(quantity)

    # Save session variable changes
    request.session.modified = True

    params['items'] = mod.Sale_Product.objects.filter(
        id__in=request.session['shopping_cart'].keys())
    params['cart'] = request.session['shopping_cart']

    return templater.render_to_response(request, 'cart.html', params)


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
@login_required(login_url='/app_account/login.loginUser/')
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
