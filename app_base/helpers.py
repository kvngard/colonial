from django.core.mail import send_mail
from . import templater


def send_mass_email(request, emailbody=None, recipient_list=None, template=None, title='Colonial Heritage Foundation'):
    '''
        method for sending email
    '''
    if emailbody is None:
        if recipient_list is not None and template is not None:
            for key, value in recipient_list:
                params = value
                emailbody = templater.render(request, template, params)

    send_mail(
        title,
        emailbody,
        'chfsite@gmail.com',
        [request.user.email],
        html_message=emailbody,
        fail_silently=False
    )
