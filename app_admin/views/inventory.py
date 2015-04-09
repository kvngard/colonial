from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from app_base.admin import group_required
from app_base.models import Item
from app_admin.forms import ItemEditForm
from . import templater


@view_function
@group_required('Manager', 'Admin')
def process_request(request):
    items = Item.objects.all().order_by('name')
    params = {}
    params['items'] = items
    return templater.render_to_response(request, 'inventory.html', params)


@view_function
@group_required('Manager', 'Admin')
def create(request):
    params = {}
    form = ItemEditForm()
    if request.method == 'POST':
        form = ItemEditForm(request.POST, request.FILES)
        if form.is_valid():
            newimg = form.save(commit=False)
            newimg.photo = request.FILES['photo']
            newimg.save()
            return HttpResponseRedirect('/app_admin/inventory/')

    params['form'] = form
    params['title'] = 'Create Item'
    return templater.render_to_response(request, 'create_item.html', params)


@view_function
@group_required('Manager', 'Admin')
def edit(request):
    try:
        item = Item.objects.get(id=request.urlparams[0])
    except Item.DoesNotExist:
        return HttpResponseRedirect('/app_admin/inventory/')

    params = {}
    form = ItemEditForm(instance=item)

    if request.method == 'POST':
        form = ItemEditForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app_admin/inventory/')

    params['form'] = form
    params['title'] = 'Edit Item'
    return templater.render_to_response(request, 'create_item.html', params)


@view_function
@group_required('Manager', 'Admin')
def delete(request):

    try:
        item = Item.objects.get(id=request.urlparams[0])
    except Item.DoesNotExist:
        return HttpResponseRedirect('/app_admin/inventory/')

    item.delete()

    return HttpResponseRedirect('/app_admin/inventory/')
