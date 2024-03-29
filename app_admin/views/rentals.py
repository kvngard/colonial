from django_mako_plus.controller import view_function
from app_admin.forms import Return_Form, Damage_Form
from app_store.storeforms import Credit_Card_Form
from django.http import HttpResponseRedirect
from app_base.admin import group_required
from django.core.mail import send_mail
import app_base.models as mod
from decimal import Decimal
from . import templater
import datetime


@view_function
@group_required('Manager', 'Admin')
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
@group_required('Manager', 'Admin')
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
@group_required('Manager', 'Admin')
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
@group_required('Manager', 'Admin')
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
        params['days_late'] = lf.days_late
        params['amount'] = lf.amount

    if request.method == "POST":
        print(request.POST)
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
                print(dict(request.POST).get('waived')[0] != 'on')
                if dict(request.POST).get('waived')[0] != 'on':
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


@view_function
@group_required('Manager', 'Admin')
def notify(request):

    params = {}

    try:
        rental = mod.Rental.objects.get(id=request.urlparams[0])
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    email = rental.transaction.customer.email

    params['user'] = rental.transaction.customer
    params['today'] = datetime.date.today()
    params['rentals'] = [rental]

    emailbody = templater.render(request, 'late_rental_email.html', params)

    send_mail(
        'Colonial Heritage Foundation - Your Rental(s) are late!',
        emailbody,
        'chfsite@gmail.com',
        [email],
        html_message=emailbody,
        fail_silently=False
    )

    return templater.render_to_response(request, 'notify.html', params)


@view_function
@group_required('Manager', 'Admin')
def report(request):

    params = {}

    try:
        rentals = mod.Rental.objects.filter(
            date_due__lt=datetime.date.today(),
            return_instance__iexact=None)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    ninety, sixty, thirty, new = [], [], [], []
    debtors = {}

    dayslate = {}

    for rental in rentals:

        if rental.transaction.customer in debtors.keys():
            debtors[rental.transaction.customer].append(rental)
        else:
            debtors[rental.transaction.customer] = []
            debtors[rental.transaction.customer].append(rental)

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

    params['dayslate'] = dayslate
    params['ninety'] = ninety
    params['sixty'] = sixty
    params['thirty'] = thirty
    params['new'] = new

    return templater.render_to_response(request, 'rental_report.html', params)


@view_function
@group_required('Manager', 'Admin')
def send_mass_overdue_emails(request):

    params = {}
    debtors = {}

    try:
        rentals = mod.Rental.objects.filter(
            date_due__lt=datetime.date.today(),
            return_instance__iexact=None)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    # Sort rentals for individual and manager report emails.
    for rental in rentals:

        if rental.transaction.customer in debtors.keys():
            debtors[rental.transaction.customer].append(rental)
        else:
            debtors[rental.transaction.customer] = []
            debtors[rental.transaction.customer].append(rental)

    # Sends individual overdue emails.
    for debtor in debtors.keys():
        email = debtor.email

        params['user'] = debtor
        params['today'] = datetime.date.today()
        params['rentals'] = debtors[debtor]

        emailbody = templater.render(request, 'late_rental_email.html', params)

        send_mail(
            'Colonial Heritage Foundation - Your Rental(s) are late!',
            emailbody,
            'chfsite@gmail.com',
            [email],
            html_message=emailbody,
            fail_silently=False
        )

    return templater.render_to_response(request, 'rental_report.html', params)


@view_function
@group_required('Manager', 'Admin')
def send_manager_report_email(request):

    params = {}

    try:
        rentals = mod.Rental.objects.filter(
            date_due__lt=datetime.date.today(),
            return_instance__iexact=None)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    ninety, sixty, thirty, new = [], [], [], []
    dayslate = {}

    # Sort rentals for individual and manager report emails.
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

    # Sends manager email to currently logged-in user.
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
