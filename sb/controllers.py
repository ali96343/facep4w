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

    dfX4040_rows=''
    fX4040= Form(db.dfX4040, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fX4040.vars is None:  
        fX4040_f0 = fX4040.vars.get('f0','')
        if len ( fX4040_f0 ):
            db.dfX4040.insert( **fX4040.vars )
            dfX4040_rows = db( db.dfX4040 ).select()
            print (f'insert: \"{fX4040.vars.f0}\" in db.dfX4040.f0; dfX4040: {len(dfX4040_rows)} rows' )

    return locals()


@action('blank', method=["GET", "POST"] )
@action.uses(Template('blank.html', delimiters='[%[ ]]',), db, session, T, )

def blank(id=None):
    ctrl_info= "ctrl: blank, view: blank.html"

    dfblank0_rows=''
    fblank0= Form(db.dfblank0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fblank0.vars is None:  
        fblank0_f0 = fblank0.vars.get('f0','')
        if len ( fblank0_f0 ):
            db.dfblank0.insert( **fblank0.vars )
            dfblank0_rows = db( db.dfblank0 ).select()
            print (f'insert: \"{fblank0.vars.f0}\" in db.dfblank0.f0; dfblank0: {len(dfblank0_rows)} rows' )

    return locals()


@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T, )

def index(id=None):
    ctrl_info= "ctrl: index, view: index.html"

    rows_tindex0= db(db.tindex0).select()
    dfindex0_rows=''
    findex0= Form(db.dfindex0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex0.vars is None:  
        findex0_f0 = findex0.vars.get('f0','')
        if len ( findex0_f0 ):
            db.dfindex0.insert( **findex0.vars )
            dfindex0_rows = db( db.dfindex0 ).select()
            print (f'insert: \"{findex0.vars.f0}\" in db.dfindex0.f0; dfindex0: {len(dfindex0_rows)} rows' )

    return locals()


@action('login', method=["GET", "POST"] )
@action.uses(Template('login.html', delimiters='[%[ ]]',), db, session, T, )

def login(id=None):
    ctrl_info= "ctrl: login, view: login.html"

    dflogin0_rows=''
    flogin0= Form(db.dflogin0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not flogin0.vars is None:  
        flogin0_f0 = flogin0.vars.get('f0','')
        if len ( flogin0_f0 ):
            db.dflogin0.insert( **flogin0.vars )
            dflogin0_rows = db( db.dflogin0 ).select()
            print (f'insert: \"{flogin0.vars.f0}\" in db.dflogin0.f0; dflogin0: {len(dflogin0_rows)} rows' )

    return locals()


@action('charts', method=["GET", "POST"] )
@action.uses(Template('charts.html', delimiters='[%[ ]]',), db, session, T, )

def charts(id=None):
    ctrl_info= "ctrl: charts, view: charts.html"

    dfcharts0_rows=''
    fcharts0= Form(db.dfcharts0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcharts0.vars is None:  
        fcharts0_f0 = fcharts0.vars.get('f0','')
        if len ( fcharts0_f0 ):
            db.dfcharts0.insert( **fcharts0.vars )
            dfcharts0_rows = db( db.dfcharts0 ).select()
            print (f'insert: \"{fcharts0.vars.f0}\" in db.dfcharts0.f0; dfcharts0: {len(dfcharts0_rows)} rows' )

    return locals()


@action('tables', method=["GET", "POST"] )
@action.uses(Template('tables.html', delimiters='[%[ ]]',), db, session, T, )

def tables(id=None):
    ctrl_info= "ctrl: tables, view: tables.html"

    rows_ttables0= db(db.ttables0).select()
    dftables0_rows=''
    ftables0= Form(db.dftables0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables0.vars is None:  
        ftables0_f0 = ftables0.vars.get('f0','')
        if len ( ftables0_f0 ):
            db.dftables0.insert( **ftables0.vars )
            dftables0_rows = db( db.dftables0 ).select()
            print (f'insert: \"{ftables0.vars.f0}\" in db.dftables0.f0; dftables0: {len(dftables0_rows)} rows' )

    return locals()


@action('register', method=["GET", "POST"] )
@action.uses(Template('register.html', delimiters='[%[ ]]',), db, session, T, )

def register(id=None):
    ctrl_info= "ctrl: register, view: register.html"

    dfregister0_rows=''
    fregister0= Form(db.dfregister0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fregister0.vars is None:  
        fregister0_f0 = fregister0.vars.get('f0','')
        if len ( fregister0_f0 ):
            db.dfregister0.insert( **fregister0.vars )
            dfregister0_rows = db( db.dfregister0 ).select()
            print (f'insert: \"{fregister0.vars.f0}\" in db.dfregister0.f0; dfregister0: {len(dfregister0_rows)} rows' )

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
