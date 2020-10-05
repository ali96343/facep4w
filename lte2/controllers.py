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
            print (f'insert: \"{fX4040.vars.f0}\" in db.dfX4040; dfX4040: {len(dfX4040_rows)} rows' )

    dfX4041_rows=''
    fX4041= Form(db.dfX4041, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fX4041.vars is None:  
        fX4041_f0 = fX4041.vars.get('f0','')
        if len ( fX4041_f0 ):
            db.dfX4041.insert( **fX4041.vars )
            dfX4041_rows = db( db.dfX4041 ).select()
            print (f'insert: \"{fX4041.vars.f0}\" in db.dfX4041; dfX4041: {len(dfX4041_rows)} rows' )

    dfX4042_rows=''
    fX4042= Form(db.dfX4042, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fX4042.vars is None:  
        fX4042_f0 = fX4042.vars.get('f0','')
        if len ( fX4042_f0 ):
            db.dfX4042.insert( **fX4042.vars )
            dfX4042_rows = db( db.dfX4042 ).select()
            print (f'insert: \"{fX4042.vars.f0}\" in db.dfX4042; dfX4042: {len(dfX4042_rows)} rows' )

    return locals()


@action('X500', method=["GET", "POST"] )
@action.uses(Template('500.html', delimiters='[%[ ]]',), db, session, T, )

def X500(id=None):
    ctrl_info= "ctrl: X500, view: 500.html"

    dfX5000_rows=''
    fX5000= Form(db.dfX5000, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fX5000.vars is None:  
        fX5000_f0 = fX5000.vars.get('f0','')
        if len ( fX5000_f0 ):
            db.dfX5000.insert( **fX5000.vars )
            dfX5000_rows = db( db.dfX5000 ).select()
            print (f'insert: \"{fX5000.vars.f0}\" in db.dfX5000; dfX5000: {len(dfX5000_rows)} rows' )

    dfX5001_rows=''
    fX5001= Form(db.dfX5001, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fX5001.vars is None:  
        fX5001_f0 = fX5001.vars.get('f0','')
        if len ( fX5001_f0 ):
            db.dfX5001.insert( **fX5001.vars )
            dfX5001_rows = db( db.dfX5001 ).select()
            print (f'insert: \"{fX5001.vars.f0}\" in db.dfX5001; dfX5001: {len(dfX5001_rows)} rows' )

    dfX5002_rows=''
    fX5002= Form(db.dfX5002, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fX5002.vars is None:  
        fX5002_f0 = fX5002.vars.get('f0','')
        if len ( fX5002_f0 ):
            db.dfX5002.insert( **fX5002.vars )
            dfX5002_rows = db( db.dfX5002 ).select()
            print (f'insert: \"{fX5002.vars.f0}\" in db.dfX5002; dfX5002: {len(dfX5002_rows)} rows' )

    return locals()


@action('data', method=["GET", "POST"] )
@action.uses(Template('data.html', delimiters='[%[ ]]',), db, session, T, )

def data(id=None):
    ctrl_info= "ctrl: data, view: data.html"

    rows_tdata0= db(db.tdata0).select()
    rows_tdata1= db(db.tdata1).select()
    dfdata0_rows=''
    fdata0= Form(db.dfdata0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fdata0.vars is None:  
        fdata0_f0 = fdata0.vars.get('f0','')
        if len ( fdata0_f0 ):
            db.dfdata0.insert( **fdata0.vars )
            dfdata0_rows = db( db.dfdata0 ).select()
            print (f'insert: \"{fdata0.vars.f0}\" in db.dfdata0; dfdata0: {len(dfdata0_rows)} rows' )

    dfdata1_rows=''
    fdata1= Form(db.dfdata1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fdata1.vars is None:  
        fdata1_f0 = fdata1.vars.get('f0','')
        if len ( fdata1_f0 ):
            db.dfdata1.insert( **fdata1.vars )
            dfdata1_rows = db( db.dfdata1 ).select()
            print (f'insert: \"{fdata1.vars.f0}\" in db.dfdata1; dfdata1: {len(dfdata1_rows)} rows' )

    return locals()


@action('flot', method=["GET", "POST"] )
@action.uses(Template('flot.html', delimiters='[%[ ]]',), db, session, T, )

def flot(id=None):
    ctrl_info= "ctrl: flot, view: flot.html"

    dfflot0_rows=''
    fflot0= Form(db.dfflot0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fflot0.vars is None:  
        fflot0_f0 = fflot0.vars.get('f0','')
        if len ( fflot0_f0 ):
            db.dfflot0.insert( **fflot0.vars )
            dfflot0_rows = db( db.dfflot0 ).select()
            print (f'insert: \"{fflot0.vars.f0}\" in db.dfflot0; dfflot0: {len(dfflot0_rows)} rows' )

    dfflot1_rows=''
    fflot1= Form(db.dfflot1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fflot1.vars is None:  
        fflot1_f0 = fflot1.vars.get('f0','')
        if len ( fflot1_f0 ):
            db.dfflot1.insert( **fflot1.vars )
            dfflot1_rows = db( db.dfflot1 ).select()
            print (f'insert: \"{fflot1.vars.f0}\" in db.dfflot1; dfflot1: {len(dfflot1_rows)} rows' )

    return locals()


@action('pace', method=["GET", "POST"] )
@action.uses(Template('pace.html', delimiters='[%[ ]]',), db, session, T, )

def pace(id=None):
    ctrl_info= "ctrl: pace, view: pace.html"

    dfpace0_rows=''
    fpace0= Form(db.dfpace0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fpace0.vars is None:  
        fpace0_f0 = fpace0.vars.get('f0','')
        if len ( fpace0_f0 ):
            db.dfpace0.insert( **fpace0.vars )
            dfpace0_rows = db( db.dfpace0 ).select()
            print (f'insert: \"{fpace0.vars.f0}\" in db.dfpace0; dfpace0: {len(dfpace0_rows)} rows' )

    dfpace1_rows=''
    fpace1= Form(db.dfpace1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fpace1.vars is None:  
        fpace1_f0 = fpace1.vars.get('f0','')
        if len ( fpace1_f0 ):
            db.dfpace1.insert( **fpace1.vars )
            dfpace1_rows = db( db.dfpace1 ).select()
            print (f'insert: \"{fpace1.vars.f0}\" in db.dfpace1; dfpace1: {len(dfpace1_rows)} rows' )

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
            print (f'insert: \"{findex0.vars.f0}\" in db.dfindex0; dfindex0: {len(dfindex0_rows)} rows' )

    dfindex1_rows=''
    findex1= Form(db.dfindex1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex1.vars is None:  
        findex1_f0 = findex1.vars.get('f0','')
        if len ( findex1_f0 ):
            db.dfindex1.insert( **findex1.vars )
            dfindex1_rows = db( db.dfindex1 ).select()
            print (f'insert: \"{findex1.vars.f0}\" in db.dfindex1; dfindex1: {len(dfindex1_rows)} rows' )

    dfindex2_rows=''
    findex2= Form(db.dfindex2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex2.vars is None:  
        findex2_f0 = findex2.vars.get('f0','')
        if len ( findex2_f0 ):
            db.dfindex2.insert( **findex2.vars )
            dfindex2_rows = db( db.dfindex2 ).select()
            print (f'insert: \"{findex2.vars.f0}\" in db.dfindex2; dfindex2: {len(dfindex2_rows)} rows' )

    return locals()


@action('fixed', method=["GET", "POST"] )
@action.uses(Template('fixed.html', delimiters='[%[ ]]',), db, session, T, )

def fixed(id=None):
    ctrl_info= "ctrl: fixed, view: fixed.html"

    dffixed0_rows=''
    ffixed0= Form(db.dffixed0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ffixed0.vars is None:  
        ffixed0_f0 = ffixed0.vars.get('f0','')
        if len ( ffixed0_f0 ):
            db.dffixed0.insert( **ffixed0.vars )
            dffixed0_rows = db( db.dffixed0 ).select()
            print (f'insert: \"{ffixed0.vars.f0}\" in db.dffixed0; dffixed0: {len(dffixed0_rows)} rows' )

    dffixed1_rows=''
    ffixed1= Form(db.dffixed1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ffixed1.vars is None:  
        ffixed1_f0 = ffixed1.vars.get('f0','')
        if len ( ffixed1_f0 ):
            db.dffixed1.insert( **ffixed1.vars )
            dffixed1_rows = db( db.dffixed1 ).select()
            print (f'insert: \"{ffixed1.vars.f0}\" in db.dffixed1; dffixed1: {len(dffixed1_rows)} rows' )

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
            print (f'insert: \"{flogin0.vars.f0}\" in db.dflogin0; dflogin0: {len(dflogin0_rows)} rows' )

    return locals()


@action('icons', method=["GET", "POST"] )
@action.uses(Template('icons.html', delimiters='[%[ ]]',), db, session, T, )

def icons(id=None):
    ctrl_info= "ctrl: icons, view: icons.html"

    dficons0_rows=''
    ficons0= Form(db.dficons0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ficons0.vars is None:  
        ficons0_f0 = ficons0.vars.get('f0','')
        if len ( ficons0_f0 ):
            db.dficons0.insert( **ficons0.vars )
            dficons0_rows = db( db.dficons0 ).select()
            print (f'insert: \"{ficons0.vars.f0}\" in db.dficons0; dficons0: {len(dficons0_rows)} rows' )

    dficons1_rows=''
    ficons1= Form(db.dficons1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ficons1.vars is None:  
        ficons1_f0 = ficons1.vars.get('f0','')
        if len ( ficons1_f0 ):
            db.dficons1.insert( **ficons1.vars )
            dficons1_rows = db( db.dficons1 ).select()
            print (f'insert: \"{ficons1.vars.f0}\" in db.dficons1; dficons1: {len(dficons1_rows)} rows' )

    return locals()


@action('boxed', method=["GET", "POST"] )
@action.uses(Template('boxed.html', delimiters='[%[ ]]',), db, session, T, )

def boxed(id=None):
    ctrl_info= "ctrl: boxed, view: boxed.html"

    dfboxed0_rows=''
    fboxed0= Form(db.dfboxed0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fboxed0.vars is None:  
        fboxed0_f0 = fboxed0.vars.get('f0','')
        if len ( fboxed0_f0 ):
            db.dfboxed0.insert( **fboxed0.vars )
            dfboxed0_rows = db( db.dfboxed0 ).select()
            print (f'insert: \"{fboxed0.vars.f0}\" in db.dfboxed0; dfboxed0: {len(dfboxed0_rows)} rows' )

    dfboxed1_rows=''
    fboxed1= Form(db.dfboxed1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fboxed1.vars is None:  
        fboxed1_f0 = fboxed1.vars.get('f0','')
        if len ( fboxed1_f0 ):
            db.dfboxed1.insert( **fboxed1.vars )
            dfboxed1_rows = db( db.dfboxed1 ).select()
            print (f'insert: \"{fboxed1.vars.f0}\" in db.dfboxed1; dfboxed1: {len(dfboxed1_rows)} rows' )

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
            print (f'insert: \"{fblank0.vars.f0}\" in db.dfblank0; dfblank0: {len(dfblank0_rows)} rows' )

    dfblank1_rows=''
    fblank1= Form(db.dfblank1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fblank1.vars is None:  
        fblank1_f0 = fblank1.vars.get('f0','')
        if len ( fblank1_f0 ):
            db.dfblank1.insert( **fblank1.vars )
            dfblank1_rows = db( db.dfblank1 ).select()
            print (f'insert: \"{fblank1.vars.f0}\" in db.dfblank1; dfblank1: {len(dfblank1_rows)} rows' )

    return locals()


@action('index2', method=["GET", "POST"] )
@action.uses(Template('index2.html', delimiters='[%[ ]]',), db, session, T, )

def index2(id=None):
    ctrl_info= "ctrl: index2, view: index2.html"

    rows_tindex20= db(db.tindex20).select()
    dfindex20_rows=''
    findex20= Form(db.dfindex20, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex20.vars is None:  
        findex20_f0 = findex20.vars.get('f0','')
        if len ( findex20_f0 ):
            db.dfindex20.insert( **findex20.vars )
            dfindex20_rows = db( db.dfindex20 ).select()
            print (f'insert: \"{findex20.vars.f0}\" in db.dfindex20; dfindex20: {len(dfindex20_rows)} rows' )

    dfindex21_rows=''
    findex21= Form(db.dfindex21, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex21.vars is None:  
        findex21_f0 = findex21.vars.get('f0','')
        if len ( findex21_f0 ):
            db.dfindex21.insert( **findex21.vars )
            dfindex21_rows = db( db.dfindex21 ).select()
            print (f'insert: \"{findex21.vars.f0}\" in db.dfindex21; dfindex21: {len(dfindex21_rows)} rows' )

    dfindex22_rows=''
    findex22= Form(db.dfindex22, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex22.vars is None:  
        findex22_f0 = findex22.vars.get('f0','')
        if len ( findex22_f0 ):
            db.dfindex22.insert( **findex22.vars )
            dfindex22_rows = db( db.dfindex22 ).select()
            print (f'insert: \"{findex22.vars.f0}\" in db.dfindex22; dfindex22: {len(dfindex22_rows)} rows' )

    return locals()


@action('morris', method=["GET", "POST"] )
@action.uses(Template('morris.html', delimiters='[%[ ]]',), db, session, T, )

def morris(id=None):
    ctrl_info= "ctrl: morris, view: morris.html"

    dfmorris0_rows=''
    fmorris0= Form(db.dfmorris0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fmorris0.vars is None:  
        fmorris0_f0 = fmorris0.vars.get('f0','')
        if len ( fmorris0_f0 ):
            db.dfmorris0.insert( **fmorris0.vars )
            dfmorris0_rows = db( db.dfmorris0 ).select()
            print (f'insert: \"{fmorris0.vars.f0}\" in db.dfmorris0; dfmorris0: {len(dfmorris0_rows)} rows' )

    dfmorris1_rows=''
    fmorris1= Form(db.dfmorris1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fmorris1.vars is None:  
        fmorris1_f0 = fmorris1.vars.get('f0','')
        if len ( fmorris1_f0 ):
            db.dfmorris1.insert( **fmorris1.vars )
            dfmorris1_rows = db( db.dfmorris1 ).select()
            print (f'insert: \"{fmorris1.vars.f0}\" in db.dfmorris1; dfmorris1: {len(dfmorris1_rows)} rows' )

    return locals()


@action('simple', method=["GET", "POST"] )
@action.uses(Template('simple.html', delimiters='[%[ ]]',), db, session, T, )

def simple(id=None):
    ctrl_info= "ctrl: simple, view: simple.html"

    rows_tsimple0= db(db.tsimple0).select()
    rows_tsimple1= db(db.tsimple1).select()
    rows_tsimple2= db(db.tsimple2).select()
    rows_tsimple3= db(db.tsimple3).select()
    rows_tsimple4= db(db.tsimple4).select()
    dfsimple0_rows=''
    fsimple0= Form(db.dfsimple0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fsimple0.vars is None:  
        fsimple0_f0 = fsimple0.vars.get('f0','')
        if len ( fsimple0_f0 ):
            db.dfsimple0.insert( **fsimple0.vars )
            dfsimple0_rows = db( db.dfsimple0 ).select()
            print (f'insert: \"{fsimple0.vars.f0}\" in db.dfsimple0; dfsimple0: {len(dfsimple0_rows)} rows' )

    dfsimple1_rows=''
    fsimple1= Form(db.dfsimple1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fsimple1.vars is None:  
        fsimple1_f0 = fsimple1.vars.get('f0','')
        if len ( fsimple1_f0 ):
            db.dfsimple1.insert( **fsimple1.vars )
            dfsimple1_rows = db( db.dfsimple1 ).select()
            print (f'insert: \"{fsimple1.vars.f0}\" in db.dfsimple1; dfsimple1: {len(dfsimple1_rows)} rows' )

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
            print (f'insert: \"{fmodals0.vars.f0}\" in db.dfmodals0; dfmodals0: {len(dfmodals0_rows)} rows' )

    dfmodals1_rows=''
    fmodals1= Form(db.dfmodals1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fmodals1.vars is None:  
        fmodals1_f0 = fmodals1.vars.get('f0','')
        if len ( fmodals1_f0 ):
            db.dfmodals1.insert( **fmodals1.vars )
            dfmodals1_rows = db( db.dfmodals1 ).select()
            print (f'insert: \"{fmodals1.vars.f0}\" in db.dfmodals1; dfmodals1: {len(dfmodals1_rows)} rows' )

    return locals()


@action('inline', method=["GET", "POST"] )
@action.uses(Template('inline.html', delimiters='[%[ ]]',), db, session, T, )

def inline(id=None):
    ctrl_info= "ctrl: inline, view: inline.html"

    dfinline0_rows=''
    finline0= Form(db.dfinline0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not finline0.vars is None:  
        finline0_f0 = finline0.vars.get('f0','')
        if len ( finline0_f0 ):
            db.dfinline0.insert( **finline0.vars )
            dfinline0_rows = db( db.dfinline0 ).select()
            print (f'insert: \"{finline0.vars.f0}\" in db.dfinline0; dfinline0: {len(dfinline0_rows)} rows' )

    dfinline1_rows=''
    finline1= Form(db.dfinline1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not finline1.vars is None:  
        finline1_f0 = finline1.vars.get('f0','')
        if len ( finline1_f0 ):
            db.dfinline1.insert( **finline1.vars )
            dfinline1_rows = db( db.dfinline1 ).select()
            print (f'insert: \"{finline1.vars.f0}\" in db.dfinline1; dfinline1: {len(dfinline1_rows)} rows' )

    return locals()


@action('general', method=["GET", "POST"] )
@action.uses(Template('general.html', delimiters='[%[ ]]',), db, session, T, )

def general(id=None):
    ctrl_info= "ctrl: general, view: general.html"

    dfgeneral0_rows=''
    fgeneral0= Form(db.dfgeneral0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fgeneral0.vars is None:  
        fgeneral0_f0 = fgeneral0.vars.get('f0','')
        if len ( fgeneral0_f0 ):
            db.dfgeneral0.insert( **fgeneral0.vars )
            dfgeneral0_rows = db( db.dfgeneral0 ).select()
            print (f'insert: \"{fgeneral0.vars.f0}\" in db.dfgeneral0; dfgeneral0: {len(dfgeneral0_rows)} rows' )

    dfgeneral1_rows=''
    fgeneral1= Form(db.dfgeneral1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fgeneral1.vars is None:  
        fgeneral1_f0 = fgeneral1.vars.get('f0','')
        if len ( fgeneral1_f0 ):
            db.dfgeneral1.insert( **fgeneral1.vars )
            dfgeneral1_rows = db( db.dfgeneral1 ).select()
            print (f'insert: \"{fgeneral1.vars.f0}\" in db.dfgeneral1; dfgeneral1: {len(dfgeneral1_rows)} rows' )

    return locals()


@action('topXnav', method=["GET", "POST"] )
@action.uses(Template('top-nav.html', delimiters='[%[ ]]',), db, session, T, )

def topXnav(id=None):
    ctrl_info= "ctrl: topXnav, view: top-nav.html"

    dftopXnav0_rows=''
    ftopXnav0= Form(db.dftopXnav0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftopXnav0.vars is None:  
        ftopXnav0_f0 = ftopXnav0.vars.get('f0','')
        if len ( ftopXnav0_f0 ):
            db.dftopXnav0.insert( **ftopXnav0.vars )
            dftopXnav0_rows = db( db.dftopXnav0 ).select()
            print (f'insert: \"{ftopXnav0.vars.f0}\" in db.dftopXnav0; dftopXnav0: {len(dftopXnav0_rows)} rows' )

    return locals()


@action('widgets', method=["GET", "POST"] )
@action.uses(Template('widgets.html', delimiters='[%[ ]]',), db, session, T, )

def widgets(id=None):
    ctrl_info= "ctrl: widgets, view: widgets.html"

    dfwidgets0_rows=''
    fwidgets0= Form(db.dfwidgets0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets0.vars is None:  
        fwidgets0_f0 = fwidgets0.vars.get('f0','')
        if len ( fwidgets0_f0 ):
            db.dfwidgets0.insert( **fwidgets0.vars )
            dfwidgets0_rows = db( db.dfwidgets0 ).select()
            print (f'insert: \"{fwidgets0.vars.f0}\" in db.dfwidgets0; dfwidgets0: {len(dfwidgets0_rows)} rows' )

    dfwidgets1_rows=''
    fwidgets1= Form(db.dfwidgets1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets1.vars is None:  
        fwidgets1_f0 = fwidgets1.vars.get('f0','')
        if len ( fwidgets1_f0 ):
            db.dfwidgets1.insert( **fwidgets1.vars )
            dfwidgets1_rows = db( db.dfwidgets1 ).select()
            print (f'insert: \"{fwidgets1.vars.f0}\" in db.dfwidgets1; dfwidgets1: {len(dfwidgets1_rows)} rows' )

    dfwidgets2_rows=''
    fwidgets2= Form(db.dfwidgets2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets2.vars is None:  
        fwidgets2_f0 = fwidgets2.vars.get('f0','')
        if len ( fwidgets2_f0 ):
            db.dfwidgets2.insert( **fwidgets2.vars )
            dfwidgets2_rows = db( db.dfwidgets2 ).select()
            print (f'insert: \"{fwidgets2.vars.f0}\" in db.dfwidgets2; dfwidgets2: {len(dfwidgets2_rows)} rows' )

    dfwidgets3_rows=''
    fwidgets3= Form(db.dfwidgets3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets3.vars is None:  
        fwidgets3_f0 = fwidgets3.vars.get('f0','')
        if len ( fwidgets3_f0 ):
            db.dfwidgets3.insert( **fwidgets3.vars )
            dfwidgets3_rows = db( db.dfwidgets3 ).select()
            print (f'insert: \"{fwidgets3.vars.f0}\" in db.dfwidgets3; dfwidgets3: {len(dfwidgets3_rows)} rows' )

    dfwidgets4_rows=''
    fwidgets4= Form(db.dfwidgets4, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets4.vars is None:  
        fwidgets4_f0 = fwidgets4.vars.get('f0','')
        if len ( fwidgets4_f0 ):
            db.dfwidgets4.insert( **fwidgets4.vars )
            dfwidgets4_rows = db( db.dfwidgets4 ).select()
            print (f'insert: \"{fwidgets4.vars.f0}\" in db.dfwidgets4; dfwidgets4: {len(dfwidgets4_rows)} rows' )

    dfwidgets5_rows=''
    fwidgets5= Form(db.dfwidgets5, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets5.vars is None:  
        fwidgets5_f0 = fwidgets5.vars.get('f0','')
        if len ( fwidgets5_f0 ):
            db.dfwidgets5.insert( **fwidgets5.vars )
            dfwidgets5_rows = db( db.dfwidgets5 ).select()
            print (f'insert: \"{fwidgets5.vars.f0}\" in db.dfwidgets5; dfwidgets5: {len(dfwidgets5_rows)} rows' )

    dfwidgets6_rows=''
    fwidgets6= Form(db.dfwidgets6, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets6.vars is None:  
        fwidgets6_f0 = fwidgets6.vars.get('f0','')
        if len ( fwidgets6_f0 ):
            db.dfwidgets6.insert( **fwidgets6.vars )
            dfwidgets6_rows = db( db.dfwidgets6 ).select()
            print (f'insert: \"{fwidgets6.vars.f0}\" in db.dfwidgets6; dfwidgets6: {len(dfwidgets6_rows)} rows' )

    dfwidgets7_rows=''
    fwidgets7= Form(db.dfwidgets7, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets7.vars is None:  
        fwidgets7_f0 = fwidgets7.vars.get('f0','')
        if len ( fwidgets7_f0 ):
            db.dfwidgets7.insert( **fwidgets7.vars )
            dfwidgets7_rows = db( db.dfwidgets7 ).select()
            print (f'insert: \"{fwidgets7.vars.f0}\" in db.dfwidgets7; dfwidgets7: {len(dfwidgets7_rows)} rows' )

    return locals()


@action('profile', method=["GET", "POST"] )
@action.uses(Template('profile.html', delimiters='[%[ ]]',), db, session, T, )

def profile(id=None):
    ctrl_info= "ctrl: profile, view: profile.html"

    dfprofile0_rows=''
    fprofile0= Form(db.dfprofile0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprofile0.vars is None:  
        fprofile0_f0 = fprofile0.vars.get('f0','')
        if len ( fprofile0_f0 ):
            db.dfprofile0.insert( **fprofile0.vars )
            dfprofile0_rows = db( db.dfprofile0 ).select()
            print (f'insert: \"{fprofile0.vars.f0}\" in db.dfprofile0; dfprofile0: {len(dfprofile0_rows)} rows' )

    dfprofile1_rows=''
    fprofile1= Form(db.dfprofile1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprofile1.vars is None:  
        fprofile1_f0 = fprofile1.vars.get('f0','')
        if len ( fprofile1_f0 ):
            db.dfprofile1.insert( **fprofile1.vars )
            dfprofile1_rows = db( db.dfprofile1 ).select()
            print (f'insert: \"{fprofile1.vars.f0}\" in db.dfprofile1; dfprofile1: {len(dfprofile1_rows)} rows' )

    dfprofile2_rows=''
    fprofile2= Form(db.dfprofile2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprofile2.vars is None:  
        fprofile2_f0 = fprofile2.vars.get('f0','')
        if len ( fprofile2_f0 ):
            db.dfprofile2.insert( **fprofile2.vars )
            dfprofile2_rows = db( db.dfprofile2 ).select()
            print (f'insert: \"{fprofile2.vars.f0}\" in db.dfprofile2; dfprofile2: {len(dfprofile2_rows)} rows' )

    dfprofile3_rows=''
    fprofile3= Form(db.dfprofile3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprofile3.vars is None:  
        fprofile3_f0 = fprofile3.vars.get('f0','')
        if len ( fprofile3_f0 ):
            db.dfprofile3.insert( **fprofile3.vars )
            dfprofile3_rows = db( db.dfprofile3 ).select()
            print (f'insert: \"{fprofile3.vars.f0}\" in db.dfprofile3; dfprofile3: {len(dfprofile3_rows)} rows' )

    return locals()


@action('sliders', method=["GET", "POST"] )
@action.uses(Template('sliders.html', delimiters='[%[ ]]',), db, session, T, )

def sliders(id=None):
    ctrl_info= "ctrl: sliders, view: sliders.html"

    dfsliders0_rows=''
    fsliders0= Form(db.dfsliders0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fsliders0.vars is None:  
        fsliders0_f0 = fsliders0.vars.get('f0','')
        if len ( fsliders0_f0 ):
            db.dfsliders0.insert( **fsliders0.vars )
            dfsliders0_rows = db( db.dfsliders0 ).select()
            print (f'insert: \"{fsliders0.vars.f0}\" in db.dfsliders0; dfsliders0: {len(dfsliders0_rows)} rows' )

    dfsliders1_rows=''
    fsliders1= Form(db.dfsliders1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fsliders1.vars is None:  
        fsliders1_f0 = fsliders1.vars.get('f0','')
        if len ( fsliders1_f0 ):
            db.dfsliders1.insert( **fsliders1.vars )
            dfsliders1_rows = db( db.dfsliders1 ).select()
            print (f'insert: \"{fsliders1.vars.f0}\" in db.dfsliders1; dfsliders1: {len(dfsliders1_rows)} rows' )

    return locals()


@action('mailbox', method=["GET", "POST"] )
@action.uses(Template('mailbox.html', delimiters='[%[ ]]',), db, session, T, )

def mailbox(id=None):
    ctrl_info= "ctrl: mailbox, view: mailbox.html"

    rows_tmailbox0= db(db.tmailbox0).select()
    dfmailbox0_rows=''
    fmailbox0= Form(db.dfmailbox0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fmailbox0.vars is None:  
        fmailbox0_f0 = fmailbox0.vars.get('f0','')
        if len ( fmailbox0_f0 ):
            db.dfmailbox0.insert( **fmailbox0.vars )
            dfmailbox0_rows = db( db.dfmailbox0 ).select()
            print (f'insert: \"{fmailbox0.vars.f0}\" in db.dfmailbox0; dfmailbox0: {len(dfmailbox0_rows)} rows' )

    dfmailbox1_rows=''
    fmailbox1= Form(db.dfmailbox1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fmailbox1.vars is None:  
        fmailbox1_f0 = fmailbox1.vars.get('f0','')
        if len ( fmailbox1_f0 ):
            db.dfmailbox1.insert( **fmailbox1.vars )
            dfmailbox1_rows = db( db.dfmailbox1 ).select()
            print (f'insert: \"{fmailbox1.vars.f0}\" in db.dfmailbox1; dfmailbox1: {len(dfmailbox1_rows)} rows' )

    return locals()


@action('chartjs', method=["GET", "POST"] )
@action.uses(Template('chartjs.html', delimiters='[%[ ]]',), db, session, T, )

def chartjs(id=None):
    ctrl_info= "ctrl: chartjs, view: chartjs.html"

    dfchartjs0_rows=''
    fchartjs0= Form(db.dfchartjs0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fchartjs0.vars is None:  
        fchartjs0_f0 = fchartjs0.vars.get('f0','')
        if len ( fchartjs0_f0 ):
            db.dfchartjs0.insert( **fchartjs0.vars )
            dfchartjs0_rows = db( db.dfchartjs0 ).select()
            print (f'insert: \"{fchartjs0.vars.f0}\" in db.dfchartjs0; dfchartjs0: {len(dfchartjs0_rows)} rows' )

    dfchartjs1_rows=''
    fchartjs1= Form(db.dfchartjs1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fchartjs1.vars is None:  
        fchartjs1_f0 = fchartjs1.vars.get('f0','')
        if len ( fchartjs1_f0 ):
            db.dfchartjs1.insert( **fchartjs1.vars )
            dfchartjs1_rows = db( db.dfchartjs1 ).select()
            print (f'insert: \"{fchartjs1.vars.f0}\" in db.dfchartjs1; dfchartjs1: {len(dfchartjs1_rows)} rows' )

    return locals()


@action('editors', method=["GET", "POST"] )
@action.uses(Template('editors.html', delimiters='[%[ ]]',), db, session, T, )

def editors(id=None):
    ctrl_info= "ctrl: editors, view: editors.html"

    dfeditors0_rows=''
    feditors0= Form(db.dfeditors0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not feditors0.vars is None:  
        feditors0_f0 = feditors0.vars.get('f0','')
        if len ( feditors0_f0 ):
            db.dfeditors0.insert( **feditors0.vars )
            dfeditors0_rows = db( db.dfeditors0 ).select()
            print (f'insert: \"{feditors0.vars.f0}\" in db.dfeditors0; dfeditors0: {len(dfeditors0_rows)} rows' )

    dfeditors1_rows=''
    feditors1= Form(db.dfeditors1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not feditors1.vars is None:  
        feditors1_f0 = feditors1.vars.get('f0','')
        if len ( feditors1_f0 ):
            db.dfeditors1.insert( **feditors1.vars )
            dfeditors1_rows = db( db.dfeditors1 ).select()
            print (f'insert: \"{feditors1.vars.f0}\" in db.dfeditors1; dfeditors1: {len(dfeditors1_rows)} rows' )

    dfeditors2_rows=''
    feditors2= Form(db.dfeditors2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not feditors2.vars is None:  
        feditors2_f0 = feditors2.vars.get('f0','')
        if len ( feditors2_f0 ):
            db.dfeditors2.insert( **feditors2.vars )
            dfeditors2_rows = db( db.dfeditors2 ).select()
            print (f'insert: \"{feditors2.vars.f0}\" in db.dfeditors2; dfeditors2: {len(dfeditors2_rows)} rows' )

    dfeditors3_rows=''
    feditors3= Form(db.dfeditors3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not feditors3.vars is None:  
        feditors3_f0 = feditors3.vars.get('f0','')
        if len ( feditors3_f0 ):
            db.dfeditors3.insert( **feditors3.vars )
            dfeditors3_rows = db( db.dfeditors3 ).select()
            print (f'insert: \"{feditors3.vars.f0}\" in db.dfeditors3; dfeditors3: {len(dfeditors3_rows)} rows' )

    return locals()


@action('buttons', method=["GET", "POST"] )
@action.uses(Template('buttons.html', delimiters='[%[ ]]',), db, session, T, )

def buttons(id=None):
    ctrl_info= "ctrl: buttons, view: buttons.html"

    rows_tbuttons0= db(db.tbuttons0).select()
    rows_tbuttons1= db(db.tbuttons1).select()
    rows_tbuttons2= db(db.tbuttons2).select()
    dfbuttons0_rows=''
    fbuttons0= Form(db.dfbuttons0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fbuttons0.vars is None:  
        fbuttons0_f0 = fbuttons0.vars.get('f0','')
        if len ( fbuttons0_f0 ):
            db.dfbuttons0.insert( **fbuttons0.vars )
            dfbuttons0_rows = db( db.dfbuttons0 ).select()
            print (f'insert: \"{fbuttons0.vars.f0}\" in db.dfbuttons0; dfbuttons0: {len(dfbuttons0_rows)} rows' )

    dfbuttons1_rows=''
    fbuttons1= Form(db.dfbuttons1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fbuttons1.vars is None:  
        fbuttons1_f0 = fbuttons1.vars.get('f0','')
        if len ( fbuttons1_f0 ):
            db.dfbuttons1.insert( **fbuttons1.vars )
            dfbuttons1_rows = db( db.dfbuttons1 ).select()
            print (f'insert: \"{fbuttons1.vars.f0}\" in db.dfbuttons1; dfbuttons1: {len(dfbuttons1_rows)} rows' )

    return locals()


@action('compose', method=["GET", "POST"] )
@action.uses(Template('compose.html', delimiters='[%[ ]]',), db, session, T, )

def compose(id=None):
    ctrl_info= "ctrl: compose, view: compose.html"

    dfcompose0_rows=''
    fcompose0= Form(db.dfcompose0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcompose0.vars is None:  
        fcompose0_f0 = fcompose0.vars.get('f0','')
        if len ( fcompose0_f0 ):
            db.dfcompose0.insert( **fcompose0.vars )
            dfcompose0_rows = db( db.dfcompose0 ).select()
            print (f'insert: \"{fcompose0.vars.f0}\" in db.dfcompose0; dfcompose0: {len(dfcompose0_rows)} rows' )

    dfcompose1_rows=''
    fcompose1= Form(db.dfcompose1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcompose1.vars is None:  
        fcompose1_f0 = fcompose1.vars.get('f0','')
        if len ( fcompose1_f0 ):
            db.dfcompose1.insert( **fcompose1.vars )
            dfcompose1_rows = db( db.dfcompose1 ).select()
            print (f'insert: \"{fcompose1.vars.f0}\" in db.dfcompose1; dfcompose1: {len(dfcompose1_rows)} rows' )

    return locals()


@action('invoice', method=["GET", "POST"] )
@action.uses(Template('invoice.html', delimiters='[%[ ]]',), db, session, T, )

def invoice(id=None):
    ctrl_info= "ctrl: invoice, view: invoice.html"

    rows_tinvoice0= db(db.tinvoice0).select()
    rows_tinvoice1= db(db.tinvoice1).select()
    dfinvoice0_rows=''
    finvoice0= Form(db.dfinvoice0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not finvoice0.vars is None:  
        finvoice0_f0 = finvoice0.vars.get('f0','')
        if len ( finvoice0_f0 ):
            db.dfinvoice0.insert( **finvoice0.vars )
            dfinvoice0_rows = db( db.dfinvoice0 ).select()
            print (f'insert: \"{finvoice0.vars.f0}\" in db.dfinvoice0; dfinvoice0: {len(dfinvoice0_rows)} rows' )

    dfinvoice1_rows=''
    finvoice1= Form(db.dfinvoice1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not finvoice1.vars is None:  
        finvoice1_f0 = finvoice1.vars.get('f0','')
        if len ( finvoice1_f0 ):
            db.dfinvoice1.insert( **finvoice1.vars )
            dfinvoice1_rows = db( db.dfinvoice1 ).select()
            print (f'insert: \"{finvoice1.vars.f0}\" in db.dfinvoice1; dfinvoice1: {len(dfinvoice1_rows)} rows' )

    return locals()


@action('calendar', method=["GET", "POST"] )
@action.uses(Template('calendar.html', delimiters='[%[ ]]',), db, session, T, )

def calendar(id=None):
    ctrl_info= "ctrl: calendar, view: calendar.html"

    dfcalendar0_rows=''
    fcalendar0= Form(db.dfcalendar0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcalendar0.vars is None:  
        fcalendar0_f0 = fcalendar0.vars.get('f0','')
        if len ( fcalendar0_f0 ):
            db.dfcalendar0.insert( **fcalendar0.vars )
            dfcalendar0_rows = db( db.dfcalendar0 ).select()
            print (f'insert: \"{fcalendar0.vars.f0}\" in db.dfcalendar0; dfcalendar0: {len(dfcalendar0_rows)} rows' )

    dfcalendar1_rows=''
    fcalendar1= Form(db.dfcalendar1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcalendar1.vars is None:  
        fcalendar1_f0 = fcalendar1.vars.get('f0','')
        if len ( fcalendar1_f0 ):
            db.dfcalendar1.insert( **fcalendar1.vars )
            dfcalendar1_rows = db( db.dfcalendar1 ).select()
            print (f'insert: \"{fcalendar1.vars.f0}\" in db.dfcalendar1; dfcalendar1: {len(dfcalendar1_rows)} rows' )

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
            print (f'insert: \"{fregister0.vars.f0}\" in db.dfregister0; dfregister0: {len(dfregister0_rows)} rows' )

    return locals()


@action('timeline', method=["GET", "POST"] )
@action.uses(Template('timeline.html', delimiters='[%[ ]]',), db, session, T, )

def timeline(id=None):
    ctrl_info= "ctrl: timeline, view: timeline.html"

    dftimeline0_rows=''
    ftimeline0= Form(db.dftimeline0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftimeline0.vars is None:  
        ftimeline0_f0 = ftimeline0.vars.get('f0','')
        if len ( ftimeline0_f0 ):
            db.dftimeline0.insert( **ftimeline0.vars )
            dftimeline0_rows = db( db.dftimeline0 ).select()
            print (f'insert: \"{ftimeline0.vars.f0}\" in db.dftimeline0; dftimeline0: {len(dftimeline0_rows)} rows' )

    dftimeline1_rows=''
    ftimeline1= Form(db.dftimeline1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftimeline1.vars is None:  
        ftimeline1_f0 = ftimeline1.vars.get('f0','')
        if len ( ftimeline1_f0 ):
            db.dftimeline1.insert( **ftimeline1.vars )
            dftimeline1_rows = db( db.dftimeline1 ).select()
            print (f'insert: \"{ftimeline1.vars.f0}\" in db.dftimeline1; dftimeline1: {len(dftimeline1_rows)} rows' )

    return locals()


@action('advanced', method=["GET", "POST"] )
@action.uses(Template('advanced.html', delimiters='[%[ ]]',), db, session, T, )

def advanced(id=None):
    ctrl_info= "ctrl: advanced, view: advanced.html"

    dfadvanced0_rows=''
    fadvanced0= Form(db.dfadvanced0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fadvanced0.vars is None:  
        fadvanced0_f0 = fadvanced0.vars.get('f0','')
        if len ( fadvanced0_f0 ):
            db.dfadvanced0.insert( **fadvanced0.vars )
            dfadvanced0_rows = db( db.dfadvanced0 ).select()
            print (f'insert: \"{fadvanced0.vars.f0}\" in db.dfadvanced0; dfadvanced0: {len(dfadvanced0_rows)} rows' )

    dfadvanced1_rows=''
    fadvanced1= Form(db.dfadvanced1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fadvanced1.vars is None:  
        fadvanced1_f0 = fadvanced1.vars.get('f0','')
        if len ( fadvanced1_f0 ):
            db.dfadvanced1.insert( **fadvanced1.vars )
            dfadvanced1_rows = db( db.dfadvanced1 ).select()
            print (f'insert: \"{fadvanced1.vars.f0}\" in db.dfadvanced1; dfadvanced1: {len(dfadvanced1_rows)} rows' )

    return locals()


@action('readXmail', method=["GET", "POST"] )
@action.uses(Template('read-mail.html', delimiters='[%[ ]]',), db, session, T, )

def readXmail(id=None):
    ctrl_info= "ctrl: readXmail, view: read-mail.html"

    dfreadXmail0_rows=''
    freadXmail0= Form(db.dfreadXmail0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not freadXmail0.vars is None:  
        freadXmail0_f0 = freadXmail0.vars.get('f0','')
        if len ( freadXmail0_f0 ):
            db.dfreadXmail0.insert( **freadXmail0.vars )
            dfreadXmail0_rows = db( db.dfreadXmail0 ).select()
            print (f'insert: \"{freadXmail0.vars.f0}\" in db.dfreadXmail0; dfreadXmail0: {len(dfreadXmail0_rows)} rows' )

    dfreadXmail1_rows=''
    freadXmail1= Form(db.dfreadXmail1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not freadXmail1.vars is None:  
        freadXmail1_f0 = freadXmail1.vars.get('f0','')
        if len ( freadXmail1_f0 ):
            db.dfreadXmail1.insert( **freadXmail1.vars )
            dfreadXmail1_rows = db( db.dfreadXmail1 ).select()
            print (f'insert: \"{freadXmail1.vars.f0}\" in db.dfreadXmail1; dfreadXmail1: {len(dfreadXmail1_rows)} rows' )

    return locals()


@action('lockscreen', method=["GET", "POST"] )
@action.uses(Template('lockscreen.html', delimiters='[%[ ]]',), db, session, T, )

def lockscreen(id=None):
    ctrl_info= "ctrl: lockscreen, view: lockscreen.html"

    dflockscreen0_rows=''
    flockscreen0= Form(db.dflockscreen0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not flockscreen0.vars is None:  
        flockscreen0_f0 = flockscreen0.vars.get('f0','')
        if len ( flockscreen0_f0 ):
            db.dflockscreen0.insert( **flockscreen0.vars )
            dflockscreen0_rows = db( db.dflockscreen0 ).select()
            print (f'insert: \"{flockscreen0.vars.f0}\" in db.dflockscreen0; dflockscreen0: {len(dflockscreen0_rows)} rows' )

    return locals()


@action('invoiceXprint', method=["GET", "POST"] )
@action.uses(Template('invoice-print.html', delimiters='[%[ ]]',), db, session, T, )

def invoiceXprint(id=None):
    ctrl_info= "ctrl: invoiceXprint, view: invoice-print.html"

    rows_tinvoiceXprint0= db(db.tinvoiceXprint0).select()
    rows_tinvoiceXprint1= db(db.tinvoiceXprint1).select()
    return locals()


@action('collapsedXsidebar', method=["GET", "POST"] )
@action.uses(Template('collapsed-sidebar.html', delimiters='[%[ ]]',), db, session, T, )

def collapsedXsidebar(id=None):
    ctrl_info= "ctrl: collapsedXsidebar, view: collapsed-sidebar.html"

    dfcollapsedXsidebar0_rows=''
    fcollapsedXsidebar0= Form(db.dfcollapsedXsidebar0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcollapsedXsidebar0.vars is None:  
        fcollapsedXsidebar0_f0 = fcollapsedXsidebar0.vars.get('f0','')
        if len ( fcollapsedXsidebar0_f0 ):
            db.dfcollapsedXsidebar0.insert( **fcollapsedXsidebar0.vars )
            dfcollapsedXsidebar0_rows = db( db.dfcollapsedXsidebar0 ).select()
            print (f'insert: \"{fcollapsedXsidebar0.vars.f0}\" in db.dfcollapsedXsidebar0; dfcollapsedXsidebar0: {len(dfcollapsedXsidebar0_rows)} rows' )

    dfcollapsedXsidebar1_rows=''
    fcollapsedXsidebar1= Form(db.dfcollapsedXsidebar1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcollapsedXsidebar1.vars is None:  
        fcollapsedXsidebar1_f0 = fcollapsedXsidebar1.vars.get('f0','')
        if len ( fcollapsedXsidebar1_f0 ):
            db.dfcollapsedXsidebar1.insert( **fcollapsedXsidebar1.vars )
            dfcollapsedXsidebar1_rows = db( db.dfcollapsedXsidebar1 ).select()
            print (f'insert: \"{fcollapsedXsidebar1.vars.f0}\" in db.dfcollapsedXsidebar1; dfcollapsedXsidebar1: {len(dfcollapsedXsidebar1_rows)} rows' )

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
