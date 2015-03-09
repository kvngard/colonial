# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425598911.747496
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial\\app_account\\templates/form_wrapper.html'
_template_uri = 'form_wrapper.html'
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
        title = context.get('title', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n    <div class='valign container'>\r\n        <h1>")
        __M_writer(str( title ))
        __M_writer('</h1>\r\n        <div id="form_wrapper">\r\n            <form id="account_form" method="POST" action="/app_account/new.validate_form/">\r\n                ')
        __M_writer(str( form ))
        __M_writer('\r\n                <button class="btn waves-effect waves-light" type="submit" name="action">Submit\r\n                    <i class="mdi-content-send right"></i>\r\n                </button>\r\n            </form>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 59, "59": 8, "36": 1, "57": 5, "55": 3, "56": 5, "41": 15, "58": 8, "27": 0, "47": 3}, "uri": "form_wrapper.html", "filename": "C:\\Users\\Kevin\\Development\\colonial\\app_account\\templates/form_wrapper.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
