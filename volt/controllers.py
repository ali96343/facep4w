#!/usr/bin/env python3

#
# py4web app, AI-biorex ported 27.10.2020 12:42:09
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


Glb= {'debug': True , 'my_app_name': "volt", 'tte_path': '/static/tte' }



@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session,  T, )

def index(id=None):
    ctrl_info= "ctrl: index, view: index.html"
    messages = []

    dfindex0_row= None
    id_dfindex0 = None
    findex0= Form(db.dfindex0, id, deletable=False, dbio = False, keep_values = False, form_name = "findex0",  formstyle=FormStyleBulma )
   
    if findex0.accepted:

        Glb['debug'] and print("     findex0 accepted with: %s " % (findex0.vars))
        findex0_f0 = findex0.vars.get('f0','')
        if len ( findex0_f0 ):
            id_dfindex0 = db.dfindex0.insert( **findex0.vars )
            db.commit()

            if not id_dfindex0 is None:
                dfindex0_row = db.dfindex0(id_dfindex0 )

                if not dfindex0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex0.vars.f0}\" into db.dfindex0.f0, id = {id_dfindex0}' )
                         print(f"     found db.dfindex0.f0: \"{dfindex0_row.f0}\", id = {id_dfindex0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findex0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findex0.vars.items() ]
                print()
   
    elif findex0.errors:
        print("findex0 has errors: %s " % (findex0.errors))
 

    return locals()


@action('dashboard', method=["GET", "POST"] )
@action.uses(Template('dashboard.html', delimiters='[%[ ]]',), db, session,  T, )

def dashboard(id=None):
    ctrl_info= "ctrl: dashboard, view: dashboard.html"
    messages = []

    rows_tdashboard0= db(db.tdashboard0).select()
    dfdashboard0_row= None
    id_dfdashboard0 = None
    fdashboard0= Form(db.dfdashboard0, id, deletable=False, dbio = False, keep_values = False, form_name = "fdashboard0",  formstyle=FormStyleBulma )
   
    if fdashboard0.accepted:

        Glb['debug'] and print("     fdashboard0 accepted with: %s " % (fdashboard0.vars))
        fdashboard0_f0 = fdashboard0.vars.get('f0','')
        if len ( fdashboard0_f0 ):
            id_dfdashboard0 = db.dfdashboard0.insert( **fdashboard0.vars )
            db.commit()

            if not id_dfdashboard0 is None:
                dfdashboard0_row = db.dfdashboard0(id_dfdashboard0 )

                if not dfdashboard0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fdashboard0.vars.f0}\" into db.dfdashboard0.f0, id = {id_dfdashboard0}' )
                         print(f"     found db.dfdashboard0.f0: \"{dfdashboard0_row.f0}\", id = {id_dfdashboard0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fdashboard0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fdashboard0.vars.items() ]
                print()
   
    elif fdashboard0.errors:
        print("fdashboard0 has errors: %s " % (fdashboard0.errors))
 

    return locals()


@action('signXin', method=["GET", "POST"] )
@action.uses(Template('sign-in.html', delimiters='[%[ ]]',), db, session,  T, )

def signXin(id=None):
    ctrl_info= "ctrl: signXin, view: sign-in.html"
    messages = []

    dfsignXin0_row= None
    id_dfsignXin0 = None
    fsignXin0= Form(db.dfsignXin0, id, deletable=False, dbio = False, keep_values = False, form_name = "fsignXin0",  formstyle=FormStyleBulma )
   
    if fsignXin0.accepted:

        Glb['debug'] and print("     fsignXin0 accepted with: %s " % (fsignXin0.vars))
        fsignXin0_f0 = fsignXin0.vars.get('f0','')
        if len ( fsignXin0_f0 ):
            id_dfsignXin0 = db.dfsignXin0.insert( **fsignXin0.vars )
            db.commit()

            if not id_dfsignXin0 is None:
                dfsignXin0_row = db.dfsignXin0(id_dfsignXin0 )

                if not dfsignXin0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fsignXin0.vars.f0}\" into db.dfsignXin0.f0, id = {id_dfsignXin0}' )
                         print(f"     found db.dfsignXin0.f0: \"{dfsignXin0_row.f0}\", id = {id_dfsignXin0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fsignXin0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fsignXin0.vars.items() ]
                print()
   
    elif fsignXin0.errors:
        print("fsignXin0 has errors: %s " % (fsignXin0.errors))
 

    return locals()


@action('signXup', method=["GET", "POST"] )
@action.uses(Template('sign-up.html', delimiters='[%[ ]]',), db, session,  T, )

def signXup(id=None):
    ctrl_info= "ctrl: signXup, view: sign-up.html"
    messages = []

    dfsignXup0_row= None
    id_dfsignXup0 = None
    fsignXup0= Form(db.dfsignXup0, id, deletable=False, dbio = False, keep_values = False, form_name = "fsignXup0",  formstyle=FormStyleBulma )
   
    if fsignXup0.accepted:

        Glb['debug'] and print("     fsignXup0 accepted with: %s " % (fsignXup0.vars))
        fsignXup0_f0 = fsignXup0.vars.get('f0','')
        if len ( fsignXup0_f0 ):
            id_dfsignXup0 = db.dfsignXup0.insert( **fsignXup0.vars )
            db.commit()

            if not id_dfsignXup0 is None:
                dfsignXup0_row = db.dfsignXup0(id_dfsignXup0 )

                if not dfsignXup0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fsignXup0.vars.f0}\" into db.dfsignXup0.f0, id = {id_dfsignXup0}' )
                         print(f"     found db.dfsignXup0.f0: \"{dfsignXup0_row.f0}\", id = {id_dfsignXup0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fsignXup0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fsignXup0.vars.items() ]
                print()
   
    elif fsignXup0.errors:
        print("fsignXup0 has errors: %s " % (fsignXup0.errors))
 

    return locals()


@action('lock', method=["GET", "POST"] )
@action.uses(Template('lock.html', delimiters='[%[ ]]',), db, session,  T, )

def lock(id=None):
    ctrl_info= "ctrl: lock, view: lock.html"
    messages = []

    dflock0_row= None
    id_dflock0 = None
    flock0= Form(db.dflock0, id, deletable=False, dbio = False, keep_values = False, form_name = "flock0",  formstyle=FormStyleBulma )
   
    if flock0.accepted:

        Glb['debug'] and print("     flock0 accepted with: %s " % (flock0.vars))
        flock0_f0 = flock0.vars.get('f0','')
        if len ( flock0_f0 ):
            id_dflock0 = db.dflock0.insert( **flock0.vars )
            db.commit()

            if not id_dflock0 is None:
                dflock0_row = db.dflock0(id_dflock0 )

                if not dflock0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flock0.vars.f0}\" into db.dflock0.f0, id = {id_dflock0}' )
                         print(f"     found db.dflock0.f0: \"{dflock0_row.f0}\", id = {id_dflock0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(flock0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in flock0.vars.items() ]
                print()
   
    elif flock0.errors:
        print("flock0 has errors: %s " % (flock0.errors))
 

    return locals()


@action('transactions', method=["GET", "POST"] )
@action.uses(Template('transactions.html', delimiters='[%[ ]]',), db, session,  T, )

def transactions(id=None):
    ctrl_info= "ctrl: transactions, view: transactions.html"
    messages = []

    rows_ttransactions0= db(db.ttransactions0).select()
    dftransactions0_row= None
    id_dftransactions0 = None
    ftransactions0= Form(db.dftransactions0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftransactions0",  formstyle=FormStyleBulma )
   
    if ftransactions0.accepted:

        Glb['debug'] and print("     ftransactions0 accepted with: %s " % (ftransactions0.vars))
        ftransactions0_f0 = ftransactions0.vars.get('f0','')
        if len ( ftransactions0_f0 ):
            id_dftransactions0 = db.dftransactions0.insert( **ftransactions0.vars )
            db.commit()

            if not id_dftransactions0 is None:
                dftransactions0_row = db.dftransactions0(id_dftransactions0 )

                if not dftransactions0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftransactions0.vars.f0}\" into db.dftransactions0.f0, id = {id_dftransactions0}' )
                         print(f"     found db.dftransactions0.f0: \"{dftransactions0_row.f0}\", id = {id_dftransactions0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftransactions0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftransactions0.vars.items() ]
                print()
   
    elif ftransactions0.errors:
        print("ftransactions0 has errors: %s " % (ftransactions0.errors))
 

    return locals()


@action('settings', method=["GET", "POST"] )
@action.uses(Template('settings.html', delimiters='[%[ ]]',), db, session,  T, )

def settings(id=None):
    ctrl_info= "ctrl: settings, view: settings.html"
    messages = []

    dfsettings0_row= None
    id_dfsettings0 = None
    fsettings0= Form(db.dfsettings0, id, deletable=False, dbio = False, keep_values = False, form_name = "fsettings0",  formstyle=FormStyleBulma )
   
    if fsettings0.accepted:

        Glb['debug'] and print("     fsettings0 accepted with: %s " % (fsettings0.vars))
        fsettings0_f0 = fsettings0.vars.get('f0','')
        if len ( fsettings0_f0 ):
            id_dfsettings0 = db.dfsettings0.insert( **fsettings0.vars )
            db.commit()

            if not id_dfsettings0 is None:
                dfsettings0_row = db.dfsettings0(id_dfsettings0 )

                if not dfsettings0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fsettings0.vars.f0}\" into db.dfsettings0.f0, id = {id_dfsettings0}' )
                         print(f"     found db.dfsettings0.f0: \"{dfsettings0_row.f0}\", id = {id_dfsettings0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fsettings0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fsettings0.vars.items() ]
                print()
   
    elif fsettings0.errors:
        print("fsettings0 has errors: %s " % (fsettings0.errors))
 

    dfsettings1_row= None
    id_dfsettings1 = None
    fsettings1= Form(db.dfsettings1, id, deletable=False, dbio = False, keep_values = False, form_name = "fsettings1",  formstyle=FormStyleBulma )
   
    if fsettings1.accepted:

        Glb['debug'] and print("     fsettings1 accepted with: %s " % (fsettings1.vars))
        fsettings1_f0 = fsettings1.vars.get('f0','')
        if len ( fsettings1_f0 ):
            id_dfsettings1 = db.dfsettings1.insert( **fsettings1.vars )
            db.commit()

            if not id_dfsettings1 is None:
                dfsettings1_row = db.dfsettings1(id_dfsettings1 )

                if not dfsettings1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fsettings1.vars.f0}\" into db.dfsettings1.f0, id = {id_dfsettings1}' )
                         print(f"     found db.dfsettings1.f0: \"{dfsettings1_row.f0}\", id = {id_dfsettings1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fsettings1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fsettings1.vars.items() ]
                print()
   
    elif fsettings1.errors:
        print("fsettings1 has errors: %s " % (fsettings1.errors))
 

    return locals()


@action('forgotXpassword', method=["GET", "POST"] )
@action.uses(Template('forgot-password.html', delimiters='[%[ ]]',), db, session,  T, )

def forgotXpassword(id=None):
    ctrl_info= "ctrl: forgotXpassword, view: forgot-password.html"
    messages = []

    dfforgotXpassword0_row= None
    id_dfforgotXpassword0 = None
    fforgotXpassword0= Form(db.dfforgotXpassword0, id, deletable=False, dbio = False, keep_values = False, form_name = "fforgotXpassword0",  formstyle=FormStyleBulma )
   
    if fforgotXpassword0.accepted:

        Glb['debug'] and print("     fforgotXpassword0 accepted with: %s " % (fforgotXpassword0.vars))
        fforgotXpassword0_f0 = fforgotXpassword0.vars.get('f0','')
        if len ( fforgotXpassword0_f0 ):
            id_dfforgotXpassword0 = db.dfforgotXpassword0.insert( **fforgotXpassword0.vars )
            db.commit()

            if not id_dfforgotXpassword0 is None:
                dfforgotXpassword0_row = db.dfforgotXpassword0(id_dfforgotXpassword0 )

                if not dfforgotXpassword0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fforgotXpassword0.vars.f0}\" into db.dfforgotXpassword0.f0, id = {id_dfforgotXpassword0}' )
                         print(f"     found db.dfforgotXpassword0.f0: \"{dfforgotXpassword0_row.f0}\", id = {id_dfforgotXpassword0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fforgotXpassword0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fforgotXpassword0.vars.items() ]
                print()
   
    elif fforgotXpassword0.errors:
        print("fforgotXpassword0 has errors: %s " % (fforgotXpassword0.errors))
 

    return locals()


@action('resetXpassword', method=["GET", "POST"] )
@action.uses(Template('reset-password.html', delimiters='[%[ ]]',), db, session,  T, )

def resetXpassword(id=None):
    ctrl_info= "ctrl: resetXpassword, view: reset-password.html"
    messages = []

    dfresetXpassword0_row= None
    id_dfresetXpassword0 = None
    fresetXpassword0= Form(db.dfresetXpassword0, id, deletable=False, dbio = False, keep_values = False, form_name = "fresetXpassword0",  formstyle=FormStyleBulma )
   
    if fresetXpassword0.accepted:

        Glb['debug'] and print("     fresetXpassword0 accepted with: %s " % (fresetXpassword0.vars))
        fresetXpassword0_f0 = fresetXpassword0.vars.get('f0','')
        if len ( fresetXpassword0_f0 ):
            id_dfresetXpassword0 = db.dfresetXpassword0.insert( **fresetXpassword0.vars )
            db.commit()

            if not id_dfresetXpassword0 is None:
                dfresetXpassword0_row = db.dfresetXpassword0(id_dfresetXpassword0 )

                if not dfresetXpassword0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fresetXpassword0.vars.f0}\" into db.dfresetXpassword0.f0, id = {id_dfresetXpassword0}' )
                         print(f"     found db.dfresetXpassword0.f0: \"{dfresetXpassword0_row.f0}\", id = {id_dfresetXpassword0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fresetXpassword0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fresetXpassword0.vars.items() ]
                print()
   
    elif fresetXpassword0.errors:
        print("fresetXpassword0 has errors: %s " % (fresetXpassword0.errors))
 

    return locals()


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

    return locals()


@action('bootstrapXtables', method=["GET", "POST"] )
@action.uses(Template('bootstrap-tables.html', delimiters='[%[ ]]',), db, session,  T, )

def bootstrapXtables(id=None):
    ctrl_info= "ctrl: bootstrapXtables, view: bootstrap-tables.html"
    messages = []

    rows_tbootstrapXtables0= db(db.tbootstrapXtables0).select()
    rows_tbootstrapXtables1= db(db.tbootstrapXtables1).select()
    dfbootstrapXtables0_row= None
    id_dfbootstrapXtables0 = None
    fbootstrapXtables0= Form(db.dfbootstrapXtables0, id, deletable=False, dbio = False, keep_values = False, form_name = "fbootstrapXtables0",  formstyle=FormStyleBulma )
   
    if fbootstrapXtables0.accepted:

        Glb['debug'] and print("     fbootstrapXtables0 accepted with: %s " % (fbootstrapXtables0.vars))
        fbootstrapXtables0_f0 = fbootstrapXtables0.vars.get('f0','')
        if len ( fbootstrapXtables0_f0 ):
            id_dfbootstrapXtables0 = db.dfbootstrapXtables0.insert( **fbootstrapXtables0.vars )
            db.commit()

            if not id_dfbootstrapXtables0 is None:
                dfbootstrapXtables0_row = db.dfbootstrapXtables0(id_dfbootstrapXtables0 )

                if not dfbootstrapXtables0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fbootstrapXtables0.vars.f0}\" into db.dfbootstrapXtables0.f0, id = {id_dfbootstrapXtables0}' )
                         print(f"     found db.dfbootstrapXtables0.f0: \"{dfbootstrapXtables0_row.f0}\", id = {id_dfbootstrapXtables0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fbootstrapXtables0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fbootstrapXtables0.vars.items() ]
                print()
   
    elif fbootstrapXtables0.errors:
        print("fbootstrapXtables0 has errors: %s " % (fbootstrapXtables0.errors))
 

    return locals()


@action('buttons', method=["GET", "POST"] )
@action.uses(Template('buttons.html', delimiters='[%[ ]]',), db, session,  T, )

def buttons(id=None):
    ctrl_info= "ctrl: buttons, view: buttons.html"
    messages = []

    dfbuttons0_row= None
    id_dfbuttons0 = None
    fbuttons0= Form(db.dfbuttons0, id, deletable=False, dbio = False, keep_values = False, form_name = "fbuttons0",  formstyle=FormStyleBulma )
   
    if fbuttons0.accepted:

        Glb['debug'] and print("     fbuttons0 accepted with: %s " % (fbuttons0.vars))
        fbuttons0_f0 = fbuttons0.vars.get('f0','')
        if len ( fbuttons0_f0 ):
            id_dfbuttons0 = db.dfbuttons0.insert( **fbuttons0.vars )
            db.commit()

            if not id_dfbuttons0 is None:
                dfbuttons0_row = db.dfbuttons0(id_dfbuttons0 )

                if not dfbuttons0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fbuttons0.vars.f0}\" into db.dfbuttons0.f0, id = {id_dfbuttons0}' )
                         print(f"     found db.dfbuttons0.f0: \"{dfbuttons0_row.f0}\", id = {id_dfbuttons0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fbuttons0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fbuttons0.vars.items() ]
                print()
   
    elif fbuttons0.errors:
        print("fbuttons0 has errors: %s " % (fbuttons0.errors))
 

    return locals()


@action('notifications', method=["GET", "POST"] )
@action.uses(Template('notifications.html', delimiters='[%[ ]]',), db, session,  T, )

def notifications(id=None):
    ctrl_info= "ctrl: notifications, view: notifications.html"
    messages = []

    dfnotifications0_row= None
    id_dfnotifications0 = None
    fnotifications0= Form(db.dfnotifications0, id, deletable=False, dbio = False, keep_values = False, form_name = "fnotifications0",  formstyle=FormStyleBulma )
   
    if fnotifications0.accepted:

        Glb['debug'] and print("     fnotifications0 accepted with: %s " % (fnotifications0.vars))
        fnotifications0_f0 = fnotifications0.vars.get('f0','')
        if len ( fnotifications0_f0 ):
            id_dfnotifications0 = db.dfnotifications0.insert( **fnotifications0.vars )
            db.commit()

            if not id_dfnotifications0 is None:
                dfnotifications0_row = db.dfnotifications0(id_dfnotifications0 )

                if not dfnotifications0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnotifications0.vars.f0}\" into db.dfnotifications0.f0, id = {id_dfnotifications0}' )
                         print(f"     found db.dfnotifications0.f0: \"{dfnotifications0_row.f0}\", id = {id_dfnotifications0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fnotifications0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fnotifications0.vars.items() ]
                print()
   
    elif fnotifications0.errors:
        print("fnotifications0 has errors: %s " % (fnotifications0.errors))
 

    return locals()


@action('forms', method=["GET", "POST"] )
@action.uses(Template('forms.html', delimiters='[%[ ]]',), db, session,  T, )

def forms(id=None):
    ctrl_info= "ctrl: forms, view: forms.html"
    messages = []

    dfforms0_row= None
    id_dfforms0 = None
    fforms0= Form(db.dfforms0, id, deletable=False, dbio = False, keep_values = False, form_name = "fforms0",  formstyle=FormStyleBulma )
   
    if fforms0.accepted:

        Glb['debug'] and print("     fforms0 accepted with: %s " % (fforms0.vars))
        fforms0_f0 = fforms0.vars.get('f0','')
        if len ( fforms0_f0 ):
            id_dfforms0 = db.dfforms0.insert( **fforms0.vars )
            db.commit()

            if not id_dfforms0 is None:
                dfforms0_row = db.dfforms0(id_dfforms0 )

                if not dfforms0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fforms0.vars.f0}\" into db.dfforms0.f0, id = {id_dfforms0}' )
                         print(f"     found db.dfforms0.f0: \"{dfforms0_row.f0}\", id = {id_dfforms0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fforms0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fforms0.vars.items() ]
                print()
   
    elif fforms0.errors:
        print("fforms0 has errors: %s " % (fforms0.errors))
 

    return locals()


@action('modals', method=["GET", "POST"] )
@action.uses(Template('modals.html', delimiters='[%[ ]]',), db, session,  T, )

def modals(id=None):
    ctrl_info= "ctrl: modals, view: modals.html"
    messages = []

    dfmodals0_row= None
    id_dfmodals0 = None
    fmodals0= Form(db.dfmodals0, id, deletable=False, dbio = False, keep_values = False, form_name = "fmodals0",  formstyle=FormStyleBulma )
   
    if fmodals0.accepted:

        Glb['debug'] and print("     fmodals0 accepted with: %s " % (fmodals0.vars))
        fmodals0_f0 = fmodals0.vars.get('f0','')
        if len ( fmodals0_f0 ):
            id_dfmodals0 = db.dfmodals0.insert( **fmodals0.vars )
            db.commit()

            if not id_dfmodals0 is None:
                dfmodals0_row = db.dfmodals0(id_dfmodals0 )

                if not dfmodals0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmodals0.vars.f0}\" into db.dfmodals0.f0, id = {id_dfmodals0}' )
                         print(f"     found db.dfmodals0.f0: \"{dfmodals0_row.f0}\", id = {id_dfmodals0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmodals0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmodals0.vars.items() ]
                print()
   
    elif fmodals0.errors:
        print("fmodals0 has errors: %s " % (fmodals0.errors))
 

    dfmodals1_row= None
    id_dfmodals1 = None
    fmodals1= Form(db.dfmodals1, id, deletable=False, dbio = False, keep_values = False, form_name = "fmodals1",  formstyle=FormStyleBulma )
   
    if fmodals1.accepted:

        Glb['debug'] and print("     fmodals1 accepted with: %s " % (fmodals1.vars))
        fmodals1_f0 = fmodals1.vars.get('f0','')
        if len ( fmodals1_f0 ):
            id_dfmodals1 = db.dfmodals1.insert( **fmodals1.vars )
            db.commit()

            if not id_dfmodals1 is None:
                dfmodals1_row = db.dfmodals1(id_dfmodals1 )

                if not dfmodals1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmodals1.vars.f0}\" into db.dfmodals1.f0, id = {id_dfmodals1}' )
                         print(f"     found db.dfmodals1.f0: \"{dfmodals1_row.f0}\", id = {id_dfmodals1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmodals1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmodals1.vars.items() ]
                print()
   
    elif fmodals1.errors:
        print("fmodals1 has errors: %s " % (fmodals1.errors))
 

    dfmodals2_row= None
    id_dfmodals2 = None
    fmodals2= Form(db.dfmodals2, id, deletable=False, dbio = False, keep_values = False, form_name = "fmodals2",  formstyle=FormStyleBulma )
   
    if fmodals2.accepted:

        Glb['debug'] and print("     fmodals2 accepted with: %s " % (fmodals2.vars))
        fmodals2_f0 = fmodals2.vars.get('f0','')
        if len ( fmodals2_f0 ):
            id_dfmodals2 = db.dfmodals2.insert( **fmodals2.vars )
            db.commit()

            if not id_dfmodals2 is None:
                dfmodals2_row = db.dfmodals2(id_dfmodals2 )

                if not dfmodals2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmodals2.vars.f0}\" into db.dfmodals2.f0, id = {id_dfmodals2}' )
                         print(f"     found db.dfmodals2.f0: \"{dfmodals2_row.f0}\", id = {id_dfmodals2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmodals2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmodals2.vars.items() ]
                print()
   
    elif fmodals2.errors:
        print("fmodals2 has errors: %s " % (fmodals2.errors))
 

    return locals()


@action('typography', method=["GET", "POST"] )
@action.uses(Template('typography.html', delimiters='[%[ ]]',), db, session,  T, )

def typography(id=None):
    ctrl_info= "ctrl: typography, view: typography.html"
    messages = []

    dftypography0_row= None
    id_dftypography0 = None
    ftypography0= Form(db.dftypography0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftypography0",  formstyle=FormStyleBulma )
   
    if ftypography0.accepted:

        Glb['debug'] and print("     ftypography0 accepted with: %s " % (ftypography0.vars))
        ftypography0_f0 = ftypography0.vars.get('f0','')
        if len ( ftypography0_f0 ):
            id_dftypography0 = db.dftypography0.insert( **ftypography0.vars )
            db.commit()

            if not id_dftypography0 is None:
                dftypography0_row = db.dftypography0(id_dftypography0 )

                if not dftypography0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftypography0.vars.f0}\" into db.dftypography0.f0, id = {id_dftypography0}' )
                         print(f"     found db.dftypography0.f0: \"{dftypography0_row.f0}\", id = {id_dftypography0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftypography0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftypography0.vars.items() ]
                print()
   
    elif ftypography0.errors:
        print("ftypography0 has errors: %s " % (ftypography0.errors))
 

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

