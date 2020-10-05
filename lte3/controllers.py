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



@action('faq', method=["GET", "POST"] )
@action.uses(Template('faq.html', delimiters='[%[ ]]',), db, session, T, )

def faq(id=None):
    ctrl_info= "ctrl: faq, view: faq.html"

    dffaq0_rows=''
    ffaq0= Form(db.dffaq0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ffaq0.vars is None:  
        ffaq0_f0 = ffaq0.vars.get('f0','')
        if len ( ffaq0_f0 ):
            db.dffaq0.insert( **ffaq0.vars )
            dffaq0_rows = db( db.dffaq0 ).select()
            print (f'insert: \"{ffaq0.vars.f0}\" in db.dffaq0.f0; dffaq0: {len(dffaq0_rows)} rows' )

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
            print (f'insert: \"{fX5000.vars.f0}\" in db.dfX5000.f0; dfX5000: {len(dfX5000_rows)} rows' )

    dfX5001_rows=''
    fX5001= Form(db.dfX5001, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fX5001.vars is None:  
        fX5001_f0 = fX5001.vars.get('f0','')
        if len ( fX5001_f0 ):
            db.dfX5001.insert( **fX5001.vars )
            dfX5001_rows = db( db.dfX5001 ).select()
            print (f'insert: \"{fX5001.vars.f0}\" in db.dfX5001.f0; dfX5001: {len(dfX5001_rows)} rows' )

    return locals()


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

    dfX4041_rows=''
    fX4041= Form(db.dfX4041, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fX4041.vars is None:  
        fX4041_f0 = fX4041.vars.get('f0','')
        if len ( fX4041_f0 ):
            db.dfX4041.insert( **fX4041.vars )
            dfX4041_rows = db( db.dfX4041 ).select()
            print (f'insert: \"{fX4041.vars.f0}\" in db.dfX4041.f0; dfX4041: {len(dfX4041_rows)} rows' )

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
            print (f'insert: \"{fdata0.vars.f0}\" in db.dfdata0.f0; dfdata0: {len(dfdata0_rows)} rows' )

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
            print (f'insert: \"{fpace0.vars.f0}\" in db.dfpace0.f0; dfpace0: {len(dfpace0_rows)} rows' )

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
            print (f'insert: \"{fflot0.vars.f0}\" in db.dfflot0.f0; dfflot0: {len(dfflot0_rows)} rows' )

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
            print (f'insert: \"{fboxed0.vars.f0}\" in db.dfboxed0.f0; dfboxed0: {len(dfboxed0_rows)} rows' )

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
            print (f'insert: \"{ficons0.vars.f0}\" in db.dficons0.f0; dficons0: {len(dficons0_rows)} rows' )

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

    dfindex1_rows=''
    findex1= Form(db.dfindex1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex1.vars is None:  
        findex1_f0 = findex1.vars.get('f0','')
        if len ( findex1_f0 ):
            db.dfindex1.insert( **findex1.vars )
            dfindex1_rows = db( db.dfindex1 ).select()
            print (f'insert: \"{findex1.vars.f0}\" in db.dfindex1.f0; dfindex1: {len(dfindex1_rows)} rows' )

    return locals()


@action('navbar', method=["GET", "POST"] )
@action.uses(Template('navbar.html', delimiters='[%[ ]]',), db, session, T, )

def navbar(id=None):
    ctrl_info= "ctrl: navbar, view: navbar.html"

    dfnavbar0_rows=''
    fnavbar0= Form(db.dfnavbar0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fnavbar0.vars is None:  
        fnavbar0_f0 = fnavbar0.vars.get('f0','')
        if len ( fnavbar0_f0 ):
            db.dfnavbar0.insert( **fnavbar0.vars )
            dfnavbar0_rows = db( db.dfnavbar0 ).select()
            print (f'insert: \"{fnavbar0.vars.f0}\" in db.dfnavbar0.f0; dfnavbar0: {len(dfnavbar0_rows)} rows' )

    dfnavbar1_rows=''
    fnavbar1= Form(db.dfnavbar1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fnavbar1.vars is None:  
        fnavbar1_f0 = fnavbar1.vars.get('f0','')
        if len ( fnavbar1_f0 ):
            db.dfnavbar1.insert( **fnavbar1.vars )
            dfnavbar1_rows = db( db.dfnavbar1 ).select()
            print (f'insert: \"{fnavbar1.vars.f0}\" in db.dfnavbar1.f0; dfnavbar1: {len(dfnavbar1_rows)} rows' )

    dfnavbar2_rows=''
    fnavbar2= Form(db.dfnavbar2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fnavbar2.vars is None:  
        fnavbar2_f0 = fnavbar2.vars.get('f0','')
        if len ( fnavbar2_f0 ):
            db.dfnavbar2.insert( **fnavbar2.vars )
            dfnavbar2_rows = db( db.dfnavbar2 ).select()
            print (f'insert: \"{fnavbar2.vars.f0}\" in db.dfnavbar2.f0; dfnavbar2: {len(dfnavbar2_rows)} rows' )

    dfnavbar3_rows=''
    fnavbar3= Form(db.dfnavbar3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fnavbar3.vars is None:  
        fnavbar3_f0 = fnavbar3.vars.get('f0','')
        if len ( fnavbar3_f0 ):
            db.dfnavbar3.insert( **fnavbar3.vars )
            dfnavbar3_rows = db( db.dfnavbar3 ).select()
            print (f'insert: \"{fnavbar3.vars.f0}\" in db.dfnavbar3.f0; dfnavbar3: {len(dfnavbar3_rows)} rows' )

    dfnavbar4_rows=''
    fnavbar4= Form(db.dfnavbar4, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fnavbar4.vars is None:  
        fnavbar4_f0 = fnavbar4.vars.get('f0','')
        if len ( fnavbar4_f0 ):
            db.dfnavbar4.insert( **fnavbar4.vars )
            dfnavbar4_rows = db( db.dfnavbar4 ).select()
            print (f'insert: \"{fnavbar4.vars.f0}\" in db.dfnavbar4.f0; dfnavbar4: {len(dfnavbar4_rows)} rows' )

    dfnavbar5_rows=''
    fnavbar5= Form(db.dfnavbar5, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fnavbar5.vars is None:  
        fnavbar5_f0 = fnavbar5.vars.get('f0','')
        if len ( fnavbar5_f0 ):
            db.dfnavbar5.insert( **fnavbar5.vars )
            dfnavbar5_rows = db( db.dfnavbar5 ).select()
            print (f'insert: \"{fnavbar5.vars.f0}\" in db.dfnavbar5.f0; dfnavbar5: {len(dfnavbar5_rows)} rows' )

    dfnavbar6_rows=''
    fnavbar6= Form(db.dfnavbar6, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fnavbar6.vars is None:  
        fnavbar6_f0 = fnavbar6.vars.get('f0','')
        if len ( fnavbar6_f0 ):
            db.dfnavbar6.insert( **fnavbar6.vars )
            dfnavbar6_rows = db( db.dfnavbar6 ).select()
            print (f'insert: \"{fnavbar6.vars.f0}\" in db.dfnavbar6.f0; dfnavbar6: {len(dfnavbar6_rows)} rows' )

    return locals()


@action('jsgrid', method=["GET", "POST"] )
@action.uses(Template('jsgrid.html', delimiters='[%[ ]]',), db, session, T, )

def jsgrid(id=None):
    ctrl_info= "ctrl: jsgrid, view: jsgrid.html"

    dfjsgrid0_rows=''
    fjsgrid0= Form(db.dfjsgrid0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fjsgrid0.vars is None:  
        fjsgrid0_f0 = fjsgrid0.vars.get('f0','')
        if len ( fjsgrid0_f0 ):
            db.dfjsgrid0.insert( **fjsgrid0.vars )
            dfjsgrid0_rows = db( db.dfjsgrid0 ).select()
            print (f'insert: \"{fjsgrid0.vars.f0}\" in db.dfjsgrid0.f0; dfjsgrid0: {len(dfjsgrid0_rows)} rows' )

    return locals()


@action('simple', method=["GET", "POST"] )
@action.uses(Template('simple.html', delimiters='[%[ ]]',), db, session, T, )

def simple(id=None):
    ctrl_info= "ctrl: simple, view: simple.html"

    dfsimple0_rows=''
    fsimple0= Form(db.dfsimple0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fsimple0.vars is None:  
        fsimple0_f0 = fsimple0.vars.get('f0','')
        if len ( fsimple0_f0 ):
            db.dfsimple0.insert( **fsimple0.vars )
            dfsimple0_rows = db( db.dfsimple0 ).select()
            print (f'insert: \"{fsimple0.vars.f0}\" in db.dfsimple0.f0; dfsimple0: {len(dfsimple0_rows)} rows' )

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
            print (f'insert: \"{finline0.vars.f0}\" in db.dfinline0.f0; dfinline0: {len(dfinline0_rows)} rows' )

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

    return locals()


@action('index3', method=["GET", "POST"] )
@action.uses(Template('index3.html', delimiters='[%[ ]]',), db, session, T, )

def index3(id=None):
    ctrl_info= "ctrl: index3, view: index3.html"

    rows_tindex30= db(db.tindex30).select()
    dfindex30_rows=''
    findex30= Form(db.dfindex30, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex30.vars is None:  
        findex30_f0 = findex30.vars.get('f0','')
        if len ( findex30_f0 ):
            db.dfindex30.insert( **findex30.vars )
            dfindex30_rows = db( db.dfindex30 ).select()
            print (f'insert: \"{findex30.vars.f0}\" in db.dfindex30.f0; dfindex30: {len(dfindex30_rows)} rows' )

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
            print (f'insert: \"{findex20.vars.f0}\" in db.dfindex20.f0; dfindex20: {len(dfindex20_rows)} rows' )

    dfindex21_rows=''
    findex21= Form(db.dfindex21, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex21.vars is None:  
        findex21_f0 = findex21.vars.get('f0','')
        if len ( findex21_f0 ):
            db.dfindex21.insert( **findex21.vars )
            dfindex21_rows = db( db.dfindex21 ).select()
            print (f'insert: \"{findex21.vars.f0}\" in db.dfindex21.f0; dfindex21: {len(dfindex21_rows)} rows' )

    return locals()


@action('starter', method=["GET", "POST"] )
@action.uses(Template('starter.html', delimiters='[%[ ]]',), db, session, T, )

def starter(id=None):
    ctrl_info= "ctrl: starter, view: starter.html"

    dfstarter0_rows=''
    fstarter0= Form(db.dfstarter0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fstarter0.vars is None:  
        fstarter0_f0 = fstarter0.vars.get('f0','')
        if len ( fstarter0_f0 ):
            db.dfstarter0.insert( **fstarter0.vars )
            dfstarter0_rows = db( db.dfstarter0 ).select()
            print (f'insert: \"{fstarter0.vars.f0}\" in db.dfstarter0.f0; dfstarter0: {len(dfstarter0_rows)} rows' )

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
            print (f'insert: \"{fwidgets0.vars.f0}\" in db.dfwidgets0.f0; dfwidgets0: {len(dfwidgets0_rows)} rows' )

    dfwidgets1_rows=''
    fwidgets1= Form(db.dfwidgets1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets1.vars is None:  
        fwidgets1_f0 = fwidgets1.vars.get('f0','')
        if len ( fwidgets1_f0 ):
            db.dfwidgets1.insert( **fwidgets1.vars )
            dfwidgets1_rows = db( db.dfwidgets1 ).select()
            print (f'insert: \"{fwidgets1.vars.f0}\" in db.dfwidgets1.f0; dfwidgets1: {len(dfwidgets1_rows)} rows' )

    dfwidgets2_rows=''
    fwidgets2= Form(db.dfwidgets2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets2.vars is None:  
        fwidgets2_f0 = fwidgets2.vars.get('f0','')
        if len ( fwidgets2_f0 ):
            db.dfwidgets2.insert( **fwidgets2.vars )
            dfwidgets2_rows = db( db.dfwidgets2 ).select()
            print (f'insert: \"{fwidgets2.vars.f0}\" in db.dfwidgets2.f0; dfwidgets2: {len(dfwidgets2_rows)} rows' )

    dfwidgets3_rows=''
    fwidgets3= Form(db.dfwidgets3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets3.vars is None:  
        fwidgets3_f0 = fwidgets3.vars.get('f0','')
        if len ( fwidgets3_f0 ):
            db.dfwidgets3.insert( **fwidgets3.vars )
            dfwidgets3_rows = db( db.dfwidgets3 ).select()
            print (f'insert: \"{fwidgets3.vars.f0}\" in db.dfwidgets3.f0; dfwidgets3: {len(dfwidgets3_rows)} rows' )

    dfwidgets4_rows=''
    fwidgets4= Form(db.dfwidgets4, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets4.vars is None:  
        fwidgets4_f0 = fwidgets4.vars.get('f0','')
        if len ( fwidgets4_f0 ):
            db.dfwidgets4.insert( **fwidgets4.vars )
            dfwidgets4_rows = db( db.dfwidgets4 ).select()
            print (f'insert: \"{fwidgets4.vars.f0}\" in db.dfwidgets4.f0; dfwidgets4: {len(dfwidgets4_rows)} rows' )

    dfwidgets5_rows=''
    fwidgets5= Form(db.dfwidgets5, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets5.vars is None:  
        fwidgets5_f0 = fwidgets5.vars.get('f0','')
        if len ( fwidgets5_f0 ):
            db.dfwidgets5.insert( **fwidgets5.vars )
            dfwidgets5_rows = db( db.dfwidgets5 ).select()
            print (f'insert: \"{fwidgets5.vars.f0}\" in db.dfwidgets5.f0; dfwidgets5: {len(dfwidgets5_rows)} rows' )

    dfwidgets6_rows=''
    fwidgets6= Form(db.dfwidgets6, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets6.vars is None:  
        fwidgets6_f0 = fwidgets6.vars.get('f0','')
        if len ( fwidgets6_f0 ):
            db.dfwidgets6.insert( **fwidgets6.vars )
            dfwidgets6_rows = db( db.dfwidgets6 ).select()
            print (f'insert: \"{fwidgets6.vars.f0}\" in db.dfwidgets6.f0; dfwidgets6: {len(dfwidgets6_rows)} rows' )

    dfwidgets7_rows=''
    fwidgets7= Form(db.dfwidgets7, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets7.vars is None:  
        fwidgets7_f0 = fwidgets7.vars.get('f0','')
        if len ( fwidgets7_f0 ):
            db.dfwidgets7.insert( **fwidgets7.vars )
            dfwidgets7_rows = db( db.dfwidgets7 ).select()
            print (f'insert: \"{fwidgets7.vars.f0}\" in db.dfwidgets7.f0; dfwidgets7: {len(dfwidgets7_rows)} rows' )

    dfwidgets8_rows=''
    fwidgets8= Form(db.dfwidgets8, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets8.vars is None:  
        fwidgets8_f0 = fwidgets8.vars.get('f0','')
        if len ( fwidgets8_f0 ):
            db.dfwidgets8.insert( **fwidgets8.vars )
            dfwidgets8_rows = db( db.dfwidgets8 ).select()
            print (f'insert: \"{fwidgets8.vars.f0}\" in db.dfwidgets8.f0; dfwidgets8: {len(dfwidgets8_rows)} rows' )

    dfwidgets9_rows=''
    fwidgets9= Form(db.dfwidgets9, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets9.vars is None:  
        fwidgets9_f0 = fwidgets9.vars.get('f0','')
        if len ( fwidgets9_f0 ):
            db.dfwidgets9.insert( **fwidgets9.vars )
            dfwidgets9_rows = db( db.dfwidgets9 ).select()
            print (f'insert: \"{fwidgets9.vars.f0}\" in db.dfwidgets9.f0; dfwidgets9: {len(dfwidgets9_rows)} rows' )

    dfwidgets10_rows=''
    fwidgets10= Form(db.dfwidgets10, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fwidgets10.vars is None:  
        fwidgets10_f0 = fwidgets10.vars.get('f0','')
        if len ( fwidgets10_f0 ):
            db.dfwidgets10.insert( **fwidgets10.vars )
            dfwidgets10_rows = db( db.dfwidgets10 ).select()
            print (f'insert: \"{fwidgets10.vars.f0}\" in db.dfwidgets10.f0; dfwidgets10: {len(dfwidgets10_rows)} rows' )

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
            print (f'insert: \"{fmailbox0.vars.f0}\" in db.dfmailbox0.f0; dfmailbox0: {len(dfmailbox0_rows)} rows' )

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
            print (f'insert: \"{ftopXnav0.vars.f0}\" in db.dftopXnav0.f0; dftopXnav0: {len(dftopXnav0_rows)} rows' )

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
            print (f'insert: \"{fcompose0.vars.f0}\" in db.dfcompose0.f0; dfcompose0: {len(dfcompose0_rows)} rows' )

    return locals()


@action('gallery', method=["GET", "POST"] )
@action.uses(Template('gallery.html', delimiters='[%[ ]]',), db, session, T, )

def gallery(id=None):
    ctrl_info= "ctrl: gallery, view: gallery.html"

    dfgallery0_rows=''
    fgallery0= Form(db.dfgallery0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fgallery0.vars is None:  
        fgallery0_f0 = fgallery0.vars.get('f0','')
        if len ( fgallery0_f0 ):
            db.dfgallery0.insert( **fgallery0.vars )
            dfgallery0_rows = db( db.dfgallery0 ).select()
            print (f'insert: \"{fgallery0.vars.f0}\" in db.dfgallery0.f0; dfgallery0: {len(dfgallery0_rows)} rows' )

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
            print (f'insert: \"{feditors0.vars.f0}\" in db.dfeditors0.f0; dfeditors0: {len(dfeditors0_rows)} rows' )

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
            print (f'insert: \"{fprofile0.vars.f0}\" in db.dfprofile0.f0; dfprofile0: {len(dfprofile0_rows)} rows' )

    dfprofile1_rows=''
    fprofile1= Form(db.dfprofile1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprofile1.vars is None:  
        fprofile1_f0 = fprofile1.vars.get('f0','')
        if len ( fprofile1_f0 ):
            db.dfprofile1.insert( **fprofile1.vars )
            dfprofile1_rows = db( db.dfprofile1 ).select()
            print (f'insert: \"{fprofile1.vars.f0}\" in db.dfprofile1.f0; dfprofile1: {len(dfprofile1_rows)} rows' )

    dfprofile2_rows=''
    fprofile2= Form(db.dfprofile2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprofile2.vars is None:  
        fprofile2_f0 = fprofile2.vars.get('f0','')
        if len ( fprofile2_f0 ):
            db.dfprofile2.insert( **fprofile2.vars )
            dfprofile2_rows = db( db.dfprofile2 ).select()
            print (f'insert: \"{fprofile2.vars.f0}\" in db.dfprofile2.f0; dfprofile2: {len(dfprofile2_rows)} rows' )

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
            print (f'insert: \"{finvoice0.vars.f0}\" in db.dfinvoice0.f0; dfinvoice0: {len(dfinvoice0_rows)} rows' )

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
            print (f'insert: \"{fchartjs0.vars.f0}\" in db.dfchartjs0.f0; dfchartjs0: {len(dfchartjs0_rows)} rows' )

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
            print (f'insert: \"{fsliders0.vars.f0}\" in db.dfsliders0.f0; dfsliders0: {len(dfsliders0_rows)} rows' )

    return locals()


@action('ribbons', method=["GET", "POST"] )
@action.uses(Template('ribbons.html', delimiters='[%[ ]]',), db, session, T, )

def ribbons(id=None):
    ctrl_info= "ctrl: ribbons, view: ribbons.html"

    dfribbons0_rows=''
    fribbons0= Form(db.dfribbons0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fribbons0.vars is None:  
        fribbons0_f0 = fribbons0.vars.get('f0','')
        if len ( fribbons0_f0 ):
            db.dfribbons0.insert( **fribbons0.vars )
            dfribbons0_rows = db( db.dfribbons0 ).select()
            print (f'insert: \"{fribbons0.vars.f0}\" in db.dfribbons0.f0; dfribbons0: {len(dfribbons0_rows)} rows' )

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
            print (f'insert: \"{fgeneral0.vars.f0}\" in db.dfgeneral0.f0; dfgeneral0: {len(dfgeneral0_rows)} rows' )

    return locals()


@action('buttons', method=["GET", "POST"] )
@action.uses(Template('buttons.html', delimiters='[%[ ]]',), db, session, T, )

def buttons(id=None):
    ctrl_info= "ctrl: buttons, view: buttons.html"

    rows_tbuttons0= db(db.tbuttons0).select()
    rows_tbuttons1= db(db.tbuttons1).select()
    rows_tbuttons2= db(db.tbuttons2).select()
    rows_tbuttons3= db(db.tbuttons3).select()
    rows_tbuttons4= db(db.tbuttons4).select()
    dfbuttons0_rows=''
    fbuttons0= Form(db.dfbuttons0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fbuttons0.vars is None:  
        fbuttons0_f0 = fbuttons0.vars.get('f0','')
        if len ( fbuttons0_f0 ):
            db.dfbuttons0.insert( **fbuttons0.vars )
            dfbuttons0_rows = db( db.dfbuttons0 ).select()
            print (f'insert: \"{fbuttons0.vars.f0}\" in db.dfbuttons0.f0; dfbuttons0: {len(dfbuttons0_rows)} rows' )

    return locals()


@action('enhanced', method=["GET", "POST"] )
@action.uses(Template('enhanced.html', delimiters='[%[ ]]',), db, session, T, )

def enhanced(id=None):
    ctrl_info= "ctrl: enhanced, view: enhanced.html"

    dfenhanced0_rows=''
    fenhanced0= Form(db.dfenhanced0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fenhanced0.vars is None:  
        fenhanced0_f0 = fenhanced0.vars.get('f0','')
        if len ( fenhanced0_f0 ):
            db.dfenhanced0.insert( **fenhanced0.vars )
            dfenhanced0_rows = db( db.dfenhanced0 ).select()
            print (f'insert: \"{fenhanced0.vars.f0}\" in db.dfenhanced0.f0; dfenhanced0: {len(dfenhanced0_rows)} rows' )

    dfenhanced1_rows=''
    fenhanced1= Form(db.dfenhanced1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fenhanced1.vars is None:  
        fenhanced1_f0 = fenhanced1.vars.get('f0','')
        if len ( fenhanced1_f0 ):
            db.dfenhanced1.insert( **fenhanced1.vars )
            dfenhanced1_rows = db( db.dfenhanced1 ).select()
            print (f'insert: \"{fenhanced1.vars.f0}\" in db.dfenhanced1.f0; dfenhanced1: {len(dfenhanced1_rows)} rows' )

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
            print (f'insert: \"{fadvanced0.vars.f0}\" in db.dfadvanced0.f0; dfadvanced0: {len(dfadvanced0_rows)} rows' )

    return locals()


@action('projects', method=["GET", "POST"] )
@action.uses(Template('projects.html', delimiters='[%[ ]]',), db, session, T, )

def projects(id=None):
    ctrl_info= "ctrl: projects, view: projects.html"

    rows_tprojects0= db(db.tprojects0).select()
    dfprojects0_rows=''
    fprojects0= Form(db.dfprojects0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprojects0.vars is None:  
        fprojects0_f0 = fprojects0.vars.get('f0','')
        if len ( fprojects0_f0 ):
            db.dfprojects0.insert( **fprojects0.vars )
            dfprojects0_rows = db( db.dfprojects0 ).select()
            print (f'insert: \"{fprojects0.vars.f0}\" in db.dfprojects0.f0; dfprojects0: {len(dfprojects0_rows)} rows' )

    return locals()


@action('loginXv2', method=["GET", "POST"] )
@action.uses(Template('login-v2.html', delimiters='[%[ ]]',), db, session, T, )

def loginXv2(id=None):
    ctrl_info= "ctrl: loginXv2, view: login-v2.html"

    dfloginXv20_rows=''
    floginXv20= Form(db.dfloginXv20, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not floginXv20.vars is None:  
        floginXv20_f0 = floginXv20.vars.get('f0','')
        if len ( floginXv20_f0 ):
            db.dfloginXv20.insert( **floginXv20.vars )
            dfloginXv20_rows = db( db.dfloginXv20 ).select()
            print (f'insert: \"{floginXv20.vars.f0}\" in db.dfloginXv20.f0; dfloginXv20: {len(dfloginXv20_rows)} rows' )

    return locals()


@action('contacts', method=["GET", "POST"] )
@action.uses(Template('contacts.html', delimiters='[%[ ]]',), db, session, T, )

def contacts(id=None):
    ctrl_info= "ctrl: contacts, view: contacts.html"

    dfcontacts0_rows=''
    fcontacts0= Form(db.dfcontacts0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcontacts0.vars is None:  
        fcontacts0_f0 = fcontacts0.vars.get('f0','')
        if len ( fcontacts0_f0 ):
            db.dfcontacts0.insert( **fcontacts0.vars )
            dfcontacts0_rows = db( db.dfcontacts0 ).select()
            print (f'insert: \"{fcontacts0.vars.f0}\" in db.dfcontacts0.f0; dfcontacts0: {len(dfcontacts0_rows)} rows' )

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
            print (f'insert: \"{fcalendar0.vars.f0}\" in db.dfcalendar0.f0; dfcalendar0: {len(dfcalendar0_rows)} rows' )

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
            print (f'insert: \"{ftimeline0.vars.f0}\" in db.dftimeline0.f0; dftimeline0: {len(dftimeline0_rows)} rows' )

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
            print (f'insert: \"{freadXmail0.vars.f0}\" in db.dfreadXmail0.f0; dfreadXmail0: {len(dfreadXmail0_rows)} rows' )

    return locals()


@action('validation', method=["GET", "POST"] )
@action.uses(Template('validation.html', delimiters='[%[ ]]',), db, session, T, )

def validation(id=None):
    ctrl_info= "ctrl: validation, view: validation.html"

    dfvalidation0_rows=''
    fvalidation0= Form(db.dfvalidation0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fvalidation0.vars is None:  
        fvalidation0_f0 = fvalidation0.vars.get('f0','')
        if len ( fvalidation0_f0 ):
            db.dfvalidation0.insert( **fvalidation0.vars )
            dfvalidation0_rows = db( db.dfvalidation0 ).select()
            print (f'insert: \"{fvalidation0.vars.f0}\" in db.dfvalidation0.f0; dfvalidation0: {len(dfvalidation0_rows)} rows' )

    dfvalidation1_rows=''
    fvalidation1= Form(db.dfvalidation1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fvalidation1.vars is None:  
        fvalidation1_f0 = fvalidation1.vars.get('f0','')
        if len ( fvalidation1_f0 ):
            db.dfvalidation1.insert( **fvalidation1.vars )
            dfvalidation1_rows = db( db.dfvalidation1 ).select()
            print (f'insert: \"{fvalidation1.vars.f0}\" in db.dfvalidation1.f0; dfvalidation1: {len(dfvalidation1_rows)} rows' )

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
            print (f'insert: \"{flockscreen0.vars.f0}\" in db.dflockscreen0.f0; dflockscreen0: {len(dflockscreen0_rows)} rows' )

    return locals()


@action('eXcommerce', method=["GET", "POST"] )
@action.uses(Template('e-commerce.html', delimiters='[%[ ]]',), db, session, T, )

def eXcommerce(id=None):
    ctrl_info= "ctrl: eXcommerce, view: e-commerce.html"

    dfeXcommerce0_rows=''
    feXcommerce0= Form(db.dfeXcommerce0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not feXcommerce0.vars is None:  
        feXcommerce0_f0 = feXcommerce0.vars.get('f0','')
        if len ( feXcommerce0_f0 ):
            db.dfeXcommerce0.insert( **feXcommerce0.vars )
            dfeXcommerce0_rows = db( db.dfeXcommerce0 ).select()
            print (f'insert: \"{feXcommerce0.vars.f0}\" in db.dfeXcommerce0.f0; dfeXcommerce0: {len(dfeXcommerce0_rows)} rows' )

    return locals()


@action('contactXus', method=["GET", "POST"] )
@action.uses(Template('contact-us.html', delimiters='[%[ ]]',), db, session, T, )

def contactXus(id=None):
    ctrl_info= "ctrl: contactXus, view: contact-us.html"

    dfcontactXus0_rows=''
    fcontactXus0= Form(db.dfcontactXus0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcontactXus0.vars is None:  
        fcontactXus0_f0 = fcontactXus0.vars.get('f0','')
        if len ( fcontactXus0_f0 ):
            db.dfcontactXus0.insert( **fcontactXus0.vars )
            dfcontactXus0_rows = db( db.dfcontactXus0 ).select()
            print (f'insert: \"{fcontactXus0.vars.f0}\" in db.dfcontactXus0.f0; dfcontactXus0: {len(dfcontactXus0_rows)} rows' )

    return locals()


@action('registerXv2', method=["GET", "POST"] )
@action.uses(Template('register-v2.html', delimiters='[%[ ]]',), db, session, T, )

def registerXv2(id=None):
    ctrl_info= "ctrl: registerXv2, view: register-v2.html"

    dfregisterXv20_rows=''
    fregisterXv20= Form(db.dfregisterXv20, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fregisterXv20.vars is None:  
        fregisterXv20_f0 = fregisterXv20.vars.get('f0','')
        if len ( fregisterXv20_f0 ):
            db.dfregisterXv20.insert( **fregisterXv20.vars )
            dfregisterXv20_rows = db( db.dfregisterXv20 ).select()
            print (f'insert: \"{fregisterXv20.vars.f0}\" in db.dfregisterXv20.f0; dfregisterXv20: {len(dfregisterXv20_rows)} rows' )

    return locals()


@action('projectXadd', method=["GET", "POST"] )
@action.uses(Template('project-add.html', delimiters='[%[ ]]',), db, session, T, )

def projectXadd(id=None):
    ctrl_info= "ctrl: projectXadd, view: project-add.html"

    dfprojectXadd0_rows=''
    fprojectXadd0= Form(db.dfprojectXadd0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprojectXadd0.vars is None:  
        fprojectXadd0_f0 = fprojectXadd0.vars.get('f0','')
        if len ( fprojectXadd0_f0 ):
            db.dfprojectXadd0.insert( **fprojectXadd0.vars )
            dfprojectXadd0_rows = db( db.dfprojectXadd0 ).select()
            print (f'insert: \"{fprojectXadd0.vars.f0}\" in db.dfprojectXadd0.f0; dfprojectXadd0: {len(dfprojectXadd0_rows)} rows' )

    return locals()


@action('fixedXtopnav', method=["GET", "POST"] )
@action.uses(Template('fixed-topnav.html', delimiters='[%[ ]]',), db, session, T, )

def fixedXtopnav(id=None):
    ctrl_info= "ctrl: fixedXtopnav, view: fixed-topnav.html"

    dffixedXtopnav0_rows=''
    ffixedXtopnav0= Form(db.dffixedXtopnav0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ffixedXtopnav0.vars is None:  
        ffixedXtopnav0_f0 = ffixedXtopnav0.vars.get('f0','')
        if len ( ffixedXtopnav0_f0 ):
            db.dffixedXtopnav0.insert( **ffixedXtopnav0.vars )
            dffixedXtopnav0_rows = db( db.dffixedXtopnav0 ).select()
            print (f'insert: \"{ffixedXtopnav0.vars.f0}\" in db.dffixedXtopnav0.f0; dffixedXtopnav0: {len(dffixedXtopnav0_rows)} rows' )

    return locals()


@action('fixedXfooter', method=["GET", "POST"] )
@action.uses(Template('fixed-footer.html', delimiters='[%[ ]]',), db, session, T, )

def fixedXfooter(id=None):
    ctrl_info= "ctrl: fixedXfooter, view: fixed-footer.html"

    dffixedXfooter0_rows=''
    ffixedXfooter0= Form(db.dffixedXfooter0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ffixedXfooter0.vars is None:  
        ffixedXfooter0_f0 = ffixedXfooter0.vars.get('f0','')
        if len ( ffixedXfooter0_f0 ):
            db.dffixedXfooter0.insert( **ffixedXfooter0.vars )
            dffixedXfooter0_rows = db( db.dffixedXfooter0 ).select()
            print (f'insert: \"{ffixedXfooter0.vars.f0}\" in db.dffixedXfooter0.f0; dffixedXfooter0: {len(dffixedXfooter0_rows)} rows' )

    return locals()


@action('projectXedit', method=["GET", "POST"] )
@action.uses(Template('project-edit.html', delimiters='[%[ ]]',), db, session, T, )

def projectXedit(id=None):
    ctrl_info= "ctrl: projectXedit, view: project-edit.html"

    rows_tprojectXedit0= db(db.tprojectXedit0).select()
    dfprojectXedit0_rows=''
    fprojectXedit0= Form(db.dfprojectXedit0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprojectXedit0.vars is None:  
        fprojectXedit0_f0 = fprojectXedit0.vars.get('f0','')
        if len ( fprojectXedit0_f0 ):
            db.dfprojectXedit0.insert( **fprojectXedit0.vars )
            dfprojectXedit0_rows = db( db.dfprojectXedit0 ).select()
            print (f'insert: \"{fprojectXedit0.vars.f0}\" in db.dfprojectXedit0.f0; dfprojectXedit0: {len(dfprojectXedit0_rows)} rows' )

    return locals()


@action('fixedXsidebar', method=["GET", "POST"] )
@action.uses(Template('fixed-sidebar.html', delimiters='[%[ ]]',), db, session, T, )

def fixedXsidebar(id=None):
    ctrl_info= "ctrl: fixedXsidebar, view: fixed-sidebar.html"

    dffixedXsidebar0_rows=''
    ffixedXsidebar0= Form(db.dffixedXsidebar0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ffixedXsidebar0.vars is None:  
        ffixedXsidebar0_f0 = ffixedXsidebar0.vars.get('f0','')
        if len ( ffixedXsidebar0_f0 ):
            db.dffixedXsidebar0.insert( **ffixedXsidebar0.vars )
            dffixedXsidebar0_rows = db( db.dffixedXsidebar0 ).select()
            print (f'insert: \"{ffixedXsidebar0.vars.f0}\" in db.dffixedXsidebar0.f0; dffixedXsidebar0: {len(dffixedXsidebar0_rows)} rows' )

    return locals()


@action('invoiceXprint', method=["GET", "POST"] )
@action.uses(Template('invoice-print.html', delimiters='[%[ ]]',), db, session, T, )

def invoiceXprint(id=None):
    ctrl_info= "ctrl: invoiceXprint, view: invoice-print.html"

    rows_tinvoiceXprint0= db(db.tinvoiceXprint0).select()
    rows_tinvoiceXprint1= db(db.tinvoiceXprint1).select()
    return locals()


@action('languageXmenu', method=["GET", "POST"] )
@action.uses(Template('language-menu.html', delimiters='[%[ ]]',), db, session, T, )

def languageXmenu(id=None):
    ctrl_info= "ctrl: languageXmenu, view: language-menu.html"

    dflanguageXmenu0_rows=''
    flanguageXmenu0= Form(db.dflanguageXmenu0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not flanguageXmenu0.vars is None:  
        flanguageXmenu0_f0 = flanguageXmenu0.vars.get('f0','')
        if len ( flanguageXmenu0_f0 ):
            db.dflanguageXmenu0.insert( **flanguageXmenu0.vars )
            dflanguageXmenu0_rows = db( db.dflanguageXmenu0 ).select()
            print (f'insert: \"{flanguageXmenu0.vars.f0}\" in db.dflanguageXmenu0.f0; dflanguageXmenu0: {len(dflanguageXmenu0_rows)} rows' )

    return locals()


@action('projectXdetail', method=["GET", "POST"] )
@action.uses(Template('project-detail.html', delimiters='[%[ ]]',), db, session, T, )

def projectXdetail(id=None):
    ctrl_info= "ctrl: projectXdetail, view: project-detail.html"

    dfprojectXdetail0_rows=''
    fprojectXdetail0= Form(db.dfprojectXdetail0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprojectXdetail0.vars is None:  
        fprojectXdetail0_f0 = fprojectXdetail0.vars.get('f0','')
        if len ( fprojectXdetail0_f0 ):
            db.dfprojectXdetail0.insert( **fprojectXdetail0.vars )
            dfprojectXdetail0_rows = db( db.dfprojectXdetail0 ).select()
            print (f'insert: \"{fprojectXdetail0.vars.f0}\" in db.dfprojectXdetail0.f0; dfprojectXdetail0: {len(dfprojectXdetail0_rows)} rows' )

    return locals()


@action('topXnavXsidebar', method=["GET", "POST"] )
@action.uses(Template('top-nav-sidebar.html', delimiters='[%[ ]]',), db, session, T, )

def topXnavXsidebar(id=None):
    ctrl_info= "ctrl: topXnavXsidebar, view: top-nav-sidebar.html"

    dftopXnavXsidebar0_rows=''
    ftopXnavXsidebar0= Form(db.dftopXnavXsidebar0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftopXnavXsidebar0.vars is None:  
        ftopXnavXsidebar0_f0 = ftopXnavXsidebar0.vars.get('f0','')
        if len ( ftopXnavXsidebar0_f0 ):
            db.dftopXnavXsidebar0.insert( **ftopXnavXsidebar0.vars )
            dftopXnavXsidebar0_rows = db( db.dftopXnavXsidebar0 ).select()
            print (f'insert: \"{ftopXnavXsidebar0.vars.f0}\" in db.dftopXnavXsidebar0.f0; dftopXnavXsidebar0: {len(dftopXnavXsidebar0_rows)} rows' )

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


@action('enhancedXresults', method=["GET", "POST"] )
@action.uses(Template('enhanced-results.html', delimiters='[%[ ]]',), db, session, T, )

def enhancedXresults(id=None):
    ctrl_info= "ctrl: enhancedXresults, view: enhanced-results.html"

    dfenhancedXresults0_rows=''
    fenhancedXresults0= Form(db.dfenhancedXresults0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fenhancedXresults0.vars is None:  
        fenhancedXresults0_f0 = fenhancedXresults0.vars.get('f0','')
        if len ( fenhancedXresults0_f0 ):
            db.dfenhancedXresults0.insert( **fenhancedXresults0.vars )
            dfenhancedXresults0_rows = db( db.dfenhancedXresults0 ).select()
            print (f'insert: \"{fenhancedXresults0.vars.f0}\" in db.dfenhancedXresults0.f0; dfenhancedXresults0: {len(dfenhancedXresults0_rows)} rows' )

    dfenhancedXresults1_rows=''
    fenhancedXresults1= Form(db.dfenhancedXresults1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fenhancedXresults1.vars is None:  
        fenhancedXresults1_f0 = fenhancedXresults1.vars.get('f0','')
        if len ( fenhancedXresults1_f0 ):
            db.dfenhancedXresults1.insert( **fenhancedXresults1.vars )
            dfenhancedXresults1_rows = db( db.dfenhancedXresults1 ).select()
            print (f'insert: \"{fenhancedXresults1.vars.f0}\" in db.dfenhancedXresults1.f0; dfenhancedXresults1: {len(dfenhancedXresults1_rows)} rows' )

    return locals()


@action('recoverXpassword', method=["GET", "POST"] )
@action.uses(Template('recover-password.html', delimiters='[%[ ]]',), db, session, T, )

def recoverXpassword(id=None):
    ctrl_info= "ctrl: recoverXpassword, view: recover-password.html"

    dfrecoverXpassword0_rows=''
    frecoverXpassword0= Form(db.dfrecoverXpassword0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not frecoverXpassword0.vars is None:  
        frecoverXpassword0_f0 = frecoverXpassword0.vars.get('f0','')
        if len ( frecoverXpassword0_f0 ):
            db.dfrecoverXpassword0.insert( **frecoverXpassword0.vars )
            dfrecoverXpassword0_rows = db( db.dfrecoverXpassword0 ).select()
            print (f'insert: \"{frecoverXpassword0.vars.f0}\" in db.dfrecoverXpassword0.f0; dfrecoverXpassword0: {len(dfrecoverXpassword0_rows)} rows' )

    return locals()


@action('legacyXuserXmenu', method=["GET", "POST"] )
@action.uses(Template('legacy-user-menu.html', delimiters='[%[ ]]',), db, session, T, )

def legacyXuserXmenu(id=None):
    ctrl_info= "ctrl: legacyXuserXmenu, view: legacy-user-menu.html"

    dflegacyXuserXmenu0_rows=''
    flegacyXuserXmenu0= Form(db.dflegacyXuserXmenu0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not flegacyXuserXmenu0.vars is None:  
        flegacyXuserXmenu0_f0 = flegacyXuserXmenu0.vars.get('f0','')
        if len ( flegacyXuserXmenu0_f0 ):
            db.dflegacyXuserXmenu0.insert( **flegacyXuserXmenu0.vars )
            dflegacyXuserXmenu0_rows = db( db.dflegacyXuserXmenu0 ).select()
            print (f'insert: \"{flegacyXuserXmenu0.vars.f0}\" in db.dflegacyXuserXmenu0.f0; dflegacyXuserXmenu0: {len(dflegacyXuserXmenu0_rows)} rows' )

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
            print (f'insert: \"{fcollapsedXsidebar0.vars.f0}\" in db.dfcollapsedXsidebar0.f0; dfcollapsedXsidebar0: {len(dfcollapsedXsidebar0_rows)} rows' )

    return locals()


@action('forgotXpasswordXv2', method=["GET", "POST"] )
@action.uses(Template('forgot-password-v2.html', delimiters='[%[ ]]',), db, session, T, )

def forgotXpasswordXv2(id=None):
    ctrl_info= "ctrl: forgotXpasswordXv2, view: forgot-password-v2.html"

    dfforgotXpasswordXv20_rows=''
    fforgotXpasswordXv20= Form(db.dfforgotXpasswordXv20, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fforgotXpasswordXv20.vars is None:  
        fforgotXpasswordXv20_f0 = fforgotXpasswordXv20.vars.get('f0','')
        if len ( fforgotXpasswordXv20_f0 ):
            db.dfforgotXpasswordXv20.insert( **fforgotXpasswordXv20.vars )
            dfforgotXpasswordXv20_rows = db( db.dfforgotXpasswordXv20 ).select()
            print (f'insert: \"{fforgotXpasswordXv20.vars.f0}\" in db.dfforgotXpasswordXv20.f0; dfforgotXpasswordXv20: {len(dfforgotXpasswordXv20_rows)} rows' )

    return locals()


@action('recoverXpasswordXv2', method=["GET", "POST"] )
@action.uses(Template('recover-password-v2.html', delimiters='[%[ ]]',), db, session, T, )

def recoverXpasswordXv2(id=None):
    ctrl_info= "ctrl: recoverXpasswordXv2, view: recover-password-v2.html"

    dfrecoverXpasswordXv20_rows=''
    frecoverXpasswordXv20= Form(db.dfrecoverXpasswordXv20, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not frecoverXpasswordXv20.vars is None:  
        frecoverXpasswordXv20_f0 = frecoverXpasswordXv20.vars.get('f0','')
        if len ( frecoverXpasswordXv20_f0 ):
            db.dfrecoverXpasswordXv20.insert( **frecoverXpasswordXv20.vars )
            dfrecoverXpasswordXv20_rows = db( db.dfrecoverXpasswordXv20 ).select()
            print (f'insert: \"{frecoverXpasswordXv20.vars.f0}\" in db.dfrecoverXpasswordXv20.f0; dfrecoverXpasswordXv20: {len(dfrecoverXpasswordXv20_rows)} rows' )

    return locals()


@action('fixedXsidebarXcustom', method=["GET", "POST"] )
@action.uses(Template('fixed-sidebar-custom.html', delimiters='[%[ ]]',), db, session, T, )

def fixedXsidebarXcustom(id=None):
    ctrl_info= "ctrl: fixedXsidebarXcustom, view: fixed-sidebar-custom.html"

    dffixedXsidebarXcustom0_rows=''
    ffixedXsidebarXcustom0= Form(db.dffixedXsidebarXcustom0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ffixedXsidebarXcustom0.vars is None:  
        ffixedXsidebarXcustom0_f0 = ffixedXsidebarXcustom0.vars.get('f0','')
        if len ( ffixedXsidebarXcustom0_f0 ):
            db.dffixedXsidebarXcustom0.insert( **ffixedXsidebarXcustom0.vars )
            dffixedXsidebarXcustom0_rows = db( db.dffixedXsidebarXcustom0 ).select()
            print (f'insert: \"{ffixedXsidebarXcustom0.vars.f0}\" in db.dffixedXsidebarXcustom0.f0; dffixedXsidebarXcustom0: {len(dffixedXsidebarXcustom0_rows)} rows' )

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
