# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425772065.702731
_enable_loop = True
_template_filename = 'C:\\Users\\Kevin\\Development\\colonial\\app_home\\templates/index.html'
_template_uri = 'index.html'
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
        community_text = context.get('community_text', UNDEFINED)
        heritage_text = context.get('heritage_text', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        craft_text = context.get('craft_text', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        community_text = context.get('community_text', UNDEFINED)
        heritage_text = context.get('heritage_text', UNDEFINED)
        def content():
            return render_content(context)
        craft_text = context.get('craft_text', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n  <div id="index-banner" class="parallax-container hero">\r\n    <div class="section no-pad-bot">\r\n      <div class="container hero-text">\r\n        <br><br>\r\n        <h1 class="header center white-text">Colonial Heritage Foundation</h1>\r\n        <div class="row center">\r\n          <h3 class="header col s12 white-text">Share The Vision</h3>\r\n        </div>\r\n        <div class="row center">\r\n          <a href="#description" id="download-button" class="btn-large waves-effect waves-light teal lighten-1">Get Started</a>\r\n        </div>\r\n        <br><br>\r\n\r\n      </div>\r\n    </div>\r\n    <div class="parallax"><img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('app_home/media/background1.jpg" alt="Unsplashed background img 2"></div>\r\n  </div>\r\n\r\n  <div class="container" id="description">\r\n    <div class="section">\r\n\r\n      <!--   Icon Section   -->\r\n      <div class="row">\r\n        <div class="col s12 m4">\r\n          <div class="icon-block">\r\n            <h2 class="center brown-text"><i class="mdi-image-brush"></i></h2>\r\n            <h5 class="center">Enjoy Crafts</h5>\r\n\r\n            <p class="light">')
        __M_writer(str( craft_text ))
        __M_writer('</p>\r\n            <div class=\'center-align\'>\r\n              <br>\r\n              <a href="/app_store/" class="btn-large waves-effect waves-light orange accent-3">Take A Look</a>\r\n            </div>\r\n          </div>\r\n        </div>\r\n\r\n        <div class="col s12 m4">\r\n          <div class="icon-block">\r\n            <h2 class="center brown-text"><i class="mdi-maps-terrain"></i></h2>\r\n            <h5 class="center">Celebrate History</h5>\r\n\r\n            <p class="light">')
        __M_writer(str( heritage_text ))
        __M_writer('</p>\r\n            <div class=\'center-align\'>\r\n              <br>\r\n              <a href="/app_store/manage.late" class="btn-large waves-effect waves-light orange accent-3">Learn More</a>\r\n            </div>\r\n          </div>\r\n        </div>\r\n\r\n        <div class="col s12 m4">\r\n          <div class="icon-block">\r\n            <h2 class="center brown-text"><i class="mdi-social-group"></i></h2>\r\n            <h5 class="center">Build Communities</h5>\r\n\r\n            <p class="light">')
        __M_writer(str( community_text ))
        __M_writer('</p>\r\n            <div class=\'center-align\'>\r\n              <br>\r\n              <a href="#description" class="btn-large waves-effect waves-light orange accent-3">Join Us</a>\r\n            </div>\r\n          </div>\r\n        </div>\r\n\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <div id="index-banner" class="parallax-container medium-parallax">\r\n      <div class="parallax"><img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('app_home/media/background3.jpg" alt="Unsplashed background img 2"></div>\r\n  </div>\r\n\r\n  <footer class="page-footer teal">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col l6 s12">\r\n          <h5 class="white-text">About Us</h5>\r\n          <p class="grey-text text-lighten-4">The Colonial Heritage Foundation came about through the work and vision of several individuals who felt that something of great value was at risk of being lost in our great nation. Our dedicated team of volunteers sincerely believe in those values of hard-work, equality, opportunity, and freedom. We know that what America has to offer to its citizens and the world is of great value, and we sacrifice our free time (and some of our not-so-free time) in order to help history come alive in an effort to preserve that legacy.</p>\r\n        </div>\r\n        <div class="col l3 s12">\r\n          <h5 class="white-text">Legal</h5>\r\n          <ul>\r\n            <li><a class="white-text" href="#!">Link 1</a></li>\r\n          </ul>\r\n        </div>\r\n        <div class="col l3 s12">\r\n          <h5 class="white-text">Contact Us</h5>\r\n          <ul>\r\n            <li><a class="white-text" href="#!">Link 1</a></li>\r\n          </ul>\r\n        </div>\r\n      </div>\r\n    </div>\r\n    <div class="footer-copyright">\r\n      <div class="container">\r\n      Made by <a class="brown-text text-lighten-3" href="google.com">Bughatti</a>\r\n      </div>\r\n    </div>\r\n  </footer>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Kevin\\Development\\colonial\\app_home\\templates/index.html", "source_encoding": "ascii", "line_map": {"64": 46, "65": 59, "66": 59, "59": 20, "68": 72, "38": 1, "74": 68, "48": 3, "67": 72, "58": 3, "27": 0, "60": 20, "61": 33, "62": 33, "63": 46}, "uri": "index.html"}
__M_END_METADATA
"""
