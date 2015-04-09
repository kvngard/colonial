from django_mako_plus.controller import view_function
from app_base.admin import group_required
from app_base.models import User, Transaction, Payment
from . import templater


@view_function
@group_required('Manager', 'Admin')
def process_request(request):
    users = User.objects.all()
    params = {}

    #Get the total amount of Users
    params['users'] = users

    user_count = 0
    for user in users:
    	user_count += 1

    print(user_count)
    params['total_users'] = user_count

    #Get the total amount of Transactions
    transactions = Transaction.objects.all()

    transaction_count = 0
    for t in transactions:
    	transaction_count += 1

    print(transaction_count)
    params['total_transactions'] = transaction_count

    #Get the total amount of Money
    payments = Payment.objects.all()
    payment_total = 0
    for p in payments:
    	payment_total += p.amount

    print(payment_total)
    params['payment_total'] = payment_total


    params['transactions'] = transactions
    params['payments'] = payments
    return templater.render_to_response(request, 'index.html', params)
