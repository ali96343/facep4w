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

    dfforms1_rows=''
    fforms1= Form(db.dfforms1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fforms1.vars is None:  
        fforms1_f0 = fforms1.vars.get('f0','')
        if len ( fforms1_f0 ):
            db.dfforms1.insert( **fforms1.vars )
            dfforms1_rows = db( db.dfforms1 ).select()
            print (f'insert: \"{fforms1.vars.f0}\" in db.dfforms1.f0; dfforms1: {len(dfforms1_rows)} rows' )

    dfforms2_rows=''
    fforms2= Form(db.dfforms2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fforms2.vars is None:  
        fforms2_f0 = fforms2.vars.get('f0','')
        if len ( fforms2_f0 ):
            db.dfforms2.insert( **fforms2.vars )
            dfforms2_rows = db( db.dfforms2 ).select()
            print (f'insert: \"{fforms2.vars.f0}\" in db.dfforms2.f0; dfforms2: {len(dfforms2_rows)} rows' )

    dfforms3_rows=''
    fforms3= Form(db.dfforms3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fforms3.vars is None:  
        fforms3_f0 = fforms3.vars.get('f0','')
        if len ( fforms3_f0 ):
            db.dfforms3.insert( **fforms3.vars )
            dfforms3_rows = db( db.dfforms3 ).select()
            print (f'insert: \"{fforms3.vars.f0}\" in db.dfforms3.f0; dfforms3: {len(dfforms3_rows)} rows' )

    dfforms4_rows=''
    fforms4= Form(db.dfforms4, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fforms4.vars is None:  
        fforms4_f0 = fforms4.vars.get('f0','')
        if len ( fforms4_f0 ):
            db.dfforms4.insert( **fforms4.vars )
            dfforms4_rows = db( db.dfforms4 ).select()
            print (f'insert: \"{fforms4.vars.f0}\" in db.dfforms4.f0; dfforms4: {len(dfforms4_rows)} rows' )

    dfforms5_rows=''
    fforms5= Form(db.dfforms5, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fforms5.vars is None:  
        fforms5_f0 = fforms5.vars.get('f0','')
        if len ( fforms5_f0 ):
            db.dfforms5.insert( **fforms5.vars )
            dfforms5_rows = db( db.dfforms5 ).select()
            print (f'insert: \"{fforms5.vars.f0}\" in db.dfforms5.f0; dfforms5: {len(dfforms5_rows)} rows' )

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
    rows_ttables1= db(db.ttables1).select()
    rows_ttables2= db(db.ttables2).select()
    rows_ttables3= db(db.ttables3).select()
    dftables0_rows=''
    ftables0= Form(db.dftables0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables0.vars is None:  
        ftables0_f0 = ftables0.vars.get('f0','')
        if len ( ftables0_f0 ):
            db.dftables0.insert( **ftables0.vars )
            dftables0_rows = db( db.dftables0 ).select()
            print (f'insert: \"{ftables0.vars.f0}\" in db.dftables0.f0; dftables0: {len(dftables0_rows)} rows' )

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
