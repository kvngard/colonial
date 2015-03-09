# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425790948.357903
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/store.html'
_template_uri = 'store.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        len = context.get('len', UNDEFINED)
        items = context.get('items', UNDEFINED)
        range = context.get('range', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        len = context.get('len', UNDEFINED)
        items = context.get('items', UNDEFINED)
        range = context.get('range', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<ul id="nav-mobile" class="side-nav fixed">\r\n      <a href="#">\r\n        <a href="/">\r\n            <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('app_home/media/logo.svg" alt=\'profile_image\' class=\'nav-logo\' />\r\n        </a>\r\n      </a>\r\n      <div class="input-field">\r\n        <input id="search" type="text" required>\r\n        <label for="search"><i class="mdi-action-search"></i></label>\r\n      </div>\r\n      <a href="#cart_modal" class="btn-flat waves-effect waves-light green accent-4 white-text cart-display">Display Cart</a>\r\n</ul>\r\n<div class="view-box">\r\n    <div class="row">\r\n')
        for item in items[0:len(items)]:
            __M_writer('        <div class="store-item card col l2 s12">\r\n            <div class="card-image waves-effect waves-block waves-light">\r\n              <img class="activator" src="')
            __M_writer(str(item.photo.image))
            __M_writer('">\r\n            </div>\r\n            <div class="card-content">\r\n              <span class="card-title activator grey-text text-darken-4">')
            __M_writer(str(item.name))
            __M_writer('<i class="mdi-navigation-more-vert right"></i></span>\r\n              <p><a href="#!" class="activator">$')
            __M_writer(str(item.price))
            __M_writer('</a></p>\r\n            </div>\r\n            <div class="card-reveal">\r\n              <span class="card-title grey-text text-darken-4">')
            __M_writer(str(item.name))
            __M_writer('<i class="mdi-navigation-close right"></i></span>\r\n              <p>')
            __M_writer(str(item.description))
            __M_writer('</p>\r\n              <form>\r\n')
            if item.quantity_on_hand:
                __M_writer('                <select class="select-dropdown">\r\n                  <option value="" disabled selected>Quantity</option>\r\n')
                if item.quantity_on_hand <= 5:
                    for j in range(1, item.quantity_on_hand+1):
                        __M_writer('                      <option value="')
                        __M_writer(str(j))
                        __M_writer('"}>')
                        __M_writer(str(j))
                        __M_writer('</option>\r\n')
                else:
                    for j in range(1, 6):
                        __M_writer('                      <option value="')
                        __M_writer(str(j))
                        __M_writer('"}>')
                        __M_writer(str(j))
                        __M_writer('</option>\r\n')
                __M_writer('                </select>\r\n')
            __M_writer('                <a rel="')
            __M_writer(str(item.id))
            __M_writer('" href="#cart_modal" class="btn-flat waves-effect waves-light orange accent-3 white-text cart-trigger">Add to Cart</a>\r\n              </form>\r\n            </div>\r\n          </div>\r\n')
        __M_writer('      </div>\r\n  </div>\r\n\r\n  <div id="cart_modal" class="modal">\r\n    <div class="modal-content">\r\n    </div>\r\n  </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/store.html", "uri": "store.html", "line_map": {"64": 21, "65": 24, "66": 24, "67": 25, "68": 25, "69": 28, "70": 28, "71": 29, "72": 29, "73": 31, "74": 32, "75": 34, "76": 35, "77": 36, "78": 36, "79": 36, "80": 36, "81": 36, "82": 38, "83": 39, "84": 40, "85": 40, "86": 40, "87": 40, "88": 40, "89": 43, "90": 45, "27": 0, "92": 45, "93": 50, "91": 45, "38": 1, "48": 3, "99": 93, "58": 3, "59": 7, "60": 7, "61": 18, "62": 19, "63": 21}, "source_encoding": "ascii"}
__M_END_METADATA
"""
