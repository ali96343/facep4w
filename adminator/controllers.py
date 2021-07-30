#
# py4web app, AI-biorex ported 07.05.2021 14:48:48 UTC+3, src: https://github.com/puikinsh/Adminator-admin-dashboard

#
# https://github.com/ali96343/facep4w py4web apps
#
# http://py4web.com 
# http://py4web.com/_documentation/static/en/index.html 
#
#

import os, json, uuid
from py4web.core import bottle

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

Glb= {'debug': True , 'my_app_name': APP_NAME, 'tte_path': '/static/tte' }

# ---------------------- Utils -------------------------------------------------------

def insert_form_vars(myform, mytable):

    row_id, table_row, f0_fld = None, None, None

    if Glb['debug'] == True:
        print("app:",Glb['my_app_name'])
        _ = [ print (f'     {k}: {v}') for k,v in myform.vars.items() if k != '_formkey']

    f0_fld = myform.vars.get('f0', None )
    if (not f0_fld is None) and ( type( f0_fld ) in (list, tuple, dict, str, bytes) ) and len(f0_fld):
        row_id = mytable.insert(**mytable._filter_fields(myform.vars))
        db.commit()

        if not row_id is None:
            table_row = mytable(row_id )

            if not table_row is None:
                if Glb['debug'] == True:
                     print( f'     inserted: \"{myform.vars["f0"]}\" into {mytable.f0}, id = {row_id}' )
                     print( f"     selected: \"{table_row.f0}\" from {mytable.f0}, id = {row_id}" )
                     print ()
    else:
        if Glb['debug'] == True:
            print( f"     no entry inserted: (f0_fld is None) or (len(f0_fld) == 0)")
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

@action('ui', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ui.html', delimiters='[%[ ]]',))

def ui():
    ctrl_info= { 'c':'ui', 'v':'ui.html' }
    messages = ['ui', 'ui.html']
    #
    ctrl_template_url = "\'" + URL('ui' ) + "\'"

    return locals()

@action('X500', method=["GET", "POST"] )
@action.uses(db, session, T, Template('500.html', delimiters='[%[ ]]',))

def X500():
    ctrl_info= { 'c':'X500', 'v':'500.html' }
    messages = ['X500', '500.html']
    #
    ctrl_template_url = "\'" + URL('X500' ) + "\'"

    return locals()

@action('X404', method=["GET", "POST"] )
@action.uses(db, session, T, Template('404.html', delimiters='[%[ ]]',))

def X404():
    ctrl_info= { 'c':'X404', 'v':'404.html' }
    messages = ['X404', '404.html']
    #
    ctrl_template_url = "\'" + URL('X404' ) + "\'"

    return locals()

@action('chat', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chat.html', delimiters='[%[ ]]',))

def chat():
    ctrl_info= { 'c':'chat', 'v':'chat.html' }
    messages = ['chat', 'chat.html']
    #
    ctrl_template_url = "\'" + URL('chat' ) + "\'"

    return locals()

@action('blank', method=["GET", "POST"] )
@action.uses(db, session, T, Template('blank.html', delimiters='[%[ ]]',))

def blank():
    ctrl_info= { 'c':'blank', 'v':'blank.html' }
    messages = ['blank', 'blank.html']
    #
    ctrl_template_url = "\'" + URL('blank' ) + "\'"

    return locals()

@action('forms', method=["GET", "POST"] )
@action.uses(db, session, T, Template('forms.html', delimiters='[%[ ]]',))

def forms():
    ctrl_info= { 'c':'forms', 'v':'forms.html' }
    messages = ['forms', 'forms.html']
    #
    ctrl_template_url = "\'" + URL('forms' ) + "\'"

    # 
    fforms0= Form(db.dfforms0, dbio=False, formstyle=FormStyleBulma)
    if fforms0.accepted:
        icon_type ='success' if insert_form_vars(fforms0, db.dfforms0) else 'info'
        return json2user(mess = str( fforms0.form_name ), icon_type=icon_type )
    elif fforms0.errors:
        print("fforms0 has errors: %s" % (fforms0.errors))
        return json2user(mess = str(fforms0.form_name), icon_type = 'error')

    # 
    fforms1= Form(db.dfforms1, dbio=False, formstyle=FormStyleBulma)
    if fforms1.accepted:
        icon_type ='success' if insert_form_vars(fforms1, db.dfforms1) else 'info'
        return json2user(mess = str( fforms1.form_name ), icon_type=icon_type )
    elif fforms1.errors:
        print("fforms1 has errors: %s" % (fforms1.errors))
        return json2user(mess = str(fforms1.form_name), icon_type = 'error')

    # 
    fforms2= Form(db.dfforms2, dbio=False, formstyle=FormStyleBulma)
    if fforms2.accepted:
        icon_type ='success' if insert_form_vars(fforms2, db.dfforms2) else 'info'
        return json2user(mess = str( fforms2.form_name ), icon_type=icon_type )
    elif fforms2.errors:
        print("fforms2 has errors: %s" % (fforms2.errors))
        return json2user(mess = str(fforms2.form_name), icon_type = 'error')

    # 
    fforms3= Form(db.dfforms3, dbio=False, formstyle=FormStyleBulma)
    if fforms3.accepted:
        icon_type ='success' if insert_form_vars(fforms3, db.dfforms3) else 'info'
        return json2user(mess = str( fforms3.form_name ), icon_type=icon_type )
    elif fforms3.errors:
        print("fforms3 has errors: %s" % (fforms3.errors))
        return json2user(mess = str(fforms3.form_name), icon_type = 'error')

    # 
    fforms4= Form(db.dfforms4, dbio=False, formstyle=FormStyleBulma)
    if fforms4.accepted:
        icon_type ='success' if insert_form_vars(fforms4, db.dfforms4) else 'info'
        return json2user(mess = str( fforms4.form_name ), icon_type=icon_type )
    elif fforms4.errors:
        print("fforms4 has errors: %s" % (fforms4.errors))
        return json2user(mess = str(fforms4.form_name), icon_type = 'error')

    return locals()

@action('email', method=["GET", "POST"] )
@action.uses(db, session, T, Template('email.html', delimiters='[%[ ]]',))

def email():
    ctrl_info= { 'c':'email', 'v':'email.html' }
    messages = ['email', 'email.html']
    #
    ctrl_template_url = "\'" + URL('email' ) + "\'"

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index.html', delimiters='[%[ ]]',))

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    messages = ['index', 'index.html']
    #
    ctrl_template_url = "\'" + URL('index' ) + "\'"

    rows_tindex0= db(db.tindex0).select()
    return locals()

@action('signup', method=["GET", "POST"] )
@action.uses(db, session, T, Template('signup.html', delimiters='[%[ ]]',))

def signup():
    ctrl_info= { 'c':'signup', 'v':'signup.html' }
    messages = ['signup', 'signup.html']
    #
    ctrl_template_url = "\'" + URL('signup' ) + "\'"

    # 
    fsignup0= Form(db.dfsignup0, dbio=False, formstyle=FormStyleBulma)
    if fsignup0.accepted:
        icon_type ='success' if insert_form_vars(fsignup0, db.dfsignup0) else 'info'
        return json2user(mess = str( fsignup0.form_name ), icon_type=icon_type )
    elif fsignup0.errors:
        print("fsignup0 has errors: %s" % (fsignup0.errors))
        return json2user(mess = str(fsignup0.form_name), icon_type = 'error')

    return locals()

@action('signin', method=["GET", "POST"] )
@action.uses(db, session, T, Template('signin.html', delimiters='[%[ ]]',))

def signin():
    ctrl_info= { 'c':'signin', 'v':'signin.html' }
    messages = ['signin', 'signin.html']
    #
    ctrl_template_url = "\'" + URL('signin' ) + "\'"

    # 
    fsignin0= Form(db.dfsignin0, dbio=False, formstyle=FormStyleBulma)
    if fsignin0.accepted:
        icon_type ='success' if insert_form_vars(fsignin0, db.dfsignin0) else 'info'
        return json2user(mess = str( fsignin0.form_name ), icon_type=icon_type )
    elif fsignin0.errors:
        print("fsignin0 has errors: %s" % (fsignin0.errors))
        return json2user(mess = str(fsignin0.form_name), icon_type = 'error')

    return locals()

@action('charts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('charts.html', delimiters='[%[ ]]',))

def charts():
    ctrl_info= { 'c':'charts', 'v':'charts.html' }
    messages = ['charts', 'charts.html']
    #
    ctrl_template_url = "\'" + URL('charts' ) + "\'"

    return locals()

@action('compose', method=["GET", "POST"] )
@action.uses(db, session, T, Template('compose.html', delimiters='[%[ ]]',))

def compose():
    ctrl_info= { 'c':'compose', 'v':'compose.html' }
    messages = ['compose', 'compose.html']
    #
    ctrl_template_url = "\'" + URL('compose' ) + "\'"

    # 
    fcompose0= Form(db.dfcompose0, dbio=False, formstyle=FormStyleBulma)
    if fcompose0.accepted:
        icon_type ='success' if insert_form_vars(fcompose0, db.dfcompose0) else 'info'
        return json2user(mess = str( fcompose0.form_name ), icon_type=icon_type )
    elif fcompose0.errors:
        print("fcompose0 has errors: %s" % (fcompose0.errors))
        return json2user(mess = str(fcompose0.form_name), icon_type = 'error')

    return locals()

@action('calendar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('calendar.html', delimiters='[%[ ]]',))

def calendar():
    ctrl_info= { 'c':'calendar', 'v':'calendar.html' }
    messages = ['calendar', 'calendar.html']
    #
    ctrl_template_url = "\'" + URL('calendar' ) + "\'"

    # 
    fcalendar0= Form(db.dfcalendar0, dbio=False, formstyle=FormStyleBulma)
    if fcalendar0.accepted:
        icon_type ='success' if insert_form_vars(fcalendar0, db.dfcalendar0) else 'info'
        return json2user(mess = str( fcalendar0.form_name ), icon_type=icon_type )
    elif fcalendar0.errors:
        print("fcalendar0 has errors: %s" % (fcalendar0.errors))
        return json2user(mess = str(fcalendar0.form_name), icon_type = 'error')

    return locals()

@action('datatable', method=["GET", "POST"] )
@action.uses(db, session, T, Template('datatable.html', delimiters='[%[ ]]',))

def datatable():
    ctrl_info= { 'c':'datatable', 'v':'datatable.html' }
    messages = ['datatable', 'datatable.html']
    #
    ctrl_template_url = "\'" + URL('datatable' ) + "\'"

    rows_tdatatable0= db(db.tdatatable0).select()
    return locals()

@action('vectorXmaps', method=["GET", "POST"] )
@action.uses(db, session, T, Template('vector-maps.html', delimiters='[%[ ]]',))

def vectorXmaps():
    ctrl_info= { 'c':'vectorXmaps', 'v':'vector-maps.html' }
    messages = ['vectorXmaps', 'vector-maps.html']
    #
    ctrl_template_url = "\'" + URL('vectorXmaps' ) + "\'"

    return locals()

@action('googleXmaps', method=["GET", "POST"] )
@action.uses(db, session, T, Template('google-maps.html', delimiters='[%[ ]]',))

def googleXmaps():
    ctrl_info= { 'c':'googleXmaps', 'v':'google-maps.html' }
    messages = ['googleXmaps', 'google-maps.html']
    #
    ctrl_template_url = "\'" + URL('googleXmaps' ) + "\'"

    return locals()

@action('basicXtable', method=["GET", "POST"] )
@action.uses(db, session, T, Template('basic-table.html', delimiters='[%[ ]]',))

def basicXtable():
    ctrl_info= { 'c':'basicXtable', 'v':'basic-table.html' }
    messages = ['basicXtable', 'basic-table.html']
    #
    ctrl_template_url = "\'" + URL('basicXtable' ) + "\'"

    rows_tbasicXtable0= db(db.tbasicXtable0).select()
    rows_tbasicXtable1= db(db.tbasicXtable1).select()
    rows_tbasicXtable2= db(db.tbasicXtable2).select()
    rows_tbasicXtable3= db(db.tbasicXtable3).select()
    rows_tbasicXtable4= db(db.tbasicXtable4).select()
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
# curl -X  GET   http://localhost:8000/adminator/api/test_table/
# curl -X  GET   http://localhost:8000/adminator/api/test_table/9
# curl -X DELETE  http://localhost:8000/adminator/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/adminator/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/adminator/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/adminator/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/adminator/api/test_table/
#  http         localhost:8000/adminator/api/test_table/9
#  http -f POST localhost:8000/adminator/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/adminator/api/test_table/2
#  http -f PUT localhost:8000/adminator/api/test_table/2 f0=111111 f1=2222222 f2=333333

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

from .atab_utils import mytab_grid
from .images_utils import ima_grid
from .upload_utils import p4wupload_file
from .tlist_utils import tlist 

@unauthenticated("tabinfo", "tabinfo.html")
def tabinfo():
    user = auth.get_user()
    # simple backand-admin-panel (to be continued)
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    menu = DIV(
               P( SPAN(f"app: {APP_NAME}", _style="color:red"),  " admin-panel"),
               A( "tlist", _role="button", _href=URL('tlist', ),) ,
               A( "app_images", _role="button", _href=URL('ima_grid', ),) ,
               A( "p4wupload_file", _role="button", _href=URL('p4wupload_file', ),) ,
               A( "sql2table", _role="button", _href=URL('mytab_grid', ),) ,
              )
    return dict(message=message, menu=menu)

