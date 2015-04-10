from django_mako_plus.controller import view_function
from app_base.admin import group_required
from app_base.models import User, Transaction, Payment, Rental
from . import templater
import datetime


@view_function
@group_required('Manager', 'Admin')
def process_request(request):
    '''
        method for getting users
    '''
    users = User.objects.all()
    params = {}

    # Get the total amount of Users
    params['users'] = users

    user_count = 0
    for user in users:
        user_count += 1

    print(user_count)
    params['total_users'] = user_count

    # Get the total amount of Transactions
    transactions = Transaction.objects.all()

    transaction_count = 0
    for t in transactions:
        transaction_count += 1

    print(transaction_count)
    params['total_transactions'] = transaction_count

    # Get the total amount of Money
    payments = Payment.objects.all()
    payment_total = 0
    for p in payments:
        payment_total += p.amount

    print(payment_total)
    params['payment_total'] = payment_total

    # Get the total rentals

    rentals_for_checkout = Rental.objects.filter(
        checkout_by_date__gte=datetime.date.today(),
        date_out__exact=None)

    late_rentals = Rental.objects.filter(
        return_instance__iexact=None).filter(
        date_due__lt=datetime.date.today())

    params['rentals'] = rentals_for_checkout
    params['late_rentals'] = late_rentals
    params['today'] = datetime.date.today()

    total_rentals = 0
    total_late_rentals = 0

    for r in Rental.objects.all():
        total_rentals += 1

    for lr in late_rentals:
        total_late_rentals += 1

    params['total_rentals'] = total_rentals
    params['total_late_rentals'] = total_late_rentals

    params['transactions'] = transactions
    params['payments'] = payments
    return templater.render_to_response(request, 'index.html', params)
