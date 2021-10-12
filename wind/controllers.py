#
# py4web app, AI-biorex ported 12.10.2021 15:16:27 UTC+3, src: https://github.com/davidgrzyb/tailwind-admin-template
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

@action('tabs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('tabs.html', delimiters='[%[ ]]',))

def tabs():
    ctrl_info= { 'c':'tabs', 'v':'tabs.html' }
    messages = ['tabs', 'tabs.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('tabs') 


    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index.html', delimiters='[%[ ]]',))

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    messages = ['index', 'index.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('index') 


    rows_tindex0= db(db.tindex0).select()
    return locals()

@action('forms', method=["GET", "POST"] )
@action.uses(db, session, T, Template('forms.html', delimiters='[%[ ]]',))

def forms():
    ctrl_info= { 'c':'forms', 'v':'forms.html' }
    messages = ['forms', 'forms.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('forms') 


    # 
    fforms0= Form(db.dfforms0, dbio=False, formstyle=FormStyleBulma)
    if fforms0.accepted:
        icon_type ='success' if insert_form_vars(fforms0, db.dfforms0) else 'info'
        return json2user(mess = str( fforms0.form_name ), icon_type=icon_type )
    elif fforms0.errors:
        print(f"fforms0 has errors: {fforms0.errors}")
        return json2user(mess = str(fforms0.form_name), icon_type = 'error')

    # 
    fforms1= Form(db.dfforms1, dbio=False, formstyle=FormStyleBulma)
    if fforms1.accepted:
        icon_type ='success' if insert_form_vars(fforms1, db.dfforms1) else 'info'
        return json2user(mess = str( fforms1.form_name ), icon_type=icon_type )
    elif fforms1.errors:
        print(f"fforms1 has errors: {fforms1.errors}")
        return json2user(mess = str(fforms1.form_name), icon_type = 'error')

    return locals()

@action('blank', method=["GET", "POST"] )
@action.uses(db, session, T, Template('blank.html', delimiters='[%[ ]]',))

def blank():
    ctrl_info= { 'c':'blank', 'v':'blank.html' }
    messages = ['blank', 'blank.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('blank') 


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
    return locals()

@action('calendar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('calendar.html', delimiters='[%[ ]]',))

def calendar():
    ctrl_info= { 'c':'calendar', 'v':'calendar.html' }
    messages = ['calendar', 'calendar.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('calendar') 


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
# curl -X  GET   http://localhost:8000/wind/api/test_table/
# curl -X  GET   http://localhost:8000/wind/api/test_table/9
# curl -X DELETE  http://localhost:8000/wind/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/wind/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/wind/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/wind/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/wind/api/test_table/
#  http         localhost:8000/wind/api/test_table/9
#  http -f POST localhost:8000/wind/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/wind/api/test_table/2
#  http -f PUT localhost:8000/wind/api/test_table/2 f0=111111 f1=2222222 f2=333333

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

