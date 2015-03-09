# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425604383.285701
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial/app_account/templates/login_modal.html'
_template_uri = '/app_account/templates/login_modal.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!-- Modal Structure -->\r\n<div id="login_modal" class="modal">\r\n    <div class="modal-content">\r\n    </div>\r\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "27": 21, "21": 1}, "filename": "C:\\Users\\Kevin\\Development\\colonial/app_account/templates/login_modal.html", "uri": "/app_account/templates/login_modal.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
