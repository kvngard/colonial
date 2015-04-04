from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # url(r'',
                       # include('registration.backends.default.urls')),
                       url(r'', include(
                           'django.contrib.auth.urls')),
                       # Password Reset URLs:
                       url(r'^password_reset/$',
                           'django.contrib.auth.views.password_reset',
                           {'post_reset_redirect':
                            '/password_reset/mailed/'},
                           name="password_reset"),
                       (r'^password_reset/mailed/$',
                        'django.contrib.auth.views.password_reset_done'),
                       (r'^password_reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                        'django.contrib.auth.views.password_reset_confirm',
                        {'post_reset_redirect': '/password_reset/complete/'}),
                       (r'^password_reset/complete/$',
                        'django.contrib.auth.views.password_reset_complete'),

                       url(r'^admin/',
                           include(admin.site.urls)),
                       # the django_mako_plus controller handles every request - this line is the
                       # glue that connects Mako to Django
                       url(r'^.*$',
                           'django_mako_plus.controller.router.route_request'),
                       )
