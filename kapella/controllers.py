#
# py4web app, AI-biorex ported 12.10.2021 08:48:01 UTC+3, src: https://github.com/BootstrapDash/Kapella-Free-Bootstrap-Admin-Template

#
# https://github.com/ali96343/facep4w py4web apps
#
# http://py4web.com 
# http://py4web.com/_documentation/static/en/index.html 
#
#

import os, json, uuid
#
import ombott

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

@action('mdi', method=["GET", "POST"] )
@action.uses(db, session, T, Template('mdi.html', delimiters='[%[ ]]',))

def mdi():
    ctrl_info= { 'c':'mdi', 'v':'mdi.html' }
    messages = ['mdi', 'mdi.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('mdi') 


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


    return locals()

@action('loginX2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('login-2.html', delimiters='[%[ ]]',))

def loginX2():
    ctrl_info= { 'c':'loginX2', 'v':'login-2.html' }
    messages = ['loginX2', 'login-2.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('loginX2') 


    # 
    floginX20= Form(db.dfloginX20, dbio=False, formstyle=FormStyleBulma)
    if floginX20.accepted:
        icon_type ='success' if insert_form_vars(floginX20, db.dfloginX20) else 'info'
        return json2user(mess = str( floginX20.form_name ), icon_type=icon_type )
    elif floginX20.errors:
        print(f"floginX20 has errors: {floginX20.errors}")
        return json2user(mess = str(floginX20.form_name), icon_type = 'error')

    return locals()

@action('chartjs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chartjs.html', delimiters='[%[ ]]',))

def chartjs():
    ctrl_info= { 'c':'chartjs', 'v':'chartjs.html' }
    messages = ['chartjs', 'chartjs.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('chartjs') 


    return locals()

@action('buttons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('buttons.html', delimiters='[%[ ]]',))

def buttons():
    ctrl_info= { 'c':'buttons', 'v':'buttons.html' }
    messages = ['buttons', 'buttons.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('buttons') 


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

@action('registerX2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('register-2.html', delimiters='[%[ ]]',))

def registerX2():
    ctrl_info= { 'c':'registerX2', 'v':'register-2.html' }
    messages = ['registerX2', 'register-2.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('registerX2') 


    # 
    fregisterX20= Form(db.dfregisterX20, dbio=False, formstyle=FormStyleBulma)
    if fregisterX20.accepted:
        icon_type ='success' if insert_form_vars(fregisterX20, db.dfregisterX20) else 'info'
        return json2user(mess = str( fregisterX20.form_name ), icon_type=icon_type )
    elif fregisterX20.errors:
        print(f"fregisterX20 has errors: {fregisterX20.errors}")
        return json2user(mess = str(fregisterX20.form_name), icon_type = 'error')

    return locals()

@action('typography', method=["GET", "POST"] )
@action.uses(db, session, T, Template('typography.html', delimiters='[%[ ]]',))

def typography():
    ctrl_info= { 'c':'typography', 'v':'typography.html' }
    messages = ['typography', 'typography.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('typography') 


    return locals()

@action('lockXscreen', method=["GET", "POST"] )
@action.uses(db, session, T, Template('lock-screen.html', delimiters='[%[ ]]',))

def lockXscreen():
    ctrl_info= { 'c':'lockXscreen', 'v':'lock-screen.html' }
    messages = ['lockXscreen', 'lock-screen.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('lockXscreen') 


    # 
    flockXscreen0= Form(db.dflockXscreen0, dbio=False, formstyle=FormStyleBulma)
    if flockXscreen0.accepted:
        icon_type ='success' if insert_form_vars(flockXscreen0, db.dflockXscreen0) else 'info'
        return json2user(mess = str( flockXscreen0.form_name ), icon_type=icon_type )
    elif flockXscreen0.errors:
        print(f"flockXscreen0 has errors: {flockXscreen0.errors}")
        return json2user(mess = str(flockXscreen0.form_name), icon_type = 'error')

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
    return locals()

@action('documentation', method=["GET", "POST"] )
@action.uses(db, session, T, Template('documentation.html', delimiters='[%[ ]]',))

def documentation():
    ctrl_info= { 'c':'documentation', 'v':'documentation.html' }
    messages = ['documentation', 'documentation.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('documentation') 


    return locals()

@action('basicXelements', method=["GET", "POST"] )
@action.uses(db, session, T, Template('basic_elements.html', delimiters='[%[ ]]',))

def basicXelements():
    ctrl_info= { 'c':'basicXelements', 'v':'basic_elements.html' }
    messages = ['basicXelements', 'basic_elements.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('basicXelements') 


    # 
    fbasicXelements0= Form(db.dfbasicXelements0, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements0.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements0, db.dfbasicXelements0) else 'info'
        return json2user(mess = str( fbasicXelements0.form_name ), icon_type=icon_type )
    elif fbasicXelements0.errors:
        print(f"fbasicXelements0 has errors: {fbasicXelements0.errors}")
        return json2user(mess = str(fbasicXelements0.form_name), icon_type = 'error')

    # 
    fbasicXelements1= Form(db.dfbasicXelements1, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements1.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements1, db.dfbasicXelements1) else 'info'
        return json2user(mess = str( fbasicXelements1.form_name ), icon_type=icon_type )
    elif fbasicXelements1.errors:
        print(f"fbasicXelements1 has errors: {fbasicXelements1.errors}")
        return json2user(mess = str(fbasicXelements1.form_name), icon_type = 'error')

    # 
    fbasicXelements2= Form(db.dfbasicXelements2, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements2.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements2, db.dfbasicXelements2) else 'info'
        return json2user(mess = str( fbasicXelements2.form_name ), icon_type=icon_type )
    elif fbasicXelements2.errors:
        print(f"fbasicXelements2 has errors: {fbasicXelements2.errors}")
        return json2user(mess = str(fbasicXelements2.form_name), icon_type = 'error')

    # 
    fbasicXelements3= Form(db.dfbasicXelements3, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements3.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements3, db.dfbasicXelements3) else 'info'
        return json2user(mess = str( fbasicXelements3.form_name ), icon_type=icon_type )
    elif fbasicXelements3.errors:
        print(f"fbasicXelements3 has errors: {fbasicXelements3.errors}")
        return json2user(mess = str(fbasicXelements3.form_name), icon_type = 'error')

    # 
    fbasicXelements4= Form(db.dfbasicXelements4, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements4.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements4, db.dfbasicXelements4) else 'info'
        return json2user(mess = str( fbasicXelements4.form_name ), icon_type=icon_type )
    elif fbasicXelements4.errors:
        print(f"fbasicXelements4 has errors: {fbasicXelements4.errors}")
        return json2user(mess = str(fbasicXelements4.form_name), icon_type = 'error')

    # 
    fbasicXelements5= Form(db.dfbasicXelements5, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements5.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements5, db.dfbasicXelements5) else 'info'
        return json2user(mess = str( fbasicXelements5.form_name ), icon_type=icon_type )
    elif fbasicXelements5.errors:
        print(f"fbasicXelements5 has errors: {fbasicXelements5.errors}")
        return json2user(mess = str(fbasicXelements5.form_name), icon_type = 'error')

    # 
    fbasicXelements6= Form(db.dfbasicXelements6, dbio=False, formstyle=FormStyleBulma)
    if fbasicXelements6.accepted:
        icon_type ='success' if insert_form_vars(fbasicXelements6, db.dfbasicXelements6) else 'info'
        return json2user(mess = str( fbasicXelements6.form_name ), icon_type=icon_type )
    elif fbasicXelements6.errors:
        print(f"fbasicXelements6 has errors: {fbasicXelements6.errors}")
        return json2user(mess = str(fbasicXelements6.form_name), icon_type = 'error')

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
# curl -X  GET   http://localhost:8000/kapella/api/test_table/
# curl -X  GET   http://localhost:8000/kapella/api/test_table/9
# curl -X DELETE  http://localhost:8000/kapella/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/kapella/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/kapella/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/kapella/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/kapella/api/test_table/
#  http         localhost:8000/kapella/api/test_table/9
#  http -f POST localhost:8000/kapella/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/kapella/api/test_table/2
#  http -f PUT localhost:8000/kapella/api/test_table/2 f0=111111 f1=2222222 f2=333333

#------------------------------------------------------------------------------------
#curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://rest-api.io/items
#curl -i -X PUT -H 'Content-Type: application/json' -d '{"name": "Updated item", "year": "2010"}' http://rest-api.io/items/5069b47aa892630aae059584


# @ombott.error(404, '/web<_:path()>')
# @ombott.error(404, '/web/<params:path>')
@ombott.error(404, f"/{APP_NAME}")
def url_not_found(route, params):
    # print ( str(dict(route=route, params=params))  )

    ombott.response.status = 303
    ombott.response.headers["Location"] = f"/{APP_NAME}"
    #ombott.response.headers['Location'] = route #f'/{APP_NAME}'




# -------------------- tabinfo: my backend ------------------------------------

@unauthenticated("tabinfo", "tabinfo.html")
def tabinfo():
    user = auth.get_user()
    # simple backand-admin-panel (to be continued)
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    return dict(message=message, )

