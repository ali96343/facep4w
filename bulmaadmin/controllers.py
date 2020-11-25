#!/usr/bin/env python3

#
# py4web app, AI-biorex ported 19.11.2020 10:44:24
#

import os
from py4web import action, request, abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A
from py4web.core import Template, Reloader
from py4web.utils.dbstore import DBStore

from .common import db, session, T, cache, authenticated, unauthenticated, auth
import bottle

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)

#db_sess = DAL('sqlite:memory')
#session =  Session(storage=DBStore(db_sess))


Glb= {'debug': True , 'my_app_name': "bulmaadmin", 'tte_path': '/static/tte' }



@action('forms', method=["GET", "POST"] )
@action.uses(Template('forms.html', delimiters='[%[ ]]',), db, session,  T, )

def forms(id=None):
    ctrl_info= "ctrl: forms, view: forms.html"
    messages = []

    dfforms0_row= None
    id_dfforms0 = None
    fforms0= Form(db.dfforms0, id, deletable= False, dbio= False, keep_values= True, form_name= "fforms0",  formstyle=FormStyleBulma )
   
    if fforms0.accepted:

        if Glb['debug'] == True:
            print("app:",Glb['my_app_name'])
            print("     fforms0 accepted with: %s " % (fforms0.vars))
        fforms0_f0 = fforms0.vars.get('f0','')
        if (not fforms0_f0 is None) and len ( fforms0_f0 ):
            id_dfforms0 = db.dfforms0.insert( **fforms0.vars )
            db.commit()

            if not id_dfforms0 is None:
                dfforms0_row = db.dfforms0(id_dfforms0 )

                if not dfforms0_row is None:
                    if Glb['debug'] == True:
                         print(f'     inserted: \"{fforms0.vars.f0}\" into db.dfforms0.f0, id = {id_dfforms0}' )
                         print(f"     select  : \"{dfforms0_row.f0}\" from db.dfforms0.f0, id = {id_dfforms0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print(f"     no entry inserted: (fforms0_f0 is None) or (len(fforms0_f0)==0)")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms0.vars.items() ]
                print()
   
    elif fforms0.errors:
        print("fforms0 has errors: %s " % (fforms0.errors))
 

    dfforms1_row= None
    id_dfforms1 = None
    fforms1= Form(db.dfforms1, id, deletable= False, dbio= False, keep_values= True, form_name= "fforms1",  formstyle=FormStyleBulma )
   
    if fforms1.accepted:

        if Glb['debug'] == True:
            print("app:",Glb['my_app_name'])
            print("     fforms1 accepted with: %s " % (fforms1.vars))
        fforms1_f0 = fforms1.vars.get('f0','')
        if (not fforms1_f0 is None) and len ( fforms1_f0 ):
            id_dfforms1 = db.dfforms1.insert( **fforms1.vars )
            db.commit()

            if not id_dfforms1 is None:
                dfforms1_row = db.dfforms1(id_dfforms1 )

                if not dfforms1_row is None:
                    if Glb['debug'] == True:
                         print(f'     inserted: \"{fforms1.vars.f0}\" into db.dfforms1.f0, id = {id_dfforms1}' )
                         print(f"     select  : \"{dfforms1_row.f0}\" from db.dfforms1.f0, id = {id_dfforms1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print(f"     no entry inserted: (fforms1_f0 is None) or (len(fforms1_f0)==0)")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms1.vars.items() ]
                print()
   
    elif fforms1.errors:
        print("fforms1 has errors: %s " % (fforms1.errors))
 

    dfforms2_row= None
    id_dfforms2 = None
    fforms2= Form(db.dfforms2, id, deletable= False, dbio= False, keep_values= True, form_name= "fforms2",  formstyle=FormStyleBulma )
   
    if fforms2.accepted:

        if Glb['debug'] == True:
            print("app:",Glb['my_app_name'])
            print("     fforms2 accepted with: %s " % (fforms2.vars))
        fforms2_f0 = fforms2.vars.get('f0','')
        if (not fforms2_f0 is None) and len ( fforms2_f0 ):
            id_dfforms2 = db.dfforms2.insert( **fforms2.vars )
            db.commit()

            if not id_dfforms2 is None:
                dfforms2_row = db.dfforms2(id_dfforms2 )

                if not dfforms2_row is None:
                    if Glb['debug'] == True:
                         print(f'     inserted: \"{fforms2.vars.f0}\" into db.dfforms2.f0, id = {id_dfforms2}' )
                         print(f"     select  : \"{dfforms2_row.f0}\" from db.dfforms2.f0, id = {id_dfforms2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print(f"     no entry inserted: (fforms2_f0 is None) or (len(fforms2_f0)==0)")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms2.vars.items() ]
                print()
   
    elif fforms2.errors:
        print("fforms2 has errors: %s " % (fforms2.errors))
 

    dfforms3_row= None
    id_dfforms3 = None
    fforms3= Form(db.dfforms3, id, deletable= False, dbio= False, keep_values= True, form_name= "fforms3",  formstyle=FormStyleBulma )
   
    if fforms3.accepted:

        if Glb['debug'] == True:
            print("app:",Glb['my_app_name'])
            print("     fforms3 accepted with: %s " % (fforms3.vars))
        fforms3_f0 = fforms3.vars.get('f0','')
        if (not fforms3_f0 is None) and len ( fforms3_f0 ):
            id_dfforms3 = db.dfforms3.insert( **fforms3.vars )
            db.commit()

            if not id_dfforms3 is None:
                dfforms3_row = db.dfforms3(id_dfforms3 )

                if not dfforms3_row is None:
                    if Glb['debug'] == True:
                         print(f'     inserted: \"{fforms3.vars.f0}\" into db.dfforms3.f0, id = {id_dfforms3}' )
                         print(f"     select  : \"{dfforms3_row.f0}\" from db.dfforms3.f0, id = {id_dfforms3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print(f"     no entry inserted: (fforms3_f0 is None) or (len(fforms3_f0)==0)")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms3.vars.items() ]
                print()
   
    elif fforms3.errors:
        print("fforms3 has errors: %s " % (fforms3.errors))
 

    dfforms4_row= None
    id_dfforms4 = None
    fforms4= Form(db.dfforms4, id, deletable= False, dbio= False, keep_values= True, form_name= "fforms4",  formstyle=FormStyleBulma )
   
    if fforms4.accepted:

        if Glb['debug'] == True:
            print("app:",Glb['my_app_name'])
            print("     fforms4 accepted with: %s " % (fforms4.vars))
        fforms4_f0 = fforms4.vars.get('f0','')
        if (not fforms4_f0 is None) and len ( fforms4_f0 ):
            id_dfforms4 = db.dfforms4.insert( **fforms4.vars )
            db.commit()

            if not id_dfforms4 is None:
                dfforms4_row = db.dfforms4(id_dfforms4 )

                if not dfforms4_row is None:
                    if Glb['debug'] == True:
                         print(f'     inserted: \"{fforms4.vars.f0}\" into db.dfforms4.f0, id = {id_dfforms4}' )
                         print(f"     select  : \"{dfforms4_row.f0}\" from db.dfforms4.f0, id = {id_dfforms4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print(f"     no entry inserted: (fforms4_f0 is None) or (len(fforms4_f0)==0)")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms4.vars.items() ]
                print()
   
    elif fforms4.errors:
        print("fforms4 has errors: %s " % (fforms4.errors))
 

    dfforms5_row= None
    id_dfforms5 = None
    fforms5= Form(db.dfforms5, id, deletable= False, dbio= False, keep_values= True, form_name= "fforms5",  formstyle=FormStyleBulma )
   
    if fforms5.accepted:

        if Glb['debug'] == True:
            print("app:",Glb['my_app_name'])
            print("     fforms5 accepted with: %s " % (fforms5.vars))
        fforms5_f0 = fforms5.vars.get('f0','')
        if (not fforms5_f0 is None) and len ( fforms5_f0 ):
            id_dfforms5 = db.dfforms5.insert( **fforms5.vars )
            db.commit()

            if not id_dfforms5 is None:
                dfforms5_row = db.dfforms5(id_dfforms5 )

                if not dfforms5_row is None:
                    if Glb['debug'] == True:
                         print(f'     inserted: \"{fforms5.vars.f0}\" into db.dfforms5.f0, id = {id_dfforms5}' )
                         print(f"     select  : \"{dfforms5_row.f0}\" from db.dfforms5.f0, id = {id_dfforms5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print(f"     no entry inserted: (fforms5_f0 is None) or (len(fforms5_f0)==0)")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms5.vars.items() ]
                print()
   
    elif fforms5.errors:
        print("fforms5 has errors: %s " % (fforms5.errors))
 

    dfforms6_row= None
    id_dfforms6 = None
    fforms6= Form(db.dfforms6, id, deletable= False, dbio= False, keep_values= True, form_name= "fforms6",  formstyle=FormStyleBulma )
   
    if fforms6.accepted:

        if Glb['debug'] == True:
            print("app:",Glb['my_app_name'])
            print("     fforms6 accepted with: %s " % (fforms6.vars))
        fforms6_f0 = fforms6.vars.get('f0','')
        if (not fforms6_f0 is None) and len ( fforms6_f0 ):
            id_dfforms6 = db.dfforms6.insert( **fforms6.vars )
            db.commit()

            if not id_dfforms6 is None:
                dfforms6_row = db.dfforms6(id_dfforms6 )

                if not dfforms6_row is None:
                    if Glb['debug'] == True:
                         print(f'     inserted: \"{fforms6.vars.f0}\" into db.dfforms6.f0, id = {id_dfforms6}' )
                         print(f"     select  : \"{dfforms6_row.f0}\" from db.dfforms6.f0, id = {id_dfforms6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print(f"     no entry inserted: (fforms6_f0 is None) or (len(fforms6_f0)==0)")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms6.vars.items() ]
                print()
   
    elif fforms6.errors:
        print("fforms6 has errors: %s " % (fforms6.errors))
 

    return locals()


@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session,  T, )

def index(id=None):
    ctrl_info= "ctrl: index, view: index.html"
    messages = []

    return locals()


@action('extras', method=["GET", "POST"] )
@action.uses(Template('extras.html', delimiters='[%[ ]]',), db, session,  T, )

def extras(id=None):
    ctrl_info= "ctrl: extras, view: extras.html"
    messages = []

    return locals()


@action('tables', method=["GET", "POST"] )
@action.uses(Template('tables.html', delimiters='[%[ ]]',), db, session,  T, )

def tables(id=None):
    ctrl_info= "ctrl: tables, view: tables.html"
    messages = []

    rows_ttables0= db(db.ttables0).select()
    rows_ttables1= db(db.ttables1).select()
    return locals()


@action('additional', method=["GET", "POST"] )
@action.uses(Template('additional.html', delimiters='[%[ ]]',), db, session,  T, )

def additional(id=None):
    ctrl_info= "ctrl: additional, view: additional.html"
    messages = []

    return locals()


@action('uiXelements', method=["GET", "POST"] )
@action.uses(Template('ui-elements.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelements(id=None):
    ctrl_info= "ctrl: uiXelements, view: ui-elements.html"
    messages = []

    dfuiXelements0_row= None
    id_dfuiXelements0 = None
    fuiXelements0= Form(db.dfuiXelements0, id, deletable= False, dbio= False, keep_values= True, form_name= "fuiXelements0",  formstyle=FormStyleBulma )
   
    if fuiXelements0.accepted:

        if Glb['debug'] == True:
            print("app:",Glb['my_app_name'])
            print("     fuiXelements0 accepted with: %s " % (fuiXelements0.vars))
        fuiXelements0_f0 = fuiXelements0.vars.get('f0','')
        if (not fuiXelements0_f0 is None) and len ( fuiXelements0_f0 ):
            id_dfuiXelements0 = db.dfuiXelements0.insert( **fuiXelements0.vars )
            db.commit()

            if not id_dfuiXelements0 is None:
                dfuiXelements0_row = db.dfuiXelements0(id_dfuiXelements0 )

                if not dfuiXelements0_row is None:
                    if Glb['debug'] == True:
                         print(f'     inserted: \"{fuiXelements0.vars.f0}\" into db.dfuiXelements0.f0, id = {id_dfuiXelements0}' )
                         print(f"     select  : \"{dfuiXelements0_row.f0}\" from db.dfuiXelements0.f0, id = {id_dfuiXelements0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print(f"     no entry inserted: (fuiXelements0_f0 is None) or (len(fuiXelements0_f0)==0)")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelements0.vars.items() ]
                print()
   
    elif fuiXelements0.errors:
        print("fuiXelements0 has errors: %s " % (fuiXelements0.errors))
 

    return locals()


@action('presentations', method=["GET", "POST"] )
@action.uses(Template('presentations.html', delimiters='[%[ ]]',), db, session,  T, )

def presentations(id=None):
    ctrl_info= "ctrl: presentations, view: presentations.html"
    messages = []

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
# curl -X  GET   http://localhost:8000/bulmaadmin/api/test_table/
# curl -X  GET   http://localhost:8000/bulmaadmin/api/test_table/9
# curl -X DELETE  http://localhost:8000/bulmaadmin/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/bulmaadmin/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/bulmaadmin/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/bulmaadmin/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/bulmaadmin/api/test_table/
#  http         localhost:8000/bulmaadmin/api/test_table/9
#  http -f POST localhost:8000/bulmaadmin/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/bulmaadmin/api/test_table/2
#  http -f PUT localhost:8000/bulmaadmin/api/test_table/2 f0=111111 f1=2222222 f2=333333


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

