#!/usr/bin/env python3

#
# py4web app, AI-biorex ported 21.10.2020 14:13:52
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

Glb= {'debug': True , 'my_app_name' : "sb", 'tte_path': '/static/tte' }



@action('X404', method=["GET", "POST"] )
@action.uses(Template('404.html', delimiters='[%[ ]]',), db, session,  T, )

def X404(id=None):
    ctrl_info= "ctrl: X404, view: 404.html"
    messages = []

    dfX4040_rows= None
    id_dfX4040 = None
    fX4040= Form(db.dfX4040, id, deletable=False, dbio = False, keep_values = False, form_name = "fX4040",  formstyle=FormStyleBulma )
   
    if fX4040.accepted:

        Glb['debug'] and print("     fX4040 accepted with: %s " % (fX4040.vars))
        fX4040_f0 = fX4040.vars.get('f0','')
        if len ( fX4040_f0 ):
            id_dfX4040 = db.dfX4040.insert( **fX4040.vars )
            db.commit()

            if not id_dfX4040 is None:
                dfX4040_rows = db.dfX4040(id_dfX4040 )

                if not dfX4040_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fX4040.vars.f0}\" into db.dfX4040.f0, id = {id_dfX4040}' )
                         print(f"     found db.dfX4040.f0: \"{dfX4040_rows.f0}\", id = {id_dfX4040}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fX4040_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fX4040.vars.items() ]
                print()
   
    elif fX4040.errors:
        print("fX4040 has errors: %s " % (fX4040.errors))
 

    return locals()


@action('blank', method=["GET", "POST"] )
@action.uses(Template('blank.html', delimiters='[%[ ]]',), db, session,  T, )

def blank(id=None):
    ctrl_info= "ctrl: blank, view: blank.html"
    messages = []

    dfblank0_rows= None
    id_dfblank0 = None
    fblank0= Form(db.dfblank0, id, deletable=False, dbio = False, keep_values = False, form_name = "fblank0",  formstyle=FormStyleBulma )
   
    if fblank0.accepted:

        Glb['debug'] and print("     fblank0 accepted with: %s " % (fblank0.vars))
        fblank0_f0 = fblank0.vars.get('f0','')
        if len ( fblank0_f0 ):
            id_dfblank0 = db.dfblank0.insert( **fblank0.vars )
            db.commit()

            if not id_dfblank0 is None:
                dfblank0_rows = db.dfblank0(id_dfblank0 )

                if not dfblank0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fblank0.vars.f0}\" into db.dfblank0.f0, id = {id_dfblank0}' )
                         print(f"     found db.dfblank0.f0: \"{dfblank0_rows.f0}\", id = {id_dfblank0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fblank0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fblank0.vars.items() ]
                print()
   
    elif fblank0.errors:
        print("fblank0 has errors: %s " % (fblank0.errors))
 

    return locals()


@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session,  T, )

def index(id=None):
    ctrl_info= "ctrl: index, view: index.html"
    messages = []

    rows_tindex0= db(db.tindex0).select()
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


@action('register', method=["GET", "POST"] )
@action.uses(Template('register.html', delimiters='[%[ ]]',), db, session,  T, )

def register(id=None):
    ctrl_info= "ctrl: register, view: register.html"
    messages = []

    dfregister0_rows= None
    id_dfregister0 = None
    fregister0= Form(db.dfregister0, id, deletable=False, dbio = False, keep_values = False, form_name = "fregister0",  formstyle=FormStyleBulma )
   
    if fregister0.accepted:

        Glb['debug'] and print("     fregister0 accepted with: %s " % (fregister0.vars))
        fregister0_f0 = fregister0.vars.get('f0','')
        if len ( fregister0_f0 ):
            id_dfregister0 = db.dfregister0.insert( **fregister0.vars )
            db.commit()

            if not id_dfregister0 is None:
                dfregister0_rows = db.dfregister0(id_dfregister0 )

                if not dfregister0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fregister0.vars.f0}\" into db.dfregister0.f0, id = {id_dfregister0}' )
                         print(f"     found db.dfregister0.f0: \"{dfregister0_rows.f0}\", id = {id_dfregister0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fregister0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fregister0.vars.items() ]
                print()
   
    elif fregister0.errors:
        print("fregister0 has errors: %s " % (fregister0.errors))
 

    return locals()


@action('forgotXpassword', method=["GET", "POST"] )
@action.uses(Template('forgot-password.html', delimiters='[%[ ]]',), db, session,  T, )

def forgotXpassword(id=None):
    ctrl_info= "ctrl: forgotXpassword, view: forgot-password.html"
    messages = []

    dfforgotXpassword0_rows= None
    id_dfforgotXpassword0 = None
    fforgotXpassword0= Form(db.dfforgotXpassword0, id, deletable=False, dbio = False, keep_values = False, form_name = "fforgotXpassword0",  formstyle=FormStyleBulma )
   
    if fforgotXpassword0.accepted:

        Glb['debug'] and print("     fforgotXpassword0 accepted with: %s " % (fforgotXpassword0.vars))
        fforgotXpassword0_f0 = fforgotXpassword0.vars.get('f0','')
        if len ( fforgotXpassword0_f0 ):
            id_dfforgotXpassword0 = db.dfforgotXpassword0.insert( **fforgotXpassword0.vars )
            db.commit()

            if not id_dfforgotXpassword0 is None:
                dfforgotXpassword0_rows = db.dfforgotXpassword0(id_dfforgotXpassword0 )

                if not dfforgotXpassword0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fforgotXpassword0.vars.f0}\" into db.dfforgotXpassword0.f0, id = {id_dfforgotXpassword0}' )
                         print(f"     found db.dfforgotXpassword0.f0: \"{dfforgotXpassword0_rows.f0}\", id = {id_dfforgotXpassword0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fforgotXpassword0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fforgotXpassword0.vars.items() ]
                print()
   
    elif fforgotXpassword0.errors:
        print("fforgotXpassword0 has errors: %s " % (fforgotXpassword0.errors))
 

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
# curl -X  GET   http://localhost:8000/sb/api/test_table/
# curl -X  GET   http://localhost:8000/sb/api/test_table/9
# curl -X DELETE  http://localhost:8000/sb/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/sb/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/sb/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/sb/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/sb/api/test_table/
#  http         localhost:8000/sb/api/test_table/9
#  http -f POST localhost:8000/sb/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/sb/api/test_table/2
#  http -f PUT localhost:8000/sb/api/test_table/2 f0=111111 f1=2222222 f2=333333

