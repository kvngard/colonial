from django_mako_plus.controller import view_function
from app_store.storeforms import Credit_Card_Form
from django.forms.widgets import CheckboxInput
from django.http import HttpResponseRedirect
from app_base.admin import group_required
from app_base.widgets import RadioSelect
from app_base.forms import site_model_form
from django.core.mail import send_mail
import app_base.models as mod
from decimal import Decimal
from django import forms
from . import templater
import datetime


@view_function
@group_required('Manager')
def process_request(request):
    params = {}

    try:
        rentals = mod.Rental.objects.filter(
            return_instance__iexact=None).filter(
            date_due__gte=datetime.date.today())
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    try:
        late_rentals = mod.Rental.objects.filter(
            return_instance__iexact=None).filter(
            date_due__lt=datetime.date.today())
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    params['rentals'] = rentals
    params['late_rentals'] = late_rentals
    params['today'] = datetime.date.today()

    return templater.render_to_response(request, 'rentals.html', params)


@view_function
@group_required('Manager')
def checkout(request):
    params = {}

    try:
        rentals = mod.Rental.objects.filter(
            checkout_by_date__gte=datetime.date.today(),
            date_out__exact=None)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    rentals_to_check_out = []
    request.session['rentals_to_check_out'] = []
    total = 0

    if request.method == 'POST':

        data = dict(request.POST)

        for rental in rentals:
            if data.get(str(rental.id))[0]:
                if data.get(str(rental.id))[0] == 'on':

                    rentals_to_check_out.append(rental)
                    request.session['rentals_to_check_out'].append(
                        str(rental.id))

                    total += rental.checkout_price

        params['total'] = total
        params['rentals'] = rentals_to_check_out
        params['credit_card_form'] = Credit_Card_Form()

        return templater.render_to_response(request, '/app_store/templates/checkout.html', params)

    params['title'] = "Checkout Rentals"
    params['rentals'] = rentals

    return templater.render_to_response(request, 'checkout_rentals.html', params)


@view_function
@group_required('Manager')
def charge(request):

    if request.method == "POST":
        params = {}

        try:
            rentals = mod.Rental.objects.filter(
                id__in=request.session['rentals_to_check_out'])
        except mod.Rental.DoesNotExist:
            return HttpResponseRedirect('/')

        request.session['rentals_to_check_out'] = []

        total = 0

        for rental in rentals:
            total += rental.checkout_price
            user = rental.transaction.customer

        credit_card_form = Credit_Card_Form(
            request.POST, total=total, user=user)

        if credit_card_form.is_valid():
            for r in rentals:

                t = r.transaction
                r.date_out = datetime.date.today()
                r.date_due = datetime.date.today() + \
                    datetime.timedelta(r.duration)
                r.handled_by = request.user
                r.save()

                p = mod.Payment()
                p.amount = r.checkout_price
                p.transaction = t
                p.charge_id = credit_card_form.resp['ID']
                p.save()

            params['rentals'] = rentals
            params['total'] = total

            return templater.render_to_response(request, '/app_store/templates/checkout_receipt.html', params)

    HttpResponseRedirect('/app_admin/rentals.checkout/')


@view_function
@group_required('Manager')
def report(request):

    params = {}

    try:
        rentals = mod.Rental.objects.filter(
            date_due__lt=datetime.date.today(),
            return_instance__iexact=None)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    ninety, sixty, thirty, new = [], [], [], []

    dayslate = {}

    for rental in rentals:
        delta = datetime.date.today() - rental.date_due.date()
        dayslate[rental.rental_item.name] = delta.days

        if delta.days < 30:
            new.append(rental)
        elif delta.days >= 30 and delta.days < 60:
            thirty.append(rental)
        elif delta.days >= 60 and delta.days < 90:
            sixty.append(rental)
        else:
            ninety.append(rental)

    params['rentals'] = rentals
    params['dayslate'] = dayslate
    params['ninety'] = ninety
    params['sixty'] = sixty
    params['thirty'] = thirty
    params['new'] = new

    emailbody = templater.render(request, 'rental_report_email.html', params)

    send_mail(
        'Colonial Heritage Foundation - Overdue Report',
        emailbody,
        'chfsite@gmail.com',
        [request.user.email],
        html_message=emailbody,
        fail_silently=False
    )

    return templater.render_to_response(request, 'rental_report.html', params)


@view_function
@group_required('Manager')
def check_in(request):
    params = {}
    id = request.urlparams[0]

    return_form = Return_Form()
    damage_form = Damage_Form()

    try:
        rental = mod.Rental.objects.get(id=id)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    if datetime.date.today() > rental.date_due.date():
        lf = mod.Late_Fee()
        lf.days_late = (datetime.date.today() - rental.date_due.date()).days
        lf.amount = Decimal(
            lf.days_late * rental.rental_item.price_per_day)
        late_form = Late_Form(instance=lf)
        params['late_form'] = late_form

    if request.method == "POST":
        return_form = Return_Form(request.POST)
        damage_form = Damage_Form(request.POST)

        if return_form.is_valid():
            rr = return_form.save(commit=False)
            rr.date_in = datetime.date.today()
            rr.rental = rental
            rr.handled_by = request.user
            rr.save()

            i = mod.Store_Item.objects.get(id=rental.rental_item.id)
            i.quantity_on_hand += 1
            i.save()

            if damage_form.is_valid():
                df = damage_form.save(commit=False)
                df.rental_return = rr
                df.handled_by = request.user
                df.transaction = rental.transaction
                df.save()

            if rr.date_in > rental.date_due.date():
                lf = Late_Form(request.POST).save(commit=False)
                if lf.waived is False:
                    lf.rental_return = rr
                    lf.transaction = rental.transaction
                    lf.amount = Decimal(
                        lf.days_late * rental.rental_item.price_per_day)
                    lf.save()

        return HttpResponseRedirect('/app_admin/rentals/')

    params['rental'] = rental
    params['return_form'] = return_form
    params['damage_form'] = damage_form

    return templater.render_to_response(request, 'rental_return.html', params)


class Return_Form(forms.ModelForm):

    class Meta:
        model = mod.Rental_Return
        fields = ['return_condition']
        widgets = {
            'return_condition': RadioSelect(),
        }


class Late_Form(site_model_form):

    class Meta:
        model = mod.Late_Fee
        fields = ['days_late', 'amount', 'waived']
        widgets = {
            'waived': CheckboxInput()
        }


class Damage_Form(forms.ModelForm):

    class Meta:
        model = mod.Damage_Fee
        fields = ['description', 'amount']
