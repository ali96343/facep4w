#!/usr/bin/env python3

#
# py4web app, AI-biorex ported 21.10.2020 16:37:42
#

import os
from py4web import action, request, abort, redirect, URL, Field
from yatl.helpers import A
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A
from py4web.core import Template, Reloader

from .common import db, session, T, cache, authenticated, unauthenticated, auth
import bottle

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)

Glb= {'debug': True , 'my_app_name' : "bubbly", 'tte_path': '/static/tte' }



@action('forms', method=["GET", "POST"] )
@action.uses(Template('forms.html', delimiters='[%[ ]]',), db, session,  T, )

def forms(id=None):
    ctrl_info= "ctrl: forms, view: forms.html"
    messages = []

    dfforms0_rows= None
    id_dfforms0 = None
    fforms0= Form(db.dfforms0, id, deletable=False, dbio = False, keep_values = False, form_name = "fforms0",  formstyle=FormStyleBulma )
   
    if fforms0.accepted:

        Glb['debug'] and print("     fforms0 accepted with: %s " % (fforms0.vars))
        fforms0_f0 = fforms0.vars.get('f0','')
        if len ( fforms0_f0 ):
            id_dfforms0 = db.dfforms0.insert( **fforms0.vars )
            db.commit()

            if not id_dfforms0 is None:
                dfforms0_rows = db.dfforms0(id_dfforms0 )

                if not dfforms0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fforms0.vars.f0}\" into db.dfforms0.f0, id = {id_dfforms0}' )
                         print(f"     found db.dfforms0.f0: \"{dfforms0_rows.f0}\", id = {id_dfforms0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fforms0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms0.vars.items() ]
                print()
   
    elif fforms0.errors:
        print("fforms0 has errors: %s " % (fforms0.errors))
 

    dfforms1_rows= None
    id_dfforms1 = None
    fforms1= Form(db.dfforms1, id, deletable=False, dbio = False, keep_values = False, form_name = "fforms1",  formstyle=FormStyleBulma )
   
    if fforms1.accepted:

        Glb['debug'] and print("     fforms1 accepted with: %s " % (fforms1.vars))
        fforms1_f0 = fforms1.vars.get('f0','')
        if len ( fforms1_f0 ):
            id_dfforms1 = db.dfforms1.insert( **fforms1.vars )
            db.commit()

            if not id_dfforms1 is None:
                dfforms1_rows = db.dfforms1(id_dfforms1 )

                if not dfforms1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fforms1.vars.f0}\" into db.dfforms1.f0, id = {id_dfforms1}' )
                         print(f"     found db.dfforms1.f0: \"{dfforms1_rows.f0}\", id = {id_dfforms1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fforms1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms1.vars.items() ]
                print()
   
    elif fforms1.errors:
        print("fforms1 has errors: %s " % (fforms1.errors))
 

    dfforms2_rows= None
    id_dfforms2 = None
    fforms2= Form(db.dfforms2, id, deletable=False, dbio = False, keep_values = False, form_name = "fforms2",  formstyle=FormStyleBulma )
   
    if fforms2.accepted:

        Glb['debug'] and print("     fforms2 accepted with: %s " % (fforms2.vars))
        fforms2_f0 = fforms2.vars.get('f0','')
        if len ( fforms2_f0 ):
            id_dfforms2 = db.dfforms2.insert( **fforms2.vars )
            db.commit()

            if not id_dfforms2 is None:
                dfforms2_rows = db.dfforms2(id_dfforms2 )

                if not dfforms2_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fforms2.vars.f0}\" into db.dfforms2.f0, id = {id_dfforms2}' )
                         print(f"     found db.dfforms2.f0: \"{dfforms2_rows.f0}\", id = {id_dfforms2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fforms2_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms2.vars.items() ]
                print()
   
    elif fforms2.errors:
        print("fforms2 has errors: %s " % (fforms2.errors))
 

    dfforms3_rows= None
    id_dfforms3 = None
    fforms3= Form(db.dfforms3, id, deletable=False, dbio = False, keep_values = False, form_name = "fforms3",  formstyle=FormStyleBulma )
   
    if fforms3.accepted:

        Glb['debug'] and print("     fforms3 accepted with: %s " % (fforms3.vars))
        fforms3_f0 = fforms3.vars.get('f0','')
        if len ( fforms3_f0 ):
            id_dfforms3 = db.dfforms3.insert( **fforms3.vars )
            db.commit()

            if not id_dfforms3 is None:
                dfforms3_rows = db.dfforms3(id_dfforms3 )

                if not dfforms3_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fforms3.vars.f0}\" into db.dfforms3.f0, id = {id_dfforms3}' )
                         print(f"     found db.dfforms3.f0: \"{dfforms3_rows.f0}\", id = {id_dfforms3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fforms3_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms3.vars.items() ]
                print()
   
    elif fforms3.errors:
        print("fforms3 has errors: %s " % (fforms3.errors))
 

    dfforms4_rows= None
    id_dfforms4 = None
    fforms4= Form(db.dfforms4, id, deletable=False, dbio = False, keep_values = False, form_name = "fforms4",  formstyle=FormStyleBulma )
   
    if fforms4.accepted:

        Glb['debug'] and print("     fforms4 accepted with: %s " % (fforms4.vars))
        fforms4_f0 = fforms4.vars.get('f0','')
        if len ( fforms4_f0 ):
            id_dfforms4 = db.dfforms4.insert( **fforms4.vars )
            db.commit()

            if not id_dfforms4 is None:
                dfforms4_rows = db.dfforms4(id_dfforms4 )

                if not dfforms4_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fforms4.vars.f0}\" into db.dfforms4.f0, id = {id_dfforms4}' )
                         print(f"     found db.dfforms4.f0: \"{dfforms4_rows.f0}\", id = {id_dfforms4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fforms4_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms4.vars.items() ]
                print()
   
    elif fforms4.errors:
        print("fforms4 has errors: %s " % (fforms4.errors))
 

    dfforms5_rows= None
    id_dfforms5 = None
    fforms5= Form(db.dfforms5, id, deletable=False, dbio = False, keep_values = False, form_name = "fforms5",  formstyle=FormStyleBulma )
   
    if fforms5.accepted:

        Glb['debug'] and print("     fforms5 accepted with: %s " % (fforms5.vars))
        fforms5_f0 = fforms5.vars.get('f0','')
        if len ( fforms5_f0 ):
            id_dfforms5 = db.dfforms5.insert( **fforms5.vars )
            db.commit()

            if not id_dfforms5 is None:
                dfforms5_rows = db.dfforms5(id_dfforms5 )

                if not dfforms5_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fforms5.vars.f0}\" into db.dfforms5.f0, id = {id_dfforms5}' )
                         print(f"     found db.dfforms5.f0: \"{dfforms5_rows.f0}\", id = {id_dfforms5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fforms5_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms5.vars.items() ]
                print()
   
    elif fforms5.errors:
        print("fforms5 has errors: %s " % (fforms5.errors))
 

    return locals()


@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session,  T, )

def index(id=None):
    ctrl_info= "ctrl: index, view: index.html"
    messages = []

    dfindex0_rows= None
    id_dfindex0 = None
    findex0= Form(db.dfindex0, id, deletable=False, dbio = False, keep_values = False, form_name = "findex0",  formstyle=FormStyleBulma )
   
    if findex0.accepted:

        Glb['debug'] and print("     findex0 accepted with: %s " % (findex0.vars))
        findex0_f0 = findex0.vars.get('f0','')
        if len ( findex0_f0 ):
            id_dfindex0 = db.dfindex0.insert( **findex0.vars )
            db.commit()

            if not id_dfindex0 is None:
                dfindex0_rows = db.dfindex0(id_dfindex0 )

                if not dfindex0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex0.vars.f0}\" into db.dfindex0.f0, id = {id_dfindex0}' )
                         print(f"     found db.dfindex0.f0: \"{dfindex0_rows.f0}\", id = {id_dfindex0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(findex0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in findex0.vars.items() ]
                print()
   
    elif findex0.errors:
        print("findex0 has errors: %s " % (findex0.errors))
 

    return locals()


@action('login', method=["GET", "POST"] )
@action.uses(Template('login.html', delimiters='[%[ ]]',), db, session,  T, )

def login(id=None):
    ctrl_info= "ctrl: login, view: login.html"
    messages = []

    dflogin0_rows= None
    id_dflogin0 = None
    flogin0= Form(db.dflogin0, id, deletable=False, dbio = False, keep_values = False, form_name = "flogin0",  formstyle=FormStyleBulma )
   
    if flogin0.accepted:

        Glb['debug'] and print("     flogin0 accepted with: %s " % (flogin0.vars))
        flogin0_f0 = flogin0.vars.get('f0','')
        if len ( flogin0_f0 ):
            id_dflogin0 = db.dflogin0.insert( **flogin0.vars )
            db.commit()

            if not id_dflogin0 is None:
                dflogin0_rows = db.dflogin0(id_dflogin0 )

                if not dflogin0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flogin0.vars.f0}\" into db.dflogin0.f0, id = {id_dflogin0}' )
                         print(f"     found db.dflogin0.f0: \"{dflogin0_rows.f0}\", id = {id_dflogin0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(flogin0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in flogin0.vars.items() ]
                print()
   
    elif flogin0.errors:
        print("flogin0 has errors: %s " % (flogin0.errors))
 

    return locals()


@action('charts', method=["GET", "POST"] )
@action.uses(Template('charts.html', delimiters='[%[ ]]',), db, session,  T, )

def charts(id=None):
    ctrl_info= "ctrl: charts, view: charts.html"
    messages = []

    dfcharts0_rows= None
    id_dfcharts0 = None
    fcharts0= Form(db.dfcharts0, id, deletable=False, dbio = False, keep_values = False, form_name = "fcharts0",  formstyle=FormStyleBulma )
   
    if fcharts0.accepted:

        Glb['debug'] and print("     fcharts0 accepted with: %s " % (fcharts0.vars))
        fcharts0_f0 = fcharts0.vars.get('f0','')
        if len ( fcharts0_f0 ):
            id_dfcharts0 = db.dfcharts0.insert( **fcharts0.vars )
            db.commit()

            if not id_dfcharts0 is None:
                dfcharts0_rows = db.dfcharts0(id_dfcharts0 )

                if not dfcharts0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcharts0.vars.f0}\" into db.dfcharts0.f0, id = {id_dfcharts0}' )
                         print(f"     found db.dfcharts0.f0: \"{dfcharts0_rows.f0}\", id = {id_dfcharts0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fcharts0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fcharts0.vars.items() ]
                print()
   
    elif fcharts0.errors:
        print("fcharts0 has errors: %s " % (fcharts0.errors))
 

    return locals()


@action('tables', method=["GET", "POST"] )
@action.uses(Template('tables.html', delimiters='[%[ ]]',), db, session,  T, )

def tables(id=None):
    ctrl_info= "ctrl: tables, view: tables.html"
    messages = []

    rows_ttables0= db(db.ttables0).select()
    rows_ttables1= db(db.ttables1).select()
    rows_ttables2= db(db.ttables2).select()
    rows_ttables3= db(db.ttables3).select()
    dftables0_rows= None
    id_dftables0 = None
    ftables0= Form(db.dftables0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftables0",  formstyle=FormStyleBulma )
   
    if ftables0.accepted:

        Glb['debug'] and print("     ftables0 accepted with: %s " % (ftables0.vars))
        ftables0_f0 = ftables0.vars.get('f0','')
        if len ( ftables0_f0 ):
            id_dftables0 = db.dftables0.insert( **ftables0.vars )
            db.commit()

            if not id_dftables0 is None:
                dftables0_rows = db.dftables0(id_dftables0 )

                if not dftables0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftables0.vars.f0}\" into db.dftables0.f0, id = {id_dftables0}' )
                         print(f"     found db.dftables0.f0: \"{dftables0_rows.f0}\", id = {id_dftables0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(ftables0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in ftables0.vars.items() ]
                print()
   
    elif ftables0.errors:
        print("ftables0 has errors: %s " % (ftables0.errors))
 

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
# curl -X  GET   http://localhost:8000/bubbly/api/test_table/
# curl -X  GET   http://localhost:8000/bubbly/api/test_table/9
# curl -X DELETE  http://localhost:8000/bubbly/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/bubbly/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/bubbly/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/bubbly/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/bubbly/api/test_table/
#  http         localhost:8000/bubbly/api/test_table/9
#  http -f POST localhost:8000/bubbly/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/bubbly/api/test_table/2
#  http -f PUT localhost:8000/bubbly/api/test_table/2 f0=111111 f1=2222222 f2=333333

