#!/usr/bin/env python3

#
# py4web app, AI-biorex ported 21.10.2020 16:02:05
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

Glb= {'debug': True , 'my_app_name' : "lte3", 'tte_path': '/static/tte' }



@action('X404', method=["GET", "POST"] )
@action.uses(Template('404.html', delimiters='[%[ ]]',), db, session,  T, )

def X404(id=None):
    ctrl_info= "ctrl: X404, view: 404.html"
    messages = []

    return locals()


@action('X500', method=["GET", "POST"] )
@action.uses(Template('500.html', delimiters='[%[ ]]',), db, session,  T, )

def X500(id=None):
    ctrl_info= "ctrl: X500, view: 500.html"
    messages = []

    dfX5000_rows= None
    id_dfX5000 = None
    fX5000= Form(db.dfX5000, id, deletable=False, dbio = False, keep_values = False, form_name = "fX5000",  formstyle=FormStyleBulma )
   
    if fX5000.accepted:

        Glb['debug'] and print("     fX5000 accepted with: %s " % (fX5000.vars))
        fX5000_f0 = fX5000.vars.get('f0','')
        if len ( fX5000_f0 ):
            id_dfX5000 = db.dfX5000.insert( **fX5000.vars )
            db.commit()

            if not id_dfX5000 is None:
                dfX5000_rows = db.dfX5000(id_dfX5000 )

                if not dfX5000_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fX5000.vars.f0}\" into db.dfX5000.f0, id = {id_dfX5000}' )
                         print(f"     found db.dfX5000.f0: \"{dfX5000_rows.f0}\", id = {id_dfX5000}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fX5000_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fX5000.vars.items() ]
                print()
   
    elif fX5000.errors:
        print("fX5000 has errors: %s " % (fX5000.errors))
 

    dfX5001_rows= None
    id_dfX5001 = None
    fX5001= Form(db.dfX5001, id, deletable=False, dbio = False, keep_values = False, form_name = "fX5001",  formstyle=FormStyleBulma )
   
    if fX5001.accepted:

        Glb['debug'] and print("     fX5001 accepted with: %s " % (fX5001.vars))
        fX5001_f0 = fX5001.vars.get('f0','')
        if len ( fX5001_f0 ):
            id_dfX5001 = db.dfX5001.insert( **fX5001.vars )
            db.commit()

            if not id_dfX5001 is None:
                dfX5001_rows = db.dfX5001(id_dfX5001 )

                if not dfX5001_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fX5001.vars.f0}\" into db.dfX5001.f0, id = {id_dfX5001}' )
                         print(f"     found db.dfX5001.f0: \"{dfX5001_rows.f0}\", id = {id_dfX5001}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fX5001_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fX5001.vars.items() ]
                print()
   
    elif fX5001.errors:
        print("fX5001 has errors: %s " % (fX5001.errors))
 

    return locals()


@action('faq', method=["GET", "POST"] )
@action.uses(Template('faq.html', delimiters='[%[ ]]',), db, session,  T, )

def faq(id=None):
    ctrl_info= "ctrl: faq, view: faq.html"
    messages = []

    dffaq0_rows= None
    id_dffaq0 = None
    ffaq0= Form(db.dffaq0, id, deletable=False, dbio = False, keep_values = False, form_name = "ffaq0",  formstyle=FormStyleBulma )
   
    if ffaq0.accepted:

        Glb['debug'] and print("     ffaq0 accepted with: %s " % (ffaq0.vars))
        ffaq0_f0 = ffaq0.vars.get('f0','')
        if len ( ffaq0_f0 ):
            id_dffaq0 = db.dffaq0.insert( **ffaq0.vars )
            db.commit()

            if not id_dffaq0 is None:
                dffaq0_rows = db.dffaq0(id_dffaq0 )

                if not dffaq0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ffaq0.vars.f0}\" into db.dffaq0.f0, id = {id_dffaq0}' )
                         print(f"     found db.dffaq0.f0: \"{dffaq0_rows.f0}\", id = {id_dffaq0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(ffaq0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in ffaq0.vars.items() ]
                print()
   
    elif ffaq0.errors:
        print("ffaq0 has errors: %s " % (ffaq0.errors))
 

    return locals()


@action('pace', method=["GET", "POST"] )
@action.uses(Template('pace.html', delimiters='[%[ ]]',), db, session,  T, )

def pace(id=None):
    ctrl_info= "ctrl: pace, view: pace.html"
    messages = []

    dfpace0_rows= None
    id_dfpace0 = None
    fpace0= Form(db.dfpace0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpace0",  formstyle=FormStyleBulma )
   
    if fpace0.accepted:

        Glb['debug'] and print("     fpace0 accepted with: %s " % (fpace0.vars))
        fpace0_f0 = fpace0.vars.get('f0','')
        if len ( fpace0_f0 ):
            id_dfpace0 = db.dfpace0.insert( **fpace0.vars )
            db.commit()

            if not id_dfpace0 is None:
                dfpace0_rows = db.dfpace0(id_dfpace0 )

                if not dfpace0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpace0.vars.f0}\" into db.dfpace0.f0, id = {id_dfpace0}' )
                         print(f"     found db.dfpace0.f0: \"{dfpace0_rows.f0}\", id = {id_dfpace0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fpace0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fpace0.vars.items() ]
                print()
   
    elif fpace0.errors:
        print("fpace0 has errors: %s " % (fpace0.errors))
 

    return locals()


@action('data', method=["GET", "POST"] )
@action.uses(Template('data.html', delimiters='[%[ ]]',), db, session,  T, )

def data(id=None):
    ctrl_info= "ctrl: data, view: data.html"
    messages = []

    rows_tdata0= db(db.tdata0).select()
    rows_tdata1= db(db.tdata1).select()
    dfdata0_rows= None
    id_dfdata0 = None
    fdata0= Form(db.dfdata0, id, deletable=False, dbio = False, keep_values = False, form_name = "fdata0",  formstyle=FormStyleBulma )
   
    if fdata0.accepted:

        Glb['debug'] and print("     fdata0 accepted with: %s " % (fdata0.vars))
        fdata0_f0 = fdata0.vars.get('f0','')
        if len ( fdata0_f0 ):
            id_dfdata0 = db.dfdata0.insert( **fdata0.vars )
            db.commit()

            if not id_dfdata0 is None:
                dfdata0_rows = db.dfdata0(id_dfdata0 )

                if not dfdata0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fdata0.vars.f0}\" into db.dfdata0.f0, id = {id_dfdata0}' )
                         print(f"     found db.dfdata0.f0: \"{dfdata0_rows.f0}\", id = {id_dfdata0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fdata0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fdata0.vars.items() ]
                print()
   
    elif fdata0.errors:
        print("fdata0 has errors: %s " % (fdata0.errors))
 

    return locals()


@action('flot', method=["GET", "POST"] )
@action.uses(Template('flot.html', delimiters='[%[ ]]',), db, session,  T, )

def flot(id=None):
    ctrl_info= "ctrl: flot, view: flot.html"
    messages = []

    dfflot0_rows= None
    id_dfflot0 = None
    fflot0= Form(db.dfflot0, id, deletable=False, dbio = False, keep_values = False, form_name = "fflot0",  formstyle=FormStyleBulma )
   
    if fflot0.accepted:

        Glb['debug'] and print("     fflot0 accepted with: %s " % (fflot0.vars))
        fflot0_f0 = fflot0.vars.get('f0','')
        if len ( fflot0_f0 ):
            id_dfflot0 = db.dfflot0.insert( **fflot0.vars )
            db.commit()

            if not id_dfflot0 is None:
                dfflot0_rows = db.dfflot0(id_dfflot0 )

                if not dfflot0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fflot0.vars.f0}\" into db.dfflot0.f0, id = {id_dfflot0}' )
                         print(f"     found db.dfflot0.f0: \"{dfflot0_rows.f0}\", id = {id_dfflot0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fflot0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fflot0.vars.items() ]
                print()
   
    elif fflot0.errors:
        print("fflot0 has errors: %s " % (fflot0.errors))
 

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


@action('icons', method=["GET", "POST"] )
@action.uses(Template('icons.html', delimiters='[%[ ]]',), db, session,  T, )

def icons(id=None):
    ctrl_info= "ctrl: icons, view: icons.html"
    messages = []

    dficons0_rows= None
    id_dficons0 = None
    ficons0= Form(db.dficons0, id, deletable=False, dbio = False, keep_values = False, form_name = "ficons0",  formstyle=FormStyleBulma )
   
    if ficons0.accepted:

        Glb['debug'] and print("     ficons0 accepted with: %s " % (ficons0.vars))
        ficons0_f0 = ficons0.vars.get('f0','')
        if len ( ficons0_f0 ):
            id_dficons0 = db.dficons0.insert( **ficons0.vars )
            db.commit()

            if not id_dficons0 is None:
                dficons0_rows = db.dficons0(id_dficons0 )

                if not dficons0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ficons0.vars.f0}\" into db.dficons0.f0, id = {id_dficons0}' )
                         print(f"     found db.dficons0.f0: \"{dficons0_rows.f0}\", id = {id_dficons0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(ficons0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in ficons0.vars.items() ]
                print()
   
    elif ficons0.errors:
        print("ficons0 has errors: %s " % (ficons0.errors))
 

    return locals()


@action('boxed', method=["GET", "POST"] )
@action.uses(Template('boxed.html', delimiters='[%[ ]]',), db, session,  T, )

def boxed(id=None):
    ctrl_info= "ctrl: boxed, view: boxed.html"
    messages = []

    dfboxed0_rows= None
    id_dfboxed0 = None
    fboxed0= Form(db.dfboxed0, id, deletable=False, dbio = False, keep_values = False, form_name = "fboxed0",  formstyle=FormStyleBulma )
   
    if fboxed0.accepted:

        Glb['debug'] and print("     fboxed0 accepted with: %s " % (fboxed0.vars))
        fboxed0_f0 = fboxed0.vars.get('f0','')
        if len ( fboxed0_f0 ):
            id_dfboxed0 = db.dfboxed0.insert( **fboxed0.vars )
            db.commit()

            if not id_dfboxed0 is None:
                dfboxed0_rows = db.dfboxed0(id_dfboxed0 )

                if not dfboxed0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fboxed0.vars.f0}\" into db.dfboxed0.f0, id = {id_dfboxed0}' )
                         print(f"     found db.dfboxed0.f0: \"{dfboxed0_rows.f0}\", id = {id_dfboxed0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fboxed0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fboxed0.vars.items() ]
                print()
   
    elif fboxed0.errors:
        print("fboxed0 has errors: %s " % (fboxed0.errors))
 

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
 

    dfindex1_rows= None
    id_dfindex1 = None
    findex1= Form(db.dfindex1, id, deletable=False, dbio = False, keep_values = False, form_name = "findex1",  formstyle=FormStyleBulma )
   
    if findex1.accepted:

        Glb['debug'] and print("     findex1 accepted with: %s " % (findex1.vars))
        findex1_f0 = findex1.vars.get('f0','')
        if len ( findex1_f0 ):
            id_dfindex1 = db.dfindex1.insert( **findex1.vars )
            db.commit()

            if not id_dfindex1 is None:
                dfindex1_rows = db.dfindex1(id_dfindex1 )

                if not dfindex1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex1.vars.f0}\" into db.dfindex1.f0, id = {id_dfindex1}' )
                         print(f"     found db.dfindex1.f0: \"{dfindex1_rows.f0}\", id = {id_dfindex1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(findex1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in findex1.vars.items() ]
                print()
   
    elif findex1.errors:
        print("findex1 has errors: %s " % (findex1.errors))
 

    return locals()


@action('navbar', method=["GET", "POST"] )
@action.uses(Template('navbar.html', delimiters='[%[ ]]',), db, session,  T, )

def navbar(id=None):
    ctrl_info= "ctrl: navbar, view: navbar.html"
    messages = []

    dfnavbar0_rows= None
    id_dfnavbar0 = None
    fnavbar0= Form(db.dfnavbar0, id, deletable=False, dbio = False, keep_values = False, form_name = "fnavbar0",  formstyle=FormStyleBulma )
   
    if fnavbar0.accepted:

        Glb['debug'] and print("     fnavbar0 accepted with: %s " % (fnavbar0.vars))
        fnavbar0_f0 = fnavbar0.vars.get('f0','')
        if len ( fnavbar0_f0 ):
            id_dfnavbar0 = db.dfnavbar0.insert( **fnavbar0.vars )
            db.commit()

            if not id_dfnavbar0 is None:
                dfnavbar0_rows = db.dfnavbar0(id_dfnavbar0 )

                if not dfnavbar0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnavbar0.vars.f0}\" into db.dfnavbar0.f0, id = {id_dfnavbar0}' )
                         print(f"     found db.dfnavbar0.f0: \"{dfnavbar0_rows.f0}\", id = {id_dfnavbar0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fnavbar0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fnavbar0.vars.items() ]
                print()
   
    elif fnavbar0.errors:
        print("fnavbar0 has errors: %s " % (fnavbar0.errors))
 

    dfnavbar1_rows= None
    id_dfnavbar1 = None
    fnavbar1= Form(db.dfnavbar1, id, deletable=False, dbio = False, keep_values = False, form_name = "fnavbar1",  formstyle=FormStyleBulma )
   
    if fnavbar1.accepted:

        Glb['debug'] and print("     fnavbar1 accepted with: %s " % (fnavbar1.vars))
        fnavbar1_f0 = fnavbar1.vars.get('f0','')
        if len ( fnavbar1_f0 ):
            id_dfnavbar1 = db.dfnavbar1.insert( **fnavbar1.vars )
            db.commit()

            if not id_dfnavbar1 is None:
                dfnavbar1_rows = db.dfnavbar1(id_dfnavbar1 )

                if not dfnavbar1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnavbar1.vars.f0}\" into db.dfnavbar1.f0, id = {id_dfnavbar1}' )
                         print(f"     found db.dfnavbar1.f0: \"{dfnavbar1_rows.f0}\", id = {id_dfnavbar1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fnavbar1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fnavbar1.vars.items() ]
                print()
   
    elif fnavbar1.errors:
        print("fnavbar1 has errors: %s " % (fnavbar1.errors))
 

    dfnavbar2_rows= None
    id_dfnavbar2 = None
    fnavbar2= Form(db.dfnavbar2, id, deletable=False, dbio = False, keep_values = False, form_name = "fnavbar2",  formstyle=FormStyleBulma )
   
    if fnavbar2.accepted:

        Glb['debug'] and print("     fnavbar2 accepted with: %s " % (fnavbar2.vars))
        fnavbar2_f0 = fnavbar2.vars.get('f0','')
        if len ( fnavbar2_f0 ):
            id_dfnavbar2 = db.dfnavbar2.insert( **fnavbar2.vars )
            db.commit()

            if not id_dfnavbar2 is None:
                dfnavbar2_rows = db.dfnavbar2(id_dfnavbar2 )

                if not dfnavbar2_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnavbar2.vars.f0}\" into db.dfnavbar2.f0, id = {id_dfnavbar2}' )
                         print(f"     found db.dfnavbar2.f0: \"{dfnavbar2_rows.f0}\", id = {id_dfnavbar2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fnavbar2_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fnavbar2.vars.items() ]
                print()
   
    elif fnavbar2.errors:
        print("fnavbar2 has errors: %s " % (fnavbar2.errors))
 

    dfnavbar3_rows= None
    id_dfnavbar3 = None
    fnavbar3= Form(db.dfnavbar3, id, deletable=False, dbio = False, keep_values = False, form_name = "fnavbar3",  formstyle=FormStyleBulma )
   
    if fnavbar3.accepted:

        Glb['debug'] and print("     fnavbar3 accepted with: %s " % (fnavbar3.vars))
        fnavbar3_f0 = fnavbar3.vars.get('f0','')
        if len ( fnavbar3_f0 ):
            id_dfnavbar3 = db.dfnavbar3.insert( **fnavbar3.vars )
            db.commit()

            if not id_dfnavbar3 is None:
                dfnavbar3_rows = db.dfnavbar3(id_dfnavbar3 )

                if not dfnavbar3_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnavbar3.vars.f0}\" into db.dfnavbar3.f0, id = {id_dfnavbar3}' )
                         print(f"     found db.dfnavbar3.f0: \"{dfnavbar3_rows.f0}\", id = {id_dfnavbar3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fnavbar3_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fnavbar3.vars.items() ]
                print()
   
    elif fnavbar3.errors:
        print("fnavbar3 has errors: %s " % (fnavbar3.errors))
 

    dfnavbar4_rows= None
    id_dfnavbar4 = None
    fnavbar4= Form(db.dfnavbar4, id, deletable=False, dbio = False, keep_values = False, form_name = "fnavbar4",  formstyle=FormStyleBulma )
   
    if fnavbar4.accepted:

        Glb['debug'] and print("     fnavbar4 accepted with: %s " % (fnavbar4.vars))
        fnavbar4_f0 = fnavbar4.vars.get('f0','')
        if len ( fnavbar4_f0 ):
            id_dfnavbar4 = db.dfnavbar4.insert( **fnavbar4.vars )
            db.commit()

            if not id_dfnavbar4 is None:
                dfnavbar4_rows = db.dfnavbar4(id_dfnavbar4 )

                if not dfnavbar4_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnavbar4.vars.f0}\" into db.dfnavbar4.f0, id = {id_dfnavbar4}' )
                         print(f"     found db.dfnavbar4.f0: \"{dfnavbar4_rows.f0}\", id = {id_dfnavbar4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fnavbar4_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fnavbar4.vars.items() ]
                print()
   
    elif fnavbar4.errors:
        print("fnavbar4 has errors: %s " % (fnavbar4.errors))
 

    dfnavbar5_rows= None
    id_dfnavbar5 = None
    fnavbar5= Form(db.dfnavbar5, id, deletable=False, dbio = False, keep_values = False, form_name = "fnavbar5",  formstyle=FormStyleBulma )
   
    if fnavbar5.accepted:

        Glb['debug'] and print("     fnavbar5 accepted with: %s " % (fnavbar5.vars))
        fnavbar5_f0 = fnavbar5.vars.get('f0','')
        if len ( fnavbar5_f0 ):
            id_dfnavbar5 = db.dfnavbar5.insert( **fnavbar5.vars )
            db.commit()

            if not id_dfnavbar5 is None:
                dfnavbar5_rows = db.dfnavbar5(id_dfnavbar5 )

                if not dfnavbar5_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnavbar5.vars.f0}\" into db.dfnavbar5.f0, id = {id_dfnavbar5}' )
                         print(f"     found db.dfnavbar5.f0: \"{dfnavbar5_rows.f0}\", id = {id_dfnavbar5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fnavbar5_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fnavbar5.vars.items() ]
                print()
   
    elif fnavbar5.errors:
        print("fnavbar5 has errors: %s " % (fnavbar5.errors))
 

    dfnavbar6_rows= None
    id_dfnavbar6 = None
    fnavbar6= Form(db.dfnavbar6, id, deletable=False, dbio = False, keep_values = False, form_name = "fnavbar6",  formstyle=FormStyleBulma )
   
    if fnavbar6.accepted:

        Glb['debug'] and print("     fnavbar6 accepted with: %s " % (fnavbar6.vars))
        fnavbar6_f0 = fnavbar6.vars.get('f0','')
        if len ( fnavbar6_f0 ):
            id_dfnavbar6 = db.dfnavbar6.insert( **fnavbar6.vars )
            db.commit()

            if not id_dfnavbar6 is None:
                dfnavbar6_rows = db.dfnavbar6(id_dfnavbar6 )

                if not dfnavbar6_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnavbar6.vars.f0}\" into db.dfnavbar6.f0, id = {id_dfnavbar6}' )
                         print(f"     found db.dfnavbar6.f0: \"{dfnavbar6_rows.f0}\", id = {id_dfnavbar6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fnavbar6_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fnavbar6.vars.items() ]
                print()
   
    elif fnavbar6.errors:
        print("fnavbar6 has errors: %s " % (fnavbar6.errors))
 

    return locals()


@action('kanban', method=["GET", "POST"] )
@action.uses(Template('kanban.html', delimiters='[%[ ]]',), db, session,  T, )

def kanban(id=None):
    ctrl_info= "ctrl: kanban, view: kanban.html"
    messages = []

    dfkanban0_rows= None
    id_dfkanban0 = None
    fkanban0= Form(db.dfkanban0, id, deletable=False, dbio = False, keep_values = False, form_name = "fkanban0",  formstyle=FormStyleBulma )
   
    if fkanban0.accepted:

        Glb['debug'] and print("     fkanban0 accepted with: %s " % (fkanban0.vars))
        fkanban0_f0 = fkanban0.vars.get('f0','')
        if len ( fkanban0_f0 ):
            id_dfkanban0 = db.dfkanban0.insert( **fkanban0.vars )
            db.commit()

            if not id_dfkanban0 is None:
                dfkanban0_rows = db.dfkanban0(id_dfkanban0 )

                if not dfkanban0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fkanban0.vars.f0}\" into db.dfkanban0.f0, id = {id_dfkanban0}' )
                         print(f"     found db.dfkanban0.f0: \"{dfkanban0_rows.f0}\", id = {id_dfkanban0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fkanban0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fkanban0.vars.items() ]
                print()
   
    elif fkanban0.errors:
        print("fkanban0 has errors: %s " % (fkanban0.errors))
 

    return locals()


@action('jsgrid', method=["GET", "POST"] )
@action.uses(Template('jsgrid.html', delimiters='[%[ ]]',), db, session,  T, )

def jsgrid(id=None):
    ctrl_info= "ctrl: jsgrid, view: jsgrid.html"
    messages = []

    dfjsgrid0_rows= None
    id_dfjsgrid0 = None
    fjsgrid0= Form(db.dfjsgrid0, id, deletable=False, dbio = False, keep_values = False, form_name = "fjsgrid0",  formstyle=FormStyleBulma )
   
    if fjsgrid0.accepted:

        Glb['debug'] and print("     fjsgrid0 accepted with: %s " % (fjsgrid0.vars))
        fjsgrid0_f0 = fjsgrid0.vars.get('f0','')
        if len ( fjsgrid0_f0 ):
            id_dfjsgrid0 = db.dfjsgrid0.insert( **fjsgrid0.vars )
            db.commit()

            if not id_dfjsgrid0 is None:
                dfjsgrid0_rows = db.dfjsgrid0(id_dfjsgrid0 )

                if not dfjsgrid0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fjsgrid0.vars.f0}\" into db.dfjsgrid0.f0, id = {id_dfjsgrid0}' )
                         print(f"     found db.dfjsgrid0.f0: \"{dfjsgrid0_rows.f0}\", id = {id_dfjsgrid0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fjsgrid0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fjsgrid0.vars.items() ]
                print()
   
    elif fjsgrid0.errors:
        print("fjsgrid0 has errors: %s " % (fjsgrid0.errors))
 

    return locals()


@action('simple', method=["GET", "POST"] )
@action.uses(Template('simple.html', delimiters='[%[ ]]',), db, session,  T, )

def simple(id=None):
    ctrl_info= "ctrl: simple, view: simple.html"
    messages = []

    dfsimple0_rows= None
    id_dfsimple0 = None
    fsimple0= Form(db.dfsimple0, id, deletable=False, dbio = False, keep_values = False, form_name = "fsimple0",  formstyle=FormStyleBulma )
   
    if fsimple0.accepted:

        Glb['debug'] and print("     fsimple0 accepted with: %s " % (fsimple0.vars))
        fsimple0_f0 = fsimple0.vars.get('f0','')
        if len ( fsimple0_f0 ):
            id_dfsimple0 = db.dfsimple0.insert( **fsimple0.vars )
            db.commit()

            if not id_dfsimple0 is None:
                dfsimple0_rows = db.dfsimple0(id_dfsimple0 )

                if not dfsimple0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fsimple0.vars.f0}\" into db.dfsimple0.f0, id = {id_dfsimple0}' )
                         print(f"     found db.dfsimple0.f0: \"{dfsimple0_rows.f0}\", id = {id_dfsimple0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fsimple0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fsimple0.vars.items() ]
                print()
   
    elif fsimple0.errors:
        print("fsimple0 has errors: %s " % (fsimple0.errors))
 

    return locals()


@action('modals', method=["GET", "POST"] )
@action.uses(Template('modals.html', delimiters='[%[ ]]',), db, session,  T, )

def modals(id=None):
    ctrl_info= "ctrl: modals, view: modals.html"
    messages = []

    dfmodals0_rows= None
    id_dfmodals0 = None
    fmodals0= Form(db.dfmodals0, id, deletable=False, dbio = False, keep_values = False, form_name = "fmodals0",  formstyle=FormStyleBulma )
   
    if fmodals0.accepted:

        Glb['debug'] and print("     fmodals0 accepted with: %s " % (fmodals0.vars))
        fmodals0_f0 = fmodals0.vars.get('f0','')
        if len ( fmodals0_f0 ):
            id_dfmodals0 = db.dfmodals0.insert( **fmodals0.vars )
            db.commit()

            if not id_dfmodals0 is None:
                dfmodals0_rows = db.dfmodals0(id_dfmodals0 )

                if not dfmodals0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmodals0.vars.f0}\" into db.dfmodals0.f0, id = {id_dfmodals0}' )
                         print(f"     found db.dfmodals0.f0: \"{dfmodals0_rows.f0}\", id = {id_dfmodals0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fmodals0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fmodals0.vars.items() ]
                print()
   
    elif fmodals0.errors:
        print("fmodals0 has errors: %s " % (fmodals0.errors))
 

    return locals()


@action('inline', method=["GET", "POST"] )
@action.uses(Template('inline.html', delimiters='[%[ ]]',), db, session,  T, )

def inline(id=None):
    ctrl_info= "ctrl: inline, view: inline.html"
    messages = []

    dfinline0_rows= None
    id_dfinline0 = None
    finline0= Form(db.dfinline0, id, deletable=False, dbio = False, keep_values = False, form_name = "finline0",  formstyle=FormStyleBulma )
   
    if finline0.accepted:

        Glb['debug'] and print("     finline0 accepted with: %s " % (finline0.vars))
        finline0_f0 = finline0.vars.get('f0','')
        if len ( finline0_f0 ):
            id_dfinline0 = db.dfinline0.insert( **finline0.vars )
            db.commit()

            if not id_dfinline0 is None:
                dfinline0_rows = db.dfinline0(id_dfinline0 )

                if not dfinline0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finline0.vars.f0}\" into db.dfinline0.f0, id = {id_dfinline0}' )
                         print(f"     found db.dfinline0.f0: \"{dfinline0_rows.f0}\", id = {id_dfinline0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(finline0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in finline0.vars.items() ]
                print()
   
    elif finline0.errors:
        print("finline0 has errors: %s " % (finline0.errors))
 

    return locals()


@action('index3', method=["GET", "POST"] )
@action.uses(Template('index3.html', delimiters='[%[ ]]',), db, session,  T, )

def index3(id=None):
    ctrl_info= "ctrl: index3, view: index3.html"
    messages = []

    rows_tindex30= db(db.tindex30).select()
    dfindex30_rows= None
    id_dfindex30 = None
    findex30= Form(db.dfindex30, id, deletable=False, dbio = False, keep_values = False, form_name = "findex30",  formstyle=FormStyleBulma )
   
    if findex30.accepted:

        Glb['debug'] and print("     findex30 accepted with: %s " % (findex30.vars))
        findex30_f0 = findex30.vars.get('f0','')
        if len ( findex30_f0 ):
            id_dfindex30 = db.dfindex30.insert( **findex30.vars )
            db.commit()

            if not id_dfindex30 is None:
                dfindex30_rows = db.dfindex30(id_dfindex30 )

                if not dfindex30_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex30.vars.f0}\" into db.dfindex30.f0, id = {id_dfindex30}' )
                         print(f"     found db.dfindex30.f0: \"{dfindex30_rows.f0}\", id = {id_dfindex30}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(findex30_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in findex30.vars.items() ]
                print()
   
    elif findex30.errors:
        print("findex30 has errors: %s " % (findex30.errors))
 

    return locals()


@action('index2', method=["GET", "POST"] )
@action.uses(Template('index2.html', delimiters='[%[ ]]',), db, session,  T, )

def index2(id=None):
    ctrl_info= "ctrl: index2, view: index2.html"
    messages = []

    rows_tindex20= db(db.tindex20).select()
    dfindex20_rows= None
    id_dfindex20 = None
    findex20= Form(db.dfindex20, id, deletable=False, dbio = False, keep_values = False, form_name = "findex20",  formstyle=FormStyleBulma )
   
    if findex20.accepted:

        Glb['debug'] and print("     findex20 accepted with: %s " % (findex20.vars))
        findex20_f0 = findex20.vars.get('f0','')
        if len ( findex20_f0 ):
            id_dfindex20 = db.dfindex20.insert( **findex20.vars )
            db.commit()

            if not id_dfindex20 is None:
                dfindex20_rows = db.dfindex20(id_dfindex20 )

                if not dfindex20_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex20.vars.f0}\" into db.dfindex20.f0, id = {id_dfindex20}' )
                         print(f"     found db.dfindex20.f0: \"{dfindex20_rows.f0}\", id = {id_dfindex20}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(findex20_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in findex20.vars.items() ]
                print()
   
    elif findex20.errors:
        print("findex20 has errors: %s " % (findex20.errors))
 

    dfindex21_rows= None
    id_dfindex21 = None
    findex21= Form(db.dfindex21, id, deletable=False, dbio = False, keep_values = False, form_name = "findex21",  formstyle=FormStyleBulma )
   
    if findex21.accepted:

        Glb['debug'] and print("     findex21 accepted with: %s " % (findex21.vars))
        findex21_f0 = findex21.vars.get('f0','')
        if len ( findex21_f0 ):
            id_dfindex21 = db.dfindex21.insert( **findex21.vars )
            db.commit()

            if not id_dfindex21 is None:
                dfindex21_rows = db.dfindex21(id_dfindex21 )

                if not dfindex21_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex21.vars.f0}\" into db.dfindex21.f0, id = {id_dfindex21}' )
                         print(f"     found db.dfindex21.f0: \"{dfindex21_rows.f0}\", id = {id_dfindex21}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(findex21_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in findex21.vars.items() ]
                print()
   
    elif findex21.errors:
        print("findex21 has errors: %s " % (findex21.errors))
 

    return locals()


@action('profile', method=["GET", "POST"] )
@action.uses(Template('profile.html', delimiters='[%[ ]]',), db, session,  T, )

def profile(id=None):
    ctrl_info= "ctrl: profile, view: profile.html"
    messages = []

    dfprofile0_rows= None
    id_dfprofile0 = None
    fprofile0= Form(db.dfprofile0, id, deletable=False, dbio = False, keep_values = False, form_name = "fprofile0",  formstyle=FormStyleBulma )
   
    if fprofile0.accepted:

        Glb['debug'] and print("     fprofile0 accepted with: %s " % (fprofile0.vars))
        fprofile0_f0 = fprofile0.vars.get('f0','')
        if len ( fprofile0_f0 ):
            id_dfprofile0 = db.dfprofile0.insert( **fprofile0.vars )
            db.commit()

            if not id_dfprofile0 is None:
                dfprofile0_rows = db.dfprofile0(id_dfprofile0 )

                if not dfprofile0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fprofile0.vars.f0}\" into db.dfprofile0.f0, id = {id_dfprofile0}' )
                         print(f"     found db.dfprofile0.f0: \"{dfprofile0_rows.f0}\", id = {id_dfprofile0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fprofile0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fprofile0.vars.items() ]
                print()
   
    elif fprofile0.errors:
        print("fprofile0 has errors: %s " % (fprofile0.errors))
 

    dfprofile1_rows= None
    id_dfprofile1 = None
    fprofile1= Form(db.dfprofile1, id, deletable=False, dbio = False, keep_values = False, form_name = "fprofile1",  formstyle=FormStyleBulma )
   
    if fprofile1.accepted:

        Glb['debug'] and print("     fprofile1 accepted with: %s " % (fprofile1.vars))
        fprofile1_f0 = fprofile1.vars.get('f0','')
        if len ( fprofile1_f0 ):
            id_dfprofile1 = db.dfprofile1.insert( **fprofile1.vars )
            db.commit()

            if not id_dfprofile1 is None:
                dfprofile1_rows = db.dfprofile1(id_dfprofile1 )

                if not dfprofile1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fprofile1.vars.f0}\" into db.dfprofile1.f0, id = {id_dfprofile1}' )
                         print(f"     found db.dfprofile1.f0: \"{dfprofile1_rows.f0}\", id = {id_dfprofile1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fprofile1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fprofile1.vars.items() ]
                print()
   
    elif fprofile1.errors:
        print("fprofile1 has errors: %s " % (fprofile1.errors))
 

    dfprofile2_rows= None
    id_dfprofile2 = None
    fprofile2= Form(db.dfprofile2, id, deletable=False, dbio = False, keep_values = False, form_name = "fprofile2",  formstyle=FormStyleBulma )
   
    if fprofile2.accepted:

        Glb['debug'] and print("     fprofile2 accepted with: %s " % (fprofile2.vars))
        fprofile2_f0 = fprofile2.vars.get('f0','')
        if len ( fprofile2_f0 ):
            id_dfprofile2 = db.dfprofile2.insert( **fprofile2.vars )
            db.commit()

            if not id_dfprofile2 is None:
                dfprofile2_rows = db.dfprofile2(id_dfprofile2 )

                if not dfprofile2_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fprofile2.vars.f0}\" into db.dfprofile2.f0, id = {id_dfprofile2}' )
                         print(f"     found db.dfprofile2.f0: \"{dfprofile2_rows.f0}\", id = {id_dfprofile2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fprofile2_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fprofile2.vars.items() ]
                print()
   
    elif fprofile2.errors:
        print("fprofile2 has errors: %s " % (fprofile2.errors))
 

    return locals()


@action('invoice', method=["GET", "POST"] )
@action.uses(Template('invoice.html', delimiters='[%[ ]]',), db, session,  T, )

def invoice(id=None):
    ctrl_info= "ctrl: invoice, view: invoice.html"
    messages = []

    rows_tinvoice0= db(db.tinvoice0).select()
    rows_tinvoice1= db(db.tinvoice1).select()
    dfinvoice0_rows= None
    id_dfinvoice0 = None
    finvoice0= Form(db.dfinvoice0, id, deletable=False, dbio = False, keep_values = False, form_name = "finvoice0",  formstyle=FormStyleBulma )
   
    if finvoice0.accepted:

        Glb['debug'] and print("     finvoice0 accepted with: %s " % (finvoice0.vars))
        finvoice0_f0 = finvoice0.vars.get('f0','')
        if len ( finvoice0_f0 ):
            id_dfinvoice0 = db.dfinvoice0.insert( **finvoice0.vars )
            db.commit()

            if not id_dfinvoice0 is None:
                dfinvoice0_rows = db.dfinvoice0(id_dfinvoice0 )

                if not dfinvoice0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finvoice0.vars.f0}\" into db.dfinvoice0.f0, id = {id_dfinvoice0}' )
                         print(f"     found db.dfinvoice0.f0: \"{dfinvoice0_rows.f0}\", id = {id_dfinvoice0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(finvoice0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in finvoice0.vars.items() ]
                print()
   
    elif finvoice0.errors:
        print("finvoice0 has errors: %s " % (finvoice0.errors))
 

    return locals()


@action('gallery', method=["GET", "POST"] )
@action.uses(Template('gallery.html', delimiters='[%[ ]]',), db, session,  T, )

def gallery(id=None):
    ctrl_info= "ctrl: gallery, view: gallery.html"
    messages = []

    dfgallery0_rows= None
    id_dfgallery0 = None
    fgallery0= Form(db.dfgallery0, id, deletable=False, dbio = False, keep_values = False, form_name = "fgallery0",  formstyle=FormStyleBulma )
   
    if fgallery0.accepted:

        Glb['debug'] and print("     fgallery0 accepted with: %s " % (fgallery0.vars))
        fgallery0_f0 = fgallery0.vars.get('f0','')
        if len ( fgallery0_f0 ):
            id_dfgallery0 = db.dfgallery0.insert( **fgallery0.vars )
            db.commit()

            if not id_dfgallery0 is None:
                dfgallery0_rows = db.dfgallery0(id_dfgallery0 )

                if not dfgallery0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fgallery0.vars.f0}\" into db.dfgallery0.f0, id = {id_dfgallery0}' )
                         print(f"     found db.dfgallery0.f0: \"{dfgallery0_rows.f0}\", id = {id_dfgallery0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fgallery0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fgallery0.vars.items() ]
                print()
   
    elif fgallery0.errors:
        print("fgallery0 has errors: %s " % (fgallery0.errors))
 

    return locals()


@action('mailbox', method=["GET", "POST"] )
@action.uses(Template('mailbox.html', delimiters='[%[ ]]',), db, session,  T, )

def mailbox(id=None):
    ctrl_info= "ctrl: mailbox, view: mailbox.html"
    messages = []

    rows_tmailbox0= db(db.tmailbox0).select()
    dfmailbox0_rows= None
    id_dfmailbox0 = None
    fmailbox0= Form(db.dfmailbox0, id, deletable=False, dbio = False, keep_values = False, form_name = "fmailbox0",  formstyle=FormStyleBulma )
   
    if fmailbox0.accepted:

        Glb['debug'] and print("     fmailbox0 accepted with: %s " % (fmailbox0.vars))
        fmailbox0_f0 = fmailbox0.vars.get('f0','')
        if len ( fmailbox0_f0 ):
            id_dfmailbox0 = db.dfmailbox0.insert( **fmailbox0.vars )
            db.commit()

            if not id_dfmailbox0 is None:
                dfmailbox0_rows = db.dfmailbox0(id_dfmailbox0 )

                if not dfmailbox0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmailbox0.vars.f0}\" into db.dfmailbox0.f0, id = {id_dfmailbox0}' )
                         print(f"     found db.dfmailbox0.f0: \"{dfmailbox0_rows.f0}\", id = {id_dfmailbox0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fmailbox0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fmailbox0.vars.items() ]
                print()
   
    elif fmailbox0.errors:
        print("fmailbox0 has errors: %s " % (fmailbox0.errors))
 

    return locals()


@action('compose', method=["GET", "POST"] )
@action.uses(Template('compose.html', delimiters='[%[ ]]',), db, session,  T, )

def compose(id=None):
    ctrl_info= "ctrl: compose, view: compose.html"
    messages = []

    dfcompose0_rows= None
    id_dfcompose0 = None
    fcompose0= Form(db.dfcompose0, id, deletable=False, dbio = False, keep_values = False, form_name = "fcompose0",  formstyle=FormStyleBulma )
   
    if fcompose0.accepted:

        Glb['debug'] and print("     fcompose0 accepted with: %s " % (fcompose0.vars))
        fcompose0_f0 = fcompose0.vars.get('f0','')
        if len ( fcompose0_f0 ):
            id_dfcompose0 = db.dfcompose0.insert( **fcompose0.vars )
            db.commit()

            if not id_dfcompose0 is None:
                dfcompose0_rows = db.dfcompose0(id_dfcompose0 )

                if not dfcompose0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcompose0.vars.f0}\" into db.dfcompose0.f0, id = {id_dfcompose0}' )
                         print(f"     found db.dfcompose0.f0: \"{dfcompose0_rows.f0}\", id = {id_dfcompose0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fcompose0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fcompose0.vars.items() ]
                print()
   
    elif fcompose0.errors:
        print("fcompose0 has errors: %s " % (fcompose0.errors))
 

    return locals()


@action('ribbons', method=["GET", "POST"] )
@action.uses(Template('ribbons.html', delimiters='[%[ ]]',), db, session,  T, )

def ribbons(id=None):
    ctrl_info= "ctrl: ribbons, view: ribbons.html"
    messages = []

    dfribbons0_rows= None
    id_dfribbons0 = None
    fribbons0= Form(db.dfribbons0, id, deletable=False, dbio = False, keep_values = False, form_name = "fribbons0",  formstyle=FormStyleBulma )
   
    if fribbons0.accepted:

        Glb['debug'] and print("     fribbons0 accepted with: %s " % (fribbons0.vars))
        fribbons0_f0 = fribbons0.vars.get('f0','')
        if len ( fribbons0_f0 ):
            id_dfribbons0 = db.dfribbons0.insert( **fribbons0.vars )
            db.commit()

            if not id_dfribbons0 is None:
                dfribbons0_rows = db.dfribbons0(id_dfribbons0 )

                if not dfribbons0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fribbons0.vars.f0}\" into db.dfribbons0.f0, id = {id_dfribbons0}' )
                         print(f"     found db.dfribbons0.f0: \"{dfribbons0_rows.f0}\", id = {id_dfribbons0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fribbons0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fribbons0.vars.items() ]
                print()
   
    elif fribbons0.errors:
        print("fribbons0 has errors: %s " % (fribbons0.errors))
 

    return locals()


@action('editors', method=["GET", "POST"] )
@action.uses(Template('editors.html', delimiters='[%[ ]]',), db, session,  T, )

def editors(id=None):
    ctrl_info= "ctrl: editors, view: editors.html"
    messages = []

    dfeditors0_rows= None
    id_dfeditors0 = None
    feditors0= Form(db.dfeditors0, id, deletable=False, dbio = False, keep_values = False, form_name = "feditors0",  formstyle=FormStyleBulma )
   
    if feditors0.accepted:

        Glb['debug'] and print("     feditors0 accepted with: %s " % (feditors0.vars))
        feditors0_f0 = feditors0.vars.get('f0','')
        if len ( feditors0_f0 ):
            id_dfeditors0 = db.dfeditors0.insert( **feditors0.vars )
            db.commit()

            if not id_dfeditors0 is None:
                dfeditors0_rows = db.dfeditors0(id_dfeditors0 )

                if not dfeditors0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{feditors0.vars.f0}\" into db.dfeditors0.f0, id = {id_dfeditors0}' )
                         print(f"     found db.dfeditors0.f0: \"{dfeditors0_rows.f0}\", id = {id_dfeditors0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(feditors0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in feditors0.vars.items() ]
                print()
   
    elif feditors0.errors:
        print("feditors0 has errors: %s " % (feditors0.errors))
 

    return locals()


@action('sliders', method=["GET", "POST"] )
@action.uses(Template('sliders.html', delimiters='[%[ ]]',), db, session,  T, )

def sliders(id=None):
    ctrl_info= "ctrl: sliders, view: sliders.html"
    messages = []

    dfsliders0_rows= None
    id_dfsliders0 = None
    fsliders0= Form(db.dfsliders0, id, deletable=False, dbio = False, keep_values = False, form_name = "fsliders0",  formstyle=FormStyleBulma )
   
    if fsliders0.accepted:

        Glb['debug'] and print("     fsliders0 accepted with: %s " % (fsliders0.vars))
        fsliders0_f0 = fsliders0.vars.get('f0','')
        if len ( fsliders0_f0 ):
            id_dfsliders0 = db.dfsliders0.insert( **fsliders0.vars )
            db.commit()

            if not id_dfsliders0 is None:
                dfsliders0_rows = db.dfsliders0(id_dfsliders0 )

                if not dfsliders0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fsliders0.vars.f0}\" into db.dfsliders0.f0, id = {id_dfsliders0}' )
                         print(f"     found db.dfsliders0.f0: \"{dfsliders0_rows.f0}\", id = {id_dfsliders0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fsliders0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fsliders0.vars.items() ]
                print()
   
    elif fsliders0.errors:
        print("fsliders0 has errors: %s " % (fsliders0.errors))
 

    return locals()


@action('buttons', method=["GET", "POST"] )
@action.uses(Template('buttons.html', delimiters='[%[ ]]',), db, session,  T, )

def buttons(id=None):
    ctrl_info= "ctrl: buttons, view: buttons.html"
    messages = []

    rows_tbuttons0= db(db.tbuttons0).select()
    rows_tbuttons1= db(db.tbuttons1).select()
    rows_tbuttons2= db(db.tbuttons2).select()
    rows_tbuttons3= db(db.tbuttons3).select()
    rows_tbuttons4= db(db.tbuttons4).select()
    dfbuttons0_rows= None
    id_dfbuttons0 = None
    fbuttons0= Form(db.dfbuttons0, id, deletable=False, dbio = False, keep_values = False, form_name = "fbuttons0",  formstyle=FormStyleBulma )
   
    if fbuttons0.accepted:

        Glb['debug'] and print("     fbuttons0 accepted with: %s " % (fbuttons0.vars))
        fbuttons0_f0 = fbuttons0.vars.get('f0','')
        if len ( fbuttons0_f0 ):
            id_dfbuttons0 = db.dfbuttons0.insert( **fbuttons0.vars )
            db.commit()

            if not id_dfbuttons0 is None:
                dfbuttons0_rows = db.dfbuttons0(id_dfbuttons0 )

                if not dfbuttons0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fbuttons0.vars.f0}\" into db.dfbuttons0.f0, id = {id_dfbuttons0}' )
                         print(f"     found db.dfbuttons0.f0: \"{dfbuttons0_rows.f0}\", id = {id_dfbuttons0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fbuttons0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fbuttons0.vars.items() ]
                print()
   
    elif fbuttons0.errors:
        print("fbuttons0 has errors: %s " % (fbuttons0.errors))
 

    return locals()


@action('general', method=["GET", "POST"] )
@action.uses(Template('general.html', delimiters='[%[ ]]',), db, session,  T, )

def general(id=None):
    ctrl_info= "ctrl: general, view: general.html"
    messages = []

    dfgeneral0_rows= None
    id_dfgeneral0 = None
    fgeneral0= Form(db.dfgeneral0, id, deletable=False, dbio = False, keep_values = False, form_name = "fgeneral0",  formstyle=FormStyleBulma )
   
    if fgeneral0.accepted:

        Glb['debug'] and print("     fgeneral0 accepted with: %s " % (fgeneral0.vars))
        fgeneral0_f0 = fgeneral0.vars.get('f0','')
        if len ( fgeneral0_f0 ):
            id_dfgeneral0 = db.dfgeneral0.insert( **fgeneral0.vars )
            db.commit()

            if not id_dfgeneral0 is None:
                dfgeneral0_rows = db.dfgeneral0(id_dfgeneral0 )

                if not dfgeneral0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fgeneral0.vars.f0}\" into db.dfgeneral0.f0, id = {id_dfgeneral0}' )
                         print(f"     found db.dfgeneral0.f0: \"{dfgeneral0_rows.f0}\", id = {id_dfgeneral0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fgeneral0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fgeneral0.vars.items() ]
                print()
   
    elif fgeneral0.errors:
        print("fgeneral0 has errors: %s " % (fgeneral0.errors))
 

    return locals()


@action('chartjs', method=["GET", "POST"] )
@action.uses(Template('chartjs.html', delimiters='[%[ ]]',), db, session,  T, )

def chartjs(id=None):
    ctrl_info= "ctrl: chartjs, view: chartjs.html"
    messages = []

    dfchartjs0_rows= None
    id_dfchartjs0 = None
    fchartjs0= Form(db.dfchartjs0, id, deletable=False, dbio = False, keep_values = False, form_name = "fchartjs0",  formstyle=FormStyleBulma )
   
    if fchartjs0.accepted:

        Glb['debug'] and print("     fchartjs0 accepted with: %s " % (fchartjs0.vars))
        fchartjs0_f0 = fchartjs0.vars.get('f0','')
        if len ( fchartjs0_f0 ):
            id_dfchartjs0 = db.dfchartjs0.insert( **fchartjs0.vars )
            db.commit()

            if not id_dfchartjs0 is None:
                dfchartjs0_rows = db.dfchartjs0(id_dfchartjs0 )

                if not dfchartjs0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fchartjs0.vars.f0}\" into db.dfchartjs0.f0, id = {id_dfchartjs0}' )
                         print(f"     found db.dfchartjs0.f0: \"{dfchartjs0_rows.f0}\", id = {id_dfchartjs0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fchartjs0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fchartjs0.vars.items() ]
                print()
   
    elif fchartjs0.errors:
        print("fchartjs0 has errors: %s " % (fchartjs0.errors))
 

    return locals()


@action('topXnav', method=["GET", "POST"] )
@action.uses(Template('top-nav.html', delimiters='[%[ ]]',), db, session,  T, )

def topXnav(id=None):
    ctrl_info= "ctrl: topXnav, view: top-nav.html"
    messages = []

    dftopXnav0_rows= None
    id_dftopXnav0 = None
    ftopXnav0= Form(db.dftopXnav0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftopXnav0",  formstyle=FormStyleBulma )
   
    if ftopXnav0.accepted:

        Glb['debug'] and print("     ftopXnav0 accepted with: %s " % (ftopXnav0.vars))
        ftopXnav0_f0 = ftopXnav0.vars.get('f0','')
        if len ( ftopXnav0_f0 ):
            id_dftopXnav0 = db.dftopXnav0.insert( **ftopXnav0.vars )
            db.commit()

            if not id_dftopXnav0 is None:
                dftopXnav0_rows = db.dftopXnav0(id_dftopXnav0 )

                if not dftopXnav0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftopXnav0.vars.f0}\" into db.dftopXnav0.f0, id = {id_dftopXnav0}' )
                         print(f"     found db.dftopXnav0.f0: \"{dftopXnav0_rows.f0}\", id = {id_dftopXnav0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(ftopXnav0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in ftopXnav0.vars.items() ]
                print()
   
    elif ftopXnav0.errors:
        print("ftopXnav0 has errors: %s " % (ftopXnav0.errors))
 

    return locals()


@action('widgets', method=["GET", "POST"] )
@action.uses(Template('widgets.html', delimiters='[%[ ]]',), db, session,  T, )

def widgets(id=None):
    ctrl_info= "ctrl: widgets, view: widgets.html"
    messages = []

    dfwidgets0_rows= None
    id_dfwidgets0 = None
    fwidgets0= Form(db.dfwidgets0, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets0",  formstyle=FormStyleBulma )
   
    if fwidgets0.accepted:

        Glb['debug'] and print("     fwidgets0 accepted with: %s " % (fwidgets0.vars))
        fwidgets0_f0 = fwidgets0.vars.get('f0','')
        if len ( fwidgets0_f0 ):
            id_dfwidgets0 = db.dfwidgets0.insert( **fwidgets0.vars )
            db.commit()

            if not id_dfwidgets0 is None:
                dfwidgets0_rows = db.dfwidgets0(id_dfwidgets0 )

                if not dfwidgets0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets0.vars.f0}\" into db.dfwidgets0.f0, id = {id_dfwidgets0}' )
                         print(f"     found db.dfwidgets0.f0: \"{dfwidgets0_rows.f0}\", id = {id_dfwidgets0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fwidgets0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets0.vars.items() ]
                print()
   
    elif fwidgets0.errors:
        print("fwidgets0 has errors: %s " % (fwidgets0.errors))
 

    dfwidgets1_rows= None
    id_dfwidgets1 = None
    fwidgets1= Form(db.dfwidgets1, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets1",  formstyle=FormStyleBulma )
   
    if fwidgets1.accepted:

        Glb['debug'] and print("     fwidgets1 accepted with: %s " % (fwidgets1.vars))
        fwidgets1_f0 = fwidgets1.vars.get('f0','')
        if len ( fwidgets1_f0 ):
            id_dfwidgets1 = db.dfwidgets1.insert( **fwidgets1.vars )
            db.commit()

            if not id_dfwidgets1 is None:
                dfwidgets1_rows = db.dfwidgets1(id_dfwidgets1 )

                if not dfwidgets1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets1.vars.f0}\" into db.dfwidgets1.f0, id = {id_dfwidgets1}' )
                         print(f"     found db.dfwidgets1.f0: \"{dfwidgets1_rows.f0}\", id = {id_dfwidgets1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fwidgets1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets1.vars.items() ]
                print()
   
    elif fwidgets1.errors:
        print("fwidgets1 has errors: %s " % (fwidgets1.errors))
 

    dfwidgets2_rows= None
    id_dfwidgets2 = None
    fwidgets2= Form(db.dfwidgets2, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets2",  formstyle=FormStyleBulma )
   
    if fwidgets2.accepted:

        Glb['debug'] and print("     fwidgets2 accepted with: %s " % (fwidgets2.vars))
        fwidgets2_f0 = fwidgets2.vars.get('f0','')
        if len ( fwidgets2_f0 ):
            id_dfwidgets2 = db.dfwidgets2.insert( **fwidgets2.vars )
            db.commit()

            if not id_dfwidgets2 is None:
                dfwidgets2_rows = db.dfwidgets2(id_dfwidgets2 )

                if not dfwidgets2_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets2.vars.f0}\" into db.dfwidgets2.f0, id = {id_dfwidgets2}' )
                         print(f"     found db.dfwidgets2.f0: \"{dfwidgets2_rows.f0}\", id = {id_dfwidgets2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fwidgets2_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets2.vars.items() ]
                print()
   
    elif fwidgets2.errors:
        print("fwidgets2 has errors: %s " % (fwidgets2.errors))
 

    dfwidgets3_rows= None
    id_dfwidgets3 = None
    fwidgets3= Form(db.dfwidgets3, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets3",  formstyle=FormStyleBulma )
   
    if fwidgets3.accepted:

        Glb['debug'] and print("     fwidgets3 accepted with: %s " % (fwidgets3.vars))
        fwidgets3_f0 = fwidgets3.vars.get('f0','')
        if len ( fwidgets3_f0 ):
            id_dfwidgets3 = db.dfwidgets3.insert( **fwidgets3.vars )
            db.commit()

            if not id_dfwidgets3 is None:
                dfwidgets3_rows = db.dfwidgets3(id_dfwidgets3 )

                if not dfwidgets3_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets3.vars.f0}\" into db.dfwidgets3.f0, id = {id_dfwidgets3}' )
                         print(f"     found db.dfwidgets3.f0: \"{dfwidgets3_rows.f0}\", id = {id_dfwidgets3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fwidgets3_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets3.vars.items() ]
                print()
   
    elif fwidgets3.errors:
        print("fwidgets3 has errors: %s " % (fwidgets3.errors))
 

    dfwidgets4_rows= None
    id_dfwidgets4 = None
    fwidgets4= Form(db.dfwidgets4, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets4",  formstyle=FormStyleBulma )
   
    if fwidgets4.accepted:

        Glb['debug'] and print("     fwidgets4 accepted with: %s " % (fwidgets4.vars))
        fwidgets4_f0 = fwidgets4.vars.get('f0','')
        if len ( fwidgets4_f0 ):
            id_dfwidgets4 = db.dfwidgets4.insert( **fwidgets4.vars )
            db.commit()

            if not id_dfwidgets4 is None:
                dfwidgets4_rows = db.dfwidgets4(id_dfwidgets4 )

                if not dfwidgets4_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets4.vars.f0}\" into db.dfwidgets4.f0, id = {id_dfwidgets4}' )
                         print(f"     found db.dfwidgets4.f0: \"{dfwidgets4_rows.f0}\", id = {id_dfwidgets4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fwidgets4_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets4.vars.items() ]
                print()
   
    elif fwidgets4.errors:
        print("fwidgets4 has errors: %s " % (fwidgets4.errors))
 

    dfwidgets5_rows= None
    id_dfwidgets5 = None
    fwidgets5= Form(db.dfwidgets5, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets5",  formstyle=FormStyleBulma )
   
    if fwidgets5.accepted:

        Glb['debug'] and print("     fwidgets5 accepted with: %s " % (fwidgets5.vars))
        fwidgets5_f0 = fwidgets5.vars.get('f0','')
        if len ( fwidgets5_f0 ):
            id_dfwidgets5 = db.dfwidgets5.insert( **fwidgets5.vars )
            db.commit()

            if not id_dfwidgets5 is None:
                dfwidgets5_rows = db.dfwidgets5(id_dfwidgets5 )

                if not dfwidgets5_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets5.vars.f0}\" into db.dfwidgets5.f0, id = {id_dfwidgets5}' )
                         print(f"     found db.dfwidgets5.f0: \"{dfwidgets5_rows.f0}\", id = {id_dfwidgets5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fwidgets5_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets5.vars.items() ]
                print()
   
    elif fwidgets5.errors:
        print("fwidgets5 has errors: %s " % (fwidgets5.errors))
 

    dfwidgets6_rows= None
    id_dfwidgets6 = None
    fwidgets6= Form(db.dfwidgets6, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets6",  formstyle=FormStyleBulma )
   
    if fwidgets6.accepted:

        Glb['debug'] and print("     fwidgets6 accepted with: %s " % (fwidgets6.vars))
        fwidgets6_f0 = fwidgets6.vars.get('f0','')
        if len ( fwidgets6_f0 ):
            id_dfwidgets6 = db.dfwidgets6.insert( **fwidgets6.vars )
            db.commit()

            if not id_dfwidgets6 is None:
                dfwidgets6_rows = db.dfwidgets6(id_dfwidgets6 )

                if not dfwidgets6_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets6.vars.f0}\" into db.dfwidgets6.f0, id = {id_dfwidgets6}' )
                         print(f"     found db.dfwidgets6.f0: \"{dfwidgets6_rows.f0}\", id = {id_dfwidgets6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fwidgets6_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets6.vars.items() ]
                print()
   
    elif fwidgets6.errors:
        print("fwidgets6 has errors: %s " % (fwidgets6.errors))
 

    dfwidgets7_rows= None
    id_dfwidgets7 = None
    fwidgets7= Form(db.dfwidgets7, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets7",  formstyle=FormStyleBulma )
   
    if fwidgets7.accepted:

        Glb['debug'] and print("     fwidgets7 accepted with: %s " % (fwidgets7.vars))
        fwidgets7_f0 = fwidgets7.vars.get('f0','')
        if len ( fwidgets7_f0 ):
            id_dfwidgets7 = db.dfwidgets7.insert( **fwidgets7.vars )
            db.commit()

            if not id_dfwidgets7 is None:
                dfwidgets7_rows = db.dfwidgets7(id_dfwidgets7 )

                if not dfwidgets7_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets7.vars.f0}\" into db.dfwidgets7.f0, id = {id_dfwidgets7}' )
                         print(f"     found db.dfwidgets7.f0: \"{dfwidgets7_rows.f0}\", id = {id_dfwidgets7}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fwidgets7_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets7.vars.items() ]
                print()
   
    elif fwidgets7.errors:
        print("fwidgets7 has errors: %s " % (fwidgets7.errors))
 

    dfwidgets8_rows= None
    id_dfwidgets8 = None
    fwidgets8= Form(db.dfwidgets8, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets8",  formstyle=FormStyleBulma )
   
    if fwidgets8.accepted:

        Glb['debug'] and print("     fwidgets8 accepted with: %s " % (fwidgets8.vars))
        fwidgets8_f0 = fwidgets8.vars.get('f0','')
        if len ( fwidgets8_f0 ):
            id_dfwidgets8 = db.dfwidgets8.insert( **fwidgets8.vars )
            db.commit()

            if not id_dfwidgets8 is None:
                dfwidgets8_rows = db.dfwidgets8(id_dfwidgets8 )

                if not dfwidgets8_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets8.vars.f0}\" into db.dfwidgets8.f0, id = {id_dfwidgets8}' )
                         print(f"     found db.dfwidgets8.f0: \"{dfwidgets8_rows.f0}\", id = {id_dfwidgets8}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fwidgets8_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets8.vars.items() ]
                print()
   
    elif fwidgets8.errors:
        print("fwidgets8 has errors: %s " % (fwidgets8.errors))
 

    dfwidgets9_rows= None
    id_dfwidgets9 = None
    fwidgets9= Form(db.dfwidgets9, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets9",  formstyle=FormStyleBulma )
   
    if fwidgets9.accepted:

        Glb['debug'] and print("     fwidgets9 accepted with: %s " % (fwidgets9.vars))
        fwidgets9_f0 = fwidgets9.vars.get('f0','')
        if len ( fwidgets9_f0 ):
            id_dfwidgets9 = db.dfwidgets9.insert( **fwidgets9.vars )
            db.commit()

            if not id_dfwidgets9 is None:
                dfwidgets9_rows = db.dfwidgets9(id_dfwidgets9 )

                if not dfwidgets9_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets9.vars.f0}\" into db.dfwidgets9.f0, id = {id_dfwidgets9}' )
                         print(f"     found db.dfwidgets9.f0: \"{dfwidgets9_rows.f0}\", id = {id_dfwidgets9}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fwidgets9_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets9.vars.items() ]
                print()
   
    elif fwidgets9.errors:
        print("fwidgets9 has errors: %s " % (fwidgets9.errors))
 

    dfwidgets10_rows= None
    id_dfwidgets10 = None
    fwidgets10= Form(db.dfwidgets10, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets10",  formstyle=FormStyleBulma )
   
    if fwidgets10.accepted:

        Glb['debug'] and print("     fwidgets10 accepted with: %s " % (fwidgets10.vars))
        fwidgets10_f0 = fwidgets10.vars.get('f0','')
        if len ( fwidgets10_f0 ):
            id_dfwidgets10 = db.dfwidgets10.insert( **fwidgets10.vars )
            db.commit()

            if not id_dfwidgets10 is None:
                dfwidgets10_rows = db.dfwidgets10(id_dfwidgets10 )

                if not dfwidgets10_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets10.vars.f0}\" into db.dfwidgets10.f0, id = {id_dfwidgets10}' )
                         print(f"     found db.dfwidgets10.f0: \"{dfwidgets10_rows.f0}\", id = {id_dfwidgets10}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fwidgets10_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets10.vars.items() ]
                print()
   
    elif fwidgets10.errors:
        print("fwidgets10 has errors: %s " % (fwidgets10.errors))
 

    return locals()


@action('starter', method=["GET", "POST"] )
@action.uses(Template('starter.html', delimiters='[%[ ]]',), db, session,  T, )

def starter(id=None):
    ctrl_info= "ctrl: starter, view: starter.html"
    messages = []

    dfstarter0_rows= None
    id_dfstarter0 = None
    fstarter0= Form(db.dfstarter0, id, deletable=False, dbio = False, keep_values = False, form_name = "fstarter0",  formstyle=FormStyleBulma )
   
    if fstarter0.accepted:

        Glb['debug'] and print("     fstarter0 accepted with: %s " % (fstarter0.vars))
        fstarter0_f0 = fstarter0.vars.get('f0','')
        if len ( fstarter0_f0 ):
            id_dfstarter0 = db.dfstarter0.insert( **fstarter0.vars )
            db.commit()

            if not id_dfstarter0 is None:
                dfstarter0_rows = db.dfstarter0(id_dfstarter0 )

                if not dfstarter0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fstarter0.vars.f0}\" into db.dfstarter0.f0, id = {id_dfstarter0}' )
                         print(f"     found db.dfstarter0.f0: \"{dfstarter0_rows.f0}\", id = {id_dfstarter0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fstarter0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fstarter0.vars.items() ]
                print()
   
    elif fstarter0.errors:
        print("fstarter0 has errors: %s " % (fstarter0.errors))
 

    return locals()


@action('enhanced', method=["GET", "POST"] )
@action.uses(Template('enhanced.html', delimiters='[%[ ]]',), db, session,  T, )

def enhanced(id=None):
    ctrl_info= "ctrl: enhanced, view: enhanced.html"
    messages = []

    dfenhanced0_rows= None
    id_dfenhanced0 = None
    fenhanced0= Form(db.dfenhanced0, id, deletable=False, dbio = False, keep_values = False, form_name = "fenhanced0",  formstyle=FormStyleBulma )
   
    if fenhanced0.accepted:

        Glb['debug'] and print("     fenhanced0 accepted with: %s " % (fenhanced0.vars))
        fenhanced0_f0 = fenhanced0.vars.get('f0','')
        if len ( fenhanced0_f0 ):
            id_dfenhanced0 = db.dfenhanced0.insert( **fenhanced0.vars )
            db.commit()

            if not id_dfenhanced0 is None:
                dfenhanced0_rows = db.dfenhanced0(id_dfenhanced0 )

                if not dfenhanced0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fenhanced0.vars.f0}\" into db.dfenhanced0.f0, id = {id_dfenhanced0}' )
                         print(f"     found db.dfenhanced0.f0: \"{dfenhanced0_rows.f0}\", id = {id_dfenhanced0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fenhanced0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fenhanced0.vars.items() ]
                print()
   
    elif fenhanced0.errors:
        print("fenhanced0 has errors: %s " % (fenhanced0.errors))
 

    dfenhanced1_rows= None
    id_dfenhanced1 = None
    fenhanced1= Form(db.dfenhanced1, id, deletable=False, dbio = False, keep_values = False, form_name = "fenhanced1",  formstyle=FormStyleBulma )
   
    if fenhanced1.accepted:

        Glb['debug'] and print("     fenhanced1 accepted with: %s " % (fenhanced1.vars))
        fenhanced1_f0 = fenhanced1.vars.get('f0','')
        if len ( fenhanced1_f0 ):
            id_dfenhanced1 = db.dfenhanced1.insert( **fenhanced1.vars )
            db.commit()

            if not id_dfenhanced1 is None:
                dfenhanced1_rows = db.dfenhanced1(id_dfenhanced1 )

                if not dfenhanced1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fenhanced1.vars.f0}\" into db.dfenhanced1.f0, id = {id_dfenhanced1}' )
                         print(f"     found db.dfenhanced1.f0: \"{dfenhanced1_rows.f0}\", id = {id_dfenhanced1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fenhanced1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fenhanced1.vars.items() ]
                print()
   
    elif fenhanced1.errors:
        print("fenhanced1 has errors: %s " % (fenhanced1.errors))
 

    return locals()


@action('loginXv2', method=["GET", "POST"] )
@action.uses(Template('login-v2.html', delimiters='[%[ ]]',), db, session,  T, )

def loginXv2(id=None):
    ctrl_info= "ctrl: loginXv2, view: login-v2.html"
    messages = []

    dfloginXv20_rows= None
    id_dfloginXv20 = None
    floginXv20= Form(db.dfloginXv20, id, deletable=False, dbio = False, keep_values = False, form_name = "floginXv20",  formstyle=FormStyleBulma )
   
    if floginXv20.accepted:

        Glb['debug'] and print("     floginXv20 accepted with: %s " % (floginXv20.vars))
        floginXv20_f0 = floginXv20.vars.get('f0','')
        if len ( floginXv20_f0 ):
            id_dfloginXv20 = db.dfloginXv20.insert( **floginXv20.vars )
            db.commit()

            if not id_dfloginXv20 is None:
                dfloginXv20_rows = db.dfloginXv20(id_dfloginXv20 )

                if not dfloginXv20_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{floginXv20.vars.f0}\" into db.dfloginXv20.f0, id = {id_dfloginXv20}' )
                         print(f"     found db.dfloginXv20.f0: \"{dfloginXv20_rows.f0}\", id = {id_dfloginXv20}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(floginXv20_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in floginXv20.vars.items() ]
                print()
   
    elif floginXv20.errors:
        print("floginXv20 has errors: %s " % (floginXv20.errors))
 

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


@action('contacts', method=["GET", "POST"] )
@action.uses(Template('contacts.html', delimiters='[%[ ]]',), db, session,  T, )

def contacts(id=None):
    ctrl_info= "ctrl: contacts, view: contacts.html"
    messages = []

    dfcontacts0_rows= None
    id_dfcontacts0 = None
    fcontacts0= Form(db.dfcontacts0, id, deletable=False, dbio = False, keep_values = False, form_name = "fcontacts0",  formstyle=FormStyleBulma )
   
    if fcontacts0.accepted:

        Glb['debug'] and print("     fcontacts0 accepted with: %s " % (fcontacts0.vars))
        fcontacts0_f0 = fcontacts0.vars.get('f0','')
        if len ( fcontacts0_f0 ):
            id_dfcontacts0 = db.dfcontacts0.insert( **fcontacts0.vars )
            db.commit()

            if not id_dfcontacts0 is None:
                dfcontacts0_rows = db.dfcontacts0(id_dfcontacts0 )

                if not dfcontacts0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcontacts0.vars.f0}\" into db.dfcontacts0.f0, id = {id_dfcontacts0}' )
                         print(f"     found db.dfcontacts0.f0: \"{dfcontacts0_rows.f0}\", id = {id_dfcontacts0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fcontacts0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fcontacts0.vars.items() ]
                print()
   
    elif fcontacts0.errors:
        print("fcontacts0 has errors: %s " % (fcontacts0.errors))
 

    return locals()


@action('projects', method=["GET", "POST"] )
@action.uses(Template('projects.html', delimiters='[%[ ]]',), db, session,  T, )

def projects(id=None):
    ctrl_info= "ctrl: projects, view: projects.html"
    messages = []

    rows_tprojects0= db(db.tprojects0).select()
    dfprojects0_rows= None
    id_dfprojects0 = None
    fprojects0= Form(db.dfprojects0, id, deletable=False, dbio = False, keep_values = False, form_name = "fprojects0",  formstyle=FormStyleBulma )
   
    if fprojects0.accepted:

        Glb['debug'] and print("     fprojects0 accepted with: %s " % (fprojects0.vars))
        fprojects0_f0 = fprojects0.vars.get('f0','')
        if len ( fprojects0_f0 ):
            id_dfprojects0 = db.dfprojects0.insert( **fprojects0.vars )
            db.commit()

            if not id_dfprojects0 is None:
                dfprojects0_rows = db.dfprojects0(id_dfprojects0 )

                if not dfprojects0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fprojects0.vars.f0}\" into db.dfprojects0.f0, id = {id_dfprojects0}' )
                         print(f"     found db.dfprojects0.f0: \"{dfprojects0_rows.f0}\", id = {id_dfprojects0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fprojects0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fprojects0.vars.items() ]
                print()
   
    elif fprojects0.errors:
        print("fprojects0 has errors: %s " % (fprojects0.errors))
 

    return locals()


@action('calendar', method=["GET", "POST"] )
@action.uses(Template('calendar.html', delimiters='[%[ ]]',), db, session,  T, )

def calendar(id=None):
    ctrl_info= "ctrl: calendar, view: calendar.html"
    messages = []

    dfcalendar0_rows= None
    id_dfcalendar0 = None
    fcalendar0= Form(db.dfcalendar0, id, deletable=False, dbio = False, keep_values = False, form_name = "fcalendar0",  formstyle=FormStyleBulma )
   
    if fcalendar0.accepted:

        Glb['debug'] and print("     fcalendar0 accepted with: %s " % (fcalendar0.vars))
        fcalendar0_f0 = fcalendar0.vars.get('f0','')
        if len ( fcalendar0_f0 ):
            id_dfcalendar0 = db.dfcalendar0.insert( **fcalendar0.vars )
            db.commit()

            if not id_dfcalendar0 is None:
                dfcalendar0_rows = db.dfcalendar0(id_dfcalendar0 )

                if not dfcalendar0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcalendar0.vars.f0}\" into db.dfcalendar0.f0, id = {id_dfcalendar0}' )
                         print(f"     found db.dfcalendar0.f0: \"{dfcalendar0_rows.f0}\", id = {id_dfcalendar0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fcalendar0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fcalendar0.vars.items() ]
                print()
   
    elif fcalendar0.errors:
        print("fcalendar0 has errors: %s " % (fcalendar0.errors))
 

    return locals()


@action('timeline', method=["GET", "POST"] )
@action.uses(Template('timeline.html', delimiters='[%[ ]]',), db, session,  T, )

def timeline(id=None):
    ctrl_info= "ctrl: timeline, view: timeline.html"
    messages = []

    dftimeline0_rows= None
    id_dftimeline0 = None
    ftimeline0= Form(db.dftimeline0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftimeline0",  formstyle=FormStyleBulma )
   
    if ftimeline0.accepted:

        Glb['debug'] and print("     ftimeline0 accepted with: %s " % (ftimeline0.vars))
        ftimeline0_f0 = ftimeline0.vars.get('f0','')
        if len ( ftimeline0_f0 ):
            id_dftimeline0 = db.dftimeline0.insert( **ftimeline0.vars )
            db.commit()

            if not id_dftimeline0 is None:
                dftimeline0_rows = db.dftimeline0(id_dftimeline0 )

                if not dftimeline0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftimeline0.vars.f0}\" into db.dftimeline0.f0, id = {id_dftimeline0}' )
                         print(f"     found db.dftimeline0.f0: \"{dftimeline0_rows.f0}\", id = {id_dftimeline0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(ftimeline0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in ftimeline0.vars.items() ]
                print()
   
    elif ftimeline0.errors:
        print("ftimeline0 has errors: %s " % (ftimeline0.errors))
 

    return locals()


@action('advanced', method=["GET", "POST"] )
@action.uses(Template('advanced.html', delimiters='[%[ ]]',), db, session,  T, )

def advanced(id=None):
    ctrl_info= "ctrl: advanced, view: advanced.html"
    messages = []

    dfadvanced0_rows= None
    id_dfadvanced0 = None
    fadvanced0= Form(db.dfadvanced0, id, deletable=False, dbio = False, keep_values = False, form_name = "fadvanced0",  formstyle=FormStyleBulma )
   
    if fadvanced0.accepted:

        Glb['debug'] and print("     fadvanced0 accepted with: %s " % (fadvanced0.vars))
        fadvanced0_f0 = fadvanced0.vars.get('f0','')
        if len ( fadvanced0_f0 ):
            id_dfadvanced0 = db.dfadvanced0.insert( **fadvanced0.vars )
            db.commit()

            if not id_dfadvanced0 is None:
                dfadvanced0_rows = db.dfadvanced0(id_dfadvanced0 )

                if not dfadvanced0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fadvanced0.vars.f0}\" into db.dfadvanced0.f0, id = {id_dfadvanced0}' )
                         print(f"     found db.dfadvanced0.f0: \"{dfadvanced0_rows.f0}\", id = {id_dfadvanced0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fadvanced0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fadvanced0.vars.items() ]
                print()
   
    elif fadvanced0.errors:
        print("fadvanced0 has errors: %s " % (fadvanced0.errors))
 

    return locals()


@action('readXmail', method=["GET", "POST"] )
@action.uses(Template('read-mail.html', delimiters='[%[ ]]',), db, session,  T, )

def readXmail(id=None):
    ctrl_info= "ctrl: readXmail, view: read-mail.html"
    messages = []

    dfreadXmail0_rows= None
    id_dfreadXmail0 = None
    freadXmail0= Form(db.dfreadXmail0, id, deletable=False, dbio = False, keep_values = False, form_name = "freadXmail0",  formstyle=FormStyleBulma )
   
    if freadXmail0.accepted:

        Glb['debug'] and print("     freadXmail0 accepted with: %s " % (freadXmail0.vars))
        freadXmail0_f0 = freadXmail0.vars.get('f0','')
        if len ( freadXmail0_f0 ):
            id_dfreadXmail0 = db.dfreadXmail0.insert( **freadXmail0.vars )
            db.commit()

            if not id_dfreadXmail0 is None:
                dfreadXmail0_rows = db.dfreadXmail0(id_dfreadXmail0 )

                if not dfreadXmail0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{freadXmail0.vars.f0}\" into db.dfreadXmail0.f0, id = {id_dfreadXmail0}' )
                         print(f"     found db.dfreadXmail0.f0: \"{dfreadXmail0_rows.f0}\", id = {id_dfreadXmail0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(freadXmail0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in freadXmail0.vars.items() ]
                print()
   
    elif freadXmail0.errors:
        print("freadXmail0 has errors: %s " % (freadXmail0.errors))
 

    return locals()


@action('lockscreen', method=["GET", "POST"] )
@action.uses(Template('lockscreen.html', delimiters='[%[ ]]',), db, session,  T, )

def lockscreen(id=None):
    ctrl_info= "ctrl: lockscreen, view: lockscreen.html"
    messages = []

    dflockscreen0_rows= None
    id_dflockscreen0 = None
    flockscreen0= Form(db.dflockscreen0, id, deletable=False, dbio = False, keep_values = False, form_name = "flockscreen0",  formstyle=FormStyleBulma )
   
    if flockscreen0.accepted:

        Glb['debug'] and print("     flockscreen0 accepted with: %s " % (flockscreen0.vars))
        flockscreen0_f0 = flockscreen0.vars.get('f0','')
        if len ( flockscreen0_f0 ):
            id_dflockscreen0 = db.dflockscreen0.insert( **flockscreen0.vars )
            db.commit()

            if not id_dflockscreen0 is None:
                dflockscreen0_rows = db.dflockscreen0(id_dflockscreen0 )

                if not dflockscreen0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flockscreen0.vars.f0}\" into db.dflockscreen0.f0, id = {id_dflockscreen0}' )
                         print(f"     found db.dflockscreen0.f0: \"{dflockscreen0_rows.f0}\", id = {id_dflockscreen0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(flockscreen0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in flockscreen0.vars.items() ]
                print()
   
    elif flockscreen0.errors:
        print("flockscreen0 has errors: %s " % (flockscreen0.errors))
 

    return locals()


@action('contactXus', method=["GET", "POST"] )
@action.uses(Template('contact-us.html', delimiters='[%[ ]]',), db, session,  T, )

def contactXus(id=None):
    ctrl_info= "ctrl: contactXus, view: contact-us.html"
    messages = []

    dfcontactXus0_rows= None
    id_dfcontactXus0 = None
    fcontactXus0= Form(db.dfcontactXus0, id, deletable=False, dbio = False, keep_values = False, form_name = "fcontactXus0",  formstyle=FormStyleBulma )
   
    if fcontactXus0.accepted:

        Glb['debug'] and print("     fcontactXus0 accepted with: %s " % (fcontactXus0.vars))
        fcontactXus0_f0 = fcontactXus0.vars.get('f0','')
        if len ( fcontactXus0_f0 ):
            id_dfcontactXus0 = db.dfcontactXus0.insert( **fcontactXus0.vars )
            db.commit()

            if not id_dfcontactXus0 is None:
                dfcontactXus0_rows = db.dfcontactXus0(id_dfcontactXus0 )

                if not dfcontactXus0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcontactXus0.vars.f0}\" into db.dfcontactXus0.f0, id = {id_dfcontactXus0}' )
                         print(f"     found db.dfcontactXus0.f0: \"{dfcontactXus0_rows.f0}\", id = {id_dfcontactXus0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fcontactXus0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fcontactXus0.vars.items() ]
                print()
   
    elif fcontactXus0.errors:
        print("fcontactXus0 has errors: %s " % (fcontactXus0.errors))
 

    return locals()


@action('eXcommerce', method=["GET", "POST"] )
@action.uses(Template('e-commerce.html', delimiters='[%[ ]]',), db, session,  T, )

def eXcommerce(id=None):
    ctrl_info= "ctrl: eXcommerce, view: e-commerce.html"
    messages = []

    dfeXcommerce0_rows= None
    id_dfeXcommerce0 = None
    feXcommerce0= Form(db.dfeXcommerce0, id, deletable=False, dbio = False, keep_values = False, form_name = "feXcommerce0",  formstyle=FormStyleBulma )
   
    if feXcommerce0.accepted:

        Glb['debug'] and print("     feXcommerce0 accepted with: %s " % (feXcommerce0.vars))
        feXcommerce0_f0 = feXcommerce0.vars.get('f0','')
        if len ( feXcommerce0_f0 ):
            id_dfeXcommerce0 = db.dfeXcommerce0.insert( **feXcommerce0.vars )
            db.commit()

            if not id_dfeXcommerce0 is None:
                dfeXcommerce0_rows = db.dfeXcommerce0(id_dfeXcommerce0 )

                if not dfeXcommerce0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{feXcommerce0.vars.f0}\" into db.dfeXcommerce0.f0, id = {id_dfeXcommerce0}' )
                         print(f"     found db.dfeXcommerce0.f0: \"{dfeXcommerce0_rows.f0}\", id = {id_dfeXcommerce0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(feXcommerce0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in feXcommerce0.vars.items() ]
                print()
   
    elif feXcommerce0.errors:
        print("feXcommerce0 has errors: %s " % (feXcommerce0.errors))
 

    return locals()


@action('validation', method=["GET", "POST"] )
@action.uses(Template('validation.html', delimiters='[%[ ]]',), db, session,  T, )

def validation(id=None):
    ctrl_info= "ctrl: validation, view: validation.html"
    messages = []

    dfvalidation0_rows= None
    id_dfvalidation0 = None
    fvalidation0= Form(db.dfvalidation0, id, deletable=False, dbio = False, keep_values = False, form_name = "fvalidation0",  formstyle=FormStyleBulma )
   
    if fvalidation0.accepted:

        Glb['debug'] and print("     fvalidation0 accepted with: %s " % (fvalidation0.vars))
        fvalidation0_f0 = fvalidation0.vars.get('f0','')
        if len ( fvalidation0_f0 ):
            id_dfvalidation0 = db.dfvalidation0.insert( **fvalidation0.vars )
            db.commit()

            if not id_dfvalidation0 is None:
                dfvalidation0_rows = db.dfvalidation0(id_dfvalidation0 )

                if not dfvalidation0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fvalidation0.vars.f0}\" into db.dfvalidation0.f0, id = {id_dfvalidation0}' )
                         print(f"     found db.dfvalidation0.f0: \"{dfvalidation0_rows.f0}\", id = {id_dfvalidation0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fvalidation0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fvalidation0.vars.items() ]
                print()
   
    elif fvalidation0.errors:
        print("fvalidation0 has errors: %s " % (fvalidation0.errors))
 

    dfvalidation1_rows= None
    id_dfvalidation1 = None
    fvalidation1= Form(db.dfvalidation1, id, deletable=False, dbio = False, keep_values = False, form_name = "fvalidation1",  formstyle=FormStyleBulma )
   
    if fvalidation1.accepted:

        Glb['debug'] and print("     fvalidation1 accepted with: %s " % (fvalidation1.vars))
        fvalidation1_f0 = fvalidation1.vars.get('f0','')
        if len ( fvalidation1_f0 ):
            id_dfvalidation1 = db.dfvalidation1.insert( **fvalidation1.vars )
            db.commit()

            if not id_dfvalidation1 is None:
                dfvalidation1_rows = db.dfvalidation1(id_dfvalidation1 )

                if not dfvalidation1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fvalidation1.vars.f0}\" into db.dfvalidation1.f0, id = {id_dfvalidation1}' )
                         print(f"     found db.dfvalidation1.f0: \"{dfvalidation1_rows.f0}\", id = {id_dfvalidation1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fvalidation1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fvalidation1.vars.items() ]
                print()
   
    elif fvalidation1.errors:
        print("fvalidation1 has errors: %s " % (fvalidation1.errors))
 

    return locals()


@action('registerXv2', method=["GET", "POST"] )
@action.uses(Template('register-v2.html', delimiters='[%[ ]]',), db, session,  T, )

def registerXv2(id=None):
    ctrl_info= "ctrl: registerXv2, view: register-v2.html"
    messages = []

    dfregisterXv20_rows= None
    id_dfregisterXv20 = None
    fregisterXv20= Form(db.dfregisterXv20, id, deletable=False, dbio = False, keep_values = False, form_name = "fregisterXv20",  formstyle=FormStyleBulma )
   
    if fregisterXv20.accepted:

        Glb['debug'] and print("     fregisterXv20 accepted with: %s " % (fregisterXv20.vars))
        fregisterXv20_f0 = fregisterXv20.vars.get('f0','')
        if len ( fregisterXv20_f0 ):
            id_dfregisterXv20 = db.dfregisterXv20.insert( **fregisterXv20.vars )
            db.commit()

            if not id_dfregisterXv20 is None:
                dfregisterXv20_rows = db.dfregisterXv20(id_dfregisterXv20 )

                if not dfregisterXv20_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fregisterXv20.vars.f0}\" into db.dfregisterXv20.f0, id = {id_dfregisterXv20}' )
                         print(f"     found db.dfregisterXv20.f0: \"{dfregisterXv20_rows.f0}\", id = {id_dfregisterXv20}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fregisterXv20_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fregisterXv20.vars.items() ]
                print()
   
    elif fregisterXv20.errors:
        print("fregisterXv20 has errors: %s " % (fregisterXv20.errors))
 

    return locals()


@action('projectXadd', method=["GET", "POST"] )
@action.uses(Template('project-add.html', delimiters='[%[ ]]',), db, session,  T, )

def projectXadd(id=None):
    ctrl_info= "ctrl: projectXadd, view: project-add.html"
    messages = []

    dfprojectXadd0_rows= None
    id_dfprojectXadd0 = None
    fprojectXadd0= Form(db.dfprojectXadd0, id, deletable=False, dbio = False, keep_values = False, form_name = "fprojectXadd0",  formstyle=FormStyleBulma )
   
    if fprojectXadd0.accepted:

        Glb['debug'] and print("     fprojectXadd0 accepted with: %s " % (fprojectXadd0.vars))
        fprojectXadd0_f0 = fprojectXadd0.vars.get('f0','')
        if len ( fprojectXadd0_f0 ):
            id_dfprojectXadd0 = db.dfprojectXadd0.insert( **fprojectXadd0.vars )
            db.commit()

            if not id_dfprojectXadd0 is None:
                dfprojectXadd0_rows = db.dfprojectXadd0(id_dfprojectXadd0 )

                if not dfprojectXadd0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fprojectXadd0.vars.f0}\" into db.dfprojectXadd0.f0, id = {id_dfprojectXadd0}' )
                         print(f"     found db.dfprojectXadd0.f0: \"{dfprojectXadd0_rows.f0}\", id = {id_dfprojectXadd0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fprojectXadd0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fprojectXadd0.vars.items() ]
                print()
   
    elif fprojectXadd0.errors:
        print("fprojectXadd0 has errors: %s " % (fprojectXadd0.errors))
 

    return locals()


@action('projectXedit', method=["GET", "POST"] )
@action.uses(Template('project-edit.html', delimiters='[%[ ]]',), db, session,  T, )

def projectXedit(id=None):
    ctrl_info= "ctrl: projectXedit, view: project-edit.html"
    messages = []

    rows_tprojectXedit0= db(db.tprojectXedit0).select()
    dfprojectXedit0_rows= None
    id_dfprojectXedit0 = None
    fprojectXedit0= Form(db.dfprojectXedit0, id, deletable=False, dbio = False, keep_values = False, form_name = "fprojectXedit0",  formstyle=FormStyleBulma )
   
    if fprojectXedit0.accepted:

        Glb['debug'] and print("     fprojectXedit0 accepted with: %s " % (fprojectXedit0.vars))
        fprojectXedit0_f0 = fprojectXedit0.vars.get('f0','')
        if len ( fprojectXedit0_f0 ):
            id_dfprojectXedit0 = db.dfprojectXedit0.insert( **fprojectXedit0.vars )
            db.commit()

            if not id_dfprojectXedit0 is None:
                dfprojectXedit0_rows = db.dfprojectXedit0(id_dfprojectXedit0 )

                if not dfprojectXedit0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fprojectXedit0.vars.f0}\" into db.dfprojectXedit0.f0, id = {id_dfprojectXedit0}' )
                         print(f"     found db.dfprojectXedit0.f0: \"{dfprojectXedit0_rows.f0}\", id = {id_dfprojectXedit0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fprojectXedit0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fprojectXedit0.vars.items() ]
                print()
   
    elif fprojectXedit0.errors:
        print("fprojectXedit0 has errors: %s " % (fprojectXedit0.errors))
 

    return locals()


@action('fixedXfooter', method=["GET", "POST"] )
@action.uses(Template('fixed-footer.html', delimiters='[%[ ]]',), db, session,  T, )

def fixedXfooter(id=None):
    ctrl_info= "ctrl: fixedXfooter, view: fixed-footer.html"
    messages = []

    dffixedXfooter0_rows= None
    id_dffixedXfooter0 = None
    ffixedXfooter0= Form(db.dffixedXfooter0, id, deletable=False, dbio = False, keep_values = False, form_name = "ffixedXfooter0",  formstyle=FormStyleBulma )
   
    if ffixedXfooter0.accepted:

        Glb['debug'] and print("     ffixedXfooter0 accepted with: %s " % (ffixedXfooter0.vars))
        ffixedXfooter0_f0 = ffixedXfooter0.vars.get('f0','')
        if len ( ffixedXfooter0_f0 ):
            id_dffixedXfooter0 = db.dffixedXfooter0.insert( **ffixedXfooter0.vars )
            db.commit()

            if not id_dffixedXfooter0 is None:
                dffixedXfooter0_rows = db.dffixedXfooter0(id_dffixedXfooter0 )

                if not dffixedXfooter0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ffixedXfooter0.vars.f0}\" into db.dffixedXfooter0.f0, id = {id_dffixedXfooter0}' )
                         print(f"     found db.dffixedXfooter0.f0: \"{dffixedXfooter0_rows.f0}\", id = {id_dffixedXfooter0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(ffixedXfooter0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in ffixedXfooter0.vars.items() ]
                print()
   
    elif ffixedXfooter0.errors:
        print("ffixedXfooter0 has errors: %s " % (ffixedXfooter0.errors))
 

    return locals()


@action('fixedXtopnav', method=["GET", "POST"] )
@action.uses(Template('fixed-topnav.html', delimiters='[%[ ]]',), db, session,  T, )

def fixedXtopnav(id=None):
    ctrl_info= "ctrl: fixedXtopnav, view: fixed-topnav.html"
    messages = []

    dffixedXtopnav0_rows= None
    id_dffixedXtopnav0 = None
    ffixedXtopnav0= Form(db.dffixedXtopnav0, id, deletable=False, dbio = False, keep_values = False, form_name = "ffixedXtopnav0",  formstyle=FormStyleBulma )
   
    if ffixedXtopnav0.accepted:

        Glb['debug'] and print("     ffixedXtopnav0 accepted with: %s " % (ffixedXtopnav0.vars))
        ffixedXtopnav0_f0 = ffixedXtopnav0.vars.get('f0','')
        if len ( ffixedXtopnav0_f0 ):
            id_dffixedXtopnav0 = db.dffixedXtopnav0.insert( **ffixedXtopnav0.vars )
            db.commit()

            if not id_dffixedXtopnav0 is None:
                dffixedXtopnav0_rows = db.dffixedXtopnav0(id_dffixedXtopnav0 )

                if not dffixedXtopnav0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ffixedXtopnav0.vars.f0}\" into db.dffixedXtopnav0.f0, id = {id_dffixedXtopnav0}' )
                         print(f"     found db.dffixedXtopnav0.f0: \"{dffixedXtopnav0_rows.f0}\", id = {id_dffixedXtopnav0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(ffixedXtopnav0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in ffixedXtopnav0.vars.items() ]
                print()
   
    elif ffixedXtopnav0.errors:
        print("ffixedXtopnav0 has errors: %s " % (ffixedXtopnav0.errors))
 

    return locals()


@action('invoiceXprint', method=["GET", "POST"] )
@action.uses(Template('invoice-print.html', delimiters='[%[ ]]',), db, session,  T, )

def invoiceXprint(id=None):
    ctrl_info= "ctrl: invoiceXprint, view: invoice-print.html"
    messages = []

    rows_tinvoiceXprint0= db(db.tinvoiceXprint0).select()
    rows_tinvoiceXprint1= db(db.tinvoiceXprint1).select()
    return locals()


@action('languageXmenu', method=["GET", "POST"] )
@action.uses(Template('language-menu.html', delimiters='[%[ ]]',), db, session,  T, )

def languageXmenu(id=None):
    ctrl_info= "ctrl: languageXmenu, view: language-menu.html"
    messages = []

    dflanguageXmenu0_rows= None
    id_dflanguageXmenu0 = None
    flanguageXmenu0= Form(db.dflanguageXmenu0, id, deletable=False, dbio = False, keep_values = False, form_name = "flanguageXmenu0",  formstyle=FormStyleBulma )
   
    if flanguageXmenu0.accepted:

        Glb['debug'] and print("     flanguageXmenu0 accepted with: %s " % (flanguageXmenu0.vars))
        flanguageXmenu0_f0 = flanguageXmenu0.vars.get('f0','')
        if len ( flanguageXmenu0_f0 ):
            id_dflanguageXmenu0 = db.dflanguageXmenu0.insert( **flanguageXmenu0.vars )
            db.commit()

            if not id_dflanguageXmenu0 is None:
                dflanguageXmenu0_rows = db.dflanguageXmenu0(id_dflanguageXmenu0 )

                if not dflanguageXmenu0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flanguageXmenu0.vars.f0}\" into db.dflanguageXmenu0.f0, id = {id_dflanguageXmenu0}' )
                         print(f"     found db.dflanguageXmenu0.f0: \"{dflanguageXmenu0_rows.f0}\", id = {id_dflanguageXmenu0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(flanguageXmenu0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in flanguageXmenu0.vars.items() ]
                print()
   
    elif flanguageXmenu0.errors:
        print("flanguageXmenu0 has errors: %s " % (flanguageXmenu0.errors))
 

    return locals()


@action('fixedXsidebar', method=["GET", "POST"] )
@action.uses(Template('fixed-sidebar.html', delimiters='[%[ ]]',), db, session,  T, )

def fixedXsidebar(id=None):
    ctrl_info= "ctrl: fixedXsidebar, view: fixed-sidebar.html"
    messages = []

    dffixedXsidebar0_rows= None
    id_dffixedXsidebar0 = None
    ffixedXsidebar0= Form(db.dffixedXsidebar0, id, deletable=False, dbio = False, keep_values = False, form_name = "ffixedXsidebar0",  formstyle=FormStyleBulma )
   
    if ffixedXsidebar0.accepted:

        Glb['debug'] and print("     ffixedXsidebar0 accepted with: %s " % (ffixedXsidebar0.vars))
        ffixedXsidebar0_f0 = ffixedXsidebar0.vars.get('f0','')
        if len ( ffixedXsidebar0_f0 ):
            id_dffixedXsidebar0 = db.dffixedXsidebar0.insert( **ffixedXsidebar0.vars )
            db.commit()

            if not id_dffixedXsidebar0 is None:
                dffixedXsidebar0_rows = db.dffixedXsidebar0(id_dffixedXsidebar0 )

                if not dffixedXsidebar0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ffixedXsidebar0.vars.f0}\" into db.dffixedXsidebar0.f0, id = {id_dffixedXsidebar0}' )
                         print(f"     found db.dffixedXsidebar0.f0: \"{dffixedXsidebar0_rows.f0}\", id = {id_dffixedXsidebar0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(ffixedXsidebar0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in ffixedXsidebar0.vars.items() ]
                print()
   
    elif ffixedXsidebar0.errors:
        print("ffixedXsidebar0 has errors: %s " % (ffixedXsidebar0.errors))
 

    return locals()


@action('projectXdetail', method=["GET", "POST"] )
@action.uses(Template('project-detail.html', delimiters='[%[ ]]',), db, session,  T, )

def projectXdetail(id=None):
    ctrl_info= "ctrl: projectXdetail, view: project-detail.html"
    messages = []

    dfprojectXdetail0_rows= None
    id_dfprojectXdetail0 = None
    fprojectXdetail0= Form(db.dfprojectXdetail0, id, deletable=False, dbio = False, keep_values = False, form_name = "fprojectXdetail0",  formstyle=FormStyleBulma )
   
    if fprojectXdetail0.accepted:

        Glb['debug'] and print("     fprojectXdetail0 accepted with: %s " % (fprojectXdetail0.vars))
        fprojectXdetail0_f0 = fprojectXdetail0.vars.get('f0','')
        if len ( fprojectXdetail0_f0 ):
            id_dfprojectXdetail0 = db.dfprojectXdetail0.insert( **fprojectXdetail0.vars )
            db.commit()

            if not id_dfprojectXdetail0 is None:
                dfprojectXdetail0_rows = db.dfprojectXdetail0(id_dfprojectXdetail0 )

                if not dfprojectXdetail0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fprojectXdetail0.vars.f0}\" into db.dfprojectXdetail0.f0, id = {id_dfprojectXdetail0}' )
                         print(f"     found db.dfprojectXdetail0.f0: \"{dfprojectXdetail0_rows.f0}\", id = {id_dfprojectXdetail0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fprojectXdetail0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fprojectXdetail0.vars.items() ]
                print()
   
    elif fprojectXdetail0.errors:
        print("fprojectXdetail0 has errors: %s " % (fprojectXdetail0.errors))
 

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


@action('topXnavXsidebar', method=["GET", "POST"] )
@action.uses(Template('top-nav-sidebar.html', delimiters='[%[ ]]',), db, session,  T, )

def topXnavXsidebar(id=None):
    ctrl_info= "ctrl: topXnavXsidebar, view: top-nav-sidebar.html"
    messages = []

    dftopXnavXsidebar0_rows= None
    id_dftopXnavXsidebar0 = None
    ftopXnavXsidebar0= Form(db.dftopXnavXsidebar0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftopXnavXsidebar0",  formstyle=FormStyleBulma )
   
    if ftopXnavXsidebar0.accepted:

        Glb['debug'] and print("     ftopXnavXsidebar0 accepted with: %s " % (ftopXnavXsidebar0.vars))
        ftopXnavXsidebar0_f0 = ftopXnavXsidebar0.vars.get('f0','')
        if len ( ftopXnavXsidebar0_f0 ):
            id_dftopXnavXsidebar0 = db.dftopXnavXsidebar0.insert( **ftopXnavXsidebar0.vars )
            db.commit()

            if not id_dftopXnavXsidebar0 is None:
                dftopXnavXsidebar0_rows = db.dftopXnavXsidebar0(id_dftopXnavXsidebar0 )

                if not dftopXnavXsidebar0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftopXnavXsidebar0.vars.f0}\" into db.dftopXnavXsidebar0.f0, id = {id_dftopXnavXsidebar0}' )
                         print(f"     found db.dftopXnavXsidebar0.f0: \"{dftopXnavXsidebar0_rows.f0}\", id = {id_dftopXnavXsidebar0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(ftopXnavXsidebar0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in ftopXnavXsidebar0.vars.items() ]
                print()
   
    elif ftopXnavXsidebar0.errors:
        print("ftopXnavXsidebar0 has errors: %s " % (ftopXnavXsidebar0.errors))
 

    return locals()


@action('enhancedXresults', method=["GET", "POST"] )
@action.uses(Template('enhanced-results.html', delimiters='[%[ ]]',), db, session,  T, )

def enhancedXresults(id=None):
    ctrl_info= "ctrl: enhancedXresults, view: enhanced-results.html"
    messages = []

    dfenhancedXresults0_rows= None
    id_dfenhancedXresults0 = None
    fenhancedXresults0= Form(db.dfenhancedXresults0, id, deletable=False, dbio = False, keep_values = False, form_name = "fenhancedXresults0",  formstyle=FormStyleBulma )
   
    if fenhancedXresults0.accepted:

        Glb['debug'] and print("     fenhancedXresults0 accepted with: %s " % (fenhancedXresults0.vars))
        fenhancedXresults0_f0 = fenhancedXresults0.vars.get('f0','')
        if len ( fenhancedXresults0_f0 ):
            id_dfenhancedXresults0 = db.dfenhancedXresults0.insert( **fenhancedXresults0.vars )
            db.commit()

            if not id_dfenhancedXresults0 is None:
                dfenhancedXresults0_rows = db.dfenhancedXresults0(id_dfenhancedXresults0 )

                if not dfenhancedXresults0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fenhancedXresults0.vars.f0}\" into db.dfenhancedXresults0.f0, id = {id_dfenhancedXresults0}' )
                         print(f"     found db.dfenhancedXresults0.f0: \"{dfenhancedXresults0_rows.f0}\", id = {id_dfenhancedXresults0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fenhancedXresults0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fenhancedXresults0.vars.items() ]
                print()
   
    elif fenhancedXresults0.errors:
        print("fenhancedXresults0 has errors: %s " % (fenhancedXresults0.errors))
 

    dfenhancedXresults1_rows= None
    id_dfenhancedXresults1 = None
    fenhancedXresults1= Form(db.dfenhancedXresults1, id, deletable=False, dbio = False, keep_values = False, form_name = "fenhancedXresults1",  formstyle=FormStyleBulma )
   
    if fenhancedXresults1.accepted:

        Glb['debug'] and print("     fenhancedXresults1 accepted with: %s " % (fenhancedXresults1.vars))
        fenhancedXresults1_f0 = fenhancedXresults1.vars.get('f0','')
        if len ( fenhancedXresults1_f0 ):
            id_dfenhancedXresults1 = db.dfenhancedXresults1.insert( **fenhancedXresults1.vars )
            db.commit()

            if not id_dfenhancedXresults1 is None:
                dfenhancedXresults1_rows = db.dfenhancedXresults1(id_dfenhancedXresults1 )

                if not dfenhancedXresults1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fenhancedXresults1.vars.f0}\" into db.dfenhancedXresults1.f0, id = {id_dfenhancedXresults1}' )
                         print(f"     found db.dfenhancedXresults1.f0: \"{dfenhancedXresults1_rows.f0}\", id = {id_dfenhancedXresults1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fenhancedXresults1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fenhancedXresults1.vars.items() ]
                print()
   
    elif fenhancedXresults1.errors:
        print("fenhancedXresults1 has errors: %s " % (fenhancedXresults1.errors))
 

    return locals()


@action('legacyXuserXmenu', method=["GET", "POST"] )
@action.uses(Template('legacy-user-menu.html', delimiters='[%[ ]]',), db, session,  T, )

def legacyXuserXmenu(id=None):
    ctrl_info= "ctrl: legacyXuserXmenu, view: legacy-user-menu.html"
    messages = []

    dflegacyXuserXmenu0_rows= None
    id_dflegacyXuserXmenu0 = None
    flegacyXuserXmenu0= Form(db.dflegacyXuserXmenu0, id, deletable=False, dbio = False, keep_values = False, form_name = "flegacyXuserXmenu0",  formstyle=FormStyleBulma )
   
    if flegacyXuserXmenu0.accepted:

        Glb['debug'] and print("     flegacyXuserXmenu0 accepted with: %s " % (flegacyXuserXmenu0.vars))
        flegacyXuserXmenu0_f0 = flegacyXuserXmenu0.vars.get('f0','')
        if len ( flegacyXuserXmenu0_f0 ):
            id_dflegacyXuserXmenu0 = db.dflegacyXuserXmenu0.insert( **flegacyXuserXmenu0.vars )
            db.commit()

            if not id_dflegacyXuserXmenu0 is None:
                dflegacyXuserXmenu0_rows = db.dflegacyXuserXmenu0(id_dflegacyXuserXmenu0 )

                if not dflegacyXuserXmenu0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flegacyXuserXmenu0.vars.f0}\" into db.dflegacyXuserXmenu0.f0, id = {id_dflegacyXuserXmenu0}' )
                         print(f"     found db.dflegacyXuserXmenu0.f0: \"{dflegacyXuserXmenu0_rows.f0}\", id = {id_dflegacyXuserXmenu0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(flegacyXuserXmenu0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in flegacyXuserXmenu0.vars.items() ]
                print()
   
    elif flegacyXuserXmenu0.errors:
        print("flegacyXuserXmenu0 has errors: %s " % (flegacyXuserXmenu0.errors))
 

    return locals()


@action('recoverXpassword', method=["GET", "POST"] )
@action.uses(Template('recover-password.html', delimiters='[%[ ]]',), db, session,  T, )

def recoverXpassword(id=None):
    ctrl_info= "ctrl: recoverXpassword, view: recover-password.html"
    messages = []

    dfrecoverXpassword0_rows= None
    id_dfrecoverXpassword0 = None
    frecoverXpassword0= Form(db.dfrecoverXpassword0, id, deletable=False, dbio = False, keep_values = False, form_name = "frecoverXpassword0",  formstyle=FormStyleBulma )
   
    if frecoverXpassword0.accepted:

        Glb['debug'] and print("     frecoverXpassword0 accepted with: %s " % (frecoverXpassword0.vars))
        frecoverXpassword0_f0 = frecoverXpassword0.vars.get('f0','')
        if len ( frecoverXpassword0_f0 ):
            id_dfrecoverXpassword0 = db.dfrecoverXpassword0.insert( **frecoverXpassword0.vars )
            db.commit()

            if not id_dfrecoverXpassword0 is None:
                dfrecoverXpassword0_rows = db.dfrecoverXpassword0(id_dfrecoverXpassword0 )

                if not dfrecoverXpassword0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{frecoverXpassword0.vars.f0}\" into db.dfrecoverXpassword0.f0, id = {id_dfrecoverXpassword0}' )
                         print(f"     found db.dfrecoverXpassword0.f0: \"{dfrecoverXpassword0_rows.f0}\", id = {id_dfrecoverXpassword0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(frecoverXpassword0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in frecoverXpassword0.vars.items() ]
                print()
   
    elif frecoverXpassword0.errors:
        print("frecoverXpassword0 has errors: %s " % (frecoverXpassword0.errors))
 

    return locals()


@action('collapsedXsidebar', method=["GET", "POST"] )
@action.uses(Template('collapsed-sidebar.html', delimiters='[%[ ]]',), db, session,  T, )

def collapsedXsidebar(id=None):
    ctrl_info= "ctrl: collapsedXsidebar, view: collapsed-sidebar.html"
    messages = []

    dfcollapsedXsidebar0_rows= None
    id_dfcollapsedXsidebar0 = None
    fcollapsedXsidebar0= Form(db.dfcollapsedXsidebar0, id, deletable=False, dbio = False, keep_values = False, form_name = "fcollapsedXsidebar0",  formstyle=FormStyleBulma )
   
    if fcollapsedXsidebar0.accepted:

        Glb['debug'] and print("     fcollapsedXsidebar0 accepted with: %s " % (fcollapsedXsidebar0.vars))
        fcollapsedXsidebar0_f0 = fcollapsedXsidebar0.vars.get('f0','')
        if len ( fcollapsedXsidebar0_f0 ):
            id_dfcollapsedXsidebar0 = db.dfcollapsedXsidebar0.insert( **fcollapsedXsidebar0.vars )
            db.commit()

            if not id_dfcollapsedXsidebar0 is None:
                dfcollapsedXsidebar0_rows = db.dfcollapsedXsidebar0(id_dfcollapsedXsidebar0 )

                if not dfcollapsedXsidebar0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcollapsedXsidebar0.vars.f0}\" into db.dfcollapsedXsidebar0.f0, id = {id_dfcollapsedXsidebar0}' )
                         print(f"     found db.dfcollapsedXsidebar0.f0: \"{dfcollapsedXsidebar0_rows.f0}\", id = {id_dfcollapsedXsidebar0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fcollapsedXsidebar0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fcollapsedXsidebar0.vars.items() ]
                print()
   
    elif fcollapsedXsidebar0.errors:
        print("fcollapsedXsidebar0 has errors: %s " % (fcollapsedXsidebar0.errors))
 

    return locals()


@action('forgotXpasswordXv2', method=["GET", "POST"] )
@action.uses(Template('forgot-password-v2.html', delimiters='[%[ ]]',), db, session,  T, )

def forgotXpasswordXv2(id=None):
    ctrl_info= "ctrl: forgotXpasswordXv2, view: forgot-password-v2.html"
    messages = []

    dfforgotXpasswordXv20_rows= None
    id_dfforgotXpasswordXv20 = None
    fforgotXpasswordXv20= Form(db.dfforgotXpasswordXv20, id, deletable=False, dbio = False, keep_values = False, form_name = "fforgotXpasswordXv20",  formstyle=FormStyleBulma )
   
    if fforgotXpasswordXv20.accepted:

        Glb['debug'] and print("     fforgotXpasswordXv20 accepted with: %s " % (fforgotXpasswordXv20.vars))
        fforgotXpasswordXv20_f0 = fforgotXpasswordXv20.vars.get('f0','')
        if len ( fforgotXpasswordXv20_f0 ):
            id_dfforgotXpasswordXv20 = db.dfforgotXpasswordXv20.insert( **fforgotXpasswordXv20.vars )
            db.commit()

            if not id_dfforgotXpasswordXv20 is None:
                dfforgotXpasswordXv20_rows = db.dfforgotXpasswordXv20(id_dfforgotXpasswordXv20 )

                if not dfforgotXpasswordXv20_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fforgotXpasswordXv20.vars.f0}\" into db.dfforgotXpasswordXv20.f0, id = {id_dfforgotXpasswordXv20}' )
                         print(f"     found db.dfforgotXpasswordXv20.f0: \"{dfforgotXpasswordXv20_rows.f0}\", id = {id_dfforgotXpasswordXv20}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fforgotXpasswordXv20_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fforgotXpasswordXv20.vars.items() ]
                print()
   
    elif fforgotXpasswordXv20.errors:
        print("fforgotXpasswordXv20 has errors: %s " % (fforgotXpasswordXv20.errors))
 

    return locals()


@action('recoverXpasswordXv2', method=["GET", "POST"] )
@action.uses(Template('recover-password-v2.html', delimiters='[%[ ]]',), db, session,  T, )

def recoverXpasswordXv2(id=None):
    ctrl_info= "ctrl: recoverXpasswordXv2, view: recover-password-v2.html"
    messages = []

    dfrecoverXpasswordXv20_rows= None
    id_dfrecoverXpasswordXv20 = None
    frecoverXpasswordXv20= Form(db.dfrecoverXpasswordXv20, id, deletable=False, dbio = False, keep_values = False, form_name = "frecoverXpasswordXv20",  formstyle=FormStyleBulma )
   
    if frecoverXpasswordXv20.accepted:

        Glb['debug'] and print("     frecoverXpasswordXv20 accepted with: %s " % (frecoverXpasswordXv20.vars))
        frecoverXpasswordXv20_f0 = frecoverXpasswordXv20.vars.get('f0','')
        if len ( frecoverXpasswordXv20_f0 ):
            id_dfrecoverXpasswordXv20 = db.dfrecoverXpasswordXv20.insert( **frecoverXpasswordXv20.vars )
            db.commit()

            if not id_dfrecoverXpasswordXv20 is None:
                dfrecoverXpasswordXv20_rows = db.dfrecoverXpasswordXv20(id_dfrecoverXpasswordXv20 )

                if not dfrecoverXpasswordXv20_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{frecoverXpasswordXv20.vars.f0}\" into db.dfrecoverXpasswordXv20.f0, id = {id_dfrecoverXpasswordXv20}' )
                         print(f"     found db.dfrecoverXpasswordXv20.f0: \"{dfrecoverXpasswordXv20_rows.f0}\", id = {id_dfrecoverXpasswordXv20}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(frecoverXpasswordXv20_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in frecoverXpasswordXv20.vars.items() ]
                print()
   
    elif frecoverXpasswordXv20.errors:
        print("frecoverXpasswordXv20 has errors: %s " % (frecoverXpasswordXv20.errors))
 

    return locals()


@action('fixedXsidebarXcustom', method=["GET", "POST"] )
@action.uses(Template('fixed-sidebar-custom.html', delimiters='[%[ ]]',), db, session,  T, )

def fixedXsidebarXcustom(id=None):
    ctrl_info= "ctrl: fixedXsidebarXcustom, view: fixed-sidebar-custom.html"
    messages = []

    dffixedXsidebarXcustom0_rows= None
    id_dffixedXsidebarXcustom0 = None
    ffixedXsidebarXcustom0= Form(db.dffixedXsidebarXcustom0, id, deletable=False, dbio = False, keep_values = False, form_name = "ffixedXsidebarXcustom0",  formstyle=FormStyleBulma )
   
    if ffixedXsidebarXcustom0.accepted:

        Glb['debug'] and print("     ffixedXsidebarXcustom0 accepted with: %s " % (ffixedXsidebarXcustom0.vars))
        ffixedXsidebarXcustom0_f0 = ffixedXsidebarXcustom0.vars.get('f0','')
        if len ( ffixedXsidebarXcustom0_f0 ):
            id_dffixedXsidebarXcustom0 = db.dffixedXsidebarXcustom0.insert( **ffixedXsidebarXcustom0.vars )
            db.commit()

            if not id_dffixedXsidebarXcustom0 is None:
                dffixedXsidebarXcustom0_rows = db.dffixedXsidebarXcustom0(id_dffixedXsidebarXcustom0 )

                if not dffixedXsidebarXcustom0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ffixedXsidebarXcustom0.vars.f0}\" into db.dffixedXsidebarXcustom0.f0, id = {id_dffixedXsidebarXcustom0}' )
                         print(f"     found db.dffixedXsidebarXcustom0.f0: \"{dffixedXsidebarXcustom0_rows.f0}\", id = {id_dffixedXsidebarXcustom0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(ffixedXsidebarXcustom0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in ffixedXsidebarXcustom0.vars.items() ]
                print()
   
    elif ffixedXsidebarXcustom0.errors:
        print("ffixedXsidebarXcustom0 has errors: %s " % (ffixedXsidebarXcustom0.errors))
 

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
# curl -X  GET   http://localhost:8000/lte3/api/test_table/
# curl -X  GET   http://localhost:8000/lte3/api/test_table/9
# curl -X DELETE  http://localhost:8000/lte3/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/lte3/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/lte3/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/lte3/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/lte3/api/test_table/
#  http         localhost:8000/lte3/api/test_table/9
#  http -f POST localhost:8000/lte3/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/lte3/api/test_table/2
#  http -f PUT localhost:8000/lte3/api/test_table/2 f0=111111 f1=2222222 f2=333333

