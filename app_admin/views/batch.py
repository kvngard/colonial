from django.core.mail import send_mail
import app_base.models as mod
from . import templater
import datetime


def main():
    '''
    Sends an email to each of the users that has a rental out.
    Only sends one email per user.
    Tells the user all of their rentals out.
    '''
    params = {}
    debtors = {}

    rentals = mod.Rental.objects.filter(
        date_due__lt=datetime.date.today(),
        return_instance__iexact=None)

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

        emailbody = templater.render('late_rental_email.html', params)

        send_mail(
            'Colonial Heritage Foundation - Your Rental(s) are late!',
            emailbody,
            'chfsite@gmail.com',
            [email],
            html_message=emailbody,
            fail_silently=False
        )

if __name__ == "__main__":
    main()
