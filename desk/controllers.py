#
# py4web app, AI-biorex ported 12.10.2021 08:22:27 UTC+3, src: https://github.com/dropways/deskapp

#
# https://github.com/ali96343/facep4w py4web apps
#
# http://py4web.com 
# http://py4web.com/_documentation/static/en/index.html 
#
#

import os, json, uuid
#
try:
   import ombott as bottle
except ImportError:
   import bottle
   #from py4web.core import bottle

from py4web import action, request, response,  abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from py4web.core import Template, Reloader
from py4web.utils.dbstore import DBStore
from py4web import Session, Cache, Translator, Flash, DAL

from py4web.utils.url_signer import URLSigner

from yatl.helpers import INPUT, H1, HTML, BODY, A, DIV, SPAN, P
from .common import db, session, T, cache, authenticated, unauthenticated, auth
from .settings import APP_NAME


#
# admin panel at APP_NAME/tabinfo
#
# ---------------------- Global -----------------------------------------------------

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)
url_signer = URLSigner(session)

Glb= {'debug': True , 'my_app_name': APP_NAME, 'tte_path': '/static/tte', }

# ---------------------- Utils -------------------------------------------------------

def get_ctrl_url(ctrl_nm):
    return "\'" + URL(ctrl_nm) + "\'"

def insert_form_vars(myform, mytable):

    ( row_id, table_row, f0_fld) = ( None, None, None )

    if Glb['debug'] == True:
        print("app:",Glb['my_app_name'])
        _ = [ print (f'     {k}: {v}') for k,v in myform.vars.items() if k != '_formkey']

    f0_name  = [ e for e in mytable.fields if e != 'id' ][0]
    f0_value = myform.vars.get( f0_name  , None )

    if f0_value and ( type( f0_value ) in (str, bytes, list, tuple, dict,) ) and len(f0_value):
        row_id = mytable.insert(**mytable._filter_fields(myform.vars))
        db.commit()

        if row_id:
            table_row = mytable(row_id )

            if table_row:
                if Glb['debug']:
                     print(f'     insert: \"{myform.vars[f0_name]}\" into {mytable[f0_name]}, id = {row_id}' )
                     print(f"     select: \"{table_row[f0_name]}\" from {mytable[f0_name]}, id = {row_id}" )
                     print ()
    else:
        if Glb['debug']:
            print( f"     no entry inserted: (f0_value is None) or (len(f0_value) == 0)")
            print()

    return row_id 



@action('callback', method="GET")
# Note that we do not use a template.  This is a JSON API, not a "web page".
@action.uses(url_signer.verify())
def callback():
     print("Called with:", dict(request.params))
     return dict(messages=request.params.echo)

#
def json2user(mess='mymess', icon_type = 'warning', js_alert='sweet2'):
    response.headers["Content-Type"] = "application/json"
    return json.dumps( {'messages' : f'{mess}', 'icon_type': icon_type, 'js_alert': js_alert})

# ---------------------- Controllers  ------------------------------------------------

@action('faq', method=["GET", "POST"] )
@action.uses(db, session, T, Template('faq.html', delimiters='[%[ ]]',))

def faq():
    ctrl_info= { 'c':'faq', 'v':'faq.html' }
    messages = ['faq', 'faq.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('faq') 


    # 
    ffaq0= Form(db.dffaq0, dbio=False, formstyle=FormStyleBulma)
    if ffaq0.accepted:
        icon_type ='success' if insert_form_vars(ffaq0, db.dffaq0) else 'info'
        return json2user(mess = str( ffaq0.form_name ), icon_type=icon_type )
    elif ffaq0.errors:
        print(f"ffaq0 has errors: {ffaq0.errors}")
        return json2user(mess = str(ffaq0.form_name), icon_type = 'error')

    return locals()

@action('X404', method=["GET", "POST"] )
@action.uses(db, session, T, Template('404.html', delimiters='[%[ ]]',))

def X404():
    ctrl_info= { 'c':'X404', 'v':'404.html' }
    messages = ['X404', '404.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('X404') 


    return locals()

@action('X500', method=["GET", "POST"] )
@action.uses(db, session, T, Template('500.html', delimiters='[%[ ]]',))

def X500():
    ctrl_info= { 'c':'X500', 'v':'500.html' }
    messages = ['X500', '500.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('X500') 


    return locals()

@action('X400', method=["GET", "POST"] )
@action.uses(db, session, T, Template('400.html', delimiters='[%[ ]]',))

def X400():
    ctrl_info= { 'c':'X400', 'v':'400.html' }
    messages = ['X400', '400.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('X400') 


    return locals()

@action('X503', method=["GET", "POST"] )
@action.uses(db, session, T, Template('503.html', delimiters='[%[ ]]',))

def X503():
    ctrl_info= { 'c':'X503', 'v':'503.html' }
    messages = ['X503', '503.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('X503') 


    return locals()

@action('X403', method=["GET", "POST"] )
@action.uses(db, session, T, Template('403.html', delimiters='[%[ ]]',))

def X403():
    ctrl_info= { 'c':'X403', 'v':'403.html' }
    messages = ['X403', '403.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('X403') 


    return locals()

@action('chat', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chat.html', delimiters='[%[ ]]',))

def chat():
    ctrl_info= { 'c':'chat', 'v':'chat.html' }
    messages = ['chat', 'chat.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('chat') 


    # 
    fchat0= Form(db.dfchat0, dbio=False, formstyle=FormStyleBulma)
    if fchat0.accepted:
        icon_type ='success' if insert_form_vars(fchat0, db.dfchat0) else 'info'
        return json2user(mess = str( fchat0.form_name ), icon_type=icon_type )
    elif fchat0.errors:
        print(f"fchat0 has errors: {fchat0.errors}")
        return json2user(mess = str(fchat0.form_name), icon_type = 'error')

    return locals()

@action('blog', method=["GET", "POST"] )
@action.uses(db, session, T, Template('blog.html', delimiters='[%[ ]]',))

def blog():
    ctrl_info= { 'c':'blog', 'v':'blog.html' }
    messages = ['blog', 'blog.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('blog') 


    # 
    fblog0= Form(db.dfblog0, dbio=False, formstyle=FormStyleBulma)
    if fblog0.accepted:
        icon_type ='success' if insert_form_vars(fblog0, db.dfblog0) else 'info'
        return json2user(mess = str( fblog0.form_name ), icon_type=icon_type )
    elif fblog0.errors:
        print(f"fblog0 has errors: {fblog0.errors}")
        return json2user(mess = str(fblog0.form_name), icon_type = 'error')

    return locals()

@action('loginA', method=["GET", "POST"] )
@action.uses(db, session, T, Template('login.html', delimiters='[%[ ]]',))

def loginA():
    ctrl_info= { 'c':'loginA', 'v':'login.html' }
    messages = ['loginA', 'login.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('loginA') 


    # 
    floginA0= Form(db.dfloginA0, dbio=False, formstyle=FormStyleBulma)
    if floginA0.accepted:
        icon_type ='success' if insert_form_vars(floginA0, db.dfloginA0) else 'info'
        return json2user(mess = str( floginA0.form_name ), icon_type=icon_type )
    elif floginA0.errors:
        print(f"floginA0 has errors: {floginA0.errors}")
        return json2user(mess = str(floginA0.form_name), icon_type = 'error')

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index.html', delimiters='[%[ ]]',))

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    messages = ['index', 'index.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('index') 


    rows_tindex0= db(db.tindex0).select()
    # 
    findex0= Form(db.dfindex0, dbio=False, formstyle=FormStyleBulma)
    if findex0.accepted:
        icon_type ='success' if insert_form_vars(findex0, db.dfindex0) else 'info'
        return json2user(mess = str( findex0.form_name ), icon_type=icon_type )
    elif findex0.errors:
        print(f"findex0 has errors: {findex0.errors}")
        return json2user(mess = str(findex0.form_name), icon_type = 'error')

    return locals()

@action('blank', method=["GET", "POST"] )
@action.uses(db, session, T, Template('blank.html', delimiters='[%[ ]]',))

def blank():
    ctrl_info= { 'c':'blank', 'v':'blank.html' }
    messages = ['blank', 'blank.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('blank') 


    # 
    fblank0= Form(db.dfblank0, dbio=False, formstyle=FormStyleBulma)
    if fblank0.accepted:
        icon_type ='success' if insert_form_vars(fblank0, db.dfblank0) else 'info'
        return json2user(mess = str( fblank0.form_name ), icon_type=icon_type )
    elif fblank0.errors:
        print(f"fblank0 has errors: {fblank0.errors}")
        return json2user(mess = str(fblank0.form_name), icon_type = 'error')

    return locals()

@action('index3', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index3.html', delimiters='[%[ ]]',))

def index3():
    ctrl_info= { 'c':'index3', 'v':'index3.html' }
    messages = ['index3', 'index3.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('index3') 


    rows_tindex30= db(db.tindex30).select()
    # 
    findex30= Form(db.dfindex30, dbio=False, formstyle=FormStyleBulma)
    if findex30.accepted:
        icon_type ='success' if insert_form_vars(findex30, db.dfindex30) else 'info'
        return json2user(mess = str( findex30.form_name ), icon_type=icon_type )
    elif findex30.errors:
        print(f"findex30 has errors: {findex30.errors}")
        return json2user(mess = str(findex30.form_name), icon_type = 'error')

    return locals()

@action('index2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index2.html', delimiters='[%[ ]]',))

def index2():
    ctrl_info= { 'c':'index2', 'v':'index2.html' }
    messages = ['index2', 'index2.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('index2') 


    # 
    findex20= Form(db.dfindex20, dbio=False, formstyle=FormStyleBulma)
    if findex20.accepted:
        icon_type ='success' if insert_form_vars(findex20, db.dfindex20) else 'info'
        return json2user(mess = str( findex20.form_name ), icon_type=icon_type )
    elif findex20.errors:
        print(f"findex20 has errors: {findex20.errors}")
        return json2user(mess = str(findex20.form_name), icon_type = 'error')

    return locals()

@action('themify', method=["GET", "POST"] )
@action.uses(db, session, T, Template('themify.html', delimiters='[%[ ]]',))

def themify():
    ctrl_info= { 'c':'themify', 'v':'themify.html' }
    messages = ['themify', 'themify.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('themify') 


    # 
    fthemify0= Form(db.dfthemify0, dbio=False, formstyle=FormStyleBulma)
    if fthemify0.accepted:
        icon_type ='success' if insert_form_vars(fthemify0, db.dfthemify0) else 'info'
        return json2user(mess = str( fthemify0.form_name ), icon_type=icon_type )
    elif fthemify0.errors:
        print(f"fthemify0 has errors: {fthemify0.errors}")
        return json2user(mess = str(fthemify0.form_name), icon_type = 'error')

    return locals()

@action('uiXtabs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-tabs.html', delimiters='[%[ ]]',))

def uiXtabs():
    ctrl_info= { 'c':'uiXtabs', 'v':'ui-tabs.html' }
    messages = ['uiXtabs', 'ui-tabs.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXtabs') 


    # 
    fuiXtabs0= Form(db.dfuiXtabs0, dbio=False, formstyle=FormStyleBulma)
    if fuiXtabs0.accepted:
        icon_type ='success' if insert_form_vars(fuiXtabs0, db.dfuiXtabs0) else 'info'
        return json2user(mess = str( fuiXtabs0.form_name ), icon_type=icon_type )
    elif fuiXtabs0.errors:
        print(f"fuiXtabs0 has errors: {fuiXtabs0.errors}")
        return json2user(mess = str(fuiXtabs0.form_name), icon_type = 'error')

    return locals()

@action('sitemap', method=["GET", "POST"] )
@action.uses(db, session, T, Template('sitemap.html', delimiters='[%[ ]]',))

def sitemap():
    ctrl_info= { 'c':'sitemap', 'v':'sitemap.html' }
    messages = ['sitemap', 'sitemap.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('sitemap') 


    # 
    fsitemap0= Form(db.dfsitemap0, dbio=False, formstyle=FormStyleBulma)
    if fsitemap0.accepted:
        icon_type ='success' if insert_form_vars(fsitemap0, db.dfsitemap0) else 'info'
        return json2user(mess = str( fsitemap0.form_name ), icon_type=icon_type )
    elif fsitemap0.errors:
        print(f"fsitemap0 has errors: {fsitemap0.errors}")
        return json2user(mess = str(fsitemap0.form_name), icon_type = 'error')

    return locals()

@action('profileA', method=["GET", "POST"] )
@action.uses(db, session, T, Template('profile.html', delimiters='[%[ ]]',))

def profileA():
    ctrl_info= { 'c':'profileA', 'v':'profile.html' }
    messages = ['profileA', 'profile.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('profileA') 


    # 
    fprofileA0= Form(db.dfprofileA0, dbio=False, formstyle=FormStyleBulma)
    if fprofileA0.accepted:
        icon_type ='success' if insert_form_vars(fprofileA0, db.dfprofileA0) else 'info'
        return json2user(mess = str( fprofileA0.form_name ), icon_type=icon_type )
    elif fprofileA0.errors:
        print(f"fprofileA0 has errors: {fprofileA0.errors}")
        return json2user(mess = str(fprofileA0.form_name), icon_type = 'error')

    # 
    fprofileA1= Form(db.dfprofileA1, dbio=False, formstyle=FormStyleBulma)
    if fprofileA1.accepted:
        icon_type ='success' if insert_form_vars(fprofileA1, db.dfprofileA1) else 'info'
        return json2user(mess = str( fprofileA1.form_name ), icon_type=icon_type )
    elif fprofileA1.errors:
        print(f"fprofileA1 has errors: {fprofileA1.errors}")
        return json2user(mess = str(fprofileA1.form_name), icon_type = 'error')

    # 
    fprofileA2= Form(db.dfprofileA2, dbio=False, formstyle=FormStyleBulma)
    if fprofileA2.accepted:
        icon_type ='success' if insert_form_vars(fprofileA2, db.dfprofileA2) else 'info'
        return json2user(mess = str( fprofileA2.form_name ), icon_type=icon_type )
    elif fprofileA2.errors:
        print(f"fprofileA2 has errors: {fprofileA2.errors}")
        return json2user(mess = str(fprofileA2.form_name), icon_type = 'error')

    # 
    fprofileA3= Form(db.dfprofileA3, dbio=False, formstyle=FormStyleBulma)
    if fprofileA3.accepted:
        icon_type ='success' if insert_form_vars(fprofileA3, db.dfprofileA3) else 'info'
        return json2user(mess = str( fprofileA3.form_name ), icon_type=icon_type )
    elif fprofileA3.errors:
        print(f"fprofileA3 has errors: {fprofileA3.errors}")
        return json2user(mess = str(fprofileA3.form_name), icon_type = 'error')

    return locals()

@action('product', method=["GET", "POST"] )
@action.uses(db, session, T, Template('product.html', delimiters='[%[ ]]',))

def product():
    ctrl_info= { 'c':'product', 'v':'product.html' }
    messages = ['product', 'product.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('product') 


    # 
    fproduct0= Form(db.dfproduct0, dbio=False, formstyle=FormStyleBulma)
    if fproduct0.accepted:
        icon_type ='success' if insert_form_vars(fproduct0, db.dfproduct0) else 'info'
        return json2user(mess = str( fproduct0.form_name ), icon_type=icon_type )
    elif fproduct0.errors:
        print(f"fproduct0 has errors: {fproduct0.errors}")
        return json2user(mess = str(fproduct0.form_name), icon_type = 'error')

    return locals()

@action('invoice', method=["GET", "POST"] )
@action.uses(db, session, T, Template('invoice.html', delimiters='[%[ ]]',))

def invoice():
    ctrl_info= { 'c':'invoice', 'v':'invoice.html' }
    messages = ['invoice', 'invoice.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('invoice') 


    # 
    finvoice0= Form(db.dfinvoice0, dbio=False, formstyle=FormStyleBulma)
    if finvoice0.accepted:
        icon_type ='success' if insert_form_vars(finvoice0, db.dfinvoice0) else 'info'
        return json2user(mess = str( finvoice0.form_name ), icon_type=icon_type )
    elif finvoice0.errors:
        print(f"finvoice0 has errors: {finvoice0.errors}")
        return json2user(mess = str(finvoice0.form_name), icon_type = 'error')

    return locals()

@action('gallery', method=["GET", "POST"] )
@action.uses(db, session, T, Template('gallery.html', delimiters='[%[ ]]',))

def gallery():
    ctrl_info= { 'c':'gallery', 'v':'gallery.html' }
    messages = ['gallery', 'gallery.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('gallery') 


    # 
    fgallery0= Form(db.dfgallery0, dbio=False, formstyle=FormStyleBulma)
    if fgallery0.accepted:
        icon_type ='success' if insert_form_vars(fgallery0, db.dfgallery0) else 'info'
        return json2user(mess = str( fgallery0.form_name ), icon_type=icon_type )
    elif fgallery0.errors:
        print(f"fgallery0 has errors: {fgallery0.errors}")
        return json2user(mess = str(fgallery0.form_name), icon_type = 'error')

    return locals()

@action('ionicons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ionicons.html', delimiters='[%[ ]]',))

def ionicons():
    ctrl_info= { 'c':'ionicons', 'v':'ionicons.html' }
    messages = ['ionicons', 'ionicons.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('ionicons') 


    # 
    fionicons0= Form(db.dfionicons0, dbio=False, formstyle=FormStyleBulma)
    if fionicons0.accepted:
        icon_type ='success' if insert_form_vars(fionicons0, db.dfionicons0) else 'info'
        return json2user(mess = str( fionicons0.form_name ), icon_type=icon_type )
    elif fionicons0.errors:
        print(f"fionicons0 has errors: {fionicons0.errors}")
        return json2user(mess = str(fionicons0.form_name), icon_type = 'error')

    return locals()

@action('uiXcards', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-cards.html', delimiters='[%[ ]]',))

def uiXcards():
    ctrl_info= { 'c':'uiXcards', 'v':'ui-cards.html' }
    messages = ['uiXcards', 'ui-cards.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXcards') 


    # 
    fuiXcards0= Form(db.dfuiXcards0, dbio=False, formstyle=FormStyleBulma)
    if fuiXcards0.accepted:
        icon_type ='success' if insert_form_vars(fuiXcards0, db.dfuiXcards0) else 'info'
        return json2user(mess = str( fuiXcards0.form_name ), icon_type=icon_type )
    elif fuiXcards0.errors:
        print(f"fuiXcards0 has errors: {fuiXcards0.errors}")
        return json2user(mess = str(fuiXcards0.form_name), icon_type = 'error')

    return locals()

@action('registerA', method=["GET", "POST"] )
@action.uses(db, session, T, Template('register.html', delimiters='[%[ ]]',))

def registerA():
    ctrl_info= { 'c':'registerA', 'v':'register.html' }
    messages = ['registerA', 'register.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('registerA') 


    # 
    fregisterA0= Form(db.dfregisterA0, dbio=False, formstyle=FormStyleBulma)
    if fregisterA0.accepted:
        icon_type ='success' if insert_form_vars(fregisterA0, db.dfregisterA0) else 'info'
        return json2user(mess = str( fregisterA0.form_name ), icon_type=icon_type )
    elif fregisterA0.errors:
        print(f"fregisterA0 has errors: {fregisterA0.errors}")
        return json2user(mess = str(fregisterA0.form_name), icon_type = 'error')

    return locals()

@action('calendar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('calendar.html', delimiters='[%[ ]]',))

def calendar():
    ctrl_info= { 'c':'calendar', 'v':'calendar.html' }
    messages = ['calendar', 'calendar.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('calendar') 


    # 
    fcalendar0= Form(db.dfcalendar0, dbio=False, formstyle=FormStyleBulma)
    if fcalendar0.accepted:
        icon_type ='success' if insert_form_vars(fcalendar0, db.dfcalendar0) else 'info'
        return json2user(mess = str( fcalendar0.form_name ), icon_type=icon_type )
    elif fcalendar0.errors:
        print(f"fcalendar0 has errors: {fcalendar0.errors}")
        return json2user(mess = str(fcalendar0.form_name), icon_type = 'error')

    # 
    fcalendar1= Form(db.dfcalendar1, dbio=False, formstyle=FormStyleBulma)
    if fcalendar1.accepted:
        icon_type ='success' if insert_form_vars(fcalendar1, db.dfcalendar1) else 'info'
        return json2user(mess = str( fcalendar1.form_name ), icon_type=icon_type )
    elif fcalendar1.errors:
        print(f"fcalendar1 has errors: {fcalendar1.errors}")
        return json2user(mess = str(fcalendar1.form_name), icon_type = 'error')

    return locals()

@action('uiXmodals', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-modals.html', delimiters='[%[ ]]',))

def uiXmodals():
    ctrl_info= { 'c':'uiXmodals', 'v':'ui-modals.html' }
    messages = ['uiXmodals', 'ui-modals.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXmodals') 


    # 
    fuiXmodals0= Form(db.dfuiXmodals0, dbio=False, formstyle=FormStyleBulma)
    if fuiXmodals0.accepted:
        icon_type ='success' if insert_form_vars(fuiXmodals0, db.dfuiXmodals0) else 'info'
        return json2user(mess = str( fuiXmodals0.form_name ), icon_type=icon_type )
    elif fuiXmodals0.errors:
        print(f"fuiXmodals0 has errors: {fuiXmodals0.errors}")
        return json2user(mess = str(fuiXmodals0.form_name), icon_type = 'error')

    # 
    fuiXmodals1= Form(db.dfuiXmodals1, dbio=False, formstyle=FormStyleBulma)
    if fuiXmodals1.accepted:
        icon_type ='success' if insert_form_vars(fuiXmodals1, db.dfuiXmodals1) else 'info'
        return json2user(mess = str( fuiXmodals1.form_name ), icon_type=icon_type )
    elif fuiXmodals1.errors:
        print(f"fuiXmodals1 has errors: {fuiXmodals1.errors}")
        return json2user(mess = str(fuiXmodals1.form_name), icon_type = 'error')

    return locals()

@action('highchart', method=["GET", "POST"] )
@action.uses(db, session, T, Template('highchart.html', delimiters='[%[ ]]',))

def highchart():
    ctrl_info= { 'c':'highchart', 'v':'highchart.html' }
    messages = ['highchart', 'highchart.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('highchart') 


    # 
    fhighchart0= Form(db.dfhighchart0, dbio=False, formstyle=FormStyleBulma)
    if fhighchart0.accepted:
        icon_type ='success' if insert_form_vars(fhighchart0, db.dfhighchart0) else 'info'
        return json2user(mess = str( fhighchart0.form_name ), icon_type=icon_type )
    elif fhighchart0.errors:
        print(f"fhighchart0 has errors: {fhighchart0.errors}")
        return json2user(mess = str(fhighchart0.form_name), icon_type = 'error')

    return locals()

@action('datatable', method=["GET", "POST"] )
@action.uses(db, session, T, Template('datatable.html', delimiters='[%[ ]]',))

def datatable():
    ctrl_info= { 'c':'datatable', 'v':'datatable.html' }
    messages = ['datatable', 'datatable.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('datatable') 


    rows_tdatatable0= db(db.tdatatable0).select()
    rows_tdatatable1= db(db.tdatatable1).select()
    rows_tdatatable2= db(db.tdatatable2).select()
    rows_tdatatable3= db(db.tdatatable3).select()
    # 
    fdatatable0= Form(db.dfdatatable0, dbio=False, formstyle=FormStyleBulma)
    if fdatatable0.accepted:
        icon_type ='success' if insert_form_vars(fdatatable0, db.dfdatatable0) else 'info'
        return json2user(mess = str( fdatatable0.form_name ), icon_type=icon_type )
    elif fdatatable0.errors:
        print(f"fdatatable0 has errors: {fdatatable0.errors}")
        return json2user(mess = str(fdatatable0.form_name), icon_type = 'error')

    return locals()

@action('foundation', method=["GET", "POST"] )
@action.uses(db, session, T, Template('foundation.html', delimiters='[%[ ]]',))

def foundation():
    ctrl_info= { 'c':'foundation', 'v':'foundation.html' }
    messages = ['foundation', 'foundation.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('foundation') 


    # 
    ffoundation0= Form(db.dffoundation0, dbio=False, formstyle=FormStyleBulma)
    if ffoundation0.accepted:
        icon_type ='success' if insert_form_vars(ffoundation0, db.dffoundation0) else 'info'
        return json2user(mess = str( ffoundation0.form_name ), icon_type=icon_type )
    elif ffoundation0.errors:
        print(f"ffoundation0 has errors: {ffoundation0.errors}")
        return json2user(mess = str(ffoundation0.form_name), icon_type = 'error')

    return locals()

@action('uiXbuttons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-buttons.html', delimiters='[%[ ]]',))

def uiXbuttons():
    ctrl_info= { 'c':'uiXbuttons', 'v':'ui-buttons.html' }
    messages = ['uiXbuttons', 'ui-buttons.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXbuttons') 


    # 
    fuiXbuttons0= Form(db.dfuiXbuttons0, dbio=False, formstyle=FormStyleBulma)
    if fuiXbuttons0.accepted:
        icon_type ='success' if insert_form_vars(fuiXbuttons0, db.dfuiXbuttons0) else 'info'
        return json2user(mess = str( fuiXbuttons0.form_name ), icon_type=icon_type )
    elif fuiXbuttons0.errors:
        print(f"fuiXbuttons0 has errors: {fuiXbuttons0.errors}")
        return json2user(mess = str(fuiXbuttons0.form_name), icon_type = 'error')

    return locals()

@action('jvectormap', method=["GET", "POST"] )
@action.uses(db, session, T, Template('jvectormap.html', delimiters='[%[ ]]',))

def jvectormap():
    ctrl_info= { 'c':'jvectormap', 'v':'jvectormap.html' }
    messages = ['jvectormap', 'jvectormap.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('jvectormap') 


    # 
    fjvectormap0= Form(db.dfjvectormap0, dbio=False, formstyle=FormStyleBulma)
    if fjvectormap0.accepted:
        icon_type ='success' if insert_form_vars(fjvectormap0, db.dfjvectormap0) else 'info'
        return json2user(mess = str( fjvectormap0.form_name ), icon_type=icon_type )
    elif fjvectormap0.errors:
        print(f"fjvectormap0 has errors: {fjvectormap0.errors}")
        return json2user(mess = str(fjvectormap0.form_name), icon_type = 'error')

    return locals()

@action('knobXchart', method=["GET", "POST"] )
@action.uses(db, session, T, Template('knob-chart.html', delimiters='[%[ ]]',))

def knobXchart():
    ctrl_info= { 'c':'knobXchart', 'v':'knob-chart.html' }
    messages = ['knobXchart', 'knob-chart.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('knobXchart') 


    # 
    fknobXchart0= Form(db.dfknobXchart0, dbio=False, formstyle=FormStyleBulma)
    if fknobXchart0.accepted:
        icon_type ='success' if insert_form_vars(fknobXchart0, db.dfknobXchart0) else 'info'
        return json2user(mess = str( fknobXchart0.form_name ), icon_type=icon_type )
    elif fknobXchart0.errors:
        print(f"fknobXchart0 has errors: {fknobXchart0.errors}")
        return json2user(mess = str(fknobXchart0.form_name), icon_type = 'error')

    return locals()

@action('formXbasic', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form-basic.html', delimiters='[%[ ]]',))

def formXbasic():
    ctrl_info= { 'c':'formXbasic', 'v':'form-basic.html' }
    messages = ['formXbasic', 'form-basic.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('formXbasic') 


    # 
    fformXbasic0= Form(db.dfformXbasic0, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic0.accepted:
        icon_type ='success' if insert_form_vars(fformXbasic0, db.dfformXbasic0) else 'info'
        return json2user(mess = str( fformXbasic0.form_name ), icon_type=icon_type )
    elif fformXbasic0.errors:
        print(f"fformXbasic0 has errors: {fformXbasic0.errors}")
        return json2user(mess = str(fformXbasic0.form_name), icon_type = 'error')

    # 
    fformXbasic1= Form(db.dfformXbasic1, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic1.accepted:
        icon_type ='success' if insert_form_vars(fformXbasic1, db.dfformXbasic1) else 'info'
        return json2user(mess = str( fformXbasic1.form_name ), icon_type=icon_type )
    elif fformXbasic1.errors:
        print(f"fformXbasic1 has errors: {fformXbasic1.errors}")
        return json2user(mess = str(fformXbasic1.form_name), icon_type = 'error')

    # 
    fformXbasic2= Form(db.dfformXbasic2, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic2.accepted:
        icon_type ='success' if insert_form_vars(fformXbasic2, db.dfformXbasic2) else 'info'
        return json2user(mess = str( fformXbasic2.form_name ), icon_type=icon_type )
    elif fformXbasic2.errors:
        print(f"fformXbasic2 has errors: {fformXbasic2.errors}")
        return json2user(mess = str(fformXbasic2.form_name), icon_type = 'error')

    # 
    fformXbasic3= Form(db.dfformXbasic3, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic3.accepted:
        icon_type ='success' if insert_form_vars(fformXbasic3, db.dfformXbasic3) else 'info'
        return json2user(mess = str( fformXbasic3.form_name ), icon_type=icon_type )
    elif fformXbasic3.errors:
        print(f"fformXbasic3 has errors: {fformXbasic3.errors}")
        return json2user(mess = str(fformXbasic3.form_name), icon_type = 'error')

    # 
    fformXbasic4= Form(db.dfformXbasic4, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic4.accepted:
        icon_type ='success' if insert_form_vars(fformXbasic4, db.dfformXbasic4) else 'info'
        return json2user(mess = str( fformXbasic4.form_name ), icon_type=icon_type )
    elif fformXbasic4.errors:
        print(f"fformXbasic4 has errors: {fformXbasic4.errors}")
        return json2user(mess = str(fformXbasic4.form_name), icon_type = 'error')

    # 
    fformXbasic5= Form(db.dfformXbasic5, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic5.accepted:
        icon_type ='success' if insert_form_vars(fformXbasic5, db.dfformXbasic5) else 'info'
        return json2user(mess = str( fformXbasic5.form_name ), icon_type=icon_type )
    elif fformXbasic5.errors:
        print(f"fformXbasic5 has errors: {fformXbasic5.errors}")
        return json2user(mess = str(fformXbasic5.form_name), icon_type = 'error')

    # 
    fformXbasic6= Form(db.dfformXbasic6, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic6.accepted:
        icon_type ='success' if insert_form_vars(fformXbasic6, db.dfformXbasic6) else 'info'
        return json2user(mess = str( fformXbasic6.form_name ), icon_type=icon_type )
    elif fformXbasic6.errors:
        print(f"fformXbasic6 has errors: {fformXbasic6.errors}")
        return json2user(mess = str(fformXbasic6.form_name), icon_type = 'error')

    # 
    fformXbasic7= Form(db.dfformXbasic7, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic7.accepted:
        icon_type ='success' if insert_form_vars(fformXbasic7, db.dfformXbasic7) else 'info'
        return json2user(mess = str( fformXbasic7.form_name ), icon_type=icon_type )
    elif fformXbasic7.errors:
        print(f"fformXbasic7 has errors: {fformXbasic7.errors}")
        return json2user(mess = str(fformXbasic7.form_name), icon_type = 'error')

    # 
    fformXbasic8= Form(db.dfformXbasic8, dbio=False, formstyle=FormStyleBulma)
    if fformXbasic8.accepted:
        icon_type ='success' if insert_form_vars(fformXbasic8, db.dfformXbasic8) else 'info'
        return json2user(mess = str( fformXbasic8.form_name ), icon_type=icon_type )
    elif fformXbasic8.errors:
        print(f"fformXbasic8 has errors: {fformXbasic8.errors}")
        return json2user(mess = str(fformXbasic8.form_name), icon_type = 'error')

    return locals()

@action('apexcharts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('apexcharts.html', delimiters='[%[ ]]',))

def apexcharts():
    ctrl_info= { 'c':'apexcharts', 'v':'apexcharts.html' }
    messages = ['apexcharts', 'apexcharts.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('apexcharts') 


    # 
    fapexcharts0= Form(db.dfapexcharts0, dbio=False, formstyle=FormStyleBulma)
    if fapexcharts0.accepted:
        icon_type ='success' if insert_form_vars(fapexcharts0, db.dfapexcharts0) else 'info'
        return json2user(mess = str( fapexcharts0.form_name ), icon_type=icon_type )
    elif fapexcharts0.errors:
        print(f"fapexcharts0 has errors: {fapexcharts0.errors}")
        return json2user(mess = str(fapexcharts0.form_name), icon_type = 'error')

    return locals()

@action('uiXcarousel', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-carousel.html', delimiters='[%[ ]]',))

def uiXcarousel():
    ctrl_info= { 'c':'uiXcarousel', 'v':'ui-carousel.html' }
    messages = ['uiXcarousel', 'ui-carousel.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXcarousel') 


    # 
    fuiXcarousel0= Form(db.dfuiXcarousel0, dbio=False, formstyle=FormStyleBulma)
    if fuiXcarousel0.accepted:
        icon_type ='success' if insert_form_vars(fuiXcarousel0, db.dfuiXcarousel0) else 'info'
        return json2user(mess = str( fuiXcarousel0.form_name ), icon_type=icon_type )
    elif fuiXcarousel0.errors:
        print(f"fuiXcarousel0 has errors: {fuiXcarousel0.errors}")
        return json2user(mess = str(fuiXcarousel0.form_name), icon_type = 'error')

    return locals()

@action('uiXtimeline', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-timeline.html', delimiters='[%[ ]]',))

def uiXtimeline():
    ctrl_info= { 'c':'uiXtimeline', 'v':'ui-timeline.html' }
    messages = ['uiXtimeline', 'ui-timeline.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXtimeline') 


    # 
    fuiXtimeline0= Form(db.dfuiXtimeline0, dbio=False, formstyle=FormStyleBulma)
    if fuiXtimeline0.accepted:
        icon_type ='success' if insert_form_vars(fuiXtimeline0, db.dfuiXtimeline0) else 'info'
        return json2user(mess = str( fuiXtimeline0.form_name ), icon_type=icon_type )
    elif fuiXtimeline0.errors:
        print(f"fuiXtimeline0 has errors: {fuiXtimeline0.errors}")
        return json2user(mess = str(fuiXtimeline0.form_name), icon_type = 'error')

    return locals()

@action('formXwizard', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form-wizard.html', delimiters='[%[ ]]',))

def formXwizard():
    ctrl_info= { 'c':'formXwizard', 'v':'form-wizard.html' }
    messages = ['formXwizard', 'form-wizard.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('formXwizard') 


    # 
    fformXwizard0= Form(db.dfformXwizard0, dbio=False, formstyle=FormStyleBulma)
    if fformXwizard0.accepted:
        icon_type ='success' if insert_form_vars(fformXwizard0, db.dfformXwizard0) else 'info'
        return json2user(mess = str( fformXwizard0.form_name ), icon_type=icon_type )
    elif fformXwizard0.errors:
        print(f"fformXwizard0 has errors: {fformXwizard0.errors}")
        return json2user(mess = str(fformXwizard0.form_name), icon_type = 'error')

    # 
    fformXwizard1= Form(db.dfformXwizard1, dbio=False, formstyle=FormStyleBulma)
    if fformXwizard1.accepted:
        icon_type ='success' if insert_form_vars(fformXwizard1, db.dfformXwizard1) else 'info'
        return json2user(mess = str( fformXwizard1.form_name ), icon_type=icon_type )
    elif fformXwizard1.errors:
        print(f"fformXwizard1 has errors: {fformXwizard1.errors}")
        return json2user(mess = str(fformXwizard1.form_name), icon_type = 'error')

    # 
    fformXwizard2= Form(db.dfformXwizard2, dbio=False, formstyle=FormStyleBulma)
    if fformXwizard2.accepted:
        icon_type ='success' if insert_form_vars(fformXwizard2, db.dfformXwizard2) else 'info'
        return json2user(mess = str( fformXwizard2.form_name ), icon_type=icon_type )
    elif fformXwizard2.errors:
        print(f"fformXwizard2 has errors: {fformXwizard2.errors}")
        return json2user(mess = str(fformXwizard2.form_name), icon_type = 'error')

    return locals()

@action('customXicon', method=["GET", "POST"] )
@action.uses(db, session, T, Template('custom-icon.html', delimiters='[%[ ]]',))

def customXicon():
    ctrl_info= { 'c':'customXicon', 'v':'custom-icon.html' }
    messages = ['customXicon', 'custom-icon.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('customXicon') 


    # 
    fcustomXicon0= Form(db.dfcustomXicon0, dbio=False, formstyle=FormStyleBulma)
    if fcustomXicon0.accepted:
        icon_type ='success' if insert_form_vars(fcustomXicon0, db.dfcustomXicon0) else 'info'
        return json2user(mess = str( fcustomXicon0.form_name ), icon_type=icon_type )
    elif fcustomXicon0.errors:
        print(f"fcustomXicon0 has errors: {fcustomXicon0.errors}")
        return json2user(mess = str(fcustomXicon0.form_name), icon_type = 'error')

    return locals()

@action('basicXtable', method=["GET", "POST"] )
@action.uses(db, session, T, Template('basic-table.html', delimiters='[%[ ]]',))

def basicXtable():
    ctrl_info= { 'c':'basicXtable', 'v':'basic-table.html' }
    messages = ['basicXtable', 'basic-table.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('basicXtable') 


    rows_tbasicXtable0= db(db.tbasicXtable0).select()
    rows_tbasicXtable1= db(db.tbasicXtable1).select()
    rows_tbasicXtable2= db(db.tbasicXtable2).select()
    rows_tbasicXtable3= db(db.tbasicXtable3).select()
    rows_tbasicXtable4= db(db.tbasicXtable4).select()
    rows_tbasicXtable5= db(db.tbasicXtable5).select()
    rows_tbasicXtable6= db(db.tbasicXtable6).select()
    rows_tbasicXtable7= db(db.tbasicXtable7).select()
    rows_tbasicXtable8= db(db.tbasicXtable8).select()
    rows_tbasicXtable9= db(db.tbasicXtable9).select()
    # 
    fbasicXtable0= Form(db.dfbasicXtable0, dbio=False, formstyle=FormStyleBulma)
    if fbasicXtable0.accepted:
        icon_type ='success' if insert_form_vars(fbasicXtable0, db.dfbasicXtable0) else 'info'
        return json2user(mess = str( fbasicXtable0.form_name ), icon_type=icon_type )
    elif fbasicXtable0.errors:
        print(f"fbasicXtable0 has errors: {fbasicXtable0.errors}")
        return json2user(mess = str(fbasicXtable0.form_name), icon_type = 'error')

    return locals()

@action('blogXdetail', method=["GET", "POST"] )
@action.uses(db, session, T, Template('blog-detail.html', delimiters='[%[ ]]',))

def blogXdetail():
    ctrl_info= { 'c':'blogXdetail', 'v':'blog-detail.html' }
    messages = ['blogXdetail', 'blog-detail.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('blogXdetail') 


    # 
    fblogXdetail0= Form(db.dfblogXdetail0, dbio=False, formstyle=FormStyleBulma)
    if fblogXdetail0.accepted:
        icon_type ='success' if insert_form_vars(fblogXdetail0, db.dfblogXdetail0) else 'info'
        return json2user(mess = str( fblogXdetail0.form_name ), icon_type=icon_type )
    elif fblogXdetail0.errors:
        print(f"fblogXdetail0 has errors: {fblogXdetail0.errors}")
        return json2user(mess = str(fblogXdetail0.form_name), icon_type = 'error')

    return locals()

@action('fontXawesome', method=["GET", "POST"] )
@action.uses(db, session, T, Template('font-awesome.html', delimiters='[%[ ]]',))

def fontXawesome():
    ctrl_info= { 'c':'fontXawesome', 'v':'font-awesome.html' }
    messages = ['fontXawesome', 'font-awesome.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('fontXawesome') 


    # 
    ffontXawesome0= Form(db.dffontXawesome0, dbio=False, formstyle=FormStyleBulma)
    if ffontXawesome0.accepted:
        icon_type ='success' if insert_form_vars(ffontXawesome0, db.dffontXawesome0) else 'info'
        return json2user(mess = str( ffontXawesome0.form_name ), icon_type=icon_type )
    elif ffontXawesome0.errors:
        print(f"ffontXawesome0 has errors: {ffontXawesome0.errors}")
        return json2user(mess = str(ffontXawesome0.form_name), icon_type = 'error')

    return locals()

@action('videoXplayer', method=["GET", "POST"] )
@action.uses(db, session, T, Template('video-player.html', delimiters='[%[ ]]',))

def videoXplayer():
    ctrl_info= { 'c':'videoXplayer', 'v':'video-player.html' }
    messages = ['videoXplayer', 'video-player.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('videoXplayer') 


    # 
    fvideoXplayer0= Form(db.dfvideoXplayer0, dbio=False, formstyle=FormStyleBulma)
    if fvideoXplayer0.accepted:
        icon_type ='success' if insert_form_vars(fvideoXplayer0, db.dfvideoXplayer0) else 'info'
        return json2user(mess = str( fvideoXplayer0.form_name ), icon_type=icon_type )
    elif fvideoXplayer0.errors:
        print(f"fvideoXplayer0 has errors: {fvideoXplayer0.errors}")
        return json2user(mess = str(fvideoXplayer0.form_name), icon_type = 'error')

    return locals()

@action('introduction', method=["GET", "POST"] )
@action.uses(db, session, T, Template('introduction.html', delimiters='[%[ ]]',))

def introduction():
    ctrl_info= { 'c':'introduction', 'v':'introduction.html' }
    messages = ['introduction', 'introduction.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('introduction') 


    # 
    fintroduction0= Form(db.dfintroduction0, dbio=False, formstyle=FormStyleBulma)
    if fintroduction0.accepted:
        icon_type ='success' if insert_form_vars(fintroduction0, db.dfintroduction0) else 'info'
        return json2user(mess = str( fintroduction0.form_name ), icon_type=icon_type )
    elif fintroduction0.errors:
        print(f"fintroduction0 has errors: {fintroduction0.errors}")
        return json2user(mess = str(fintroduction0.form_name), icon_type = 'error')

    return locals()

@action('formXpickers', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form-pickers.html', delimiters='[%[ ]]',))

def formXpickers():
    ctrl_info= { 'c':'formXpickers', 'v':'form-pickers.html' }
    messages = ['formXpickers', 'form-pickers.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('formXpickers') 


    # 
    fformXpickers0= Form(db.dfformXpickers0, dbio=False, formstyle=FormStyleBulma)
    if fformXpickers0.accepted:
        icon_type ='success' if insert_form_vars(fformXpickers0, db.dfformXpickers0) else 'info'
        return json2user(mess = str( fformXpickers0.form_name ), icon_type=icon_type )
    elif fformXpickers0.errors:
        print(f"fformXpickers0 has errors: {fformXpickers0.errors}")
        return json2user(mess = str(fformXpickers0.form_name), icon_type = 'error')

    # 
    fformXpickers1= Form(db.dfformXpickers1, dbio=False, formstyle=FormStyleBulma)
    if fformXpickers1.accepted:
        icon_type ='success' if insert_form_vars(fformXpickers1, db.dfformXpickers1) else 'info'
        return json2user(mess = str( fformXpickers1.form_name ), icon_type=icon_type )
    elif fformXpickers1.errors:
        print(f"fformXpickers1 has errors: {fformXpickers1.errors}")
        return json2user(mess = str(fformXpickers1.form_name), icon_type = 'error')

    # 
    fformXpickers2= Form(db.dfformXpickers2, dbio=False, formstyle=FormStyleBulma)
    if fformXpickers2.accepted:
        icon_type ='success' if insert_form_vars(fformXpickers2, db.dfformXpickers2) else 'info'
        return json2user(mess = str( fformXpickers2.form_name ), icon_type=icon_type )
    elif fformXpickers2.errors:
        print(f"fformXpickers2 has errors: {fformXpickers2.errors}")
        return json2user(mess = str(fformXpickers2.form_name), icon_type = 'error')

    return locals()

@action('html5Xeditor', method=["GET", "POST"] )
@action.uses(db, session, T, Template('html5-editor.html', delimiters='[%[ ]]',))

def html5Xeditor():
    ctrl_info= { 'c':'html5Xeditor', 'v':'html5-editor.html' }
    messages = ['html5Xeditor', 'html5-editor.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('html5Xeditor') 


    # 
    fhtml5Xeditor0= Form(db.dfhtml5Xeditor0, dbio=False, formstyle=FormStyleBulma)
    if fhtml5Xeditor0.accepted:
        icon_type ='success' if insert_form_vars(fhtml5Xeditor0, db.dfhtml5Xeditor0) else 'info'
        return json2user(mess = str( fhtml5Xeditor0.form_name ), icon_type=icon_type )
    elif fhtml5Xeditor0.errors:
        print(f"fhtml5Xeditor0 has errors: {fhtml5Xeditor0.errors}")
        return json2user(mess = str(fhtml5Xeditor0.form_name), icon_type = 'error')

    return locals()

@action('uiXtypography', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-typography.html', delimiters='[%[ ]]',))

def uiXtypography():
    ctrl_info= { 'c':'uiXtypography', 'v':'ui-typography.html' }
    messages = ['uiXtypography', 'ui-typography.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXtypography') 


    # 
    fuiXtypography0= Form(db.dfuiXtypography0, dbio=False, formstyle=FormStyleBulma)
    if fuiXtypography0.accepted:
        icon_type ='success' if insert_form_vars(fuiXtypography0, db.dfuiXtypography0) else 'info'
        return json2user(mess = str( fuiXtypography0.form_name ), icon_type=icon_type )
    elif fuiXtypography0.errors:
        print(f"fuiXtypography0 has errors: {fuiXtypography0.errors}")
        return json2user(mess = str(fuiXtypography0.form_name), icon_type = 'error')

    return locals()

@action('uiXlistXgroup', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-list-group.html', delimiters='[%[ ]]',))

def uiXlistXgroup():
    ctrl_info= { 'c':'uiXlistXgroup', 'v':'ui-list-group.html' }
    messages = ['uiXlistXgroup', 'ui-list-group.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXlistXgroup') 


    # 
    fuiXlistXgroup0= Form(db.dfuiXlistXgroup0, dbio=False, formstyle=FormStyleBulma)
    if fuiXlistXgroup0.accepted:
        icon_type ='success' if insert_form_vars(fuiXlistXgroup0, db.dfuiXlistXgroup0) else 'info'
        return json2user(mess = str( fuiXlistXgroup0.form_name ), icon_type=icon_type )
    elif fuiXlistXgroup0.errors:
        print(f"fuiXlistXgroup0 has errors: {fuiXlistXgroup0.errors}")
        return json2user(mess = str(fuiXlistXgroup0.form_name), icon_type = 'error')

    return locals()

@action('pricingXtable', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pricing-table.html', delimiters='[%[ ]]',))

def pricingXtable():
    ctrl_info= { 'c':'pricingXtable', 'v':'pricing-table.html' }
    messages = ['pricingXtable', 'pricing-table.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('pricingXtable') 


    # 
    fpricingXtable0= Form(db.dfpricingXtable0, dbio=False, formstyle=FormStyleBulma)
    if fpricingXtable0.accepted:
        icon_type ='success' if insert_form_vars(fpricingXtable0, db.dfpricingXtable0) else 'info'
        return json2user(mess = str( fpricingXtable0.form_name ), icon_type=icon_type )
    elif fpricingXtable0.errors:
        print(f"fpricingXtable0 has errors: {fpricingXtable0.errors}")
        return json2user(mess = str(fpricingXtable0.form_name), icon_type = 'error')

    return locals()

@action('imageXcropper', method=["GET", "POST"] )
@action.uses(db, session, T, Template('image-cropper.html', delimiters='[%[ ]]',))

def imageXcropper():
    ctrl_info= { 'c':'imageXcropper', 'v':'image-cropper.html' }
    messages = ['imageXcropper', 'image-cropper.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('imageXcropper') 


    # 
    fimageXcropper0= Form(db.dfimageXcropper0, dbio=False, formstyle=FormStyleBulma)
    if fimageXcropper0.accepted:
        icon_type ='success' if insert_form_vars(fimageXcropper0, db.dfimageXcropper0) else 'info'
        return json2user(mess = str( fimageXcropper0.form_name ), icon_type=icon_type )
    elif fimageXcropper0.errors:
        print(f"fimageXcropper0 has errors: {fimageXcropper0.errors}")
        return json2user(mess = str(fimageXcropper0.form_name), icon_type = 'error')

    return locals()

@action('uiXsweetXalert', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-sweet-alert.html', delimiters='[%[ ]]',))

def uiXsweetXalert():
    ctrl_info= { 'c':'uiXsweetXalert', 'v':'ui-sweet-alert.html' }
    messages = ['uiXsweetXalert', 'ui-sweet-alert.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXsweetXalert') 


    # 
    fuiXsweetXalert0= Form(db.dfuiXsweetXalert0, dbio=False, formstyle=FormStyleBulma)
    if fuiXsweetXalert0.accepted:
        icon_type ='success' if insert_form_vars(fuiXsweetXalert0, db.dfuiXsweetXalert0) else 'info'
        return json2user(mess = str( fuiXsweetXalert0.form_name ), icon_type=icon_type )
    elif fuiXsweetXalert0.errors:
        print(f"fuiXsweetXalert0 has errors: {fuiXsweetXalert0.errors}")
        return json2user(mess = str(fuiXsweetXalert0.form_name), icon_type = 'error')

    return locals()

@action('uiXprogressbar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-progressbar.html', delimiters='[%[ ]]',))

def uiXprogressbar():
    ctrl_info= { 'c':'uiXprogressbar', 'v':'ui-progressbar.html' }
    messages = ['uiXprogressbar', 'ui-progressbar.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXprogressbar') 


    # 
    fuiXprogressbar0= Form(db.dfuiXprogressbar0, dbio=False, formstyle=FormStyleBulma)
    if fuiXprogressbar0.accepted:
        icon_type ='success' if insert_form_vars(fuiXprogressbar0, db.dfuiXprogressbar0) else 'info'
        return json2user(mess = str( fuiXprogressbar0.form_name ), icon_type=icon_type )
    elif fuiXprogressbar0.errors:
        print(f"fuiXprogressbar0 has errors: {fuiXprogressbar0.errors}")
        return json2user(mess = str(fuiXprogressbar0.form_name), icon_type = 'error')

    return locals()

@action('uiXcardsXhover', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-cards-hover.html', delimiters='[%[ ]]',))

def uiXcardsXhover():
    ctrl_info= { 'c':'uiXcardsXhover', 'v':'ui-cards-hover.html' }
    messages = ['uiXcardsXhover', 'ui-cards-hover.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXcardsXhover') 


    # 
    fuiXcardsXhover0= Form(db.dfuiXcardsXhover0, dbio=False, formstyle=FormStyleBulma)
    if fuiXcardsXhover0.accepted:
        icon_type ='success' if insert_form_vars(fuiXcardsXhover0, db.dfuiXcardsXhover0) else 'info'
        return json2user(mess = str( fuiXcardsXhover0.form_name ), icon_type=icon_type )
    elif fuiXcardsXhover0.errors:
        print(f"fuiXcardsXhover0 has errors: {fuiXcardsXhover0.errors}")
        return json2user(mess = str(fuiXcardsXhover0.form_name), icon_type = 'error')

    return locals()

@action('resetXpassword', method=["GET", "POST"] )
@action.uses(db, session, T, Template('reset-password.html', delimiters='[%[ ]]',))

def resetXpassword():
    ctrl_info= { 'c':'resetXpassword', 'v':'reset-password.html' }
    messages = ['resetXpassword', 'reset-password.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('resetXpassword') 


    # 
    fresetXpassword0= Form(db.dfresetXpassword0, dbio=False, formstyle=FormStyleBulma)
    if fresetXpassword0.accepted:
        icon_type ='success' if insert_form_vars(fresetXpassword0, db.dfresetXpassword0) else 'info'
        return json2user(mess = str( fresetXpassword0.form_name ), icon_type=icon_type )
    elif fresetXpassword0.errors:
        print(f"fresetXpassword0 has errors: {fresetXpassword0.errors}")
        return json2user(mess = str(fresetXpassword0.form_name), icon_type = 'error')

    return locals()

@action('productXdetail', method=["GET", "POST"] )
@action.uses(db, session, T, Template('product-detail.html', delimiters='[%[ ]]',))

def productXdetail():
    ctrl_info= { 'c':'productXdetail', 'v':'product-detail.html' }
    messages = ['productXdetail', 'product-detail.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('productXdetail') 


    # 
    fproductXdetail0= Form(db.dfproductXdetail0, dbio=False, formstyle=FormStyleBulma)
    if fproductXdetail0.accepted:
        icon_type ='success' if insert_form_vars(fproductXdetail0, db.dfproductXdetail0) else 'info'
        return json2user(mess = str( fproductXdetail0.form_name ), icon_type=icon_type )
    elif fproductXdetail0.errors:
        print(f"fproductXdetail0 has errors: {fproductXdetail0.errors}")
        return json2user(mess = str(fproductXdetail0.form_name), icon_type = 'error')

    return locals()

@action('imageXdropzone', method=["GET", "POST"] )
@action.uses(db, session, T, Template('image-dropzone.html', delimiters='[%[ ]]',))

def imageXdropzone():
    ctrl_info= { 'c':'imageXdropzone', 'v':'image-dropzone.html' }
    messages = ['imageXdropzone', 'image-dropzone.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('imageXdropzone') 


    # 
    fimageXdropzone0= Form(db.dfimageXdropzone0, dbio=False, formstyle=FormStyleBulma)
    if fimageXdropzone0.accepted:
        icon_type ='success' if insert_form_vars(fimageXdropzone0, db.dfimageXdropzone0) else 'info'
        return json2user(mess = str( fimageXdropzone0.form_name ), icon_type=icon_type )
    elif fimageXdropzone0.errors:
        print(f"fimageXdropzone0 has errors: {fimageXdropzone0.errors}")
        return json2user(mess = str(fimageXdropzone0.form_name), icon_type = 'error')

    # 
    fimageXdropzone1= Form(db.dfimageXdropzone1, dbio=False, formstyle=FormStyleBulma)
    if fimageXdropzone1.accepted:
        icon_type ='success' if insert_form_vars(fimageXdropzone1, db.dfimageXdropzone1) else 'info'
        return json2user(mess = str( fimageXdropzone1.form_name ), icon_type=icon_type )
    elif fimageXdropzone1.errors:
        print(f"fimageXdropzone1 has errors: {fimageXdropzone1.errors}")
        return json2user(mess = str(fimageXdropzone1.form_name), icon_type = 'error')

    return locals()

@action('colorXsettings', method=["GET", "POST"] )
@action.uses(db, session, T, Template('color-settings.html', delimiters='[%[ ]]',))

def colorXsettings():
    ctrl_info= { 'c':'colorXsettings', 'v':'color-settings.html' }
    messages = ['colorXsettings', 'color-settings.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('colorXsettings') 


    # 
    fcolorXsettings0= Form(db.dfcolorXsettings0, dbio=False, formstyle=FormStyleBulma)
    if fcolorXsettings0.accepted:
        icon_type ='success' if insert_form_vars(fcolorXsettings0, db.dfcolorXsettings0) else 'info'
        return json2user(mess = str( fcolorXsettings0.form_name ), icon_type=icon_type )
    elif fcolorXsettings0.errors:
        print(f"fcolorXsettings0 has errors: {fcolorXsettings0.errors}")
        return json2user(mess = str(fcolorXsettings0.form_name), icon_type = 'error')

    return locals()

@action('uiXnotification', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-notification.html', delimiters='[%[ ]]',))

def uiXnotification():
    ctrl_info= { 'c':'uiXnotification', 'v':'ui-notification.html' }
    messages = ['uiXnotification', 'ui-notification.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXnotification') 


    # 
    fuiXnotification0= Form(db.dfuiXnotification0, dbio=False, formstyle=FormStyleBulma)
    if fuiXnotification0.accepted:
        icon_type ='success' if insert_form_vars(fuiXnotification0, db.dfuiXnotification0) else 'info'
        return json2user(mess = str( fuiXnotification0.form_name ), icon_type=icon_type )
    elif fuiXnotification0.errors:
        print(f"fuiXnotification0 has errors: {fuiXnotification0.errors}")
        return json2user(mess = str(fuiXnotification0.form_name), icon_type = 'error')

    return locals()

@action('uiXrangeXslider', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-range-slider.html', delimiters='[%[ ]]',))

def uiXrangeXslider():
    ctrl_info= { 'c':'uiXrangeXslider', 'v':'ui-range-slider.html' }
    messages = ['uiXrangeXslider', 'ui-range-slider.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXrangeXslider') 


    # 
    fuiXrangeXslider0= Form(db.dfuiXrangeXslider0, dbio=False, formstyle=FormStyleBulma)
    if fuiXrangeXslider0.accepted:
        icon_type ='success' if insert_form_vars(fuiXrangeXslider0, db.dfuiXrangeXslider0) else 'info'
        return json2user(mess = str( fuiXrangeXslider0.form_name ), icon_type=icon_type )
    elif fuiXrangeXslider0.errors:
        print(f"fuiXrangeXslider0 has errors: {fuiXrangeXslider0.errors}")
        return json2user(mess = str(fuiXrangeXslider0.form_name), icon_type = 'error')

    return locals()

@action('gettingXstarted', method=["GET", "POST"] )
@action.uses(db, session, T, Template('getting-started.html', delimiters='[%[ ]]',))

def gettingXstarted():
    ctrl_info= { 'c':'gettingXstarted', 'v':'getting-started.html' }
    messages = ['gettingXstarted', 'getting-started.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('gettingXstarted') 


    # 
    fgettingXstarted0= Form(db.dfgettingXstarted0, dbio=False, formstyle=FormStyleBulma)
    if fgettingXstarted0.accepted:
        icon_type ='success' if insert_form_vars(fgettingXstarted0, db.dfgettingXstarted0) else 'info'
        return json2user(mess = str( fgettingXstarted0.form_name ), icon_type=icon_type )
    elif fgettingXstarted0.errors:
        print(f"fgettingXstarted0 has errors: {fgettingXstarted0.errors}")
        return json2user(mess = str(fgettingXstarted0.form_name), icon_type = 'error')

    return locals()

@action('forgotXpassword', method=["GET", "POST"] )
@action.uses(db, session, T, Template('forgot-password.html', delimiters='[%[ ]]',))

def forgotXpassword():
    ctrl_info= { 'c':'forgotXpassword', 'v':'forgot-password.html' }
    messages = ['forgotXpassword', 'forgot-password.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('forgotXpassword') 


    # 
    fforgotXpassword0= Form(db.dfforgotXpassword0, dbio=False, formstyle=FormStyleBulma)
    if fforgotXpassword0.accepted:
        icon_type ='success' if insert_form_vars(fforgotXpassword0, db.dfforgotXpassword0) else 'info'
        return json2user(mess = str( fforgotXpassword0.form_name ), icon_type=icon_type )
    elif fforgotXpassword0.errors:
        print(f"fforgotXpassword0 has errors: {fforgotXpassword0.errors}")
        return json2user(mess = str(fforgotXpassword0.form_name), icon_type = 'error')

    return locals()

@action('contactXdirectory', method=["GET", "POST"] )
@action.uses(db, session, T, Template('contact-directory.html', delimiters='[%[ ]]',))

def contactXdirectory():
    ctrl_info= { 'c':'contactXdirectory', 'v':'contact-directory.html' }
    messages = ['contactXdirectory', 'contact-directory.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('contactXdirectory') 


    # 
    fcontactXdirectory0= Form(db.dfcontactXdirectory0, dbio=False, formstyle=FormStyleBulma)
    if fcontactXdirectory0.accepted:
        icon_type ='success' if insert_form_vars(fcontactXdirectory0, db.dfcontactXdirectory0) else 'info'
        return json2user(mess = str( fcontactXdirectory0.form_name ), icon_type=icon_type )
    elif fcontactXdirectory0.errors:
        print(f"fcontactXdirectory0 has errors: {fcontactXdirectory0.errors}")
        return json2user(mess = str(fcontactXdirectory0.form_name), icon_type = 'error')

    return locals()

@action('uiXtooltipXpopover', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-tooltip-popover.html', delimiters='[%[ ]]',))

def uiXtooltipXpopover():
    ctrl_info= { 'c':'uiXtooltipXpopover', 'v':'ui-tooltip-popover.html' }
    messages = ['uiXtooltipXpopover', 'ui-tooltip-popover.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXtooltipXpopover') 


    # 
    fuiXtooltipXpopover0= Form(db.dfuiXtooltipXpopover0, dbio=False, formstyle=FormStyleBulma)
    if fuiXtooltipXpopover0.accepted:
        icon_type ='success' if insert_form_vars(fuiXtooltipXpopover0, db.dfuiXtooltipXpopover0) else 'info'
        return json2user(mess = str( fuiXtooltipXpopover0.form_name ), icon_type=icon_type )
    elif fuiXtooltipXpopover0.errors:
        print(f"fuiXtooltipXpopover0 has errors: {fuiXtooltipXpopover0.errors}")
        return json2user(mess = str(fuiXtooltipXpopover0.form_name), icon_type = 'error')

    return locals()

@action('thirdXpartyXplugins', method=["GET", "POST"] )
@action.uses(db, session, T, Template('third-party-plugins.html', delimiters='[%[ ]]',))

def thirdXpartyXplugins():
    ctrl_info= { 'c':'thirdXpartyXplugins', 'v':'third-party-plugins.html' }
    messages = ['thirdXpartyXplugins', 'third-party-plugins.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('thirdXpartyXplugins') 


    rows_tthirdXpartyXplugins0= db(db.tthirdXpartyXplugins0).select()
    # 
    fthirdXpartyXplugins0= Form(db.dfthirdXpartyXplugins0, dbio=False, formstyle=FormStyleBulma)
    if fthirdXpartyXplugins0.accepted:
        icon_type ='success' if insert_form_vars(fthirdXpartyXplugins0, db.dfthirdXpartyXplugins0) else 'info'
        return json2user(mess = str( fthirdXpartyXplugins0.form_name ), icon_type=icon_type )
    elif fthirdXpartyXplugins0.errors:
        print(f"fthirdXpartyXplugins0 has errors: {fthirdXpartyXplugins0.errors}")
        return json2user(mess = str(fthirdXpartyXplugins0.form_name), icon_type = 'error')

    return locals()

@action('advancedXcomponents', method=["GET", "POST"] )
@action.uses(db, session, T, Template('advanced-components.html', delimiters='[%[ ]]',))

def advancedXcomponents():
    ctrl_info= { 'c':'advancedXcomponents', 'v':'advanced-components.html' }
    messages = ['advancedXcomponents', 'advanced-components.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('advancedXcomponents') 


    # 
    fadvancedXcomponents0= Form(db.dfadvancedXcomponents0, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents0.accepted:
        icon_type ='success' if insert_form_vars(fadvancedXcomponents0, db.dfadvancedXcomponents0) else 'info'
        return json2user(mess = str( fadvancedXcomponents0.form_name ), icon_type=icon_type )
    elif fadvancedXcomponents0.errors:
        print(f"fadvancedXcomponents0 has errors: {fadvancedXcomponents0.errors}")
        return json2user(mess = str(fadvancedXcomponents0.form_name), icon_type = 'error')

    # 
    fadvancedXcomponents1= Form(db.dfadvancedXcomponents1, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents1.accepted:
        icon_type ='success' if insert_form_vars(fadvancedXcomponents1, db.dfadvancedXcomponents1) else 'info'
        return json2user(mess = str( fadvancedXcomponents1.form_name ), icon_type=icon_type )
    elif fadvancedXcomponents1.errors:
        print(f"fadvancedXcomponents1 has errors: {fadvancedXcomponents1.errors}")
        return json2user(mess = str(fadvancedXcomponents1.form_name), icon_type = 'error')

    # 
    fadvancedXcomponents2= Form(db.dfadvancedXcomponents2, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents2.accepted:
        icon_type ='success' if insert_form_vars(fadvancedXcomponents2, db.dfadvancedXcomponents2) else 'info'
        return json2user(mess = str( fadvancedXcomponents2.form_name ), icon_type=icon_type )
    elif fadvancedXcomponents2.errors:
        print(f"fadvancedXcomponents2 has errors: {fadvancedXcomponents2.errors}")
        return json2user(mess = str(fadvancedXcomponents2.form_name), icon_type = 'error')

    # 
    fadvancedXcomponents3= Form(db.dfadvancedXcomponents3, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents3.accepted:
        icon_type ='success' if insert_form_vars(fadvancedXcomponents3, db.dfadvancedXcomponents3) else 'info'
        return json2user(mess = str( fadvancedXcomponents3.form_name ), icon_type=icon_type )
    elif fadvancedXcomponents3.errors:
        print(f"fadvancedXcomponents3 has errors: {fadvancedXcomponents3.errors}")
        return json2user(mess = str(fadvancedXcomponents3.form_name), icon_type = 'error')

    # 
    fadvancedXcomponents4= Form(db.dfadvancedXcomponents4, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents4.accepted:
        icon_type ='success' if insert_form_vars(fadvancedXcomponents4, db.dfadvancedXcomponents4) else 'info'
        return json2user(mess = str( fadvancedXcomponents4.form_name ), icon_type=icon_type )
    elif fadvancedXcomponents4.errors:
        print(f"fadvancedXcomponents4 has errors: {fadvancedXcomponents4.errors}")
        return json2user(mess = str(fadvancedXcomponents4.form_name), icon_type = 'error')

    # 
    fadvancedXcomponents5= Form(db.dfadvancedXcomponents5, dbio=False, formstyle=FormStyleBulma)
    if fadvancedXcomponents5.accepted:
        icon_type ='success' if insert_form_vars(fadvancedXcomponents5, db.dfadvancedXcomponents5) else 'info'
        return json2user(mess = str( fadvancedXcomponents5.form_name ), icon_type=icon_type )
    elif fadvancedXcomponents5.errors:
        print(f"fadvancedXcomponents5 has errors: {fadvancedXcomponents5.errors}")
        return json2user(mess = str(fadvancedXcomponents5.form_name), icon_type = 'error')

    return locals()


from pydal.restapi import RestAPI, Policy

policy = Policy()

policy.set('*', 'GET', authorize=True, allowed_patterns=['*'])
policy.set('*', 'PUT', authorize=True)
policy.set('*', 'POST', authorize=True)
policy.set('*', 'DELETE', authorize=True)

@action('api/<tablename>/', method=["GET", "POST", "PUT", "DELETE"])
@action('api/<tablename>/<rec_id>', method=["GET", "POST", "PUT", "DELETE"])
def api(tablename, rec_id=None):
    return RestAPI(db, policy)(request.method,
                               tablename,
                               rec_id,
                               request.GET,
                               request.POST
                               )
# 
# curl -X  GET   http://localhost:8000/desk/api/test_table/
# curl -X  GET   http://localhost:8000/desk/api/test_table/9
# curl -X DELETE  http://localhost:8000/desk/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/desk/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/desk/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/desk/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/desk/api/test_table/
#  http         localhost:8000/desk/api/test_table/9
#  http -f POST localhost:8000/desk/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/desk/api/test_table/2
#  http -f PUT localhost:8000/desk/api/test_table/2 f0=111111 f1=2222222 f2=333333

#------------------------------------------------------------------------------------
#curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://rest-api.io/items
#curl -i -X PUT -H 'Content-Type: application/json' -d '{"name": "Updated item", "year": "2010"}' http://rest-api.io/items/5069b47aa892630aae059584






@bottle.error(404)
def error404(error):

    func_mess = []

    def check_rule(maybe_app_root):
        for e in Reloader.ROUTES:
            if ('rule' in e ) and ( e["rule"] == maybe_app_root) :
                Glb["debug"] and func_mess.append(f"     found_rule: {e['rule']}")
                return True
        return False

    location = "/" + Glb["my_app_name"]
    lx = bottle.request.path.split("/", 2)

    if len(lx) >= 2 and check_rule("/" + lx[1]):
        location = "/" + lx[1]

# this code is not necessary for modern py4web 
#
#        files_prefix = location + Glb["tte_path"]
#
#        location_2x = location + location + "/"
#        files_prefix_2x = files_prefix + files_prefix + "/"
#
#        def rm_bad_prefix(bad_prefix):
#            new_location = bottle.request.path.replace(bad_prefix, "", 1)
#            Glb["debug"] and func_mess.append(f"     rm_bad_prefix: {bad_prefix}")
#            return new_location
#
#        if bottle.request.path.startswith(files_prefix_2x):
#            if len(bottle.request.path) > len(files_prefix_2x):
#                location = rm_bad_prefix(files_prefix)
#
#        elif bottle.request.path.startswith(location_2x):
#            if len(bottle.request.path) > len(location_2x):
#                location = rm_bad_prefix(location)

    if Glb["debug"]:
        debug_mess = [  f"404  app=/{Glb['my_app_name']}, err_path={bottle.request.path}",
                        f"     info: {error}", ]
        if len(func_mess):
            debug_mess += func_mess
        debug_mess.append(f"     goto_new_path: {location}\n")
        print("\n".join(debug_mess))

    bottle.response.status = 303
    bottle.response.set_header("Location", location)


# -------------------- tabinfo: my backend ------------------------------------

@unauthenticated("tabinfo", "tabinfo.html")
def tabinfo():
    user = auth.get_user()
    # simple backand-admin-panel (to be continued)
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    return dict(message=message, )

