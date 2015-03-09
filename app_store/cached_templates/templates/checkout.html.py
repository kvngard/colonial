# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425791403.876464
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/checkout.html'
_template_uri = 'checkout.html'
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
        reversed = context.get('reversed', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        form = context.get('form', UNDEFINED)
        range = context.get('range', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        reversed = context.get('reversed', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        form = context.get('form', UNDEFINED)
        range = context.get('range', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<ul id="nav-mobile" class="side-nav fixed">\r\n  <a href="#">\r\n    <a href="/">\r\n        <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('app_home/media/logo.svg" alt=\'profile_image\' class=\'nav-logo\' />\r\n    </a>\r\n  </a>\r\n  <div class="input-field">\r\n    <input id="search" type="text" required>\r\n    <label for="search"><i class="mdi-action-search"></i></label>\r\n  </div>\r\n  <a class="btn-flat waves-effect waves-light green accent-4 white-text cart-display">Display Cart</a>\r\n</ul>\r\n<div class="view-box container">\r\n  <h2>Check Out</h2>\r\n  <table class="striped">\r\n    <thead>\r\n      <tr>\r\n        <th data-field="id">Item Name</th>\r\n        <th data-field="quantity">Quantity</th>\r\n        <th data-field="price">Price</th>\r\n        <th>Options</th>\r\n      </tr>\r\n    </thead>\r\n    <tbody>\r\n')
        for item in items:
            __M_writer('      <tr>\r\n        <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\r\n        <td>\r\n          <select class="select-dropdown">\r\n')
            for j in reversed(range(1,cart[str(item.id)]+1)):
                __M_writer('            <option value="')
                __M_writer(str(j))
                __M_writer('"}>')
                __M_writer(str(j))
                __M_writer('</option>\r\n')
            __M_writer('        </td>\r\n        <td>$')
            __M_writer(str(cart[str(item.id)] * item.price))
            __M_writer('</td>\r\n        <td>\r\n          <div class=\'options\'>\r\n            <a rel="')
            __M_writer(str(item.id))
            __M_writer('" class="btn-flat waves-effect waves-light red accent-3 white-text">Delete</a>\r\n          </div>\r\n        </td>\r\n      </tr>\r\n')
        __M_writer('    </tbody>\r\n  </table>\r\n  <br>\r\n  ')
        __M_writer(str(form))
        __M_writer('\r\n  <a href="/app_store/congrats/">\r\n  <button class="btn waves-effect waves-light orange accent-3 " type="submit" name="action">Purchase\r\n    <i class="mdi-content-send right"></i>\r\n  </button>\r\n  </a>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/checkout.html", "uri": "checkout.html", "line_map": {"64": 3, "65": 7, "66": 7, "67": 28, "68": 29, "69": 30, "70": 30, "71": 33, "72": 34, "73": 34, "74": 34, "75": 34, "76": 34, "77": 36, "78": 37, "79": 37, "80": 40, "81": 40, "82": 45, "83": 48, "84": 48, "90": 84, "27": 0, "41": 1, "51": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
