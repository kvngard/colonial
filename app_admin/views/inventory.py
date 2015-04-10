from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from app_base.admin import group_required
from app_base.models import Item, Sale_Item, Rental_Item
from app_admin.forms import ItemEditForm, SaleItemEditForm, RentalItemEditForm, CustomItemEditForm
from . import templater


@view_function
@group_required('Manager', 'Admin')
def process_request(request):
    '''
        method for ajax for items
    '''
    params = {}
    if request.urlparams[0] == "true_false":
        params['items'] = Sale_Item.objects.all().order_by('name')
        return templater.render_to_response(request, 'inventory_ajax.html', params)

    if request.urlparams[0] == "false_true":
        params['items'] = Rental_Item.objects.all().order_by('name')
        return templater.render_to_response(request, 'inventory_ajax.html', params)

    if request.urlparams[0] == "false_false" or request.urlparams[0] == "true_true":
        params['items'] = Item.objects.all().order_by('name')
        return templater.render_to_response(request, 'inventory_ajax.html', params)

    params['items'] = Item.objects.all().order_by('name')
    return templater.render_to_response(request, 'inventory.html', params)


@view_function
@group_required('Manager', 'Admin')
def create(request):
    '''
        method for creating and editing items
    '''
    params = {}
    sale_item_form = SaleItemEditForm()
    rental_item_form = RentalItemEditForm()
    custom_item_form = CustomItemEditForm()
    if request.method == 'POST':
        if request.POST.get('price'):
            form = SaleItemEditForm(request.POST, request.FILES)
            if form.is_valid():
                newimg = form.save(commit=False)
                newimg.photo = request.FILES['photo']
                newimg.save()
                return HttpResponseRedirect('/app_admin/inventory/')
        elif request.POST.get('price_per_day'):
            form = RentalItemEditForm(request.POST, request.FILES)
            if form.is_valid():
                newimg = form.save(commit=False)
                newimg.photo = request.FILES['photo']
                newimg.save()
                return HttpResponseRedirect('/app_admin/inventory/')
        else:
            form = CustomItemEditForm(request.POST, request.FILES)
            if form.is_valid():
                newimg = form.save(commit=False)
                newimg.photo = request.FILES['photo']
                newimg.save()
                return HttpResponseRedirect('/app_admin/inventory/')

    params['sale_item_form'] = sale_item_form
    params['rental_item_form'] = rental_item_form
    params['custom_item_form'] = custom_item_form
    params['title'] = 'Create Item'
    return templater.render_to_response(request, 'create_item.html', params)


@view_function
@group_required('Manager', 'Admin')
def edit(request):
    '''
        method for editing
    '''
    try:
        item = Item.objects.get(id=request.urlparams[0])
    except Item.DoesNotExist:
        return HttpResponseRedirect('/app_admin/inventory/')

    params = {}
    item_type = Item.cast(item).__class__.__name__
    item = Item.cast(item)
    print('########################')
    print(item_type)
    print('########################')

    sale_item_form = ''
    rental_item_form = ''
    custom_item_form = ''

    if item_type == 'Sale_Item':
        sale_item_form = SaleItemEditForm(instance=item)
        if request.method == 'POST':
            sale_item_form = SaleItemEditForm(request.POST, request.FILES, instance=item)
            if sale_item_form.is_valid():
                sale_item_form.save()
                return HttpResponseRedirect('/app_admin/inventory/')
    elif item_type == 'Rental_Item':
        rental_item_form = RentalItemEditForm(instance=item)
        if request.method == 'POST':
            rental_item_form = RentalItemEditForm(request.POST, request.FILES, instance=item)
            if rental_item_form.is_valid():
                rental_item_form.save()
                return HttpResponseRedirect('/app_admin/inventory/')
    else:
        custom_item_form = CustomItemEditForm(instance=item)
        if request.method == 'POST':
            custom_item_form = CustomItemEditForm(request.POST, request.FILES, instance=item)
            if custom_item_form.is_valid():
                custom_item_form.save()
                return HttpResponseRedirect('/app_admin/inventory/')

    params['item_type'] = item_type
    params['sale_item_form'] = sale_item_form
    params['rental_item_form'] = rental_item_form
    params['custom_item_form'] = custom_item_form
    params['title'] = 'Edit Item'
    return templater.render_to_response(request, 'create_item.html', params)


@view_function
@group_required('Manager', 'Admin')
def delete(request):
    '''
        method for deleting
    '''
    try:
        item = Item.objects.get(id=request.urlparams[0])
    except Item.DoesNotExist:
        return HttpResponseRedirect('/app_admin/inventory/')

    item = Item.cast(item)
    item.delete()

    return HttpResponseRedirect('/app_admin/inventory/')
