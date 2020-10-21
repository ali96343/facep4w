#!/usr/bin/env python3

#
# py4web app, AI-biorex ported 21.10.2020 16:07:41
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

Glb= {'debug': True , 'my_app_name' : "gentelella", 'tte_path': '/static/tte' }



@action('form', method=["GET", "POST"] )
@action.uses(Template('form.html', delimiters='[%[ ]]',), db, session,  T, )

def form(id=None):
    ctrl_info= "ctrl: form, view: form.html"
    messages = []

    dfform0_rows= None
    id_dfform0 = None
    fform0= Form(db.dfform0, id, deletable=False, dbio = False, keep_values = False, form_name = "fform0",  formstyle=FormStyleBulma )
   
    if fform0.accepted:

        Glb['debug'] and print("     fform0 accepted with: %s " % (fform0.vars))
        fform0_f0 = fform0.vars.get('f0','')
        if len ( fform0_f0 ):
            id_dfform0 = db.dfform0.insert( **fform0.vars )
            db.commit()

            if not id_dfform0 is None:
                dfform0_rows = db.dfform0(id_dfform0 )

                if not dfform0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fform0.vars.f0}\" into db.dfform0.f0, id = {id_dfform0}' )
                         print(f"     found db.dfform0.f0: \"{dfform0_rows.f0}\", id = {id_dfform0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fform0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fform0.vars.items() ]
                print()
   
    elif fform0.errors:
        print("fform0 has errors: %s " % (fform0.errors))
 

    dfform1_rows= None
    id_dfform1 = None
    fform1= Form(db.dfform1, id, deletable=False, dbio = False, keep_values = False, form_name = "fform1",  formstyle=FormStyleBulma )
   
    if fform1.accepted:

        Glb['debug'] and print("     fform1 accepted with: %s " % (fform1.vars))
        fform1_f0 = fform1.vars.get('f0','')
        if len ( fform1_f0 ):
            id_dfform1 = db.dfform1.insert( **fform1.vars )
            db.commit()

            if not id_dfform1 is None:
                dfform1_rows = db.dfform1(id_dfform1 )

                if not dfform1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fform1.vars.f0}\" into db.dfform1.f0, id = {id_dfform1}' )
                         print(f"     found db.dfform1.f0: \"{dfform1_rows.f0}\", id = {id_dfform1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fform1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fform1.vars.items() ]
                print()
   
    elif fform1.errors:
        print("fform1 has errors: %s " % (fform1.errors))
 

    dfform2_rows= None
    id_dfform2 = None
    fform2= Form(db.dfform2, id, deletable=False, dbio = False, keep_values = False, form_name = "fform2",  formstyle=FormStyleBulma )
   
    if fform2.accepted:

        Glb['debug'] and print("     fform2 accepted with: %s " % (fform2.vars))
        fform2_f0 = fform2.vars.get('f0','')
        if len ( fform2_f0 ):
            id_dfform2 = db.dfform2.insert( **fform2.vars )
            db.commit()

            if not id_dfform2 is None:
                dfform2_rows = db.dfform2(id_dfform2 )

                if not dfform2_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fform2.vars.f0}\" into db.dfform2.f0, id = {id_dfform2}' )
                         print(f"     found db.dfform2.f0: \"{dfform2_rows.f0}\", id = {id_dfform2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fform2_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fform2.vars.items() ]
                print()
   
    elif fform2.errors:
        print("fform2 has errors: %s " % (fform2.errors))
 

    dfform3_rows= None
    id_dfform3 = None
    fform3= Form(db.dfform3, id, deletable=False, dbio = False, keep_values = False, form_name = "fform3",  formstyle=FormStyleBulma )
   
    if fform3.accepted:

        Glb['debug'] and print("     fform3 accepted with: %s " % (fform3.vars))
        fform3_f0 = fform3.vars.get('f0','')
        if len ( fform3_f0 ):
            id_dfform3 = db.dfform3.insert( **fform3.vars )
            db.commit()

            if not id_dfform3 is None:
                dfform3_rows = db.dfform3(id_dfform3 )

                if not dfform3_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fform3.vars.f0}\" into db.dfform3.f0, id = {id_dfform3}' )
                         print(f"     found db.dfform3.f0: \"{dfform3_rows.f0}\", id = {id_dfform3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fform3_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fform3.vars.items() ]
                print()
   
    elif fform3.errors:
        print("fform3 has errors: %s " % (fform3.errors))
 

    dfform4_rows= None
    id_dfform4 = None
    fform4= Form(db.dfform4, id, deletable=False, dbio = False, keep_values = False, form_name = "fform4",  formstyle=FormStyleBulma )
   
    if fform4.accepted:

        Glb['debug'] and print("     fform4 accepted with: %s " % (fform4.vars))
        fform4_f0 = fform4.vars.get('f0','')
        if len ( fform4_f0 ):
            id_dfform4 = db.dfform4.insert( **fform4.vars )
            db.commit()

            if not id_dfform4 is None:
                dfform4_rows = db.dfform4(id_dfform4 )

                if not dfform4_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fform4.vars.f0}\" into db.dfform4.f0, id = {id_dfform4}' )
                         print(f"     found db.dfform4.f0: \"{dfform4_rows.f0}\", id = {id_dfform4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fform4_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fform4.vars.items() ]
                print()
   
    elif fform4.errors:
        print("fform4 has errors: %s " % (fform4.errors))
 

    dfform5_rows= None
    id_dfform5 = None
    fform5= Form(db.dfform5, id, deletable=False, dbio = False, keep_values = False, form_name = "fform5",  formstyle=FormStyleBulma )
   
    if fform5.accepted:

        Glb['debug'] and print("     fform5 accepted with: %s " % (fform5.vars))
        fform5_f0 = fform5.vars.get('f0','')
        if len ( fform5_f0 ):
            id_dfform5 = db.dfform5.insert( **fform5.vars )
            db.commit()

            if not id_dfform5 is None:
                dfform5_rows = db.dfform5(id_dfform5 )

                if not dfform5_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fform5.vars.f0}\" into db.dfform5.f0, id = {id_dfform5}' )
                         print(f"     found db.dfform5.f0: \"{dfform5_rows.f0}\", id = {id_dfform5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fform5_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fform5.vars.items() ]
                print()
   
    elif fform5.errors:
        print("fform5 has errors: %s " % (fform5.errors))
 

    dfform6_rows= None
    id_dfform6 = None
    fform6= Form(db.dfform6, id, deletable=False, dbio = False, keep_values = False, form_name = "fform6",  formstyle=FormStyleBulma )
   
    if fform6.accepted:

        Glb['debug'] and print("     fform6 accepted with: %s " % (fform6.vars))
        fform6_f0 = fform6.vars.get('f0','')
        if len ( fform6_f0 ):
            id_dfform6 = db.dfform6.insert( **fform6.vars )
            db.commit()

            if not id_dfform6 is None:
                dfform6_rows = db.dfform6(id_dfform6 )

                if not dfform6_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fform6.vars.f0}\" into db.dfform6.f0, id = {id_dfform6}' )
                         print(f"     found db.dfform6.f0: \"{dfform6_rows.f0}\", id = {id_dfform6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fform6_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fform6.vars.items() ]
                print()
   
    elif fform6.errors:
        print("fform6 has errors: %s " % (fform6.errors))
 

    dfform7_rows= None
    id_dfform7 = None
    fform7= Form(db.dfform7, id, deletable=False, dbio = False, keep_values = False, form_name = "fform7",  formstyle=FormStyleBulma )
   
    if fform7.accepted:

        Glb['debug'] and print("     fform7 accepted with: %s " % (fform7.vars))
        fform7_f0 = fform7.vars.get('f0','')
        if len ( fform7_f0 ):
            id_dfform7 = db.dfform7.insert( **fform7.vars )
            db.commit()

            if not id_dfform7 is None:
                dfform7_rows = db.dfform7(id_dfform7 )

                if not dfform7_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fform7.vars.f0}\" into db.dfform7.f0, id = {id_dfform7}' )
                         print(f"     found db.dfform7.f0: \"{dfform7_rows.f0}\", id = {id_dfform7}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fform7_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fform7.vars.items() ]
                print()
   
    elif fform7.errors:
        print("fform7 has errors: %s " % (fform7.errors))
 

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
 

    dflogin1_rows= None
    id_dflogin1 = None
    flogin1= Form(db.dflogin1, id, deletable=False, dbio = False, keep_values = False, form_name = "flogin1",  formstyle=FormStyleBulma )
   
    if flogin1.accepted:

        Glb['debug'] and print("     flogin1 accepted with: %s " % (flogin1.vars))
        flogin1_f0 = flogin1.vars.get('f0','')
        if len ( flogin1_f0 ):
            id_dflogin1 = db.dflogin1.insert( **flogin1.vars )
            db.commit()

            if not id_dflogin1 is None:
                dflogin1_rows = db.dflogin1(id_dflogin1 )

                if not dflogin1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flogin1.vars.f0}\" into db.dflogin1.f0, id = {id_dflogin1}' )
                         print(f"     found db.dflogin1.f0: \"{dflogin1_rows.f0}\", id = {id_dflogin1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(flogin1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in flogin1.vars.items() ]
                print()
   
    elif flogin1.errors:
        print("flogin1 has errors: %s " % (flogin1.errors))
 

    return locals()


@action('inbox', method=["GET", "POST"] )
@action.uses(Template('inbox.html', delimiters='[%[ ]]',), db, session,  T, )

def inbox(id=None):
    ctrl_info= "ctrl: inbox, view: inbox.html"
    messages = []

    return locals()


@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session,  T, )

def index(id=None):
    ctrl_info= "ctrl: index, view: index.html"
    messages = []

    return locals()


@action('icons', method=["GET", "POST"] )
@action.uses(Template('icons.html', delimiters='[%[ ]]',), db, session,  T, )

def icons(id=None):
    ctrl_info= "ctrl: icons, view: icons.html"
    messages = []

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
    rows_ttables4= db(db.ttables4).select()
    return locals()


@action('level2', method=["GET", "POST"] )
@action.uses(Template('level2.html', delimiters='[%[ ]]',), db, session,  T, )

def level2(id=None):
    ctrl_info= "ctrl: level2, view: level2.html"
    messages = []

    return locals()


@action('index3', method=["GET", "POST"] )
@action.uses(Template('index3.html', delimiters='[%[ ]]',), db, session,  T, )

def index3(id=None):
    ctrl_info= "ctrl: index3, view: index3.html"
    messages = []

    return locals()


@action('index2', method=["GET", "POST"] )
@action.uses(Template('index2.html', delimiters='[%[ ]]',), db, session,  T, )

def index2(id=None):
    ctrl_info= "ctrl: index2, view: index2.html"
    messages = []

    return locals()


@action('widgets', method=["GET", "POST"] )
@action.uses(Template('widgets.html', delimiters='[%[ ]]',), db, session,  T, )

def widgets(id=None):
    ctrl_info= "ctrl: widgets, view: widgets.html"
    messages = []

    return locals()


@action('profile', method=["GET", "POST"] )
@action.uses(Template('profile.html', delimiters='[%[ ]]',), db, session,  T, )

def profile(id=None):
    ctrl_info= "ctrl: profile, view: profile.html"
    messages = []

    rows_tprofile0= db(db.tprofile0).select()
    return locals()


@action('morisjs', method=["GET", "POST"] )
@action.uses(Template('morisjs.html', delimiters='[%[ ]]',), db, session,  T, )

def morisjs(id=None):
    ctrl_info= "ctrl: morisjs, view: morisjs.html"
    messages = []

    return locals()


@action('invoice', method=["GET", "POST"] )
@action.uses(Template('invoice.html', delimiters='[%[ ]]',), db, session,  T, )

def invoice(id=None):
    ctrl_info= "ctrl: invoice, view: invoice.html"
    messages = []

    rows_tinvoice0= db(db.tinvoice0).select()
    rows_tinvoice1= db(db.tinvoice1).select()
    return locals()


@action('echarts', method=["GET", "POST"] )
@action.uses(Template('echarts.html', delimiters='[%[ ]]',), db, session,  T, )

def echarts(id=None):
    ctrl_info= "ctrl: echarts, view: echarts.html"
    messages = []

    return locals()


@action('chartjs', method=["GET", "POST"] )
@action.uses(Template('chartjs.html', delimiters='[%[ ]]',), db, session,  T, )

def chartjs(id=None):
    ctrl_info= "ctrl: chartjs, view: chartjs.html"
    messages = []

    return locals()


@action('projects', method=["GET", "POST"] )
@action.uses(Template('projects.html', delimiters='[%[ ]]',), db, session,  T, )

def projects(id=None):
    ctrl_info= "ctrl: projects, view: projects.html"
    messages = []

    rows_tprojects0= db(db.tprojects0).select()
    return locals()


@action('pageX500', method=["GET", "POST"] )
@action.uses(Template('page_500.html', delimiters='[%[ ]]',), db, session,  T, )

def pageX500(id=None):
    ctrl_info= "ctrl: pageX500, view: page_500.html"
    messages = []

    dfpageX5000_rows= None
    id_dfpageX5000 = None
    fpageX5000= Form(db.dfpageX5000, id, deletable=False, dbio = False, keep_values = False, form_name = "fpageX5000",  formstyle=FormStyleBulma )
   
    if fpageX5000.accepted:

        Glb['debug'] and print("     fpageX5000 accepted with: %s " % (fpageX5000.vars))
        fpageX5000_f0 = fpageX5000.vars.get('f0','')
        if len ( fpageX5000_f0 ):
            id_dfpageX5000 = db.dfpageX5000.insert( **fpageX5000.vars )
            db.commit()

            if not id_dfpageX5000 is None:
                dfpageX5000_rows = db.dfpageX5000(id_dfpageX5000 )

                if not dfpageX5000_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpageX5000.vars.f0}\" into db.dfpageX5000.f0, id = {id_dfpageX5000}' )
                         print(f"     found db.dfpageX5000.f0: \"{dfpageX5000_rows.f0}\", id = {id_dfpageX5000}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fpageX5000_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fpageX5000.vars.items() ]
                print()
   
    elif fpageX5000.errors:
        print("fpageX5000 has errors: %s " % (fpageX5000.errors))
 

    return locals()


@action('pageX404', method=["GET", "POST"] )
@action.uses(Template('page_404.html', delimiters='[%[ ]]',), db, session,  T, )

def pageX404(id=None):
    ctrl_info= "ctrl: pageX404, view: page_404.html"
    messages = []

    dfpageX4040_rows= None
    id_dfpageX4040 = None
    fpageX4040= Form(db.dfpageX4040, id, deletable=False, dbio = False, keep_values = False, form_name = "fpageX4040",  formstyle=FormStyleBulma )
   
    if fpageX4040.accepted:

        Glb['debug'] and print("     fpageX4040 accepted with: %s " % (fpageX4040.vars))
        fpageX4040_f0 = fpageX4040.vars.get('f0','')
        if len ( fpageX4040_f0 ):
            id_dfpageX4040 = db.dfpageX4040.insert( **fpageX4040.vars )
            db.commit()

            if not id_dfpageX4040 is None:
                dfpageX4040_rows = db.dfpageX4040(id_dfpageX4040 )

                if not dfpageX4040_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpageX4040.vars.f0}\" into db.dfpageX4040.f0, id = {id_dfpageX4040}' )
                         print(f"     found db.dfpageX4040.f0: \"{dfpageX4040_rows.f0}\", id = {id_dfpageX4040}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fpageX4040_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fpageX4040.vars.items() ]
                print()
   
    elif fpageX4040.errors:
        print("fpageX4040 has errors: %s " % (fpageX4040.errors))
 

    return locals()


@action('pageX403', method=["GET", "POST"] )
@action.uses(Template('page_403.html', delimiters='[%[ ]]',), db, session,  T, )

def pageX403(id=None):
    ctrl_info= "ctrl: pageX403, view: page_403.html"
    messages = []

    dfpageX4030_rows= None
    id_dfpageX4030 = None
    fpageX4030= Form(db.dfpageX4030, id, deletable=False, dbio = False, keep_values = False, form_name = "fpageX4030",  formstyle=FormStyleBulma )
   
    if fpageX4030.accepted:

        Glb['debug'] and print("     fpageX4030 accepted with: %s " % (fpageX4030.vars))
        fpageX4030_f0 = fpageX4030.vars.get('f0','')
        if len ( fpageX4030_f0 ):
            id_dfpageX4030 = db.dfpageX4030.insert( **fpageX4030.vars )
            db.commit()

            if not id_dfpageX4030 is None:
                dfpageX4030_rows = db.dfpageX4030(id_dfpageX4030 )

                if not dfpageX4030_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpageX4030.vars.f0}\" into db.dfpageX4030.f0, id = {id_dfpageX4030}' )
                         print(f"     found db.dfpageX4030.f0: \"{dfpageX4030_rows.f0}\", id = {id_dfpageX4030}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fpageX4030_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fpageX4030.vars.items() ]
                print()
   
    elif fpageX4030.errors:
        print("fpageX4030 has errors: %s " % (fpageX4030.errors))
 

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
 

    dfcalendar1_rows= None
    id_dfcalendar1 = None
    fcalendar1= Form(db.dfcalendar1, id, deletable=False, dbio = False, keep_values = False, form_name = "fcalendar1",  formstyle=FormStyleBulma )
   
    if fcalendar1.accepted:

        Glb['debug'] and print("     fcalendar1 accepted with: %s " % (fcalendar1.vars))
        fcalendar1_f0 = fcalendar1.vars.get('f0','')
        if len ( fcalendar1_f0 ):
            id_dfcalendar1 = db.dfcalendar1.insert( **fcalendar1.vars )
            db.commit()

            if not id_dfcalendar1 is None:
                dfcalendar1_rows = db.dfcalendar1(id_dfcalendar1 )

                if not dfcalendar1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcalendar1.vars.f0}\" into db.dfcalendar1.f0, id = {id_dfcalendar1}' )
                         print(f"     found db.dfcalendar1.f0: \"{dfcalendar1_rows.f0}\", id = {id_dfcalendar1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fcalendar1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fcalendar1.vars.items() ]
                print()
   
    elif fcalendar1.errors:
        print("fcalendar1 has errors: %s " % (fcalendar1.errors))
 

    return locals()


@action('chartjs2', method=["GET", "POST"] )
@action.uses(Template('chartjs2.html', delimiters='[%[ ]]',), db, session,  T, )

def chartjs2(id=None):
    ctrl_info= "ctrl: chartjs2, view: chartjs2.html"
    messages = []

    return locals()


@action('contacts', method=["GET", "POST"] )
@action.uses(Template('contacts.html', delimiters='[%[ ]]',), db, session,  T, )

def contacts(id=None):
    ctrl_info= "ctrl: contacts, view: contacts.html"
    messages = []

    return locals()


@action('typography', method=["GET", "POST"] )
@action.uses(Template('typography.html', delimiters='[%[ ]]',), db, session,  T, )

def typography(id=None):
    ctrl_info= "ctrl: typography, view: typography.html"
    messages = []

    return locals()


@action('plainXpage', method=["GET", "POST"] )
@action.uses(Template('plain_page.html', delimiters='[%[ ]]',), db, session,  T, )

def plainXpage(id=None):
    ctrl_info= "ctrl: plainXpage, view: plain_page.html"
    messages = []

    return locals()


@action('glyphicons', method=["GET", "POST"] )
@action.uses(Template('glyphicons.html', delimiters='[%[ ]]',), db, session,  T, )

def glyphicons(id=None):
    ctrl_info= "ctrl: glyphicons, view: glyphicons.html"
    messages = []

    return locals()


@action('eXcommerce', method=["GET", "POST"] )
@action.uses(Template('e_commerce.html', delimiters='[%[ ]]',), db, session,  T, )

def eXcommerce(id=None):
    ctrl_info= "ctrl: eXcommerce, view: e_commerce.html"
    messages = []

    return locals()


@action('formXupload', method=["GET", "POST"] )
@action.uses(Template('form_upload.html', delimiters='[%[ ]]',), db, session,  T, )

def formXupload(id=None):
    ctrl_info= "ctrl: formXupload, view: form_upload.html"
    messages = []

    dfformXupload0_rows= None
    id_dfformXupload0 = None
    fformXupload0= Form(db.dfformXupload0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXupload0",  formstyle=FormStyleBulma )
   
    if fformXupload0.accepted:

        Glb['debug'] and print("     fformXupload0 accepted with: %s " % (fformXupload0.vars))
        fformXupload0_f0 = fformXupload0.vars.get('f0','')
        if len ( fformXupload0_f0 ):
            id_dfformXupload0 = db.dfformXupload0.insert( **fformXupload0.vars )
            db.commit()

            if not id_dfformXupload0 is None:
                dfformXupload0_rows = db.dfformXupload0(id_dfformXupload0 )

                if not dfformXupload0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXupload0.vars.f0}\" into db.dfformXupload0.f0, id = {id_dfformXupload0}' )
                         print(f"     found db.dfformXupload0.f0: \"{dfformXupload0_rows.f0}\", id = {id_dfformXupload0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fformXupload0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXupload0.vars.items() ]
                print()
   
    elif fformXupload0.errors:
        print("fformXupload0 has errors: %s " % (fformXupload0.errors))
 

    return locals()


@action('otherXcharts', method=["GET", "POST"] )
@action.uses(Template('other_charts.html', delimiters='[%[ ]]',), db, session,  T, )

def otherXcharts(id=None):
    ctrl_info= "ctrl: otherXcharts, view: other_charts.html"
    messages = []

    rows_totherXcharts0= db(db.totherXcharts0).select()
    return locals()


@action('formXwizards', method=["GET", "POST"] )
@action.uses(Template('form_wizards.html', delimiters='[%[ ]]',), db, session,  T, )

def formXwizards(id=None):
    ctrl_info= "ctrl: formXwizards, view: form_wizards.html"
    messages = []

    dfformXwizards0_rows= None
    id_dfformXwizards0 = None
    fformXwizards0= Form(db.dfformXwizards0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXwizards0",  formstyle=FormStyleBulma )
   
    if fformXwizards0.accepted:

        Glb['debug'] and print("     fformXwizards0 accepted with: %s " % (fformXwizards0.vars))
        fformXwizards0_f0 = fformXwizards0.vars.get('f0','')
        if len ( fformXwizards0_f0 ):
            id_dfformXwizards0 = db.dfformXwizards0.insert( **fformXwizards0.vars )
            db.commit()

            if not id_dfformXwizards0 is None:
                dfformXwizards0_rows = db.dfformXwizards0(id_dfformXwizards0 )

                if not dfformXwizards0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXwizards0.vars.f0}\" into db.dfformXwizards0.f0, id = {id_dfformXwizards0}' )
                         print(f"     found db.dfformXwizards0.f0: \"{dfformXwizards0_rows.f0}\", id = {id_dfformXwizards0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fformXwizards0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXwizards0.vars.items() ]
                print()
   
    elif fformXwizards0.errors:
        print("fformXwizards0 has errors: %s " % (fformXwizards0.errors))
 

    dfformXwizards1_rows= None
    id_dfformXwizards1 = None
    fformXwizards1= Form(db.dfformXwizards1, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXwizards1",  formstyle=FormStyleBulma )
   
    if fformXwizards1.accepted:

        Glb['debug'] and print("     fformXwizards1 accepted with: %s " % (fformXwizards1.vars))
        fformXwizards1_f0 = fformXwizards1.vars.get('f0','')
        if len ( fformXwizards1_f0 ):
            id_dfformXwizards1 = db.dfformXwizards1.insert( **fformXwizards1.vars )
            db.commit()

            if not id_dfformXwizards1 is None:
                dfformXwizards1_rows = db.dfformXwizards1(id_dfformXwizards1 )

                if not dfformXwizards1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXwizards1.vars.f0}\" into db.dfformXwizards1.f0, id = {id_dfformXwizards1}' )
                         print(f"     found db.dfformXwizards1.f0: \"{dfformXwizards1_rows.f0}\", id = {id_dfformXwizards1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fformXwizards1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXwizards1.vars.items() ]
                print()
   
    elif fformXwizards1.errors:
        print("fformXwizards1 has errors: %s " % (fformXwizards1.errors))
 

    return locals()


@action('formXbuttons', method=["GET", "POST"] )
@action.uses(Template('form_buttons.html', delimiters='[%[ ]]',), db, session,  T, )

def formXbuttons(id=None):
    ctrl_info= "ctrl: formXbuttons, view: form_buttons.html"
    messages = []

    return locals()


@action('fixedXfooter', method=["GET", "POST"] )
@action.uses(Template('fixed_footer.html', delimiters='[%[ ]]',), db, session,  T, )

def fixedXfooter(id=None):
    ctrl_info= "ctrl: fixedXfooter, view: fixed_footer.html"
    messages = []

    return locals()


@action('formXadvanced', method=["GET", "POST"] )
@action.uses(Template('form_advanced.html', delimiters='[%[ ]]',), db, session,  T, )

def formXadvanced(id=None):
    ctrl_info= "ctrl: formXadvanced, view: form_advanced.html"
    messages = []

    rows_tformXadvanced0= db(db.tformXadvanced0).select()
    rows_tformXadvanced1= db(db.tformXadvanced1).select()
    rows_tformXadvanced2= db(db.tformXadvanced2).select()
    rows_tformXadvanced3= db(db.tformXadvanced3).select()
    rows_tformXadvanced4= db(db.tformXadvanced4).select()
    rows_tformXadvanced5= db(db.tformXadvanced5).select()
    rows_tformXadvanced6= db(db.tformXadvanced6).select()
    rows_tformXadvanced7= db(db.tformXadvanced7).select()
    dfformXadvanced0_rows= None
    id_dfformXadvanced0 = None
    fformXadvanced0= Form(db.dfformXadvanced0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXadvanced0",  formstyle=FormStyleBulma )
   
    if fformXadvanced0.accepted:

        Glb['debug'] and print("     fformXadvanced0 accepted with: %s " % (fformXadvanced0.vars))
        fformXadvanced0_f0 = fformXadvanced0.vars.get('f0','')
        if len ( fformXadvanced0_f0 ):
            id_dfformXadvanced0 = db.dfformXadvanced0.insert( **fformXadvanced0.vars )
            db.commit()

            if not id_dfformXadvanced0 is None:
                dfformXadvanced0_rows = db.dfformXadvanced0(id_dfformXadvanced0 )

                if not dfformXadvanced0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXadvanced0.vars.f0}\" into db.dfformXadvanced0.f0, id = {id_dfformXadvanced0}' )
                         print(f"     found db.dfformXadvanced0.f0: \"{dfformXadvanced0_rows.f0}\", id = {id_dfformXadvanced0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fformXadvanced0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXadvanced0.vars.items() ]
                print()
   
    elif fformXadvanced0.errors:
        print("fformXadvanced0 has errors: %s " % (fformXadvanced0.errors))
 

    dfformXadvanced1_rows= None
    id_dfformXadvanced1 = None
    fformXadvanced1= Form(db.dfformXadvanced1, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXadvanced1",  formstyle=FormStyleBulma )
   
    if fformXadvanced1.accepted:

        Glb['debug'] and print("     fformXadvanced1 accepted with: %s " % (fformXadvanced1.vars))
        fformXadvanced1_f0 = fformXadvanced1.vars.get('f0','')
        if len ( fformXadvanced1_f0 ):
            id_dfformXadvanced1 = db.dfformXadvanced1.insert( **fformXadvanced1.vars )
            db.commit()

            if not id_dfformXadvanced1 is None:
                dfformXadvanced1_rows = db.dfformXadvanced1(id_dfformXadvanced1 )

                if not dfformXadvanced1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXadvanced1.vars.f0}\" into db.dfformXadvanced1.f0, id = {id_dfformXadvanced1}' )
                         print(f"     found db.dfformXadvanced1.f0: \"{dfformXadvanced1_rows.f0}\", id = {id_dfformXadvanced1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fformXadvanced1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXadvanced1.vars.items() ]
                print()
   
    elif fformXadvanced1.errors:
        print("fformXadvanced1 has errors: %s " % (fformXadvanced1.errors))
 

    dfformXadvanced2_rows= None
    id_dfformXadvanced2 = None
    fformXadvanced2= Form(db.dfformXadvanced2, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXadvanced2",  formstyle=FormStyleBulma )
   
    if fformXadvanced2.accepted:

        Glb['debug'] and print("     fformXadvanced2 accepted with: %s " % (fformXadvanced2.vars))
        fformXadvanced2_f0 = fformXadvanced2.vars.get('f0','')
        if len ( fformXadvanced2_f0 ):
            id_dfformXadvanced2 = db.dfformXadvanced2.insert( **fformXadvanced2.vars )
            db.commit()

            if not id_dfformXadvanced2 is None:
                dfformXadvanced2_rows = db.dfformXadvanced2(id_dfformXadvanced2 )

                if not dfformXadvanced2_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXadvanced2.vars.f0}\" into db.dfformXadvanced2.f0, id = {id_dfformXadvanced2}' )
                         print(f"     found db.dfformXadvanced2.f0: \"{dfformXadvanced2_rows.f0}\", id = {id_dfformXadvanced2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fformXadvanced2_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXadvanced2.vars.items() ]
                print()
   
    elif fformXadvanced2.errors:
        print("fformXadvanced2 has errors: %s " % (fformXadvanced2.errors))
 

    dfformXadvanced3_rows= None
    id_dfformXadvanced3 = None
    fformXadvanced3= Form(db.dfformXadvanced3, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXadvanced3",  formstyle=FormStyleBulma )
   
    if fformXadvanced3.accepted:

        Glb['debug'] and print("     fformXadvanced3 accepted with: %s " % (fformXadvanced3.vars))
        fformXadvanced3_f0 = fformXadvanced3.vars.get('f0','')
        if len ( fformXadvanced3_f0 ):
            id_dfformXadvanced3 = db.dfformXadvanced3.insert( **fformXadvanced3.vars )
            db.commit()

            if not id_dfformXadvanced3 is None:
                dfformXadvanced3_rows = db.dfformXadvanced3(id_dfformXadvanced3 )

                if not dfformXadvanced3_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXadvanced3.vars.f0}\" into db.dfformXadvanced3.f0, id = {id_dfformXadvanced3}' )
                         print(f"     found db.dfformXadvanced3.f0: \"{dfformXadvanced3_rows.f0}\", id = {id_dfformXadvanced3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fformXadvanced3_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXadvanced3.vars.items() ]
                print()
   
    elif fformXadvanced3.errors:
        print("fformXadvanced3 has errors: %s " % (fformXadvanced3.errors))
 

    return locals()


@action('mediaXgallery', method=["GET", "POST"] )
@action.uses(Template('media_gallery.html', delimiters='[%[ ]]',), db, session,  T, )

def mediaXgallery(id=None):
    ctrl_info= "ctrl: mediaXgallery, view: media_gallery.html"
    messages = []

    return locals()


@action('fixedXsidebar', method=["GET", "POST"] )
@action.uses(Template('fixed_sidebar.html', delimiters='[%[ ]]',), db, session,  T, )

def fixedXsidebar(id=None):
    ctrl_info= "ctrl: fixedXsidebar, view: fixed_sidebar.html"
    messages = []

    return locals()


@action('tablesXdynamic', method=["GET", "POST"] )
@action.uses(Template('tables_dynamic.html', delimiters='[%[ ]]',), db, session,  T, )

def tablesXdynamic(id=None):
    ctrl_info= "ctrl: tablesXdynamic, view: tables_dynamic.html"
    messages = []

    rows_ttablesXdynamic0= db(db.ttablesXdynamic0).select()
    rows_ttablesXdynamic1= db(db.ttablesXdynamic1).select()
    rows_ttablesXdynamic2= db(db.ttablesXdynamic2).select()
    rows_ttablesXdynamic3= db(db.ttablesXdynamic3).select()
    rows_ttablesXdynamic4= db(db.ttablesXdynamic4).select()
    rows_ttablesXdynamic5= db(db.ttablesXdynamic5).select()
    return locals()


@action('projectXdetail', method=["GET", "POST"] )
@action.uses(Template('project_detail.html', delimiters='[%[ ]]',), db, session,  T, )

def projectXdetail(id=None):
    ctrl_info= "ctrl: projectXdetail, view: project_detail.html"
    messages = []

    return locals()


@action('pricingXtables', method=["GET", "POST"] )
@action.uses(Template('pricing_tables.html', delimiters='[%[ ]]',), db, session,  T, )

def pricingXtables(id=None):
    ctrl_info= "ctrl: pricingXtables, view: pricing_tables.html"
    messages = []

    return locals()


@action('formXvalidation', method=["GET", "POST"] )
@action.uses(Template('form_validation.html', delimiters='[%[ ]]',), db, session,  T, )

def formXvalidation(id=None):
    ctrl_info= "ctrl: formXvalidation, view: form_validation.html"
    messages = []

    dfformXvalidation0_rows= None
    id_dfformXvalidation0 = None
    fformXvalidation0= Form(db.dfformXvalidation0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXvalidation0",  formstyle=FormStyleBulma )
   
    if fformXvalidation0.accepted:

        Glb['debug'] and print("     fformXvalidation0 accepted with: %s " % (fformXvalidation0.vars))
        fformXvalidation0_f0 = fformXvalidation0.vars.get('f0','')
        if len ( fformXvalidation0_f0 ):
            id_dfformXvalidation0 = db.dfformXvalidation0.insert( **fformXvalidation0.vars )
            db.commit()

            if not id_dfformXvalidation0 is None:
                dfformXvalidation0_rows = db.dfformXvalidation0(id_dfformXvalidation0 )

                if not dfformXvalidation0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXvalidation0.vars.f0}\" into db.dfformXvalidation0.f0, id = {id_dfformXvalidation0}' )
                         print(f"     found db.dfformXvalidation0.f0: \"{dfformXvalidation0_rows.f0}\", id = {id_dfformXvalidation0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fformXvalidation0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXvalidation0.vars.items() ]
                print()
   
    elif fformXvalidation0.errors:
        print("fformXvalidation0 has errors: %s " % (fformXvalidation0.errors))
 

    return locals()


@action('generalXelements', method=["GET", "POST"] )
@action.uses(Template('general_elements.html', delimiters='[%[ ]]',), db, session,  T, )

def generalXelements(id=None):
    ctrl_info= "ctrl: generalXelements, view: general_elements.html"
    messages = []

    rows_tgeneralXelements0= db(db.tgeneralXelements0).select()
    rows_tgeneralXelements1= db(db.tgeneralXelements1).select()
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
# curl -X  GET   http://localhost:8000/gentelella/api/test_table/
# curl -X  GET   http://localhost:8000/gentelella/api/test_table/9
# curl -X DELETE  http://localhost:8000/gentelella/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/gentelella/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/gentelella/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/gentelella/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/gentelella/api/test_table/
#  http         localhost:8000/gentelella/api/test_table/9
#  http -f POST localhost:8000/gentelella/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/gentelella/api/test_table/2
#  http -f PUT localhost:8000/gentelella/api/test_table/2 f0=111111 f1=2222222 f2=333333

