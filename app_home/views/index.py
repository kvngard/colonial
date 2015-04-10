from django_mako_plus.controller import view_function
from django.core.mail import send_mail
from . import templater


@view_function
def process_request(request):
    '''
        method for getting index text
    '''
    params = {}

    params[
        "heritage_text"] = "America is a nation built on certain ideals, ideals that have helped catapult our country to the forefront of international politics and commerce. We see it as our duty to preserve these values and help America continue to shine forth as a beacon to the world."
    params[
        "community_text"] = "The Foundation is a community organization that values the opportunity to teach individuals both young and old about the history of our nation. We often host educational demonstrations and lectures at schools and other locations."
    params[
        "craft_text"] = "The era of America's founding was a time of great mental and material creativity. We sponsor a variety of artisans who are helping to carry on this legacy of craft and art. Our online collection features some of their best works."

    #end_mail('Subject here', 'Here is the message.', 'Kevin@colonialheritagefoundation.org',
        #['pedantfool@gmail.com'], fail_silently=False)

    return templater.render_to_response(request, 'index.html', params)
