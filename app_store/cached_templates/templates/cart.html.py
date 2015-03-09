# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425788296.58039
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/cart.html'
_template_uri = 'cart.html'
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
    return runtime._inherit_from(context, 'app_base/templates/base_ajax.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        reversed = context.get('reversed', UNDEFINED)
        str = context.get('str', UNDEFINED)
        items = context.get('items', UNDEFINED)
        range = context.get('range', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
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
        def content():
            return render_content(context)
        reversed = context.get('reversed', UNDEFINED)
        str = context.get('str', UNDEFINED)
        items = context.get('items', UNDEFINED)
        range = context.get('range', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <h2>Shopping Cart</h2>\r\n  <table class="striped">\r\n    <thead>\r\n      <tr>\r\n        <th data-field="id">Item Name</th>\r\n        <th data-field="quantity">Quantity</th>\r\n        <th data-field="price">Price</th>\r\n        <th>Options</th>\r\n      </tr>\r\n    </thead>\r\n    <tbody>\r\n')
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
        __M_writer('    </tbody>\r\n  </table>\r\n  <a href="/app_store/index.checkout/">\r\n    <button class="btn waves-effect waves-light orange accent-3" type="submit" name="action">Checkout\r\n      <i class="mdi-action-shopping-cart right"></i>\r\n    </button>\r\n  </a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "cart.html", "line_map": {"64": 17, "65": 20, "66": 21, "67": 21, "68": 21, "69": 21, "70": 21, "39": 1, "72": 24, "73": 24, "74": 27, "71": 23, "76": 32, "82": 76, "49": 3, "75": 27, "27": 0, "60": 3, "61": 15, "62": 16, "63": 17}, "source_encoding": "ascii", "filename": "C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/cart.html"}
__M_END_METADATA
"""
