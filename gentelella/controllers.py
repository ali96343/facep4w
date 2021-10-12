#
# py4web app, AI-biorex ported 09.10.2021 11:20:40 UTC+3, src: https://github.com/ColorlibHQ/gentelella

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
                if Glb['debug'] == True:
                     print(f'     inserted: \"{myform.vars[f0_name]}\" into {mytable[f0_name]}, id = {row_id}' )
                     print(f"     selected: \"{table_row[f0_name]}\" from {mytable[f0_name]}, id = {row_id}" )
                     print ()
    else:
        if Glb['debug'] == True:
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

@action('form', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form.html', delimiters='[%[ ]]',))

def form():
    ctrl_info= { 'c':'form', 'v':'form.html' }
    messages = ['form', 'form.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('form') 


    # 
    fform0= Form(db.dfform0, dbio=False, formstyle=FormStyleBulma)
    if fform0.accepted:
        icon_type ='success' if insert_form_vars(fform0, db.dfform0) else 'info'
        return json2user(mess = str( fform0.form_name ), icon_type=icon_type )
    elif fform0.errors:
        print(f"fform0 has errors: {fform0.errors}")
        return json2user(mess = str(fform0.form_name), icon_type = 'error')

    # 
    fform1= Form(db.dfform1, dbio=False, formstyle=FormStyleBulma)
    if fform1.accepted:
        icon_type ='success' if insert_form_vars(fform1, db.dfform1) else 'info'
        return json2user(mess = str( fform1.form_name ), icon_type=icon_type )
    elif fform1.errors:
        print(f"fform1 has errors: {fform1.errors}")
        return json2user(mess = str(fform1.form_name), icon_type = 'error')

    # 
    fform2= Form(db.dfform2, dbio=False, formstyle=FormStyleBulma)
    if fform2.accepted:
        icon_type ='success' if insert_form_vars(fform2, db.dfform2) else 'info'
        return json2user(mess = str( fform2.form_name ), icon_type=icon_type )
    elif fform2.errors:
        print(f"fform2 has errors: {fform2.errors}")
        return json2user(mess = str(fform2.form_name), icon_type = 'error')

    # 
    fform3= Form(db.dfform3, dbio=False, formstyle=FormStyleBulma)
    if fform3.accepted:
        icon_type ='success' if insert_form_vars(fform3, db.dfform3) else 'info'
        return json2user(mess = str( fform3.form_name ), icon_type=icon_type )
    elif fform3.errors:
        print(f"fform3 has errors: {fform3.errors}")
        return json2user(mess = str(fform3.form_name), icon_type = 'error')

    # 
    fform4= Form(db.dfform4, dbio=False, formstyle=FormStyleBulma)
    if fform4.accepted:
        icon_type ='success' if insert_form_vars(fform4, db.dfform4) else 'info'
        return json2user(mess = str( fform4.form_name ), icon_type=icon_type )
    elif fform4.errors:
        print(f"fform4 has errors: {fform4.errors}")
        return json2user(mess = str(fform4.form_name), icon_type = 'error')

    # 
    fform5= Form(db.dfform5, dbio=False, formstyle=FormStyleBulma)
    if fform5.accepted:
        icon_type ='success' if insert_form_vars(fform5, db.dfform5) else 'info'
        return json2user(mess = str( fform5.form_name ), icon_type=icon_type )
    elif fform5.errors:
        print(f"fform5 has errors: {fform5.errors}")
        return json2user(mess = str(fform5.form_name), icon_type = 'error')

    # 
    fform6= Form(db.dfform6, dbio=False, formstyle=FormStyleBulma)
    if fform6.accepted:
        icon_type ='success' if insert_form_vars(fform6, db.dfform6) else 'info'
        return json2user(mess = str( fform6.form_name ), icon_type=icon_type )
    elif fform6.errors:
        print(f"fform6 has errors: {fform6.errors}")
        return json2user(mess = str(fform6.form_name), icon_type = 'error')

    # 
    fform7= Form(db.dfform7, dbio=False, formstyle=FormStyleBulma)
    if fform7.accepted:
        icon_type ='success' if insert_form_vars(fform7, db.dfform7) else 'info'
        return json2user(mess = str( fform7.form_name ), icon_type=icon_type )
    elif fform7.errors:
        print(f"fform7 has errors: {fform7.errors}")
        return json2user(mess = str(fform7.form_name), icon_type = 'error')

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

    # 
    floginA1= Form(db.dfloginA1, dbio=False, formstyle=FormStyleBulma)
    if floginA1.accepted:
        icon_type ='success' if insert_form_vars(floginA1, db.dfloginA1) else 'info'
        return json2user(mess = str( floginA1.form_name ), icon_type=icon_type )
    elif floginA1.errors:
        print(f"floginA1 has errors: {floginA1.errors}")
        return json2user(mess = str(floginA1.form_name), icon_type = 'error')

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index.html', delimiters='[%[ ]]',))

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    messages = ['index', 'index.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('index') 


    return locals()

@action('inbox', method=["GET", "POST"] )
@action.uses(db, session, T, Template('inbox.html', delimiters='[%[ ]]',))

def inbox():
    ctrl_info= { 'c':'inbox', 'v':'inbox.html' }
    messages = ['inbox', 'inbox.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('inbox') 


    return locals()

@action('icons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('icons.html', delimiters='[%[ ]]',))

def icons():
    ctrl_info= { 'c':'icons', 'v':'icons.html' }
    messages = ['icons', 'icons.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('icons') 


    return locals()

@action('tables', method=["GET", "POST"] )
@action.uses(db, session, T, Template('tables.html', delimiters='[%[ ]]',))

def tables():
    ctrl_info= { 'c':'tables', 'v':'tables.html' }
    messages = ['tables', 'tables.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('tables') 


    rows_ttables0= db(db.ttables0).select()
    rows_ttables1= db(db.ttables1).select()
    rows_ttables2= db(db.ttables2).select()
    rows_ttables3= db(db.ttables3).select()
    rows_ttables4= db(db.ttables4).select()
    return locals()

@action('level2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('level2.html', delimiters='[%[ ]]',))

def level2():
    ctrl_info= { 'c':'level2', 'v':'level2.html' }
    messages = ['level2', 'level2.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('level2') 


    return locals()

@action('index3', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index3.html', delimiters='[%[ ]]',))

def index3():
    ctrl_info= { 'c':'index3', 'v':'index3.html' }
    messages = ['index3', 'index3.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('index3') 


    return locals()

@action('index2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index2.html', delimiters='[%[ ]]',))

def index2():
    ctrl_info= { 'c':'index2', 'v':'index2.html' }
    messages = ['index2', 'index2.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('index2') 


    return locals()

@action('widgets', method=["GET", "POST"] )
@action.uses(db, session, T, Template('widgets.html', delimiters='[%[ ]]',))

def widgets():
    ctrl_info= { 'c':'widgets', 'v':'widgets.html' }
    messages = ['widgets', 'widgets.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('widgets') 


    return locals()

@action('profileA', method=["GET", "POST"] )
@action.uses(db, session, T, Template('profile.html', delimiters='[%[ ]]',))

def profileA():
    ctrl_info= { 'c':'profileA', 'v':'profile.html' }
    messages = ['profileA', 'profile.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('profileA') 


    rows_tprofileA0= db(db.tprofileA0).select()
    return locals()

@action('morisjs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('morisjs.html', delimiters='[%[ ]]',))

def morisjs():
    ctrl_info= { 'c':'morisjs', 'v':'morisjs.html' }
    messages = ['morisjs', 'morisjs.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('morisjs') 


    return locals()

@action('invoice', method=["GET", "POST"] )
@action.uses(db, session, T, Template('invoice.html', delimiters='[%[ ]]',))

def invoice():
    ctrl_info= { 'c':'invoice', 'v':'invoice.html' }
    messages = ['invoice', 'invoice.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('invoice') 


    rows_tinvoice0= db(db.tinvoice0).select()
    rows_tinvoice1= db(db.tinvoice1).select()
    return locals()

@action('echarts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('echarts.html', delimiters='[%[ ]]',))

def echarts():
    ctrl_info= { 'c':'echarts', 'v':'echarts.html' }
    messages = ['echarts', 'echarts.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('echarts') 


    return locals()

@action('chartjs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chartjs.html', delimiters='[%[ ]]',))

def chartjs():
    ctrl_info= { 'c':'chartjs', 'v':'chartjs.html' }
    messages = ['chartjs', 'chartjs.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('chartjs') 


    return locals()

@action('projects', method=["GET", "POST"] )
@action.uses(db, session, T, Template('projects.html', delimiters='[%[ ]]',))

def projects():
    ctrl_info= { 'c':'projects', 'v':'projects.html' }
    messages = ['projects', 'projects.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('projects') 


    rows_tprojects0= db(db.tprojects0).select()
    return locals()

@action('pageX404', method=["GET", "POST"] )
@action.uses(db, session, T, Template('page_404.html', delimiters='[%[ ]]',))

def pageX404():
    ctrl_info= { 'c':'pageX404', 'v':'page_404.html' }
    messages = ['pageX404', 'page_404.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('pageX404') 


    # 
    fpageX4040= Form(db.dfpageX4040, dbio=False, formstyle=FormStyleBulma)
    if fpageX4040.accepted:
        icon_type ='success' if insert_form_vars(fpageX4040, db.dfpageX4040) else 'info'
        return json2user(mess = str( fpageX4040.form_name ), icon_type=icon_type )
    elif fpageX4040.errors:
        print(f"fpageX4040 has errors: {fpageX4040.errors}")
        return json2user(mess = str(fpageX4040.form_name), icon_type = 'error')

    return locals()

@action('pageX403', method=["GET", "POST"] )
@action.uses(db, session, T, Template('page_403.html', delimiters='[%[ ]]',))

def pageX403():
    ctrl_info= { 'c':'pageX403', 'v':'page_403.html' }
    messages = ['pageX403', 'page_403.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('pageX403') 


    # 
    fpageX4030= Form(db.dfpageX4030, dbio=False, formstyle=FormStyleBulma)
    if fpageX4030.accepted:
        icon_type ='success' if insert_form_vars(fpageX4030, db.dfpageX4030) else 'info'
        return json2user(mess = str( fpageX4030.form_name ), icon_type=icon_type )
    elif fpageX4030.errors:
        print(f"fpageX4030 has errors: {fpageX4030.errors}")
        return json2user(mess = str(fpageX4030.form_name), icon_type = 'error')

    return locals()

@action('pageX500', method=["GET", "POST"] )
@action.uses(db, session, T, Template('page_500.html', delimiters='[%[ ]]',))

def pageX500():
    ctrl_info= { 'c':'pageX500', 'v':'page_500.html' }
    messages = ['pageX500', 'page_500.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('pageX500') 


    # 
    fpageX5000= Form(db.dfpageX5000, dbio=False, formstyle=FormStyleBulma)
    if fpageX5000.accepted:
        icon_type ='success' if insert_form_vars(fpageX5000, db.dfpageX5000) else 'info'
        return json2user(mess = str( fpageX5000.form_name ), icon_type=icon_type )
    elif fpageX5000.errors:
        print(f"fpageX5000 has errors: {fpageX5000.errors}")
        return json2user(mess = str(fpageX5000.form_name), icon_type = 'error')

    return locals()

@action('contacts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('contacts.html', delimiters='[%[ ]]',))

def contacts():
    ctrl_info= { 'c':'contacts', 'v':'contacts.html' }
    messages = ['contacts', 'contacts.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('contacts') 


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

@action('chartjs2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chartjs2.html', delimiters='[%[ ]]',))

def chartjs2():
    ctrl_info= { 'c':'chartjs2', 'v':'chartjs2.html' }
    messages = ['chartjs2', 'chartjs2.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('chartjs2') 


    return locals()

@action('typography', method=["GET", "POST"] )
@action.uses(db, session, T, Template('typography.html', delimiters='[%[ ]]',))

def typography():
    ctrl_info= { 'c':'typography', 'v':'typography.html' }
    messages = ['typography', 'typography.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('typography') 


    return locals()

@action('plainXpage', method=["GET", "POST"] )
@action.uses(db, session, T, Template('plain_page.html', delimiters='[%[ ]]',))

def plainXpage():
    ctrl_info= { 'c':'plainXpage', 'v':'plain_page.html' }
    messages = ['plainXpage', 'plain_page.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('plainXpage') 


    return locals()

@action('glyphicons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('glyphicons.html', delimiters='[%[ ]]',))

def glyphicons():
    ctrl_info= { 'c':'glyphicons', 'v':'glyphicons.html' }
    messages = ['glyphicons', 'glyphicons.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('glyphicons') 


    return locals()

@action('eXcommerce', method=["GET", "POST"] )
@action.uses(db, session, T, Template('e_commerce.html', delimiters='[%[ ]]',))

def eXcommerce():
    ctrl_info= { 'c':'eXcommerce', 'v':'e_commerce.html' }
    messages = ['eXcommerce', 'e_commerce.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('eXcommerce') 


    return locals()

@action('formXupload', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form_upload.html', delimiters='[%[ ]]',))

def formXupload():
    ctrl_info= { 'c':'formXupload', 'v':'form_upload.html' }
    messages = ['formXupload', 'form_upload.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('formXupload') 


    # 
    fformXupload0= Form(db.dfformXupload0, dbio=False, formstyle=FormStyleBulma)
    if fformXupload0.accepted:
        icon_type ='success' if insert_form_vars(fformXupload0, db.dfformXupload0) else 'info'
        return json2user(mess = str( fformXupload0.form_name ), icon_type=icon_type )
    elif fformXupload0.errors:
        print(f"fformXupload0 has errors: {fformXupload0.errors}")
        return json2user(mess = str(fformXupload0.form_name), icon_type = 'error')

    return locals()

@action('otherXcharts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('other_charts.html', delimiters='[%[ ]]',))

def otherXcharts():
    ctrl_info= { 'c':'otherXcharts', 'v':'other_charts.html' }
    messages = ['otherXcharts', 'other_charts.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('otherXcharts') 


    rows_totherXcharts0= db(db.totherXcharts0).select()
    return locals()

@action('formXwizards', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form_wizards.html', delimiters='[%[ ]]',))

def formXwizards():
    ctrl_info= { 'c':'formXwizards', 'v':'form_wizards.html' }
    messages = ['formXwizards', 'form_wizards.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('formXwizards') 


    # 
    fformXwizards0= Form(db.dfformXwizards0, dbio=False, formstyle=FormStyleBulma)
    if fformXwizards0.accepted:
        icon_type ='success' if insert_form_vars(fformXwizards0, db.dfformXwizards0) else 'info'
        return json2user(mess = str( fformXwizards0.form_name ), icon_type=icon_type )
    elif fformXwizards0.errors:
        print(f"fformXwizards0 has errors: {fformXwizards0.errors}")
        return json2user(mess = str(fformXwizards0.form_name), icon_type = 'error')

    # 
    fformXwizards1= Form(db.dfformXwizards1, dbio=False, formstyle=FormStyleBulma)
    if fformXwizards1.accepted:
        icon_type ='success' if insert_form_vars(fformXwizards1, db.dfformXwizards1) else 'info'
        return json2user(mess = str( fformXwizards1.form_name ), icon_type=icon_type )
    elif fformXwizards1.errors:
        print(f"fformXwizards1 has errors: {fformXwizards1.errors}")
        return json2user(mess = str(fformXwizards1.form_name), icon_type = 'error')

    return locals()

@action('formXbuttons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form_buttons.html', delimiters='[%[ ]]',))

def formXbuttons():
    ctrl_info= { 'c':'formXbuttons', 'v':'form_buttons.html' }
    messages = ['formXbuttons', 'form_buttons.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('formXbuttons') 


    return locals()

@action('fixedXfooter', method=["GET", "POST"] )
@action.uses(db, session, T, Template('fixed_footer.html', delimiters='[%[ ]]',))

def fixedXfooter():
    ctrl_info= { 'c':'fixedXfooter', 'v':'fixed_footer.html' }
    messages = ['fixedXfooter', 'fixed_footer.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('fixedXfooter') 


    return locals()

@action('formXadvanced', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form_advanced.html', delimiters='[%[ ]]',))

def formXadvanced():
    ctrl_info= { 'c':'formXadvanced', 'v':'form_advanced.html' }
    messages = ['formXadvanced', 'form_advanced.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('formXadvanced') 


    rows_tformXadvanced0= db(db.tformXadvanced0).select()
    rows_tformXadvanced1= db(db.tformXadvanced1).select()
    rows_tformXadvanced2= db(db.tformXadvanced2).select()
    rows_tformXadvanced3= db(db.tformXadvanced3).select()
    rows_tformXadvanced4= db(db.tformXadvanced4).select()
    rows_tformXadvanced5= db(db.tformXadvanced5).select()
    rows_tformXadvanced6= db(db.tformXadvanced6).select()
    rows_tformXadvanced7= db(db.tformXadvanced7).select()
    # 
    fformXadvanced0= Form(db.dfformXadvanced0, dbio=False, formstyle=FormStyleBulma)
    if fformXadvanced0.accepted:
        icon_type ='success' if insert_form_vars(fformXadvanced0, db.dfformXadvanced0) else 'info'
        return json2user(mess = str( fformXadvanced0.form_name ), icon_type=icon_type )
    elif fformXadvanced0.errors:
        print(f"fformXadvanced0 has errors: {fformXadvanced0.errors}")
        return json2user(mess = str(fformXadvanced0.form_name), icon_type = 'error')

    # 
    fformXadvanced1= Form(db.dfformXadvanced1, dbio=False, formstyle=FormStyleBulma)
    if fformXadvanced1.accepted:
        icon_type ='success' if insert_form_vars(fformXadvanced1, db.dfformXadvanced1) else 'info'
        return json2user(mess = str( fformXadvanced1.form_name ), icon_type=icon_type )
    elif fformXadvanced1.errors:
        print(f"fformXadvanced1 has errors: {fformXadvanced1.errors}")
        return json2user(mess = str(fformXadvanced1.form_name), icon_type = 'error')

    # 
    fformXadvanced2= Form(db.dfformXadvanced2, dbio=False, formstyle=FormStyleBulma)
    if fformXadvanced2.accepted:
        icon_type ='success' if insert_form_vars(fformXadvanced2, db.dfformXadvanced2) else 'info'
        return json2user(mess = str( fformXadvanced2.form_name ), icon_type=icon_type )
    elif fformXadvanced2.errors:
        print(f"fformXadvanced2 has errors: {fformXadvanced2.errors}")
        return json2user(mess = str(fformXadvanced2.form_name), icon_type = 'error')

    # 
    fformXadvanced3= Form(db.dfformXadvanced3, dbio=False, formstyle=FormStyleBulma)
    if fformXadvanced3.accepted:
        icon_type ='success' if insert_form_vars(fformXadvanced3, db.dfformXadvanced3) else 'info'
        return json2user(mess = str( fformXadvanced3.form_name ), icon_type=icon_type )
    elif fformXadvanced3.errors:
        print(f"fformXadvanced3 has errors: {fformXadvanced3.errors}")
        return json2user(mess = str(fformXadvanced3.form_name), icon_type = 'error')

    return locals()

@action('mediaXgallery', method=["GET", "POST"] )
@action.uses(db, session, T, Template('media_gallery.html', delimiters='[%[ ]]',))

def mediaXgallery():
    ctrl_info= { 'c':'mediaXgallery', 'v':'media_gallery.html' }
    messages = ['mediaXgallery', 'media_gallery.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('mediaXgallery') 


    return locals()

@action('fixedXsidebar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('fixed_sidebar.html', delimiters='[%[ ]]',))

def fixedXsidebar():
    ctrl_info= { 'c':'fixedXsidebar', 'v':'fixed_sidebar.html' }
    messages = ['fixedXsidebar', 'fixed_sidebar.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('fixedXsidebar') 


    return locals()

@action('tablesXdynamic', method=["GET", "POST"] )
@action.uses(db, session, T, Template('tables_dynamic.html', delimiters='[%[ ]]',))

def tablesXdynamic():
    ctrl_info= { 'c':'tablesXdynamic', 'v':'tables_dynamic.html' }
    messages = ['tablesXdynamic', 'tables_dynamic.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('tablesXdynamic') 


    rows_ttablesXdynamic0= db(db.ttablesXdynamic0).select()
    rows_ttablesXdynamic1= db(db.ttablesXdynamic1).select()
    rows_ttablesXdynamic2= db(db.ttablesXdynamic2).select()
    rows_ttablesXdynamic3= db(db.ttablesXdynamic3).select()
    rows_ttablesXdynamic4= db(db.ttablesXdynamic4).select()
    rows_ttablesXdynamic5= db(db.ttablesXdynamic5).select()
    return locals()

@action('projectXdetail', method=["GET", "POST"] )
@action.uses(db, session, T, Template('project_detail.html', delimiters='[%[ ]]',))

def projectXdetail():
    ctrl_info= { 'c':'projectXdetail', 'v':'project_detail.html' }
    messages = ['projectXdetail', 'project_detail.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('projectXdetail') 


    return locals()

@action('pricingXtables', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pricing_tables.html', delimiters='[%[ ]]',))

def pricingXtables():
    ctrl_info= { 'c':'pricingXtables', 'v':'pricing_tables.html' }
    messages = ['pricingXtables', 'pricing_tables.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('pricingXtables') 


    return locals()

@action('formXvalidation', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form_validation.html', delimiters='[%[ ]]',))

def formXvalidation():
    ctrl_info= { 'c':'formXvalidation', 'v':'form_validation.html' }
    messages = ['formXvalidation', 'form_validation.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('formXvalidation') 


    # 
    fformXvalidation0= Form(db.dfformXvalidation0, dbio=False, formstyle=FormStyleBulma)
    if fformXvalidation0.accepted:
        icon_type ='success' if insert_form_vars(fformXvalidation0, db.dfformXvalidation0) else 'info'
        return json2user(mess = str( fformXvalidation0.form_name ), icon_type=icon_type )
    elif fformXvalidation0.errors:
        print(f"fformXvalidation0 has errors: {fformXvalidation0.errors}")
        return json2user(mess = str(fformXvalidation0.form_name), icon_type = 'error')

    return locals()

@action('generalXelements', method=["GET", "POST"] )
@action.uses(db, session, T, Template('general_elements.html', delimiters='[%[ ]]',))

def generalXelements():
    ctrl_info= { 'c':'generalXelements', 'v':'general_elements.html' }
    messages = ['generalXelements', 'general_elements.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('generalXelements') 


    rows_tgeneralXelements0= db(db.tgeneralXelements0).select()
    rows_tgeneralXelements1= db(db.tgeneralXelements1).select()
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
# curl -X  GET   http://localhost:8000/gentelella/api/test_table/
# curl -X  GET   http://localhost:8000/gentelella/api/test_table/9
# curl -X DELETE  http://localhost:8000/gentelella/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/gentelella/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/gentelella/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/gentelella/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/gentelella/api/test_table/
#  http         localhost:8000/gentelella/api/test_table/9
#  http -f POST localhost:8000/gentelella/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/gentelella/api/test_table/2
#  http -f PUT localhost:8000/gentelella/api/test_table/2 f0=111111 f1=2222222 f2=333333

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

