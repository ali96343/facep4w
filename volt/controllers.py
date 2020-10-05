#!/usr/bin/env python3

import os
from py4web import action, request, abort, redirect, URL, Field
from yatl.helpers import A
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A
from py4web.core import Template

from .common import db, session, T, cache, authenticated, unauthenticated, auth

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)



@action('X404', method=["GET", "POST"] )
@action.uses(Template('404.html', delimiters='[%[ ]]',), db, session, T, )

def X404(id=None):
    ctrl_info= "ctrl: X404, view: 404.html"

    return locals()


@action('X500', method=["GET", "POST"] )
@action.uses(Template('500.html', delimiters='[%[ ]]',), db, session, T, )

def X500(id=None):
    ctrl_info= "ctrl: X500, view: 500.html"

    return locals()


@action('lock', method=["GET", "POST"] )
@action.uses(Template('lock.html', delimiters='[%[ ]]',), db, session, T, )

def lock(id=None):
    ctrl_info= "ctrl: lock, view: lock.html"

    dflock0_rows=''
    flock0= Form(db.dflock0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not flock0.vars is None:  
        flock0_f0 = flock0.vars.get('f0','')
        if len ( flock0_f0 ):
            db.dflock0.insert( **flock0.vars )
            dflock0_rows = db( db.dflock0 ).select()
            print (f'insert: \"{flock0.vars.f0}\" in db.dflock0.f0; dflock0: {len(dflock0_rows)} rows' )

    return locals()


@action('forms', method=["GET", "POST"] )
@action.uses(Template('forms.html', delimiters='[%[ ]]',), db, session, T, )

def forms(id=None):
    ctrl_info= "ctrl: forms, view: forms.html"

    dfforms0_rows=''
    fforms0= Form(db.dfforms0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fforms0.vars is None:  
        fforms0_f0 = fforms0.vars.get('f0','')
        if len ( fforms0_f0 ):
            db.dfforms0.insert( **fforms0.vars )
            dfforms0_rows = db( db.dfforms0 ).select()
            print (f'insert: \"{fforms0.vars.f0}\" in db.dfforms0.f0; dfforms0: {len(dfforms0_rows)} rows' )

    return locals()


@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T, )

def index(id=None):
    ctrl_info= "ctrl: index, view: index.html"

    dfindex0_rows=''
    findex0= Form(db.dfindex0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex0.vars is None:  
        findex0_f0 = findex0.vars.get('f0','')
        if len ( findex0_f0 ):
            db.dfindex0.insert( **findex0.vars )
            dfindex0_rows = db( db.dfindex0 ).select()
            print (f'insert: \"{findex0.vars.f0}\" in db.dfindex0.f0; dfindex0: {len(dfindex0_rows)} rows' )

    return locals()


@action('modals', method=["GET", "POST"] )
@action.uses(Template('modals.html', delimiters='[%[ ]]',), db, session, T, )

def modals(id=None):
    ctrl_info= "ctrl: modals, view: modals.html"

    dfmodals0_rows=''
    fmodals0= Form(db.dfmodals0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fmodals0.vars is None:  
        fmodals0_f0 = fmodals0.vars.get('f0','')
        if len ( fmodals0_f0 ):
            db.dfmodals0.insert( **fmodals0.vars )
            dfmodals0_rows = db( db.dfmodals0 ).select()
            print (f'insert: \"{fmodals0.vars.f0}\" in db.dfmodals0.f0; dfmodals0: {len(dfmodals0_rows)} rows' )

    dfmodals1_rows=''
    fmodals1= Form(db.dfmodals1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fmodals1.vars is None:  
        fmodals1_f0 = fmodals1.vars.get('f0','')
        if len ( fmodals1_f0 ):
            db.dfmodals1.insert( **fmodals1.vars )
            dfmodals1_rows = db( db.dfmodals1 ).select()
            print (f'insert: \"{fmodals1.vars.f0}\" in db.dfmodals1.f0; dfmodals1: {len(dfmodals1_rows)} rows' )

    dfmodals2_rows=''
    fmodals2= Form(db.dfmodals2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fmodals2.vars is None:  
        fmodals2_f0 = fmodals2.vars.get('f0','')
        if len ( fmodals2_f0 ):
            db.dfmodals2.insert( **fmodals2.vars )
            dfmodals2_rows = db( db.dfmodals2 ).select()
            print (f'insert: \"{fmodals2.vars.f0}\" in db.dfmodals2.f0; dfmodals2: {len(dfmodals2_rows)} rows' )

    return locals()


@action('buttons', method=["GET", "POST"] )
@action.uses(Template('buttons.html', delimiters='[%[ ]]',), db, session, T, )

def buttons(id=None):
    ctrl_info= "ctrl: buttons, view: buttons.html"

    dfbuttons0_rows=''
    fbuttons0= Form(db.dfbuttons0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fbuttons0.vars is None:  
        fbuttons0_f0 = fbuttons0.vars.get('f0','')
        if len ( fbuttons0_f0 ):
            db.dfbuttons0.insert( **fbuttons0.vars )
            dfbuttons0_rows = db( db.dfbuttons0 ).select()
            print (f'insert: \"{fbuttons0.vars.f0}\" in db.dfbuttons0.f0; dfbuttons0: {len(dfbuttons0_rows)} rows' )

    return locals()


@action('signXup', method=["GET", "POST"] )
@action.uses(Template('sign-up.html', delimiters='[%[ ]]',), db, session, T, )

def signXup(id=None):
    ctrl_info= "ctrl: signXup, view: sign-up.html"

    dfsignXup0_rows=''
    fsignXup0= Form(db.dfsignXup0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fsignXup0.vars is None:  
        fsignXup0_f0 = fsignXup0.vars.get('f0','')
        if len ( fsignXup0_f0 ):
            db.dfsignXup0.insert( **fsignXup0.vars )
            dfsignXup0_rows = db( db.dfsignXup0 ).select()
            print (f'insert: \"{fsignXup0.vars.f0}\" in db.dfsignXup0.f0; dfsignXup0: {len(dfsignXup0_rows)} rows' )

    return locals()


@action('signXin', method=["GET", "POST"] )
@action.uses(Template('sign-in.html', delimiters='[%[ ]]',), db, session, T, )

def signXin(id=None):
    ctrl_info= "ctrl: signXin, view: sign-in.html"

    dfsignXin0_rows=''
    fsignXin0= Form(db.dfsignXin0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fsignXin0.vars is None:  
        fsignXin0_f0 = fsignXin0.vars.get('f0','')
        if len ( fsignXin0_f0 ):
            db.dfsignXin0.insert( **fsignXin0.vars )
            dfsignXin0_rows = db( db.dfsignXin0 ).select()
            print (f'insert: \"{fsignXin0.vars.f0}\" in db.dfsignXin0.f0; dfsignXin0: {len(dfsignXin0_rows)} rows' )

    return locals()


@action('settings', method=["GET", "POST"] )
@action.uses(Template('settings.html', delimiters='[%[ ]]',), db, session, T, )

def settings(id=None):
    ctrl_info= "ctrl: settings, view: settings.html"

    dfsettings0_rows=''
    fsettings0= Form(db.dfsettings0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fsettings0.vars is None:  
        fsettings0_f0 = fsettings0.vars.get('f0','')
        if len ( fsettings0_f0 ):
            db.dfsettings0.insert( **fsettings0.vars )
            dfsettings0_rows = db( db.dfsettings0 ).select()
            print (f'insert: \"{fsettings0.vars.f0}\" in db.dfsettings0.f0; dfsettings0: {len(dfsettings0_rows)} rows' )

    dfsettings1_rows=''
    fsettings1= Form(db.dfsettings1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fsettings1.vars is None:  
        fsettings1_f0 = fsettings1.vars.get('f0','')
        if len ( fsettings1_f0 ):
            db.dfsettings1.insert( **fsettings1.vars )
            dfsettings1_rows = db( db.dfsettings1 ).select()
            print (f'insert: \"{fsettings1.vars.f0}\" in db.dfsettings1.f0; dfsettings1: {len(dfsettings1_rows)} rows' )

    return locals()


@action('dashboard', method=["GET", "POST"] )
@action.uses(Template('dashboard.html', delimiters='[%[ ]]',), db, session, T, )

def dashboard(id=None):
    ctrl_info= "ctrl: dashboard, view: dashboard.html"

    rows_tdashboard0= db(db.tdashboard0).select()
    dfdashboard0_rows=''
    fdashboard0= Form(db.dfdashboard0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fdashboard0.vars is None:  
        fdashboard0_f0 = fdashboard0.vars.get('f0','')
        if len ( fdashboard0_f0 ):
            db.dfdashboard0.insert( **fdashboard0.vars )
            dfdashboard0_rows = db( db.dfdashboard0 ).select()
            print (f'insert: \"{fdashboard0.vars.f0}\" in db.dfdashboard0.f0; dfdashboard0: {len(dfdashboard0_rows)} rows' )

    return locals()


@action('typography', method=["GET", "POST"] )
@action.uses(Template('typography.html', delimiters='[%[ ]]',), db, session, T, )

def typography(id=None):
    ctrl_info= "ctrl: typography, view: typography.html"

    dftypography0_rows=''
    ftypography0= Form(db.dftypography0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftypography0.vars is None:  
        ftypography0_f0 = ftypography0.vars.get('f0','')
        if len ( ftypography0_f0 ):
            db.dftypography0.insert( **ftypography0.vars )
            dftypography0_rows = db( db.dftypography0 ).select()
            print (f'insert: \"{ftypography0.vars.f0}\" in db.dftypography0.f0; dftypography0: {len(dftypography0_rows)} rows' )

    return locals()


@action('transactions', method=["GET", "POST"] )
@action.uses(Template('transactions.html', delimiters='[%[ ]]',), db, session, T, )

def transactions(id=None):
    ctrl_info= "ctrl: transactions, view: transactions.html"

    rows_ttransactions0= db(db.ttransactions0).select()
    dftransactions0_rows=''
    ftransactions0= Form(db.dftransactions0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftransactions0.vars is None:  
        ftransactions0_f0 = ftransactions0.vars.get('f0','')
        if len ( ftransactions0_f0 ):
            db.dftransactions0.insert( **ftransactions0.vars )
            dftransactions0_rows = db( db.dftransactions0 ).select()
            print (f'insert: \"{ftransactions0.vars.f0}\" in db.dftransactions0.f0; dftransactions0: {len(dftransactions0_rows)} rows' )

    return locals()


@action('notifications', method=["GET", "POST"] )
@action.uses(Template('notifications.html', delimiters='[%[ ]]',), db, session, T, )

def notifications(id=None):
    ctrl_info= "ctrl: notifications, view: notifications.html"

    dfnotifications0_rows=''
    fnotifications0= Form(db.dfnotifications0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fnotifications0.vars is None:  
        fnotifications0_f0 = fnotifications0.vars.get('f0','')
        if len ( fnotifications0_f0 ):
            db.dfnotifications0.insert( **fnotifications0.vars )
            dfnotifications0_rows = db( db.dfnotifications0 ).select()
            print (f'insert: \"{fnotifications0.vars.f0}\" in db.dfnotifications0.f0; dfnotifications0: {len(dfnotifications0_rows)} rows' )

    return locals()


@action('resetXpassword', method=["GET", "POST"] )
@action.uses(Template('reset-password.html', delimiters='[%[ ]]',), db, session, T, )

def resetXpassword(id=None):
    ctrl_info= "ctrl: resetXpassword, view: reset-password.html"

    dfresetXpassword0_rows=''
    fresetXpassword0= Form(db.dfresetXpassword0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fresetXpassword0.vars is None:  
        fresetXpassword0_f0 = fresetXpassword0.vars.get('f0','')
        if len ( fresetXpassword0_f0 ):
            db.dfresetXpassword0.insert( **fresetXpassword0.vars )
            dfresetXpassword0_rows = db( db.dfresetXpassword0 ).select()
            print (f'insert: \"{fresetXpassword0.vars.f0}\" in db.dfresetXpassword0.f0; dfresetXpassword0: {len(dfresetXpassword0_rows)} rows' )

    return locals()


@action('forgotXpassword', method=["GET", "POST"] )
@action.uses(Template('forgot-password.html', delimiters='[%[ ]]',), db, session, T, )

def forgotXpassword(id=None):
    ctrl_info= "ctrl: forgotXpassword, view: forgot-password.html"

    dfforgotXpassword0_rows=''
    fforgotXpassword0= Form(db.dfforgotXpassword0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fforgotXpassword0.vars is None:  
        fforgotXpassword0_f0 = fforgotXpassword0.vars.get('f0','')
        if len ( fforgotXpassword0_f0 ):
            db.dfforgotXpassword0.insert( **fforgotXpassword0.vars )
            dfforgotXpassword0_rows = db( db.dfforgotXpassword0 ).select()
            print (f'insert: \"{fforgotXpassword0.vars.f0}\" in db.dfforgotXpassword0.f0; dfforgotXpassword0: {len(dfforgotXpassword0_rows)} rows' )

    return locals()


@action('bootstrapXtables', method=["GET", "POST"] )
@action.uses(Template('bootstrap-tables.html', delimiters='[%[ ]]',), db, session, T, )

def bootstrapXtables(id=None):
    ctrl_info= "ctrl: bootstrapXtables, view: bootstrap-tables.html"

    rows_tbootstrapXtables0= db(db.tbootstrapXtables0).select()
    rows_tbootstrapXtables1= db(db.tbootstrapXtables1).select()
    dfbootstrapXtables0_rows=''
    fbootstrapXtables0= Form(db.dfbootstrapXtables0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fbootstrapXtables0.vars is None:  
        fbootstrapXtables0_f0 = fbootstrapXtables0.vars.get('f0','')
        if len ( fbootstrapXtables0_f0 ):
            db.dfbootstrapXtables0.insert( **fbootstrapXtables0.vars )
            dfbootstrapXtables0_rows = db( db.dfbootstrapXtables0 ).select()
            print (f'insert: \"{fbootstrapXtables0.vars.f0}\" in db.dfbootstrapXtables0.f0; dfbootstrapXtables0: {len(dfbootstrapXtables0_rows)} rows' )

    return locals()


from pydal.restapi import RestAPI, Policy

policy = Policy()

policy.set('*', 'GET', authorize=True, allowed_patterns=['*'])
policy.set('*', 'PUT', authorize=True)
policy.set('*', 'POST', authorize=True)
policy.set('*', 'DELETE', authorize=True)

@action('api/<tablename>/')
@action('api/<tablename>/<rec_id>')
def api(tablename, rec_id=None):
    return RestAPI(db, policy)(request.method, 
                               tablename, 
                               rec_id,
                               request.GET, 
                               request.POST
                               )
# /superheroes/rest/api/superhero?name.eq=Superman
