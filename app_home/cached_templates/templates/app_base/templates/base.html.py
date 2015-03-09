# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425779754.308137
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial/app_base/templates/base.html'
_template_uri = 'app_base/templates/base.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['navigation', 'content', 'style']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def navigation():
            return render_navigation(context._locals(__M_locals))
        def style():
            return render_style(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        from django_mako_plus.controller import static_files 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_files'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>\r\n        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>\r\n        <title>Colonial Heritage Foundation</title>\r\n\r\n        <!-- CSS  -->\r\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('components/materialize/bin/materialize.css">\r\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'style'):
            context['self'].style(**pageargs)
        

        __M_writer("\r\n\r\n        <!-- Fonts -->\r\n        <link href='http://fonts.googleapis.com/css?family=IM+Fell+DW+Pica:400,400italic' rel='stylesheet' type='text/css'>\r\n\r\n")
        __M_writer('        <link rel="icon" type="image/x-icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('app_base/media/favicon.ico">\r\n\r\n        <!--  Scripts-->\r\n        <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>\r\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('components/materialize/bin/materialize.js"></script>\r\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('app_base/media/jquery.form.js"></script>\r\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('app_base/media/jquery.loadmodal.js"></script>\r\n\r\n')
        __M_writer('        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('components/webcomponentsjs/webcomponents.js"></script>\r\n\r\n    </head>\r\n    <body>\r\n\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navigation'):
            context['self'].navigation(**pageargs)
        

        __M_writer('\r\n\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n    </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navigation():
            return render_navigation(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n            <nav class="white" role="navigation">\r\n              <div class="nav-wrapper">\r\n                <ul class="left" id="logo">\r\n                    <a href="/">\r\n                        <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('app_home/media/logo.svg" alt=\'profile_image\' class=\'logo responsive-img\' />\r\n                    </a>\r\n                </ul>\r\n                <ul class="right" id="account-mgmt">\r\n')
        if request.user.is_authenticated():
            __M_writer('                      <li><a href="#user_modal" class=\'grey-text user-trigger\'>\r\n                           ')
            __M_writer(str( request.user.get_full_name() ))
            __M_writer('</a></li>\r\n')
        else:
            __M_writer('                      <li><a href="#login_modal" class="grey-text login-trigger">Log In</a></li>\r\n                      <li><a href="#signup_modal" class="grey-text signup-trigger">Sign Up</a></li>\r\n')
        __M_writer('                </ul>\r\n                <ul id="nav-mobile" class="side-nav">\r\n                  <li><a href="#">Navbar Link</a></li>\r\n                </ul>\r\n                <a href="#" data-activates="nav-mobile" class="button-collapse"><i class="mdi-navigation-menu"></i></a>\r\n              </div>\r\n          </nav>\r\n\r\n')
        if request.user.is_authenticated():
            __M_writer('          <div id="user_modal" class="modal user-tag z-depth-1">\r\n            <ul class="user-content">\r\n                <li><a href="/app_account/login.logoutUser/" class="btn-flat waves-effect waves-teal logout-btn">Log Out</a></li>\r\n                <li><a href="/app_account/manage/" class="btn-flat waves-effect waves-teal account-btn">Account</a></li>\r\n            </ul>\r\n            <img src=')
            __M_writer(str( request.user.profile_image ))
            __M_writer(" alt='profile_image' class='circle responsive-img' />\r\n          </div>\r\n")
        __M_writer('\r\n          <div id="login_modal" class="modal">\r\n            <div class="modal-content">\r\n            </div>\r\n          </div>\r\n\r\n          <div id="signup_modal" class="modal">\r\n            <div class="modal-content">\r\n            </div>\r\n          </div>\r\n\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n          Site content goes here in sub-templates.\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_style(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def style():
            return render_style(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "app_base/templates/base.html", "filename": "C:\\Users\\Kevin\\Development\\colonial/app_base/templates/base.html", "source_encoding": "ascii", "line_map": {"132": 121, "16": 0, "30": 2, "31": 4, "35": 4, "36": 5, "40": 5, "41": 17, "42": 17, "43": 19, "44": 19, "45": 19, "50": 20, "51": 26, "52": 26, "53": 26, "54": 30, "55": 30, "56": 31, "57": 31, "58": 32, "59": 32, "60": 35, "61": 35, "62": 35, "67": 84, "72": 88, "73": 91, "74": 91, "75": 91, "81": 40, "89": 40, "90": 45, "91": 45, "92": 49, "93": 50, "94": 51, "95": 51, "96": 52, "97": 53, "98": 56, "99": 64, "100": 65, "101": 70, "102": 70, "103": 73, "109": 86, "115": 86, "121": 20}}
__M_END_METADATA
"""
