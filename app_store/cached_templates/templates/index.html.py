# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425749630.70806
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'style']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def style():
            return render_style(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'style'):
            context['self'].style(**pageargs)
        

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
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="containter">\r\n')
        for i in range(0,2):
            __M_writer('    <div class="row">\r\n')
            for i in range(0,4):
                __M_writer('       <div class="store-item card col l2 s12">\r\n            <div class="card-image waves-effect waves-block waves-light">\r\n              <img class="activator" src="">\r\n            </div>\r\n            <div class="card-content">\r\n              <span class="card-title activator grey-text text-darken-4">Card Title <i class="mdi-navigation-more-vert right"></i></span>\r\n              <p><a href="#">This is a link</a></p>\r\n            </div>\r\n            <div class="card-reveal">\r\n              <span class="card-title grey-text text-darken-4">Card Title <i class="mdi-navigation-close right"></i></span>\r\n              <p>Here is some more information about this product that is only revealed once clicked on.</p>\r\n            </div>\r\n          </div>\r\n')
            __M_writer('      </div>\r\n')
        __M_writer('  </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_style(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def style():
            return render_style(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('app_store/styles/store.css">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "filename": "C:\\Users\\Kevin\\Development\\colonial\\app_store\\templates/index.html", "line_map": {"64": 12, "65": 26, "66": 28, "38": 1, "72": 3, "43": 5, "79": 3, "80": 4, "81": 4, "53": 7, "87": 81, "27": 0, "60": 7, "61": 9, "62": 10, "63": 11}, "source_encoding": "ascii"}
__M_END_METADATA
"""
