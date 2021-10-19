#
# py4web app, AI-biorex ported 12.10.2021 09:05:10 UTC+3, src: https://github.com/adminkit/adminkit
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

@action('index', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index.html', delimiters='[%[ ]]',))

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    messages = ['index', 'index.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('index') 


    rows_tindex0= db(db.tindex0).select()
    rows_tindex1= db(db.tindex1).select()
    return locals()

@action('uiXcards', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-cards.html', delimiters='[%[ ]]',))

def uiXcards():
    ctrl_info= { 'c':'uiXcards', 'v':'ui-cards.html' }
    messages = ['uiXcards', 'ui-cards.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXcards') 


    return locals()

@action('uiXforms', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-forms.html', delimiters='[%[ ]]',))

def uiXforms():
    ctrl_info= { 'c':'uiXforms', 'v':'ui-forms.html' }
    messages = ['uiXforms', 'ui-forms.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXforms') 


    return locals()

@action('uiXbuttons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-buttons.html', delimiters='[%[ ]]',))

def uiXbuttons():
    ctrl_info= { 'c':'uiXbuttons', 'v':'ui-buttons.html' }
    messages = ['uiXbuttons', 'ui-buttons.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXbuttons') 


    return locals()

@action('pagesXblank', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pages-blank.html', delimiters='[%[ ]]',))

def pagesXblank():
    ctrl_info= { 'c':'pagesXblank', 'v':'pages-blank.html' }
    messages = ['pagesXblank', 'pages-blank.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('pagesXblank') 


    return locals()

@action('mapsXgoogle', method=["GET", "POST"] )
@action.uses(db, session, T, Template('maps-google.html', delimiters='[%[ ]]',))

def mapsXgoogle():
    ctrl_info= { 'c':'mapsXgoogle', 'v':'maps-google.html' }
    messages = ['mapsXgoogle', 'maps-google.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('mapsXgoogle') 


    return locals()

@action('uiXtypography', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui-typography.html', delimiters='[%[ ]]',))

def uiXtypography():
    ctrl_info= { 'c':'uiXtypography', 'v':'ui-typography.html' }
    messages = ['uiXtypography', 'ui-typography.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('uiXtypography') 


    return locals()

@action('pagesXsignXin', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pages-sign-in.html', delimiters='[%[ ]]',))

def pagesXsignXin():
    ctrl_info= { 'c':'pagesXsignXin', 'v':'pages-sign-in.html' }
    messages = ['pagesXsignXin', 'pages-sign-in.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('pagesXsignXin') 


    # 
    fpagesXsignXin0= Form(db.dfpagesXsignXin0, dbio=False, formstyle=FormStyleBulma)
    if fpagesXsignXin0.accepted:
        icon_type ='success' if insert_form_vars(fpagesXsignXin0, db.dfpagesXsignXin0) else 'info'
        return json2user(mess = str( fpagesXsignXin0.form_name ), icon_type=icon_type )
    elif fpagesXsignXin0.errors:
        print(f"fpagesXsignXin0 has errors: {fpagesXsignXin0.errors}")
        return json2user(mess = str(fpagesXsignXin0.form_name), icon_type = 'error')

    return locals()

@action('pagesXsignXup', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pages-sign-up.html', delimiters='[%[ ]]',))

def pagesXsignXup():
    ctrl_info= { 'c':'pagesXsignXup', 'v':'pages-sign-up.html' }
    messages = ['pagesXsignXup', 'pages-sign-up.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('pagesXsignXup') 


    # 
    fpagesXsignXup0= Form(db.dfpagesXsignXup0, dbio=False, formstyle=FormStyleBulma)
    if fpagesXsignXup0.accepted:
        icon_type ='success' if insert_form_vars(fpagesXsignXup0, db.dfpagesXsignXup0) else 'info'
        return json2user(mess = str( fpagesXsignXup0.form_name ), icon_type=icon_type )
    elif fpagesXsignXup0.errors:
        print(f"fpagesXsignXup0 has errors: {fpagesXsignXup0.errors}")
        return json2user(mess = str(fpagesXsignXup0.form_name), icon_type = 'error')

    return locals()

@action('pagesXprofile', method=["GET", "POST"] )
@action.uses(db, session, T, Template('pages-profile.html', delimiters='[%[ ]]',))

def pagesXprofile():
    ctrl_info= { 'c':'pagesXprofile', 'v':'pages-profile.html' }
    messages = ['pagesXprofile', 'pages-profile.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('pagesXprofile') 


    return locals()

@action('iconsXfeather', method=["GET", "POST"] )
@action.uses(db, session, T, Template('icons-feather.html', delimiters='[%[ ]]',))

def iconsXfeather():
    ctrl_info= { 'c':'iconsXfeather', 'v':'icons-feather.html' }
    messages = ['iconsXfeather', 'icons-feather.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('iconsXfeather') 


    return locals()

@action('upgradeXtoXpro', method=["GET", "POST"] )
@action.uses(db, session, T, Template('upgrade-to-pro.html', delimiters='[%[ ]]',))

def upgradeXtoXpro():
    ctrl_info= { 'c':'upgradeXtoXpro', 'v':'upgrade-to-pro.html' }
    messages = ['upgradeXtoXpro', 'upgrade-to-pro.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('upgradeXtoXpro') 


    rows_tupgradeXtoXpro0= db(db.tupgradeXtoXpro0).select()
    return locals()

@action('chartsXchartjs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('charts-chartjs.html', delimiters='[%[ ]]',))

def chartsXchartjs():
    ctrl_info= { 'c':'chartsXchartjs', 'v':'charts-chartjs.html' }
    messages = ['chartsXchartjs', 'charts-chartjs.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('chartsXchartjs') 


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
# curl -X  GET   http://localhost:8000/kit/api/test_table/
# curl -X  GET   http://localhost:8000/kit/api/test_table/9
# curl -X DELETE  http://localhost:8000/kit/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/kit/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/kit/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/kit/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/kit/api/test_table/
#  http         localhost:8000/kit/api/test_table/9
#  http -f POST localhost:8000/kit/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/kit/api/test_table/2
#  http -f PUT localhost:8000/kit/api/test_table/2 f0=111111 f1=2222222 f2=333333

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

