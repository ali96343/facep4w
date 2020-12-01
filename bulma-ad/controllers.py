#
# py4web app, AI-biorex ported 01.12.2020 12:59:38 UTC+3
# https://github.com/ali96343/facep4w
#

import os, json
import bottle

from py4web import action, request, response,  abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from py4web.core import Template, Reloader
from py4web.utils.dbstore import DBStore

#from yatl.helpers import INPUT, H1, HTML, BODY, A
from .common import db, session, T, cache, authenticated, unauthenticated, auth
from .settings import APP_NAME


 
# ---------------------- Global -----------------------------------------------------

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)

#db_sess = DAL('sqlite:memory')
#session =  Session(storage=DBStore(db_sess))

Glb= {'debug': True , 'my_app_name': APP_NAME, 'tte_path': '/static/tte' }

# ---------------------- Utils -------------------------------------------------------

def prn_form_vars(myform, mydb,):

        id_db = None; row_db = None; f0_fld = None; inserted = False

        if Glb['debug'] == True:
            print("app:",Glb['my_app_name'])
            _ = [ print (f'     {k}: {v}') for k,v in myform.vars.items() if k != '_formkey']

        f0_fld = myform.vars.get('f0', None )
        if (not f0_fld is None) and len(f0_fld):
            id_db = mydb.insert(**mydb._filter_fields(myform.vars))
            db.commit()

            if not id_db is None:
                row_db = mydb(id_db )

                if not row_db is None:
                    if Glb['debug'] == True:
                         print(f'     inserted: \"{myform.vars.f0}\" into {mydb.f0}, id = {id_db}' )
                         print(f"     select  : \"{row_db.f0}\" from {mydb.f0}, id = {id_db}" )
                         print ()
                    inserted =True
        else:
            if Glb['debug'] == True:
                print(f"     no entry inserted: (f0_fld is None) or (len(f0_fld) == 0)")
                print()

        return inserted
            
def put_json_messages(mess='mymess'):
    response.headers["Content-Type"] = "application/json"
    return json.dumps( {'messages' : f'{mess}'})
    
# ---------------------- Controllers  ------------------------------------------------

@action('login', method=["GET", "POST"] )
@action.uses(Template('login.html', delimiters='[%[ ]]',), db, session, T,)

def login():
    ctrl_info= "ctrl: login, view: login.html"
    page_url = "\'" + URL('login' ) + "\'"
    messages = []

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T,)

def index():
    ctrl_info= "ctrl: index, view: index.html"
    page_url = "\'" + URL('index' ) + "\'"
    messages = []

    rows_tindex0= db(db.tindex0).select()
    rows_tindex1= db(db.tindex1).select()
    return locals()

@action('forms', method=["GET", "POST"] )
@action.uses(Template('forms.html', delimiters='[%[ ]]',), db, session, T,)

def forms():
    ctrl_info= "ctrl: forms, view: forms.html"
    page_url = "\'" + URL('forms' ) + "\'"
    messages = []

    fforms0= Form(db.dfforms0, dbio=False, formstyle=FormStyleBulma)

    if fforms0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms0, db.dfforms0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms0.form_name ))
    elif fforms0.errors:
        print("fforms0 has errors: %s" % (fforms0.errors))
        return put_json_messages('error: ' + str( fforms0.form_name ))
 

    fforms1= Form(db.dfforms1, dbio=False, formstyle=FormStyleBulma)

    if fforms1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms1, db.dfforms1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms1.form_name ))
    elif fforms1.errors:
        print("fforms1 has errors: %s" % (fforms1.errors))
        return put_json_messages('error: ' + str( fforms1.form_name ))
 

    fforms2= Form(db.dfforms2, dbio=False, formstyle=FormStyleBulma)

    if fforms2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms2, db.dfforms2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms2.form_name ))
    elif fforms2.errors:
        print("fforms2 has errors: %s" % (fforms2.errors))
        return put_json_messages('error: ' + str( fforms2.form_name ))
 

    fforms3= Form(db.dfforms3, dbio=False, formstyle=FormStyleBulma)

    if fforms3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms3, db.dfforms3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms3.form_name ))
    elif fforms3.errors:
        print("fforms3 has errors: %s" % (fforms3.errors))
        return put_json_messages('error: ' + str( fforms3.form_name ))
 

    fforms4= Form(db.dfforms4, dbio=False, formstyle=FormStyleBulma)

    if fforms4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms4, db.dfforms4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms4.form_name ))
    elif fforms4.errors:
        print("fforms4 has errors: %s" % (fforms4.errors))
        return put_json_messages('error: ' + str( fforms4.form_name ))
 

    fforms5= Form(db.dfforms5, dbio=False, formstyle=FormStyleBulma)

    if fforms5.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms5, db.dfforms5 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms5.form_name ))
    elif fforms5.errors:
        print("fforms5 has errors: %s" % (fforms5.errors))
        return put_json_messages('error: ' + str( fforms5.form_name ))
 

    fforms6= Form(db.dfforms6, dbio=False, formstyle=FormStyleBulma)

    if fforms6.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms6, db.dfforms6 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms6.form_name ))
    elif fforms6.errors:
        print("fforms6 has errors: %s" % (fforms6.errors))
        return put_json_messages('error: ' + str( fforms6.form_name ))
 

    fforms7= Form(db.dfforms7, dbio=False, formstyle=FormStyleBulma)

    if fforms7.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms7, db.dfforms7 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms7.form_name ))
    elif fforms7.errors:
        print("fforms7 has errors: %s" % (fforms7.errors))
        return put_json_messages('error: ' + str( fforms7.form_name ))
 

    fforms8= Form(db.dfforms8, dbio=False, formstyle=FormStyleBulma)

    if fforms8.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms8, db.dfforms8 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms8.form_name ))
    elif fforms8.errors:
        print("fforms8 has errors: %s" % (fforms8.errors))
        return put_json_messages('error: ' + str( fforms8.form_name ))
 

    fforms9= Form(db.dfforms9, dbio=False, formstyle=FormStyleBulma)

    if fforms9.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms9, db.dfforms9 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms9.form_name ))
    elif fforms9.errors:
        print("fforms9 has errors: %s" % (fforms9.errors))
        return put_json_messages('error: ' + str( fforms9.form_name ))
 

    fforms10= Form(db.dfforms10, dbio=False, formstyle=FormStyleBulma)

    if fforms10.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms10, db.dfforms10 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms10.form_name ))
    elif fforms10.errors:
        print("fforms10 has errors: %s" % (fforms10.errors))
        return put_json_messages('error: ' + str( fforms10.form_name ))
 

    fforms11= Form(db.dfforms11, dbio=False, formstyle=FormStyleBulma)

    if fforms11.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms11, db.dfforms11 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms11.form_name ))
    elif fforms11.errors:
        print("fforms11 has errors: %s" % (fforms11.errors))
        return put_json_messages('error: ' + str( fforms11.form_name ))
 

    fforms12= Form(db.dfforms12, dbio=False, formstyle=FormStyleBulma)

    if fforms12.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms12, db.dfforms12 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms12.form_name ))
    elif fforms12.errors:
        print("fforms12 has errors: %s" % (fforms12.errors))
        return put_json_messages('error: ' + str( fforms12.form_name ))
 

    fforms13= Form(db.dfforms13, dbio=False, formstyle=FormStyleBulma)

    if fforms13.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms13, db.dfforms13 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms13.form_name ))
    elif fforms13.errors:
        print("fforms13 has errors: %s" % (fforms13.errors))
        return put_json_messages('error: ' + str( fforms13.form_name ))
 

    fforms14= Form(db.dfforms14, dbio=False, formstyle=FormStyleBulma)

    if fforms14.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms14, db.dfforms14 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms14.form_name ))
    elif fforms14.errors:
        print("fforms14 has errors: %s" % (fforms14.errors))
        return put_json_messages('error: ' + str( fforms14.form_name ))
 

    fforms15= Form(db.dfforms15, dbio=False, formstyle=FormStyleBulma)

    if fforms15.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms15, db.dfforms15 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms15.form_name ))
    elif fforms15.errors:
        print("fforms15 has errors: %s" % (fforms15.errors))
        return put_json_messages('error: ' + str( fforms15.form_name ))
 

    fforms16= Form(db.dfforms16, dbio=False, formstyle=FormStyleBulma)

    if fforms16.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms16, db.dfforms16 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms16.form_name ))
    elif fforms16.errors:
        print("fforms16 has errors: %s" % (fforms16.errors))
        return put_json_messages('error: ' + str( fforms16.form_name ))
 

    fforms17= Form(db.dfforms17, dbio=False, formstyle=FormStyleBulma)

    if fforms17.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms17, db.dfforms17 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms17.form_name ))
    elif fforms17.errors:
        print("fforms17 has errors: %s" % (fforms17.errors))
        return put_json_messages('error: ' + str( fforms17.form_name ))
 

    fforms18= Form(db.dfforms18, dbio=False, formstyle=FormStyleBulma)

    if fforms18.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms18, db.dfforms18 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms18.form_name ))
    elif fforms18.errors:
        print("fforms18 has errors: %s" % (fforms18.errors))
        return put_json_messages('error: ' + str( fforms18.form_name ))
 

    fforms19= Form(db.dfforms19, dbio=False, formstyle=FormStyleBulma)

    if fforms19.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms19, db.dfforms19 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms19.form_name ))
    elif fforms19.errors:
        print("fforms19 has errors: %s" % (fforms19.errors))
        return put_json_messages('error: ' + str( fforms19.form_name ))
 

    fforms20= Form(db.dfforms20, dbio=False, formstyle=FormStyleBulma)

    if fforms20.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms20, db.dfforms20 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms20.form_name ))
    elif fforms20.errors:
        print("fforms20 has errors: %s" % (fforms20.errors))
        return put_json_messages('error: ' + str( fforms20.form_name ))
 

    fforms21= Form(db.dfforms21, dbio=False, formstyle=FormStyleBulma)

    if fforms21.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms21, db.dfforms21 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms21.form_name ))
    elif fforms21.errors:
        print("fforms21 has errors: %s" % (fforms21.errors))
        return put_json_messages('error: ' + str( fforms21.form_name ))
 

    fforms22= Form(db.dfforms22, dbio=False, formstyle=FormStyleBulma)

    if fforms22.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms22, db.dfforms22 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms22.form_name ))
    elif fforms22.errors:
        print("fforms22 has errors: %s" % (fforms22.errors))
        return put_json_messages('error: ' + str( fforms22.form_name ))
 

    fforms23= Form(db.dfforms23, dbio=False, formstyle=FormStyleBulma)

    if fforms23.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms23, db.dfforms23 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms23.form_name ))
    elif fforms23.errors:
        print("fforms23 has errors: %s" % (fforms23.errors))
        return put_json_messages('error: ' + str( fforms23.form_name ))
 

    fforms24= Form(db.dfforms24, dbio=False, formstyle=FormStyleBulma)

    if fforms24.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms24, db.dfforms24 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms24.form_name ))
    elif fforms24.errors:
        print("fforms24 has errors: %s" % (fforms24.errors))
        return put_json_messages('error: ' + str( fforms24.form_name ))
 

    fforms25= Form(db.dfforms25, dbio=False, formstyle=FormStyleBulma)

    if fforms25.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms25, db.dfforms25 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms25.form_name ))
    elif fforms25.errors:
        print("fforms25 has errors: %s" % (fforms25.errors))
        return put_json_messages('error: ' + str( fforms25.form_name ))
 

    fforms26= Form(db.dfforms26, dbio=False, formstyle=FormStyleBulma)

    if fforms26.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms26, db.dfforms26 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms26.form_name ))
    elif fforms26.errors:
        print("fforms26 has errors: %s" % (fforms26.errors))
        return put_json_messages('error: ' + str( fforms26.form_name ))
 

    fforms27= Form(db.dfforms27, dbio=False, formstyle=FormStyleBulma)

    if fforms27.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforms27, db.dfforms27 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforms27.form_name ))
    elif fforms27.errors:
        print("fforms27 has errors: %s" % (fforms27.errors))
        return put_json_messages('error: ' + str( fforms27.form_name ))
 

    return locals()

@action('elements', method=["GET", "POST"] )
@action.uses(Template('elements.html', delimiters='[%[ ]]',), db, session, T,)

def elements():
    ctrl_info= "ctrl: elements, view: elements.html"
    page_url = "\'" + URL('elements' ) + "\'"
    messages = []

    rows_telements0= db(db.telements0).select()
    return locals()

@action('datatables', method=["GET", "POST"] )
@action.uses(Template('datatables.html', delimiters='[%[ ]]',), db, session, T,)

def datatables():
    ctrl_info= "ctrl: datatables, view: datatables.html"
    page_url = "\'" + URL('datatables' ) + "\'"
    messages = []

    rows_tdatatables0= db(db.tdatatables0).select()
    fdatatables0= Form(db.dfdatatables0, dbio=False, formstyle=FormStyleBulma)

    if fdatatables0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fdatatables0, db.dfdatatables0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fdatatables0.form_name ))
    elif fdatatables0.errors:
        print("fdatatables0 has errors: %s" % (fdatatables0.errors))
        return put_json_messages('error: ' + str( fdatatables0.form_name ))
 

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
# curl -X  GET   http://localhost:8000/bulma-ad/api/test_table/
# curl -X  GET   http://localhost:8000/bulma-ad/api/test_table/9
# curl -X DELETE  http://localhost:8000/bulma-ad/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/bulma-ad/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/bulma-ad/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/bulma-ad/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/bulma-ad/api/test_table/
#  http         localhost:8000/bulma-ad/api/test_table/9
#  http -f POST localhost:8000/bulma-ad/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/bulma-ad/api/test_table/2
#  http -f PUT localhost:8000/bulma-ad/api/test_table/2 f0=111111 f1=2222222 f2=333333


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
        files_prefix = location + Glb["tte_path"]

        location_2x = location + location + "/"
        files_prefix_2x = files_prefix + files_prefix + "/"

        def rm_bad_prefix(bad_prefix):
            new_location = bottle.request.path.replace(bad_prefix, "", 1)
            Glb["debug"] and func_mess.append(f"     rm_bad_prefix: {bad_prefix}")
            return new_location

        if bottle.request.path.startswith(files_prefix_2x):
            if len(bottle.request.path) > len(files_prefix_2x):
                location = rm_bad_prefix(files_prefix)

        elif bottle.request.path.startswith(location_2x):
            if len(bottle.request.path) > len(location_2x):
                location = rm_bad_prefix(location)
    if Glb["debug"]:
        debug_mess = [  f"404  app=/{Glb['my_app_name']}, err_path={bottle.request.path}",
                        f"     info: {error}", ]
        if len(func_mess):
            debug_mess += func_mess
        debug_mess.append(f"     goto_new_path: {location}\n")
        print("\n".join(debug_mess))

    bottle.response.status = 303
    bottle.response.set_header("Location", location)

