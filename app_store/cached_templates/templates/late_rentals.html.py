# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425772071.173028
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/late_rentals.html'
_template_uri = 'late_rentals.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base/templates/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        rentals = context.get('rentals', UNDEFINED)
        dayslate = context.get('dayslate', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('w\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        rentals = context.get('rentals', UNDEFINED)
        dayslate = context.get('dayslate', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<ul id="nav-mobile" class="side-nav  fixed">\r\n      <a href="#">\r\n        <a href="/">\r\n            <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('app_home/media/logo.svg" alt=\'profile_image\' class=\'nav-logo\' />\r\n        </a>\r\n      </a>\r\n      <div class="input-field">\r\n        <input id="search" type="text" required>\r\n        <label for="search"><i class="mdi-action-search"></i></label>\r\n      </div>\r\n</ul>\r\n<div class="view-box">\r\n    <div class="row">\r\n')
        for rental in rentals:
            __M_writer('        <div class="store-item card col l2 s12">\r\n            <div class="card-content">\r\n              <div class="card-image waves-effect waves-block waves-light">\r\n                <img class="activator" src="')
            __M_writer(str(rental.rentable_article.photo.image))
            __M_writer('">\r\n              </div>\r\n              <span class="card-title grey-text text-darken-4">')
            __M_writer(str(rental.rentable_article.name))
            __M_writer('</span>\r\n              <p>Rented By: ')
            __M_writer(str(rental.transaction.customer))
            __M_writer('</p>\r\n              <p>Current Fee: <a href="#!">$')
            __M_writer(str(rental.rentable_article.price_per_day*dayslate[rental.rentable_article.name]))
            __M_writer('</a></p>\r\n              <p>Days late: ')
            __M_writer(str(dayslate[rental.rentable_article.name]))
            __M_writer('</p>\r\n            </div>\r\n          </div>\r\n')
        __M_writer('      </div>\r\n  </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/late_rentals.html", "source_encoding": "ascii", "line_map": {"64": 23, "65": 24, "66": 24, "27": 0, "68": 25, "37": 1, "70": 26, "71": 30, "77": 71, "47": 3, "67": 25, "69": 26, "56": 3, "57": 7, "58": 7, "59": 17, "60": 18, "61": 21, "62": 21, "63": 23}, "uri": "late_rentals.html"}
__M_END_METADATA
"""
