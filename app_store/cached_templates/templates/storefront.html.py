# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425764992.602727
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/storefront.html'
_template_uri = 'storefront.html'
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
        items = context.get('items', UNDEFINED)
        range = context.get('range', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        range = context.get('range', UNDEFINED)
        def content():
            return render_content(context)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n      <div class="row">\r\n')
        for item in items[0:len(items)]:
            __M_writer('          <div class="store-item card col l2 s12">\r\n              <div class="card-image waves-effect waves-block waves-light">\r\n                <img class="activator" src="')
            __M_writer(str(item.photo.image))
            __M_writer('">\r\n              </div>\r\n              <div class="card-content">\r\n                <span class="card-title activator grey-text text-darken-4">')
            __M_writer(str(item.name))
            __M_writer('<i class="mdi-navigation-more-vert right"></i></span>\r\n                <p><a href="#!" class="activator">$')
            __M_writer(str(item.price))
            __M_writer('</a></p>\r\n              </div>\r\n              <div class="card-reveal">\r\n                <span class="card-title grey-text text-darken-4">')
            __M_writer(str(item.name))
            __M_writer('<i class="mdi-navigation-close right"></i></span>\r\n                <p>')
            __M_writer(str(item.description))
            __M_writer('</p>\r\n                <form>\r\n')
            if item.quantity_on_hand:
                __M_writer('                  <select class="select-dropdown">\r\n                    <option value="" disabled selected>Quantity</option>\r\n')
                if item.quantity_on_hand <= 5:
                    for j in range(1, item.quantity_on_hand+1):
                        __M_writer('                        <option value="')
                        __M_writer(str(j))
                        __M_writer('"}>')
                        __M_writer(str(j))
                        __M_writer('</option>\r\n')
                else:
                    for j in range(1, 6):
                        __M_writer('                        <option value="')
                        __M_writer(str(j))
                        __M_writer('"}>')
                        __M_writer(str(j))
                        __M_writer('</option>\r\n')
                __M_writer('                  </select>\r\n')
            __M_writer('                <a href="#description" class="btn-flat waves-effect waves-light orange accent-3 white-text">Add to Cart</a>\r\n                </form>\r\n              </div>\r\n            </div>\r\n')
        __M_writer('        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "storefront.html", "filename": "C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/storefront.html", "source_encoding": "ascii", "line_map": {"64": 12, "65": 15, "66": 15, "67": 16, "68": 16, "69": 18, "70": 19, "71": 21, "72": 22, "73": 23, "74": 23, "75": 23, "76": 23, "77": 23, "78": 25, "79": 26, "80": 27, "81": 27, "82": 27, "83": 27, "84": 27, "85": 30, "86": 32, "87": 37, "27": 0, "93": 87, "37": 1, "47": 3, "56": 3, "57": 5, "58": 6, "59": 8, "60": 8, "61": 11, "62": 11, "63": 12}}
__M_END_METADATA
"""
