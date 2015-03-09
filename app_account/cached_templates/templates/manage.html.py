# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425681980.740967
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial\\app_account\\templates/manage.html'
_template_uri = 'manage.html'
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
        form = context.get('form', UNDEFINED)
        title = context.get('title', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n\r\n    <div class='container'>\r\n        <h3>")
        __M_writer(str( title ))
        __M_writer('</h3>\r\n        <div class=\'valign\'>\r\n            <form method="POST">\r\n                ')
        __M_writer(str( form ))
        __M_writer('\r\n                <button class="btn waves-effect waves-light" type="submit" name="action">Submit\r\n                    <i class="mdi-content-send right"></i>\r\n                </button>\r\n                <a href="#password_modal" class="btn-flat waves-effect waves-teal password-trigger">Change Password</a>\r\n            </form>\r\n            <div id="password_modal" class="modal">\r\n                <div class="modal-content">\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 58, "36": 1, "54": 3, "55": 6, "56": 6, "57": 9, "58": 9, "27": 0, "46": 3}, "filename": "C:\\Users\\Kevin\\Development\\colonial\\app_account\\templates/manage.html", "source_encoding": "ascii", "uri": "manage.html"}
__M_END_METADATA
"""
