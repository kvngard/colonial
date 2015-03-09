# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1424752504.437583
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial\\home\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        from django_mako_plus.controller import static_files 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_files'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n\r\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>\r\n    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>\r\n    <title>Parallax Template - Materialize</title>\r\n\r\n    <!-- CSS  -->\r\n    <link href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('components/materialize/bin/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>\r\n    <link href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('components/materialize/templates/parallax-template/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n      Site content goes here in sub-templates.\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "filename": "C:\\Users\\Kevin\\Development\\colonial\\home\\templates/base.htm", "line_map": {"32": 5, "48": 28, "36": 5, "37": 17, "38": 17, "39": 18, "40": 18, "41": 21, "42": 21, "43": 21, "63": 26, "16": 0, "49": 31, "50": 31, "51": 31, "57": 26, "26": 2, "27": 4, "69": 63, "31": 4}, "source_encoding": "ascii"}
__M_END_METADATA
"""
