#
# py4web app, AI-biorex ported 01.12.2020 11:27:59 UTC+3
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

@action('X404', method=["GET", "POST"] )
@action.uses(Template('404.html', delimiters='[%[ ]]',), db, session, T,)

def X404():
    ctrl_info= "ctrl: X404, view: 404.html"
    page_url = "\'" + URL('X404' ) + "\'"
    messages = []

    return locals()

@action('X500', method=["GET", "POST"] )
@action.uses(Template('500.html', delimiters='[%[ ]]',), db, session, T,)

def X500():
    ctrl_info= "ctrl: X500, view: 500.html"
    page_url = "\'" + URL('X500' ) + "\'"
    messages = []

    return locals()

@action('lock', method=["GET", "POST"] )
@action.uses(Template('lock.html', delimiters='[%[ ]]',), db, session, T,)

def lock():
    ctrl_info= "ctrl: lock, view: lock.html"
    page_url = "\'" + URL('lock' ) + "\'"
    messages = []

    flock0= Form(db.dflock0, dbio=False, formstyle=FormStyleBulma)

    if flock0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( flock0, db.dflock0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( flock0.form_name ))
    elif flock0.errors:
        print("flock0 has errors: %s" % (flock0.errors))
        return put_json_messages('error: ' + str( flock0.form_name ))
 

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T,)

def index():
    ctrl_info= "ctrl: index, view: index.html"
    page_url = "\'" + URL('index' ) + "\'"
    messages = []

    findex0= Form(db.dfindex0, dbio=False, formstyle=FormStyleBulma)

    if findex0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex0, db.dfindex0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex0.form_name ))
    elif findex0.errors:
        print("findex0 has errors: %s" % (findex0.errors))
        return put_json_messages('error: ' + str( findex0.form_name ))
 

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
 

    return locals()

@action('modals', method=["GET", "POST"] )
@action.uses(Template('modals.html', delimiters='[%[ ]]',), db, session, T,)

def modals():
    ctrl_info= "ctrl: modals, view: modals.html"
    page_url = "\'" + URL('modals' ) + "\'"
    messages = []

    fmodals0= Form(db.dfmodals0, dbio=False, formstyle=FormStyleBulma)

    if fmodals0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmodals0, db.dfmodals0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmodals0.form_name ))
    elif fmodals0.errors:
        print("fmodals0 has errors: %s" % (fmodals0.errors))
        return put_json_messages('error: ' + str( fmodals0.form_name ))
 

    fmodals1= Form(db.dfmodals1, dbio=False, formstyle=FormStyleBulma)

    if fmodals1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmodals1, db.dfmodals1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmodals1.form_name ))
    elif fmodals1.errors:
        print("fmodals1 has errors: %s" % (fmodals1.errors))
        return put_json_messages('error: ' + str( fmodals1.form_name ))
 

    fmodals2= Form(db.dfmodals2, dbio=False, formstyle=FormStyleBulma)

    if fmodals2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmodals2, db.dfmodals2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmodals2.form_name ))
    elif fmodals2.errors:
        print("fmodals2 has errors: %s" % (fmodals2.errors))
        return put_json_messages('error: ' + str( fmodals2.form_name ))
 

    fmodals3= Form(db.dfmodals3, dbio=False, formstyle=FormStyleBulma)

    if fmodals3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmodals3, db.dfmodals3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmodals3.form_name ))
    elif fmodals3.errors:
        print("fmodals3 has errors: %s" % (fmodals3.errors))
        return put_json_messages('error: ' + str( fmodals3.form_name ))
 

    return locals()

@action('buttons', method=["GET", "POST"] )
@action.uses(Template('buttons.html', delimiters='[%[ ]]',), db, session, T,)

def buttons():
    ctrl_info= "ctrl: buttons, view: buttons.html"
    page_url = "\'" + URL('buttons' ) + "\'"
    messages = []

    fbuttons0= Form(db.dfbuttons0, dbio=False, formstyle=FormStyleBulma)

    if fbuttons0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fbuttons0, db.dfbuttons0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fbuttons0.form_name ))
    elif fbuttons0.errors:
        print("fbuttons0 has errors: %s" % (fbuttons0.errors))
        return put_json_messages('error: ' + str( fbuttons0.form_name ))
 

    return locals()

@action('signXup', method=["GET", "POST"] )
@action.uses(Template('sign-up.html', delimiters='[%[ ]]',), db, session, T,)

def signXup():
    ctrl_info= "ctrl: signXup, view: sign-up.html"
    page_url = "\'" + URL('signXup' ) + "\'"
    messages = []

    fsignXup0= Form(db.dfsignXup0, dbio=False, formstyle=FormStyleBulma)

    if fsignXup0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fsignXup0, db.dfsignXup0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fsignXup0.form_name ))
    elif fsignXup0.errors:
        print("fsignXup0 has errors: %s" % (fsignXup0.errors))
        return put_json_messages('error: ' + str( fsignXup0.form_name ))
 

    return locals()

@action('signXin', method=["GET", "POST"] )
@action.uses(Template('sign-in.html', delimiters='[%[ ]]',), db, session, T,)

def signXin():
    ctrl_info= "ctrl: signXin, view: sign-in.html"
    page_url = "\'" + URL('signXin' ) + "\'"
    messages = []

    fsignXin0= Form(db.dfsignXin0, dbio=False, formstyle=FormStyleBulma)

    if fsignXin0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fsignXin0, db.dfsignXin0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fsignXin0.form_name ))
    elif fsignXin0.errors:
        print("fsignXin0 has errors: %s" % (fsignXin0.errors))
        return put_json_messages('error: ' + str( fsignXin0.form_name ))
 

    return locals()

@action('settings', method=["GET", "POST"] )
@action.uses(Template('settings.html', delimiters='[%[ ]]',), db, session, T,)

def settings():
    ctrl_info= "ctrl: settings, view: settings.html"
    page_url = "\'" + URL('settings' ) + "\'"
    messages = []

    fsettings0= Form(db.dfsettings0, dbio=False, formstyle=FormStyleBulma)

    if fsettings0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fsettings0, db.dfsettings0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fsettings0.form_name ))
    elif fsettings0.errors:
        print("fsettings0 has errors: %s" % (fsettings0.errors))
        return put_json_messages('error: ' + str( fsettings0.form_name ))
 

    fsettings1= Form(db.dfsettings1, dbio=False, formstyle=FormStyleBulma)

    if fsettings1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fsettings1, db.dfsettings1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fsettings1.form_name ))
    elif fsettings1.errors:
        print("fsettings1 has errors: %s" % (fsettings1.errors))
        return put_json_messages('error: ' + str( fsettings1.form_name ))
 

    return locals()

@action('dashboard', method=["GET", "POST"] )
@action.uses(Template('dashboard.html', delimiters='[%[ ]]',), db, session, T,)

def dashboard():
    ctrl_info= "ctrl: dashboard, view: dashboard.html"
    page_url = "\'" + URL('dashboard' ) + "\'"
    messages = []

    rows_tdashboard0= db(db.tdashboard0).select()
    fdashboard0= Form(db.dfdashboard0, dbio=False, formstyle=FormStyleBulma)

    if fdashboard0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fdashboard0, db.dfdashboard0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fdashboard0.form_name ))
    elif fdashboard0.errors:
        print("fdashboard0 has errors: %s" % (fdashboard0.errors))
        return put_json_messages('error: ' + str( fdashboard0.form_name ))
 

    return locals()

@action('typography', method=["GET", "POST"] )
@action.uses(Template('typography.html', delimiters='[%[ ]]',), db, session, T,)

def typography():
    ctrl_info= "ctrl: typography, view: typography.html"
    page_url = "\'" + URL('typography' ) + "\'"
    messages = []

    ftypography0= Form(db.dftypography0, dbio=False, formstyle=FormStyleBulma)

    if ftypography0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftypography0, db.dftypography0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftypography0.form_name ))
    elif ftypography0.errors:
        print("ftypography0 has errors: %s" % (ftypography0.errors))
        return put_json_messages('error: ' + str( ftypography0.form_name ))
 

    return locals()

@action('transactions', method=["GET", "POST"] )
@action.uses(Template('transactions.html', delimiters='[%[ ]]',), db, session, T,)

def transactions():
    ctrl_info= "ctrl: transactions, view: transactions.html"
    page_url = "\'" + URL('transactions' ) + "\'"
    messages = []

    rows_ttransactions0= db(db.ttransactions0).select()
    ftransactions0= Form(db.dftransactions0, dbio=False, formstyle=FormStyleBulma)

    if ftransactions0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftransactions0, db.dftransactions0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftransactions0.form_name ))
    elif ftransactions0.errors:
        print("ftransactions0 has errors: %s" % (ftransactions0.errors))
        return put_json_messages('error: ' + str( ftransactions0.form_name ))
 

    return locals()

@action('notifications', method=["GET", "POST"] )
@action.uses(Template('notifications.html', delimiters='[%[ ]]',), db, session, T,)

def notifications():
    ctrl_info= "ctrl: notifications, view: notifications.html"
    page_url = "\'" + URL('notifications' ) + "\'"
    messages = []

    fnotifications0= Form(db.dfnotifications0, dbio=False, formstyle=FormStyleBulma)

    if fnotifications0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fnotifications0, db.dfnotifications0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fnotifications0.form_name ))
    elif fnotifications0.errors:
        print("fnotifications0 has errors: %s" % (fnotifications0.errors))
        return put_json_messages('error: ' + str( fnotifications0.form_name ))
 

    return locals()

@action('upgradeXtoXpro', method=["GET", "POST"] )
@action.uses(Template('upgrade-to-pro.html', delimiters='[%[ ]]',), db, session, T,)

def upgradeXtoXpro():
    ctrl_info= "ctrl: upgradeXtoXpro, view: upgrade-to-pro.html"
    page_url = "\'" + URL('upgradeXtoXpro' ) + "\'"
    messages = []

    rows_tupgradeXtoXpro0= db(db.tupgradeXtoXpro0).select()
    return locals()

@action('resetXpassword', method=["GET", "POST"] )
@action.uses(Template('reset-password.html', delimiters='[%[ ]]',), db, session, T,)

def resetXpassword():
    ctrl_info= "ctrl: resetXpassword, view: reset-password.html"
    page_url = "\'" + URL('resetXpassword' ) + "\'"
    messages = []

    fresetXpassword0= Form(db.dfresetXpassword0, dbio=False, formstyle=FormStyleBulma)

    if fresetXpassword0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fresetXpassword0, db.dfresetXpassword0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fresetXpassword0.form_name ))
    elif fresetXpassword0.errors:
        print("fresetXpassword0 has errors: %s" % (fresetXpassword0.errors))
        return put_json_messages('error: ' + str( fresetXpassword0.form_name ))
 

    return locals()

@action('forgotXpassword', method=["GET", "POST"] )
@action.uses(Template('forgot-password.html', delimiters='[%[ ]]',), db, session, T,)

def forgotXpassword():
    ctrl_info= "ctrl: forgotXpassword, view: forgot-password.html"
    page_url = "\'" + URL('forgotXpassword' ) + "\'"
    messages = []

    fforgotXpassword0= Form(db.dfforgotXpassword0, dbio=False, formstyle=FormStyleBulma)

    if fforgotXpassword0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fforgotXpassword0, db.dfforgotXpassword0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fforgotXpassword0.form_name ))
    elif fforgotXpassword0.errors:
        print("fforgotXpassword0 has errors: %s" % (fforgotXpassword0.errors))
        return put_json_messages('error: ' + str( fforgotXpassword0.form_name ))
 

    return locals()

@action('bootstrapXtables', method=["GET", "POST"] )
@action.uses(Template('bootstrap-tables.html', delimiters='[%[ ]]',), db, session, T,)

def bootstrapXtables():
    ctrl_info= "ctrl: bootstrapXtables, view: bootstrap-tables.html"
    page_url = "\'" + URL('bootstrapXtables' ) + "\'"
    messages = []

    rows_tbootstrapXtables0= db(db.tbootstrapXtables0).select()
    rows_tbootstrapXtables1= db(db.tbootstrapXtables1).select()
    fbootstrapXtables0= Form(db.dfbootstrapXtables0, dbio=False, formstyle=FormStyleBulma)

    if fbootstrapXtables0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fbootstrapXtables0, db.dfbootstrapXtables0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fbootstrapXtables0.form_name ))
    elif fbootstrapXtables0.errors:
        print("fbootstrapXtables0 has errors: %s" % (fbootstrapXtables0.errors))
        return put_json_messages('error: ' + str( fbootstrapXtables0.form_name ))
 

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
# curl -X  GET   http://localhost:8000/volt/api/test_table/
# curl -X  GET   http://localhost:8000/volt/api/test_table/9
# curl -X DELETE  http://localhost:8000/volt/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/volt/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/volt/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/volt/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/volt/api/test_table/
#  http         localhost:8000/volt/api/test_table/9
#  http -f POST localhost:8000/volt/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/volt/api/test_table/2
#  http -f PUT localhost:8000/volt/api/test_table/2 f0=111111 f1=2222222 f2=333333


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

