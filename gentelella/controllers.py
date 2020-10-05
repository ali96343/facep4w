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



@action('form', method=["GET", "POST"] )
@action.uses(Template('form.html', delimiters='[%[ ]]',), db, session, T, )

def form(id=None):
    ctrl_info= "ctrl: form, view: form.html"

    dfform0_rows=''
    fform0= Form(db.dfform0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fform0.vars is None:  
        fform0_f0 = fform0.vars.get('f0','')
        if len ( fform0_f0 ):
            db.dfform0.insert( **fform0.vars )
            dfform0_rows = db( db.dfform0 ).select()
            print (f'insert: \"{fform0.vars.f0}\" in db.dfform0.f0; dfform0: {len(dfform0_rows)} rows' )

    dfform1_rows=''
    fform1= Form(db.dfform1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fform1.vars is None:  
        fform1_f0 = fform1.vars.get('f0','')
        if len ( fform1_f0 ):
            db.dfform1.insert( **fform1.vars )
            dfform1_rows = db( db.dfform1 ).select()
            print (f'insert: \"{fform1.vars.f0}\" in db.dfform1.f0; dfform1: {len(dfform1_rows)} rows' )

    dfform2_rows=''
    fform2= Form(db.dfform2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fform2.vars is None:  
        fform2_f0 = fform2.vars.get('f0','')
        if len ( fform2_f0 ):
            db.dfform2.insert( **fform2.vars )
            dfform2_rows = db( db.dfform2 ).select()
            print (f'insert: \"{fform2.vars.f0}\" in db.dfform2.f0; dfform2: {len(dfform2_rows)} rows' )

    dfform3_rows=''
    fform3= Form(db.dfform3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fform3.vars is None:  
        fform3_f0 = fform3.vars.get('f0','')
        if len ( fform3_f0 ):
            db.dfform3.insert( **fform3.vars )
            dfform3_rows = db( db.dfform3 ).select()
            print (f'insert: \"{fform3.vars.f0}\" in db.dfform3.f0; dfform3: {len(dfform3_rows)} rows' )

    dfform4_rows=''
    fform4= Form(db.dfform4, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fform4.vars is None:  
        fform4_f0 = fform4.vars.get('f0','')
        if len ( fform4_f0 ):
            db.dfform4.insert( **fform4.vars )
            dfform4_rows = db( db.dfform4 ).select()
            print (f'insert: \"{fform4.vars.f0}\" in db.dfform4.f0; dfform4: {len(dfform4_rows)} rows' )

    dfform5_rows=''
    fform5= Form(db.dfform5, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fform5.vars is None:  
        fform5_f0 = fform5.vars.get('f0','')
        if len ( fform5_f0 ):
            db.dfform5.insert( **fform5.vars )
            dfform5_rows = db( db.dfform5 ).select()
            print (f'insert: \"{fform5.vars.f0}\" in db.dfform5.f0; dfform5: {len(dfform5_rows)} rows' )

    dfform6_rows=''
    fform6= Form(db.dfform6, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fform6.vars is None:  
        fform6_f0 = fform6.vars.get('f0','')
        if len ( fform6_f0 ):
            db.dfform6.insert( **fform6.vars )
            dfform6_rows = db( db.dfform6 ).select()
            print (f'insert: \"{fform6.vars.f0}\" in db.dfform6.f0; dfform6: {len(dfform6_rows)} rows' )

    dfform7_rows=''
    fform7= Form(db.dfform7, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fform7.vars is None:  
        fform7_f0 = fform7.vars.get('f0','')
        if len ( fform7_f0 ):
            db.dfform7.insert( **fform7.vars )
            dfform7_rows = db( db.dfform7 ).select()
            print (f'insert: \"{fform7.vars.f0}\" in db.dfform7.f0; dfform7: {len(dfform7_rows)} rows' )

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

    dflogin1_rows=''
    flogin1= Form(db.dflogin1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not flogin1.vars is None:  
        flogin1_f0 = flogin1.vars.get('f0','')
        if len ( flogin1_f0 ):
            db.dflogin1.insert( **flogin1.vars )
            dflogin1_rows = db( db.dflogin1 ).select()
            print (f'insert: \"{flogin1.vars.f0}\" in db.dflogin1.f0; dflogin1: {len(dflogin1_rows)} rows' )

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

    dfindex2_rows=''
    findex2= Form(db.dfindex2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex2.vars is None:  
        findex2_f0 = findex2.vars.get('f0','')
        if len ( findex2_f0 ):
            db.dfindex2.insert( **findex2.vars )
            dfindex2_rows = db( db.dfindex2 ).select()
            print (f'insert: \"{findex2.vars.f0}\" in db.dfindex2.f0; dfindex2: {len(dfindex2_rows)} rows' )

    dfindex3_rows=''
    findex3= Form(db.dfindex3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex3.vars is None:  
        findex3_f0 = findex3.vars.get('f0','')
        if len ( findex3_f0 ):
            db.dfindex3.insert( **findex3.vars )
            dfindex3_rows = db( db.dfindex3 ).select()
            print (f'insert: \"{findex3.vars.f0}\" in db.dfindex3.f0; dfindex3: {len(dfindex3_rows)} rows' )

    dfindex4_rows=''
    findex4= Form(db.dfindex4, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex4.vars is None:  
        findex4_f0 = findex4.vars.get('f0','')
        if len ( findex4_f0 ):
            db.dfindex4.insert( **findex4.vars )
            dfindex4_rows = db( db.dfindex4 ).select()
            print (f'insert: \"{findex4.vars.f0}\" in db.dfindex4.f0; dfindex4: {len(dfindex4_rows)} rows' )

    dfindex5_rows=''
    findex5= Form(db.dfindex5, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex5.vars is None:  
        findex5_f0 = findex5.vars.get('f0','')
        if len ( findex5_f0 ):
            db.dfindex5.insert( **findex5.vars )
            dfindex5_rows = db( db.dfindex5 ).select()
            print (f'insert: \"{findex5.vars.f0}\" in db.dfindex5.f0; dfindex5: {len(dfindex5_rows)} rows' )

    dfindex6_rows=''
    findex6= Form(db.dfindex6, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex6.vars is None:  
        findex6_f0 = findex6.vars.get('f0','')
        if len ( findex6_f0 ):
            db.dfindex6.insert( **findex6.vars )
            dfindex6_rows = db( db.dfindex6 ).select()
            print (f'insert: \"{findex6.vars.f0}\" in db.dfindex6.f0; dfindex6: {len(dfindex6_rows)} rows' )

    dfindex7_rows=''
    findex7= Form(db.dfindex7, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex7.vars is None:  
        findex7_f0 = findex7.vars.get('f0','')
        if len ( findex7_f0 ):
            db.dfindex7.insert( **findex7.vars )
            dfindex7_rows = db( db.dfindex7 ).select()
            print (f'insert: \"{findex7.vars.f0}\" in db.dfindex7.f0; dfindex7: {len(dfindex7_rows)} rows' )

    dfindex8_rows=''
    findex8= Form(db.dfindex8, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not findex8.vars is None:  
        findex8_f0 = findex8.vars.get('f0','')
        if len ( findex8_f0 ):
            db.dfindex8.insert( **findex8.vars )
            dfindex8_rows = db( db.dfindex8 ).select()
            print (f'insert: \"{findex8.vars.f0}\" in db.dfindex8.f0; dfindex8: {len(dfindex8_rows)} rows' )

    return locals()


@action('inbox', method=["GET", "POST"] )
@action.uses(Template('inbox.html', delimiters='[%[ ]]',), db, session, T, )

def inbox(id=None):
    ctrl_info= "ctrl: inbox, view: inbox.html"

    dfinbox0_rows=''
    finbox0= Form(db.dfinbox0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not finbox0.vars is None:  
        finbox0_f0 = finbox0.vars.get('f0','')
        if len ( finbox0_f0 ):
            db.dfinbox0.insert( **finbox0.vars )
            dfinbox0_rows = db( db.dfinbox0 ).select()
            print (f'insert: \"{finbox0.vars.f0}\" in db.dfinbox0.f0; dfinbox0: {len(dfinbox0_rows)} rows' )

    dfinbox1_rows=''
    finbox1= Form(db.dfinbox1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not finbox1.vars is None:  
        finbox1_f0 = finbox1.vars.get('f0','')
        if len ( finbox1_f0 ):
            db.dfinbox1.insert( **finbox1.vars )
            dfinbox1_rows = db( db.dfinbox1 ).select()
            print (f'insert: \"{finbox1.vars.f0}\" in db.dfinbox1.f0; dfinbox1: {len(dfinbox1_rows)} rows' )

    dfinbox2_rows=''
    finbox2= Form(db.dfinbox2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not finbox2.vars is None:  
        finbox2_f0 = finbox2.vars.get('f0','')
        if len ( finbox2_f0 ):
            db.dfinbox2.insert( **finbox2.vars )
            dfinbox2_rows = db( db.dfinbox2 ).select()
            print (f'insert: \"{finbox2.vars.f0}\" in db.dfinbox2.f0; dfinbox2: {len(dfinbox2_rows)} rows' )

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


@action('tables', method=["GET", "POST"] )
@action.uses(Template('tables.html', delimiters='[%[ ]]',), db, session, T, )

def tables(id=None):
    ctrl_info= "ctrl: tables, view: tables.html"

    rows_ttables0= db(db.ttables0).select()
    rows_ttables1= db(db.ttables1).select()
    rows_ttables2= db(db.ttables2).select()
    rows_ttables3= db(db.ttables3).select()
    rows_ttables4= db(db.ttables4).select()
    dftables0_rows=''
    ftables0= Form(db.dftables0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables0.vars is None:  
        ftables0_f0 = ftables0.vars.get('f0','')
        if len ( ftables0_f0 ):
            db.dftables0.insert( **ftables0.vars )
            dftables0_rows = db( db.dftables0 ).select()
            print (f'insert: \"{ftables0.vars.f0}\" in db.dftables0.f0; dftables0: {len(dftables0_rows)} rows' )

    dftables1_rows=''
    ftables1= Form(db.dftables1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables1.vars is None:  
        ftables1_f0 = ftables1.vars.get('f0','')
        if len ( ftables1_f0 ):
            db.dftables1.insert( **ftables1.vars )
            dftables1_rows = db( db.dftables1 ).select()
            print (f'insert: \"{ftables1.vars.f0}\" in db.dftables1.f0; dftables1: {len(dftables1_rows)} rows' )

    dftables2_rows=''
    ftables2= Form(db.dftables2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables2.vars is None:  
        ftables2_f0 = ftables2.vars.get('f0','')
        if len ( ftables2_f0 ):
            db.dftables2.insert( **ftables2.vars )
            dftables2_rows = db( db.dftables2 ).select()
            print (f'insert: \"{ftables2.vars.f0}\" in db.dftables2.f0; dftables2: {len(dftables2_rows)} rows' )

    dftables3_rows=''
    ftables3= Form(db.dftables3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables3.vars is None:  
        ftables3_f0 = ftables3.vars.get('f0','')
        if len ( ftables3_f0 ):
            db.dftables3.insert( **ftables3.vars )
            dftables3_rows = db( db.dftables3 ).select()
            print (f'insert: \"{ftables3.vars.f0}\" in db.dftables3.f0; dftables3: {len(dftables3_rows)} rows' )

    dftables4_rows=''
    ftables4= Form(db.dftables4, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables4.vars is None:  
        ftables4_f0 = ftables4.vars.get('f0','')
        if len ( ftables4_f0 ):
            db.dftables4.insert( **ftables4.vars )
            dftables4_rows = db( db.dftables4 ).select()
            print (f'insert: \"{ftables4.vars.f0}\" in db.dftables4.f0; dftables4: {len(dftables4_rows)} rows' )

    dftables5_rows=''
    ftables5= Form(db.dftables5, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables5.vars is None:  
        ftables5_f0 = ftables5.vars.get('f0','')
        if len ( ftables5_f0 ):
            db.dftables5.insert( **ftables5.vars )
            dftables5_rows = db( db.dftables5 ).select()
            print (f'insert: \"{ftables5.vars.f0}\" in db.dftables5.f0; dftables5: {len(dftables5_rows)} rows' )

    dftables6_rows=''
    ftables6= Form(db.dftables6, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables6.vars is None:  
        ftables6_f0 = ftables6.vars.get('f0','')
        if len ( ftables6_f0 ):
            db.dftables6.insert( **ftables6.vars )
            dftables6_rows = db( db.dftables6 ).select()
            print (f'insert: \"{ftables6.vars.f0}\" in db.dftables6.f0; dftables6: {len(dftables6_rows)} rows' )

    dftables7_rows=''
    ftables7= Form(db.dftables7, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables7.vars is None:  
        ftables7_f0 = ftables7.vars.get('f0','')
        if len ( ftables7_f0 ):
            db.dftables7.insert( **ftables7.vars )
            dftables7_rows = db( db.dftables7 ).select()
            print (f'insert: \"{ftables7.vars.f0}\" in db.dftables7.f0; dftables7: {len(dftables7_rows)} rows' )

    dftables8_rows=''
    ftables8= Form(db.dftables8, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables8.vars is None:  
        ftables8_f0 = ftables8.vars.get('f0','')
        if len ( ftables8_f0 ):
            db.dftables8.insert( **ftables8.vars )
            dftables8_rows = db( db.dftables8 ).select()
            print (f'insert: \"{ftables8.vars.f0}\" in db.dftables8.f0; dftables8: {len(dftables8_rows)} rows' )

    dftables9_rows=''
    ftables9= Form(db.dftables9, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables9.vars is None:  
        ftables9_f0 = ftables9.vars.get('f0','')
        if len ( ftables9_f0 ):
            db.dftables9.insert( **ftables9.vars )
            dftables9_rows = db( db.dftables9 ).select()
            print (f'insert: \"{ftables9.vars.f0}\" in db.dftables9.f0; dftables9: {len(dftables9_rows)} rows' )

    dftables10_rows=''
    ftables10= Form(db.dftables10, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables10.vars is None:  
        ftables10_f0 = ftables10.vars.get('f0','')
        if len ( ftables10_f0 ):
            db.dftables10.insert( **ftables10.vars )
            dftables10_rows = db( db.dftables10 ).select()
            print (f'insert: \"{ftables10.vars.f0}\" in db.dftables10.f0; dftables10: {len(dftables10_rows)} rows' )

    dftables11_rows=''
    ftables11= Form(db.dftables11, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftables11.vars is None:  
        ftables11_f0 = ftables11.vars.get('f0','')
        if len ( ftables11_f0 ):
            db.dftables11.insert( **ftables11.vars )
            dftables11_rows = db( db.dftables11 ).select()
            print (f'insert: \"{ftables11.vars.f0}\" in db.dftables11.f0; dftables11: {len(dftables11_rows)} rows' )

    return locals()


@action('level2', method=["GET", "POST"] )
@action.uses(Template('level2.html', delimiters='[%[ ]]',), db, session, T, )

def level2(id=None):
    ctrl_info= "ctrl: level2, view: level2.html"

    return locals()


@action('index3', method=["GET", "POST"] )
@action.uses(Template('index3.html', delimiters='[%[ ]]',), db, session, T, )

def index3(id=None):
    ctrl_info= "ctrl: index3, view: index3.html"

    return locals()


@action('index2', method=["GET", "POST"] )
@action.uses(Template('index2.html', delimiters='[%[ ]]',), db, session, T, )

def index2(id=None):
    ctrl_info= "ctrl: index2, view: index2.html"

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

    return locals()


@action('profile', method=["GET", "POST"] )
@action.uses(Template('profile.html', delimiters='[%[ ]]',), db, session, T, )

def profile(id=None):
    ctrl_info= "ctrl: profile, view: profile.html"

    rows_tprofile0= db(db.tprofile0).select()
    dfprofile0_rows=''
    fprofile0= Form(db.dfprofile0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprofile0.vars is None:  
        fprofile0_f0 = fprofile0.vars.get('f0','')
        if len ( fprofile0_f0 ):
            db.dfprofile0.insert( **fprofile0.vars )
            dfprofile0_rows = db( db.dfprofile0 ).select()
            print (f'insert: \"{fprofile0.vars.f0}\" in db.dfprofile0.f0; dfprofile0: {len(dfprofile0_rows)} rows' )

    return locals()


@action('morisjs', method=["GET", "POST"] )
@action.uses(Template('morisjs.html', delimiters='[%[ ]]',), db, session, T, )

def morisjs(id=None):
    ctrl_info= "ctrl: morisjs, view: morisjs.html"

    dfmorisjs0_rows=''
    fmorisjs0= Form(db.dfmorisjs0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fmorisjs0.vars is None:  
        fmorisjs0_f0 = fmorisjs0.vars.get('f0','')
        if len ( fmorisjs0_f0 ):
            db.dfmorisjs0.insert( **fmorisjs0.vars )
            dfmorisjs0_rows = db( db.dfmorisjs0 ).select()
            print (f'insert: \"{fmorisjs0.vars.f0}\" in db.dfmorisjs0.f0; dfmorisjs0: {len(dfmorisjs0_rows)} rows' )

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


@action('echarts', method=["GET", "POST"] )
@action.uses(Template('echarts.html', delimiters='[%[ ]]',), db, session, T, )

def echarts(id=None):
    ctrl_info= "ctrl: echarts, view: echarts.html"

    dfecharts0_rows=''
    fecharts0= Form(db.dfecharts0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fecharts0.vars is None:  
        fecharts0_f0 = fecharts0.vars.get('f0','')
        if len ( fecharts0_f0 ):
            db.dfecharts0.insert( **fecharts0.vars )
            dfecharts0_rows = db( db.dfecharts0 ).select()
            print (f'insert: \"{fecharts0.vars.f0}\" in db.dfecharts0.f0; dfecharts0: {len(dfecharts0_rows)} rows' )

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


@action('pageX500', method=["GET", "POST"] )
@action.uses(Template('page_500.html', delimiters='[%[ ]]',), db, session, T, )

def pageX500(id=None):
    ctrl_info= "ctrl: pageX500, view: page_500.html"

    dfpageX5000_rows=''
    fpageX5000= Form(db.dfpageX5000, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fpageX5000.vars is None:  
        fpageX5000_f0 = fpageX5000.vars.get('f0','')
        if len ( fpageX5000_f0 ):
            db.dfpageX5000.insert( **fpageX5000.vars )
            dfpageX5000_rows = db( db.dfpageX5000 ).select()
            print (f'insert: \"{fpageX5000.vars.f0}\" in db.dfpageX5000.f0; dfpageX5000: {len(dfpageX5000_rows)} rows' )

    return locals()


@action('pageX404', method=["GET", "POST"] )
@action.uses(Template('page_404.html', delimiters='[%[ ]]',), db, session, T, )

def pageX404(id=None):
    ctrl_info= "ctrl: pageX404, view: page_404.html"

    dfpageX4040_rows=''
    fpageX4040= Form(db.dfpageX4040, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fpageX4040.vars is None:  
        fpageX4040_f0 = fpageX4040.vars.get('f0','')
        if len ( fpageX4040_f0 ):
            db.dfpageX4040.insert( **fpageX4040.vars )
            dfpageX4040_rows = db( db.dfpageX4040 ).select()
            print (f'insert: \"{fpageX4040.vars.f0}\" in db.dfpageX4040.f0; dfpageX4040: {len(dfpageX4040_rows)} rows' )

    return locals()


@action('pageX403', method=["GET", "POST"] )
@action.uses(Template('page_403.html', delimiters='[%[ ]]',), db, session, T, )

def pageX403(id=None):
    ctrl_info= "ctrl: pageX403, view: page_403.html"

    dfpageX4030_rows=''
    fpageX4030= Form(db.dfpageX4030, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fpageX4030.vars is None:  
        fpageX4030_f0 = fpageX4030.vars.get('f0','')
        if len ( fpageX4030_f0 ):
            db.dfpageX4030.insert( **fpageX4030.vars )
            dfpageX4030_rows = db( db.dfpageX4030 ).select()
            print (f'insert: \"{fpageX4030.vars.f0}\" in db.dfpageX4030.f0; dfpageX4030: {len(dfpageX4030_rows)} rows' )

    return locals()


@action('chartjs2', method=["GET", "POST"] )
@action.uses(Template('chartjs2.html', delimiters='[%[ ]]',), db, session, T, )

def chartjs2(id=None):
    ctrl_info= "ctrl: chartjs2, view: chartjs2.html"

    dfchartjs20_rows=''
    fchartjs20= Form(db.dfchartjs20, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fchartjs20.vars is None:  
        fchartjs20_f0 = fchartjs20.vars.get('f0','')
        if len ( fchartjs20_f0 ):
            db.dfchartjs20.insert( **fchartjs20.vars )
            dfchartjs20_rows = db( db.dfchartjs20 ).select()
            print (f'insert: \"{fchartjs20.vars.f0}\" in db.dfchartjs20.f0; dfchartjs20: {len(dfchartjs20_rows)} rows' )

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

    dfcalendar1_rows=''
    fcalendar1= Form(db.dfcalendar1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcalendar1.vars is None:  
        fcalendar1_f0 = fcalendar1.vars.get('f0','')
        if len ( fcalendar1_f0 ):
            db.dfcalendar1.insert( **fcalendar1.vars )
            dfcalendar1_rows = db( db.dfcalendar1 ).select()
            print (f'insert: \"{fcalendar1.vars.f0}\" in db.dfcalendar1.f0; dfcalendar1: {len(dfcalendar1_rows)} rows' )

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


@action('plainXpage', method=["GET", "POST"] )
@action.uses(Template('plain_page.html', delimiters='[%[ ]]',), db, session, T, )

def plainXpage(id=None):
    ctrl_info= "ctrl: plainXpage, view: plain_page.html"

    dfplainXpage0_rows=''
    fplainXpage0= Form(db.dfplainXpage0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fplainXpage0.vars is None:  
        fplainXpage0_f0 = fplainXpage0.vars.get('f0','')
        if len ( fplainXpage0_f0 ):
            db.dfplainXpage0.insert( **fplainXpage0.vars )
            dfplainXpage0_rows = db( db.dfplainXpage0 ).select()
            print (f'insert: \"{fplainXpage0.vars.f0}\" in db.dfplainXpage0.f0; dfplainXpage0: {len(dfplainXpage0_rows)} rows' )

    return locals()


@action('glyphicons', method=["GET", "POST"] )
@action.uses(Template('glyphicons.html', delimiters='[%[ ]]',), db, session, T, )

def glyphicons(id=None):
    ctrl_info= "ctrl: glyphicons, view: glyphicons.html"

    dfglyphicons0_rows=''
    fglyphicons0= Form(db.dfglyphicons0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fglyphicons0.vars is None:  
        fglyphicons0_f0 = fglyphicons0.vars.get('f0','')
        if len ( fglyphicons0_f0 ):
            db.dfglyphicons0.insert( **fglyphicons0.vars )
            dfglyphicons0_rows = db( db.dfglyphicons0 ).select()
            print (f'insert: \"{fglyphicons0.vars.f0}\" in db.dfglyphicons0.f0; dfglyphicons0: {len(dfglyphicons0_rows)} rows' )

    return locals()


@action('eXcommerce', method=["GET", "POST"] )
@action.uses(Template('e_commerce.html', delimiters='[%[ ]]',), db, session, T, )

def eXcommerce(id=None):
    ctrl_info= "ctrl: eXcommerce, view: e_commerce.html"

    dfeXcommerce0_rows=''
    feXcommerce0= Form(db.dfeXcommerce0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not feXcommerce0.vars is None:  
        feXcommerce0_f0 = feXcommerce0.vars.get('f0','')
        if len ( feXcommerce0_f0 ):
            db.dfeXcommerce0.insert( **feXcommerce0.vars )
            dfeXcommerce0_rows = db( db.dfeXcommerce0 ).select()
            print (f'insert: \"{feXcommerce0.vars.f0}\" in db.dfeXcommerce0.f0; dfeXcommerce0: {len(dfeXcommerce0_rows)} rows' )

    return locals()


@action('formXupload', method=["GET", "POST"] )
@action.uses(Template('form_upload.html', delimiters='[%[ ]]',), db, session, T, )

def formXupload(id=None):
    ctrl_info= "ctrl: formXupload, view: form_upload.html"

    dfformXupload0_rows=''
    fformXupload0= Form(db.dfformXupload0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXupload0.vars is None:  
        fformXupload0_f0 = fformXupload0.vars.get('f0','')
        if len ( fformXupload0_f0 ):
            db.dfformXupload0.insert( **fformXupload0.vars )
            dfformXupload0_rows = db( db.dfformXupload0 ).select()
            print (f'insert: \"{fformXupload0.vars.f0}\" in db.dfformXupload0.f0; dfformXupload0: {len(dfformXupload0_rows)} rows' )

    return locals()


@action('otherXcharts', method=["GET", "POST"] )
@action.uses(Template('other_charts.html', delimiters='[%[ ]]',), db, session, T, )

def otherXcharts(id=None):
    ctrl_info= "ctrl: otherXcharts, view: other_charts.html"

    rows_totherXcharts0= db(db.totherXcharts0).select()
    dfotherXcharts0_rows=''
    fotherXcharts0= Form(db.dfotherXcharts0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fotherXcharts0.vars is None:  
        fotherXcharts0_f0 = fotherXcharts0.vars.get('f0','')
        if len ( fotherXcharts0_f0 ):
            db.dfotherXcharts0.insert( **fotherXcharts0.vars )
            dfotherXcharts0_rows = db( db.dfotherXcharts0 ).select()
            print (f'insert: \"{fotherXcharts0.vars.f0}\" in db.dfotherXcharts0.f0; dfotherXcharts0: {len(dfotherXcharts0_rows)} rows' )

    return locals()


@action('formXwizards', method=["GET", "POST"] )
@action.uses(Template('form_wizards.html', delimiters='[%[ ]]',), db, session, T, )

def formXwizards(id=None):
    ctrl_info= "ctrl: formXwizards, view: form_wizards.html"

    dfformXwizards0_rows=''
    fformXwizards0= Form(db.dfformXwizards0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXwizards0.vars is None:  
        fformXwizards0_f0 = fformXwizards0.vars.get('f0','')
        if len ( fformXwizards0_f0 ):
            db.dfformXwizards0.insert( **fformXwizards0.vars )
            dfformXwizards0_rows = db( db.dfformXwizards0 ).select()
            print (f'insert: \"{fformXwizards0.vars.f0}\" in db.dfformXwizards0.f0; dfformXwizards0: {len(dfformXwizards0_rows)} rows' )

    dfformXwizards1_rows=''
    fformXwizards1= Form(db.dfformXwizards1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXwizards1.vars is None:  
        fformXwizards1_f0 = fformXwizards1.vars.get('f0','')
        if len ( fformXwizards1_f0 ):
            db.dfformXwizards1.insert( **fformXwizards1.vars )
            dfformXwizards1_rows = db( db.dfformXwizards1 ).select()
            print (f'insert: \"{fformXwizards1.vars.f0}\" in db.dfformXwizards1.f0; dfformXwizards1: {len(dfformXwizards1_rows)} rows' )

    return locals()


@action('formXbuttons', method=["GET", "POST"] )
@action.uses(Template('form_buttons.html', delimiters='[%[ ]]',), db, session, T, )

def formXbuttons(id=None):
    ctrl_info= "ctrl: formXbuttons, view: form_buttons.html"

    dfformXbuttons0_rows=''
    fformXbuttons0= Form(db.dfformXbuttons0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXbuttons0.vars is None:  
        fformXbuttons0_f0 = fformXbuttons0.vars.get('f0','')
        if len ( fformXbuttons0_f0 ):
            db.dfformXbuttons0.insert( **fformXbuttons0.vars )
            dfformXbuttons0_rows = db( db.dfformXbuttons0 ).select()
            print (f'insert: \"{fformXbuttons0.vars.f0}\" in db.dfformXbuttons0.f0; dfformXbuttons0: {len(dfformXbuttons0_rows)} rows' )

    dfformXbuttons1_rows=''
    fformXbuttons1= Form(db.dfformXbuttons1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXbuttons1.vars is None:  
        fformXbuttons1_f0 = fformXbuttons1.vars.get('f0','')
        if len ( fformXbuttons1_f0 ):
            db.dfformXbuttons1.insert( **fformXbuttons1.vars )
            dfformXbuttons1_rows = db( db.dfformXbuttons1 ).select()
            print (f'insert: \"{fformXbuttons1.vars.f0}\" in db.dfformXbuttons1.f0; dfformXbuttons1: {len(dfformXbuttons1_rows)} rows' )

    dfformXbuttons2_rows=''
    fformXbuttons2= Form(db.dfformXbuttons2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXbuttons2.vars is None:  
        fformXbuttons2_f0 = fformXbuttons2.vars.get('f0','')
        if len ( fformXbuttons2_f0 ):
            db.dfformXbuttons2.insert( **fformXbuttons2.vars )
            dfformXbuttons2_rows = db( db.dfformXbuttons2 ).select()
            print (f'insert: \"{fformXbuttons2.vars.f0}\" in db.dfformXbuttons2.f0; dfformXbuttons2: {len(dfformXbuttons2_rows)} rows' )

    dfformXbuttons3_rows=''
    fformXbuttons3= Form(db.dfformXbuttons3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXbuttons3.vars is None:  
        fformXbuttons3_f0 = fformXbuttons3.vars.get('f0','')
        if len ( fformXbuttons3_f0 ):
            db.dfformXbuttons3.insert( **fformXbuttons3.vars )
            dfformXbuttons3_rows = db( db.dfformXbuttons3 ).select()
            print (f'insert: \"{fformXbuttons3.vars.f0}\" in db.dfformXbuttons3.f0; dfformXbuttons3: {len(dfformXbuttons3_rows)} rows' )

    return locals()


@action('fixedXfooter', method=["GET", "POST"] )
@action.uses(Template('fixed_footer.html', delimiters='[%[ ]]',), db, session, T, )

def fixedXfooter(id=None):
    ctrl_info= "ctrl: fixedXfooter, view: fixed_footer.html"

    return locals()


@action('formXadvanced', method=["GET", "POST"] )
@action.uses(Template('form_advanced.html', delimiters='[%[ ]]',), db, session, T, )

def formXadvanced(id=None):
    ctrl_info= "ctrl: formXadvanced, view: form_advanced.html"

    rows_tformXadvanced0= db(db.tformXadvanced0).select()
    rows_tformXadvanced1= db(db.tformXadvanced1).select()
    rows_tformXadvanced2= db(db.tformXadvanced2).select()
    rows_tformXadvanced3= db(db.tformXadvanced3).select()
    rows_tformXadvanced4= db(db.tformXadvanced4).select()
    rows_tformXadvanced5= db(db.tformXadvanced5).select()
    rows_tformXadvanced6= db(db.tformXadvanced6).select()
    rows_tformXadvanced7= db(db.tformXadvanced7).select()
    dfformXadvanced0_rows=''
    fformXadvanced0= Form(db.dfformXadvanced0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXadvanced0.vars is None:  
        fformXadvanced0_f0 = fformXadvanced0.vars.get('f0','')
        if len ( fformXadvanced0_f0 ):
            db.dfformXadvanced0.insert( **fformXadvanced0.vars )
            dfformXadvanced0_rows = db( db.dfformXadvanced0 ).select()
            print (f'insert: \"{fformXadvanced0.vars.f0}\" in db.dfformXadvanced0.f0; dfformXadvanced0: {len(dfformXadvanced0_rows)} rows' )

    dfformXadvanced1_rows=''
    fformXadvanced1= Form(db.dfformXadvanced1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXadvanced1.vars is None:  
        fformXadvanced1_f0 = fformXadvanced1.vars.get('f0','')
        if len ( fformXadvanced1_f0 ):
            db.dfformXadvanced1.insert( **fformXadvanced1.vars )
            dfformXadvanced1_rows = db( db.dfformXadvanced1 ).select()
            print (f'insert: \"{fformXadvanced1.vars.f0}\" in db.dfformXadvanced1.f0; dfformXadvanced1: {len(dfformXadvanced1_rows)} rows' )

    dfformXadvanced2_rows=''
    fformXadvanced2= Form(db.dfformXadvanced2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXadvanced2.vars is None:  
        fformXadvanced2_f0 = fformXadvanced2.vars.get('f0','')
        if len ( fformXadvanced2_f0 ):
            db.dfformXadvanced2.insert( **fformXadvanced2.vars )
            dfformXadvanced2_rows = db( db.dfformXadvanced2 ).select()
            print (f'insert: \"{fformXadvanced2.vars.f0}\" in db.dfformXadvanced2.f0; dfformXadvanced2: {len(dfformXadvanced2_rows)} rows' )

    dfformXadvanced3_rows=''
    fformXadvanced3= Form(db.dfformXadvanced3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXadvanced3.vars is None:  
        fformXadvanced3_f0 = fformXadvanced3.vars.get('f0','')
        if len ( fformXadvanced3_f0 ):
            db.dfformXadvanced3.insert( **fformXadvanced3.vars )
            dfformXadvanced3_rows = db( db.dfformXadvanced3 ).select()
            print (f'insert: \"{fformXadvanced3.vars.f0}\" in db.dfformXadvanced3.f0; dfformXadvanced3: {len(dfformXadvanced3_rows)} rows' )

    return locals()


@action('mediaXgallery', method=["GET", "POST"] )
@action.uses(Template('media_gallery.html', delimiters='[%[ ]]',), db, session, T, )

def mediaXgallery(id=None):
    ctrl_info= "ctrl: mediaXgallery, view: media_gallery.html"

    dfmediaXgallery0_rows=''
    fmediaXgallery0= Form(db.dfmediaXgallery0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fmediaXgallery0.vars is None:  
        fmediaXgallery0_f0 = fmediaXgallery0.vars.get('f0','')
        if len ( fmediaXgallery0_f0 ):
            db.dfmediaXgallery0.insert( **fmediaXgallery0.vars )
            dfmediaXgallery0_rows = db( db.dfmediaXgallery0 ).select()
            print (f'insert: \"{fmediaXgallery0.vars.f0}\" in db.dfmediaXgallery0.f0; dfmediaXgallery0: {len(dfmediaXgallery0_rows)} rows' )

    return locals()


@action('fixedXsidebar', method=["GET", "POST"] )
@action.uses(Template('fixed_sidebar.html', delimiters='[%[ ]]',), db, session, T, )

def fixedXsidebar(id=None):
    ctrl_info= "ctrl: fixedXsidebar, view: fixed_sidebar.html"

    return locals()


@action('tablesXdynamic', method=["GET", "POST"] )
@action.uses(Template('tables_dynamic.html', delimiters='[%[ ]]',), db, session, T, )

def tablesXdynamic(id=None):
    ctrl_info= "ctrl: tablesXdynamic, view: tables_dynamic.html"

    rows_ttablesXdynamic0= db(db.ttablesXdynamic0).select()
    rows_ttablesXdynamic1= db(db.ttablesXdynamic1).select()
    rows_ttablesXdynamic2= db(db.ttablesXdynamic2).select()
    rows_ttablesXdynamic3= db(db.ttablesXdynamic3).select()
    rows_ttablesXdynamic4= db(db.ttablesXdynamic4).select()
    rows_ttablesXdynamic5= db(db.ttablesXdynamic5).select()
    dftablesXdynamic0_rows=''
    ftablesXdynamic0= Form(db.dftablesXdynamic0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic0.vars is None:  
        ftablesXdynamic0_f0 = ftablesXdynamic0.vars.get('f0','')
        if len ( ftablesXdynamic0_f0 ):
            db.dftablesXdynamic0.insert( **ftablesXdynamic0.vars )
            dftablesXdynamic0_rows = db( db.dftablesXdynamic0 ).select()
            print (f'insert: \"{ftablesXdynamic0.vars.f0}\" in db.dftablesXdynamic0.f0; dftablesXdynamic0: {len(dftablesXdynamic0_rows)} rows' )

    dftablesXdynamic1_rows=''
    ftablesXdynamic1= Form(db.dftablesXdynamic1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic1.vars is None:  
        ftablesXdynamic1_f0 = ftablesXdynamic1.vars.get('f0','')
        if len ( ftablesXdynamic1_f0 ):
            db.dftablesXdynamic1.insert( **ftablesXdynamic1.vars )
            dftablesXdynamic1_rows = db( db.dftablesXdynamic1 ).select()
            print (f'insert: \"{ftablesXdynamic1.vars.f0}\" in db.dftablesXdynamic1.f0; dftablesXdynamic1: {len(dftablesXdynamic1_rows)} rows' )

    dftablesXdynamic2_rows=''
    ftablesXdynamic2= Form(db.dftablesXdynamic2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic2.vars is None:  
        ftablesXdynamic2_f0 = ftablesXdynamic2.vars.get('f0','')
        if len ( ftablesXdynamic2_f0 ):
            db.dftablesXdynamic2.insert( **ftablesXdynamic2.vars )
            dftablesXdynamic2_rows = db( db.dftablesXdynamic2 ).select()
            print (f'insert: \"{ftablesXdynamic2.vars.f0}\" in db.dftablesXdynamic2.f0; dftablesXdynamic2: {len(dftablesXdynamic2_rows)} rows' )

    dftablesXdynamic3_rows=''
    ftablesXdynamic3= Form(db.dftablesXdynamic3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic3.vars is None:  
        ftablesXdynamic3_f0 = ftablesXdynamic3.vars.get('f0','')
        if len ( ftablesXdynamic3_f0 ):
            db.dftablesXdynamic3.insert( **ftablesXdynamic3.vars )
            dftablesXdynamic3_rows = db( db.dftablesXdynamic3 ).select()
            print (f'insert: \"{ftablesXdynamic3.vars.f0}\" in db.dftablesXdynamic3.f0; dftablesXdynamic3: {len(dftablesXdynamic3_rows)} rows' )

    dftablesXdynamic4_rows=''
    ftablesXdynamic4= Form(db.dftablesXdynamic4, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic4.vars is None:  
        ftablesXdynamic4_f0 = ftablesXdynamic4.vars.get('f0','')
        if len ( ftablesXdynamic4_f0 ):
            db.dftablesXdynamic4.insert( **ftablesXdynamic4.vars )
            dftablesXdynamic4_rows = db( db.dftablesXdynamic4 ).select()
            print (f'insert: \"{ftablesXdynamic4.vars.f0}\" in db.dftablesXdynamic4.f0; dftablesXdynamic4: {len(dftablesXdynamic4_rows)} rows' )

    dftablesXdynamic5_rows=''
    ftablesXdynamic5= Form(db.dftablesXdynamic5, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic5.vars is None:  
        ftablesXdynamic5_f0 = ftablesXdynamic5.vars.get('f0','')
        if len ( ftablesXdynamic5_f0 ):
            db.dftablesXdynamic5.insert( **ftablesXdynamic5.vars )
            dftablesXdynamic5_rows = db( db.dftablesXdynamic5 ).select()
            print (f'insert: \"{ftablesXdynamic5.vars.f0}\" in db.dftablesXdynamic5.f0; dftablesXdynamic5: {len(dftablesXdynamic5_rows)} rows' )

    dftablesXdynamic6_rows=''
    ftablesXdynamic6= Form(db.dftablesXdynamic6, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic6.vars is None:  
        ftablesXdynamic6_f0 = ftablesXdynamic6.vars.get('f0','')
        if len ( ftablesXdynamic6_f0 ):
            db.dftablesXdynamic6.insert( **ftablesXdynamic6.vars )
            dftablesXdynamic6_rows = db( db.dftablesXdynamic6 ).select()
            print (f'insert: \"{ftablesXdynamic6.vars.f0}\" in db.dftablesXdynamic6.f0; dftablesXdynamic6: {len(dftablesXdynamic6_rows)} rows' )

    dftablesXdynamic7_rows=''
    ftablesXdynamic7= Form(db.dftablesXdynamic7, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic7.vars is None:  
        ftablesXdynamic7_f0 = ftablesXdynamic7.vars.get('f0','')
        if len ( ftablesXdynamic7_f0 ):
            db.dftablesXdynamic7.insert( **ftablesXdynamic7.vars )
            dftablesXdynamic7_rows = db( db.dftablesXdynamic7 ).select()
            print (f'insert: \"{ftablesXdynamic7.vars.f0}\" in db.dftablesXdynamic7.f0; dftablesXdynamic7: {len(dftablesXdynamic7_rows)} rows' )

    dftablesXdynamic8_rows=''
    ftablesXdynamic8= Form(db.dftablesXdynamic8, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic8.vars is None:  
        ftablesXdynamic8_f0 = ftablesXdynamic8.vars.get('f0','')
        if len ( ftablesXdynamic8_f0 ):
            db.dftablesXdynamic8.insert( **ftablesXdynamic8.vars )
            dftablesXdynamic8_rows = db( db.dftablesXdynamic8 ).select()
            print (f'insert: \"{ftablesXdynamic8.vars.f0}\" in db.dftablesXdynamic8.f0; dftablesXdynamic8: {len(dftablesXdynamic8_rows)} rows' )

    dftablesXdynamic9_rows=''
    ftablesXdynamic9= Form(db.dftablesXdynamic9, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic9.vars is None:  
        ftablesXdynamic9_f0 = ftablesXdynamic9.vars.get('f0','')
        if len ( ftablesXdynamic9_f0 ):
            db.dftablesXdynamic9.insert( **ftablesXdynamic9.vars )
            dftablesXdynamic9_rows = db( db.dftablesXdynamic9 ).select()
            print (f'insert: \"{ftablesXdynamic9.vars.f0}\" in db.dftablesXdynamic9.f0; dftablesXdynamic9: {len(dftablesXdynamic9_rows)} rows' )

    dftablesXdynamic10_rows=''
    ftablesXdynamic10= Form(db.dftablesXdynamic10, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic10.vars is None:  
        ftablesXdynamic10_f0 = ftablesXdynamic10.vars.get('f0','')
        if len ( ftablesXdynamic10_f0 ):
            db.dftablesXdynamic10.insert( **ftablesXdynamic10.vars )
            dftablesXdynamic10_rows = db( db.dftablesXdynamic10 ).select()
            print (f'insert: \"{ftablesXdynamic10.vars.f0}\" in db.dftablesXdynamic10.f0; dftablesXdynamic10: {len(dftablesXdynamic10_rows)} rows' )

    dftablesXdynamic11_rows=''
    ftablesXdynamic11= Form(db.dftablesXdynamic11, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic11.vars is None:  
        ftablesXdynamic11_f0 = ftablesXdynamic11.vars.get('f0','')
        if len ( ftablesXdynamic11_f0 ):
            db.dftablesXdynamic11.insert( **ftablesXdynamic11.vars )
            dftablesXdynamic11_rows = db( db.dftablesXdynamic11 ).select()
            print (f'insert: \"{ftablesXdynamic11.vars.f0}\" in db.dftablesXdynamic11.f0; dftablesXdynamic11: {len(dftablesXdynamic11_rows)} rows' )

    dftablesXdynamic12_rows=''
    ftablesXdynamic12= Form(db.dftablesXdynamic12, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic12.vars is None:  
        ftablesXdynamic12_f0 = ftablesXdynamic12.vars.get('f0','')
        if len ( ftablesXdynamic12_f0 ):
            db.dftablesXdynamic12.insert( **ftablesXdynamic12.vars )
            dftablesXdynamic12_rows = db( db.dftablesXdynamic12 ).select()
            print (f'insert: \"{ftablesXdynamic12.vars.f0}\" in db.dftablesXdynamic12.f0; dftablesXdynamic12: {len(dftablesXdynamic12_rows)} rows' )

    dftablesXdynamic13_rows=''
    ftablesXdynamic13= Form(db.dftablesXdynamic13, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic13.vars is None:  
        ftablesXdynamic13_f0 = ftablesXdynamic13.vars.get('f0','')
        if len ( ftablesXdynamic13_f0 ):
            db.dftablesXdynamic13.insert( **ftablesXdynamic13.vars )
            dftablesXdynamic13_rows = db( db.dftablesXdynamic13 ).select()
            print (f'insert: \"{ftablesXdynamic13.vars.f0}\" in db.dftablesXdynamic13.f0; dftablesXdynamic13: {len(dftablesXdynamic13_rows)} rows' )

    dftablesXdynamic14_rows=''
    ftablesXdynamic14= Form(db.dftablesXdynamic14, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic14.vars is None:  
        ftablesXdynamic14_f0 = ftablesXdynamic14.vars.get('f0','')
        if len ( ftablesXdynamic14_f0 ):
            db.dftablesXdynamic14.insert( **ftablesXdynamic14.vars )
            dftablesXdynamic14_rows = db( db.dftablesXdynamic14 ).select()
            print (f'insert: \"{ftablesXdynamic14.vars.f0}\" in db.dftablesXdynamic14.f0; dftablesXdynamic14: {len(dftablesXdynamic14_rows)} rows' )

    dftablesXdynamic15_rows=''
    ftablesXdynamic15= Form(db.dftablesXdynamic15, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic15.vars is None:  
        ftablesXdynamic15_f0 = ftablesXdynamic15.vars.get('f0','')
        if len ( ftablesXdynamic15_f0 ):
            db.dftablesXdynamic15.insert( **ftablesXdynamic15.vars )
            dftablesXdynamic15_rows = db( db.dftablesXdynamic15 ).select()
            print (f'insert: \"{ftablesXdynamic15.vars.f0}\" in db.dftablesXdynamic15.f0; dftablesXdynamic15: {len(dftablesXdynamic15_rows)} rows' )

    dftablesXdynamic16_rows=''
    ftablesXdynamic16= Form(db.dftablesXdynamic16, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic16.vars is None:  
        ftablesXdynamic16_f0 = ftablesXdynamic16.vars.get('f0','')
        if len ( ftablesXdynamic16_f0 ):
            db.dftablesXdynamic16.insert( **ftablesXdynamic16.vars )
            dftablesXdynamic16_rows = db( db.dftablesXdynamic16 ).select()
            print (f'insert: \"{ftablesXdynamic16.vars.f0}\" in db.dftablesXdynamic16.f0; dftablesXdynamic16: {len(dftablesXdynamic16_rows)} rows' )

    dftablesXdynamic17_rows=''
    ftablesXdynamic17= Form(db.dftablesXdynamic17, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic17.vars is None:  
        ftablesXdynamic17_f0 = ftablesXdynamic17.vars.get('f0','')
        if len ( ftablesXdynamic17_f0 ):
            db.dftablesXdynamic17.insert( **ftablesXdynamic17.vars )
            dftablesXdynamic17_rows = db( db.dftablesXdynamic17 ).select()
            print (f'insert: \"{ftablesXdynamic17.vars.f0}\" in db.dftablesXdynamic17.f0; dftablesXdynamic17: {len(dftablesXdynamic17_rows)} rows' )

    dftablesXdynamic18_rows=''
    ftablesXdynamic18= Form(db.dftablesXdynamic18, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic18.vars is None:  
        ftablesXdynamic18_f0 = ftablesXdynamic18.vars.get('f0','')
        if len ( ftablesXdynamic18_f0 ):
            db.dftablesXdynamic18.insert( **ftablesXdynamic18.vars )
            dftablesXdynamic18_rows = db( db.dftablesXdynamic18 ).select()
            print (f'insert: \"{ftablesXdynamic18.vars.f0}\" in db.dftablesXdynamic18.f0; dftablesXdynamic18: {len(dftablesXdynamic18_rows)} rows' )

    dftablesXdynamic19_rows=''
    ftablesXdynamic19= Form(db.dftablesXdynamic19, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic19.vars is None:  
        ftablesXdynamic19_f0 = ftablesXdynamic19.vars.get('f0','')
        if len ( ftablesXdynamic19_f0 ):
            db.dftablesXdynamic19.insert( **ftablesXdynamic19.vars )
            dftablesXdynamic19_rows = db( db.dftablesXdynamic19 ).select()
            print (f'insert: \"{ftablesXdynamic19.vars.f0}\" in db.dftablesXdynamic19.f0; dftablesXdynamic19: {len(dftablesXdynamic19_rows)} rows' )

    dftablesXdynamic20_rows=''
    ftablesXdynamic20= Form(db.dftablesXdynamic20, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic20.vars is None:  
        ftablesXdynamic20_f0 = ftablesXdynamic20.vars.get('f0','')
        if len ( ftablesXdynamic20_f0 ):
            db.dftablesXdynamic20.insert( **ftablesXdynamic20.vars )
            dftablesXdynamic20_rows = db( db.dftablesXdynamic20 ).select()
            print (f'insert: \"{ftablesXdynamic20.vars.f0}\" in db.dftablesXdynamic20.f0; dftablesXdynamic20: {len(dftablesXdynamic20_rows)} rows' )

    dftablesXdynamic21_rows=''
    ftablesXdynamic21= Form(db.dftablesXdynamic21, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic21.vars is None:  
        ftablesXdynamic21_f0 = ftablesXdynamic21.vars.get('f0','')
        if len ( ftablesXdynamic21_f0 ):
            db.dftablesXdynamic21.insert( **ftablesXdynamic21.vars )
            dftablesXdynamic21_rows = db( db.dftablesXdynamic21 ).select()
            print (f'insert: \"{ftablesXdynamic21.vars.f0}\" in db.dftablesXdynamic21.f0; dftablesXdynamic21: {len(dftablesXdynamic21_rows)} rows' )

    dftablesXdynamic22_rows=''
    ftablesXdynamic22= Form(db.dftablesXdynamic22, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic22.vars is None:  
        ftablesXdynamic22_f0 = ftablesXdynamic22.vars.get('f0','')
        if len ( ftablesXdynamic22_f0 ):
            db.dftablesXdynamic22.insert( **ftablesXdynamic22.vars )
            dftablesXdynamic22_rows = db( db.dftablesXdynamic22 ).select()
            print (f'insert: \"{ftablesXdynamic22.vars.f0}\" in db.dftablesXdynamic22.f0; dftablesXdynamic22: {len(dftablesXdynamic22_rows)} rows' )

    dftablesXdynamic23_rows=''
    ftablesXdynamic23= Form(db.dftablesXdynamic23, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic23.vars is None:  
        ftablesXdynamic23_f0 = ftablesXdynamic23.vars.get('f0','')
        if len ( ftablesXdynamic23_f0 ):
            db.dftablesXdynamic23.insert( **ftablesXdynamic23.vars )
            dftablesXdynamic23_rows = db( db.dftablesXdynamic23 ).select()
            print (f'insert: \"{ftablesXdynamic23.vars.f0}\" in db.dftablesXdynamic23.f0; dftablesXdynamic23: {len(dftablesXdynamic23_rows)} rows' )

    dftablesXdynamic24_rows=''
    ftablesXdynamic24= Form(db.dftablesXdynamic24, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic24.vars is None:  
        ftablesXdynamic24_f0 = ftablesXdynamic24.vars.get('f0','')
        if len ( ftablesXdynamic24_f0 ):
            db.dftablesXdynamic24.insert( **ftablesXdynamic24.vars )
            dftablesXdynamic24_rows = db( db.dftablesXdynamic24 ).select()
            print (f'insert: \"{ftablesXdynamic24.vars.f0}\" in db.dftablesXdynamic24.f0; dftablesXdynamic24: {len(dftablesXdynamic24_rows)} rows' )

    dftablesXdynamic25_rows=''
    ftablesXdynamic25= Form(db.dftablesXdynamic25, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic25.vars is None:  
        ftablesXdynamic25_f0 = ftablesXdynamic25.vars.get('f0','')
        if len ( ftablesXdynamic25_f0 ):
            db.dftablesXdynamic25.insert( **ftablesXdynamic25.vars )
            dftablesXdynamic25_rows = db( db.dftablesXdynamic25 ).select()
            print (f'insert: \"{ftablesXdynamic25.vars.f0}\" in db.dftablesXdynamic25.f0; dftablesXdynamic25: {len(dftablesXdynamic25_rows)} rows' )

    dftablesXdynamic26_rows=''
    ftablesXdynamic26= Form(db.dftablesXdynamic26, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic26.vars is None:  
        ftablesXdynamic26_f0 = ftablesXdynamic26.vars.get('f0','')
        if len ( ftablesXdynamic26_f0 ):
            db.dftablesXdynamic26.insert( **ftablesXdynamic26.vars )
            dftablesXdynamic26_rows = db( db.dftablesXdynamic26 ).select()
            print (f'insert: \"{ftablesXdynamic26.vars.f0}\" in db.dftablesXdynamic26.f0; dftablesXdynamic26: {len(dftablesXdynamic26_rows)} rows' )

    dftablesXdynamic27_rows=''
    ftablesXdynamic27= Form(db.dftablesXdynamic27, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic27.vars is None:  
        ftablesXdynamic27_f0 = ftablesXdynamic27.vars.get('f0','')
        if len ( ftablesXdynamic27_f0 ):
            db.dftablesXdynamic27.insert( **ftablesXdynamic27.vars )
            dftablesXdynamic27_rows = db( db.dftablesXdynamic27 ).select()
            print (f'insert: \"{ftablesXdynamic27.vars.f0}\" in db.dftablesXdynamic27.f0; dftablesXdynamic27: {len(dftablesXdynamic27_rows)} rows' )

    dftablesXdynamic28_rows=''
    ftablesXdynamic28= Form(db.dftablesXdynamic28, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic28.vars is None:  
        ftablesXdynamic28_f0 = ftablesXdynamic28.vars.get('f0','')
        if len ( ftablesXdynamic28_f0 ):
            db.dftablesXdynamic28.insert( **ftablesXdynamic28.vars )
            dftablesXdynamic28_rows = db( db.dftablesXdynamic28 ).select()
            print (f'insert: \"{ftablesXdynamic28.vars.f0}\" in db.dftablesXdynamic28.f0; dftablesXdynamic28: {len(dftablesXdynamic28_rows)} rows' )

    dftablesXdynamic29_rows=''
    ftablesXdynamic29= Form(db.dftablesXdynamic29, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic29.vars is None:  
        ftablesXdynamic29_f0 = ftablesXdynamic29.vars.get('f0','')
        if len ( ftablesXdynamic29_f0 ):
            db.dftablesXdynamic29.insert( **ftablesXdynamic29.vars )
            dftablesXdynamic29_rows = db( db.dftablesXdynamic29 ).select()
            print (f'insert: \"{ftablesXdynamic29.vars.f0}\" in db.dftablesXdynamic29.f0; dftablesXdynamic29: {len(dftablesXdynamic29_rows)} rows' )

    dftablesXdynamic30_rows=''
    ftablesXdynamic30= Form(db.dftablesXdynamic30, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic30.vars is None:  
        ftablesXdynamic30_f0 = ftablesXdynamic30.vars.get('f0','')
        if len ( ftablesXdynamic30_f0 ):
            db.dftablesXdynamic30.insert( **ftablesXdynamic30.vars )
            dftablesXdynamic30_rows = db( db.dftablesXdynamic30 ).select()
            print (f'insert: \"{ftablesXdynamic30.vars.f0}\" in db.dftablesXdynamic30.f0; dftablesXdynamic30: {len(dftablesXdynamic30_rows)} rows' )

    dftablesXdynamic31_rows=''
    ftablesXdynamic31= Form(db.dftablesXdynamic31, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic31.vars is None:  
        ftablesXdynamic31_f0 = ftablesXdynamic31.vars.get('f0','')
        if len ( ftablesXdynamic31_f0 ):
            db.dftablesXdynamic31.insert( **ftablesXdynamic31.vars )
            dftablesXdynamic31_rows = db( db.dftablesXdynamic31 ).select()
            print (f'insert: \"{ftablesXdynamic31.vars.f0}\" in db.dftablesXdynamic31.f0; dftablesXdynamic31: {len(dftablesXdynamic31_rows)} rows' )

    dftablesXdynamic32_rows=''
    ftablesXdynamic32= Form(db.dftablesXdynamic32, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic32.vars is None:  
        ftablesXdynamic32_f0 = ftablesXdynamic32.vars.get('f0','')
        if len ( ftablesXdynamic32_f0 ):
            db.dftablesXdynamic32.insert( **ftablesXdynamic32.vars )
            dftablesXdynamic32_rows = db( db.dftablesXdynamic32 ).select()
            print (f'insert: \"{ftablesXdynamic32.vars.f0}\" in db.dftablesXdynamic32.f0; dftablesXdynamic32: {len(dftablesXdynamic32_rows)} rows' )

    dftablesXdynamic33_rows=''
    ftablesXdynamic33= Form(db.dftablesXdynamic33, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic33.vars is None:  
        ftablesXdynamic33_f0 = ftablesXdynamic33.vars.get('f0','')
        if len ( ftablesXdynamic33_f0 ):
            db.dftablesXdynamic33.insert( **ftablesXdynamic33.vars )
            dftablesXdynamic33_rows = db( db.dftablesXdynamic33 ).select()
            print (f'insert: \"{ftablesXdynamic33.vars.f0}\" in db.dftablesXdynamic33.f0; dftablesXdynamic33: {len(dftablesXdynamic33_rows)} rows' )

    dftablesXdynamic34_rows=''
    ftablesXdynamic34= Form(db.dftablesXdynamic34, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic34.vars is None:  
        ftablesXdynamic34_f0 = ftablesXdynamic34.vars.get('f0','')
        if len ( ftablesXdynamic34_f0 ):
            db.dftablesXdynamic34.insert( **ftablesXdynamic34.vars )
            dftablesXdynamic34_rows = db( db.dftablesXdynamic34 ).select()
            print (f'insert: \"{ftablesXdynamic34.vars.f0}\" in db.dftablesXdynamic34.f0; dftablesXdynamic34: {len(dftablesXdynamic34_rows)} rows' )

    dftablesXdynamic35_rows=''
    ftablesXdynamic35= Form(db.dftablesXdynamic35, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic35.vars is None:  
        ftablesXdynamic35_f0 = ftablesXdynamic35.vars.get('f0','')
        if len ( ftablesXdynamic35_f0 ):
            db.dftablesXdynamic35.insert( **ftablesXdynamic35.vars )
            dftablesXdynamic35_rows = db( db.dftablesXdynamic35 ).select()
            print (f'insert: \"{ftablesXdynamic35.vars.f0}\" in db.dftablesXdynamic35.f0; dftablesXdynamic35: {len(dftablesXdynamic35_rows)} rows' )

    dftablesXdynamic36_rows=''
    ftablesXdynamic36= Form(db.dftablesXdynamic36, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic36.vars is None:  
        ftablesXdynamic36_f0 = ftablesXdynamic36.vars.get('f0','')
        if len ( ftablesXdynamic36_f0 ):
            db.dftablesXdynamic36.insert( **ftablesXdynamic36.vars )
            dftablesXdynamic36_rows = db( db.dftablesXdynamic36 ).select()
            print (f'insert: \"{ftablesXdynamic36.vars.f0}\" in db.dftablesXdynamic36.f0; dftablesXdynamic36: {len(dftablesXdynamic36_rows)} rows' )

    dftablesXdynamic37_rows=''
    ftablesXdynamic37= Form(db.dftablesXdynamic37, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic37.vars is None:  
        ftablesXdynamic37_f0 = ftablesXdynamic37.vars.get('f0','')
        if len ( ftablesXdynamic37_f0 ):
            db.dftablesXdynamic37.insert( **ftablesXdynamic37.vars )
            dftablesXdynamic37_rows = db( db.dftablesXdynamic37 ).select()
            print (f'insert: \"{ftablesXdynamic37.vars.f0}\" in db.dftablesXdynamic37.f0; dftablesXdynamic37: {len(dftablesXdynamic37_rows)} rows' )

    dftablesXdynamic38_rows=''
    ftablesXdynamic38= Form(db.dftablesXdynamic38, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic38.vars is None:  
        ftablesXdynamic38_f0 = ftablesXdynamic38.vars.get('f0','')
        if len ( ftablesXdynamic38_f0 ):
            db.dftablesXdynamic38.insert( **ftablesXdynamic38.vars )
            dftablesXdynamic38_rows = db( db.dftablesXdynamic38 ).select()
            print (f'insert: \"{ftablesXdynamic38.vars.f0}\" in db.dftablesXdynamic38.f0; dftablesXdynamic38: {len(dftablesXdynamic38_rows)} rows' )

    dftablesXdynamic39_rows=''
    ftablesXdynamic39= Form(db.dftablesXdynamic39, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic39.vars is None:  
        ftablesXdynamic39_f0 = ftablesXdynamic39.vars.get('f0','')
        if len ( ftablesXdynamic39_f0 ):
            db.dftablesXdynamic39.insert( **ftablesXdynamic39.vars )
            dftablesXdynamic39_rows = db( db.dftablesXdynamic39 ).select()
            print (f'insert: \"{ftablesXdynamic39.vars.f0}\" in db.dftablesXdynamic39.f0; dftablesXdynamic39: {len(dftablesXdynamic39_rows)} rows' )

    dftablesXdynamic40_rows=''
    ftablesXdynamic40= Form(db.dftablesXdynamic40, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic40.vars is None:  
        ftablesXdynamic40_f0 = ftablesXdynamic40.vars.get('f0','')
        if len ( ftablesXdynamic40_f0 ):
            db.dftablesXdynamic40.insert( **ftablesXdynamic40.vars )
            dftablesXdynamic40_rows = db( db.dftablesXdynamic40 ).select()
            print (f'insert: \"{ftablesXdynamic40.vars.f0}\" in db.dftablesXdynamic40.f0; dftablesXdynamic40: {len(dftablesXdynamic40_rows)} rows' )

    dftablesXdynamic41_rows=''
    ftablesXdynamic41= Form(db.dftablesXdynamic41, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic41.vars is None:  
        ftablesXdynamic41_f0 = ftablesXdynamic41.vars.get('f0','')
        if len ( ftablesXdynamic41_f0 ):
            db.dftablesXdynamic41.insert( **ftablesXdynamic41.vars )
            dftablesXdynamic41_rows = db( db.dftablesXdynamic41 ).select()
            print (f'insert: \"{ftablesXdynamic41.vars.f0}\" in db.dftablesXdynamic41.f0; dftablesXdynamic41: {len(dftablesXdynamic41_rows)} rows' )

    dftablesXdynamic42_rows=''
    ftablesXdynamic42= Form(db.dftablesXdynamic42, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic42.vars is None:  
        ftablesXdynamic42_f0 = ftablesXdynamic42.vars.get('f0','')
        if len ( ftablesXdynamic42_f0 ):
            db.dftablesXdynamic42.insert( **ftablesXdynamic42.vars )
            dftablesXdynamic42_rows = db( db.dftablesXdynamic42 ).select()
            print (f'insert: \"{ftablesXdynamic42.vars.f0}\" in db.dftablesXdynamic42.f0; dftablesXdynamic42: {len(dftablesXdynamic42_rows)} rows' )

    dftablesXdynamic43_rows=''
    ftablesXdynamic43= Form(db.dftablesXdynamic43, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic43.vars is None:  
        ftablesXdynamic43_f0 = ftablesXdynamic43.vars.get('f0','')
        if len ( ftablesXdynamic43_f0 ):
            db.dftablesXdynamic43.insert( **ftablesXdynamic43.vars )
            dftablesXdynamic43_rows = db( db.dftablesXdynamic43 ).select()
            print (f'insert: \"{ftablesXdynamic43.vars.f0}\" in db.dftablesXdynamic43.f0; dftablesXdynamic43: {len(dftablesXdynamic43_rows)} rows' )

    dftablesXdynamic44_rows=''
    ftablesXdynamic44= Form(db.dftablesXdynamic44, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic44.vars is None:  
        ftablesXdynamic44_f0 = ftablesXdynamic44.vars.get('f0','')
        if len ( ftablesXdynamic44_f0 ):
            db.dftablesXdynamic44.insert( **ftablesXdynamic44.vars )
            dftablesXdynamic44_rows = db( db.dftablesXdynamic44 ).select()
            print (f'insert: \"{ftablesXdynamic44.vars.f0}\" in db.dftablesXdynamic44.f0; dftablesXdynamic44: {len(dftablesXdynamic44_rows)} rows' )

    dftablesXdynamic45_rows=''
    ftablesXdynamic45= Form(db.dftablesXdynamic45, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic45.vars is None:  
        ftablesXdynamic45_f0 = ftablesXdynamic45.vars.get('f0','')
        if len ( ftablesXdynamic45_f0 ):
            db.dftablesXdynamic45.insert( **ftablesXdynamic45.vars )
            dftablesXdynamic45_rows = db( db.dftablesXdynamic45 ).select()
            print (f'insert: \"{ftablesXdynamic45.vars.f0}\" in db.dftablesXdynamic45.f0; dftablesXdynamic45: {len(dftablesXdynamic45_rows)} rows' )

    dftablesXdynamic46_rows=''
    ftablesXdynamic46= Form(db.dftablesXdynamic46, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic46.vars is None:  
        ftablesXdynamic46_f0 = ftablesXdynamic46.vars.get('f0','')
        if len ( ftablesXdynamic46_f0 ):
            db.dftablesXdynamic46.insert( **ftablesXdynamic46.vars )
            dftablesXdynamic46_rows = db( db.dftablesXdynamic46 ).select()
            print (f'insert: \"{ftablesXdynamic46.vars.f0}\" in db.dftablesXdynamic46.f0; dftablesXdynamic46: {len(dftablesXdynamic46_rows)} rows' )

    dftablesXdynamic47_rows=''
    ftablesXdynamic47= Form(db.dftablesXdynamic47, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic47.vars is None:  
        ftablesXdynamic47_f0 = ftablesXdynamic47.vars.get('f0','')
        if len ( ftablesXdynamic47_f0 ):
            db.dftablesXdynamic47.insert( **ftablesXdynamic47.vars )
            dftablesXdynamic47_rows = db( db.dftablesXdynamic47 ).select()
            print (f'insert: \"{ftablesXdynamic47.vars.f0}\" in db.dftablesXdynamic47.f0; dftablesXdynamic47: {len(dftablesXdynamic47_rows)} rows' )

    dftablesXdynamic48_rows=''
    ftablesXdynamic48= Form(db.dftablesXdynamic48, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic48.vars is None:  
        ftablesXdynamic48_f0 = ftablesXdynamic48.vars.get('f0','')
        if len ( ftablesXdynamic48_f0 ):
            db.dftablesXdynamic48.insert( **ftablesXdynamic48.vars )
            dftablesXdynamic48_rows = db( db.dftablesXdynamic48 ).select()
            print (f'insert: \"{ftablesXdynamic48.vars.f0}\" in db.dftablesXdynamic48.f0; dftablesXdynamic48: {len(dftablesXdynamic48_rows)} rows' )

    dftablesXdynamic49_rows=''
    ftablesXdynamic49= Form(db.dftablesXdynamic49, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic49.vars is None:  
        ftablesXdynamic49_f0 = ftablesXdynamic49.vars.get('f0','')
        if len ( ftablesXdynamic49_f0 ):
            db.dftablesXdynamic49.insert( **ftablesXdynamic49.vars )
            dftablesXdynamic49_rows = db( db.dftablesXdynamic49 ).select()
            print (f'insert: \"{ftablesXdynamic49.vars.f0}\" in db.dftablesXdynamic49.f0; dftablesXdynamic49: {len(dftablesXdynamic49_rows)} rows' )

    dftablesXdynamic50_rows=''
    ftablesXdynamic50= Form(db.dftablesXdynamic50, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic50.vars is None:  
        ftablesXdynamic50_f0 = ftablesXdynamic50.vars.get('f0','')
        if len ( ftablesXdynamic50_f0 ):
            db.dftablesXdynamic50.insert( **ftablesXdynamic50.vars )
            dftablesXdynamic50_rows = db( db.dftablesXdynamic50 ).select()
            print (f'insert: \"{ftablesXdynamic50.vars.f0}\" in db.dftablesXdynamic50.f0; dftablesXdynamic50: {len(dftablesXdynamic50_rows)} rows' )

    dftablesXdynamic51_rows=''
    ftablesXdynamic51= Form(db.dftablesXdynamic51, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic51.vars is None:  
        ftablesXdynamic51_f0 = ftablesXdynamic51.vars.get('f0','')
        if len ( ftablesXdynamic51_f0 ):
            db.dftablesXdynamic51.insert( **ftablesXdynamic51.vars )
            dftablesXdynamic51_rows = db( db.dftablesXdynamic51 ).select()
            print (f'insert: \"{ftablesXdynamic51.vars.f0}\" in db.dftablesXdynamic51.f0; dftablesXdynamic51: {len(dftablesXdynamic51_rows)} rows' )

    dftablesXdynamic52_rows=''
    ftablesXdynamic52= Form(db.dftablesXdynamic52, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic52.vars is None:  
        ftablesXdynamic52_f0 = ftablesXdynamic52.vars.get('f0','')
        if len ( ftablesXdynamic52_f0 ):
            db.dftablesXdynamic52.insert( **ftablesXdynamic52.vars )
            dftablesXdynamic52_rows = db( db.dftablesXdynamic52 ).select()
            print (f'insert: \"{ftablesXdynamic52.vars.f0}\" in db.dftablesXdynamic52.f0; dftablesXdynamic52: {len(dftablesXdynamic52_rows)} rows' )

    dftablesXdynamic53_rows=''
    ftablesXdynamic53= Form(db.dftablesXdynamic53, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic53.vars is None:  
        ftablesXdynamic53_f0 = ftablesXdynamic53.vars.get('f0','')
        if len ( ftablesXdynamic53_f0 ):
            db.dftablesXdynamic53.insert( **ftablesXdynamic53.vars )
            dftablesXdynamic53_rows = db( db.dftablesXdynamic53 ).select()
            print (f'insert: \"{ftablesXdynamic53.vars.f0}\" in db.dftablesXdynamic53.f0; dftablesXdynamic53: {len(dftablesXdynamic53_rows)} rows' )

    dftablesXdynamic54_rows=''
    ftablesXdynamic54= Form(db.dftablesXdynamic54, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic54.vars is None:  
        ftablesXdynamic54_f0 = ftablesXdynamic54.vars.get('f0','')
        if len ( ftablesXdynamic54_f0 ):
            db.dftablesXdynamic54.insert( **ftablesXdynamic54.vars )
            dftablesXdynamic54_rows = db( db.dftablesXdynamic54 ).select()
            print (f'insert: \"{ftablesXdynamic54.vars.f0}\" in db.dftablesXdynamic54.f0; dftablesXdynamic54: {len(dftablesXdynamic54_rows)} rows' )

    dftablesXdynamic55_rows=''
    ftablesXdynamic55= Form(db.dftablesXdynamic55, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic55.vars is None:  
        ftablesXdynamic55_f0 = ftablesXdynamic55.vars.get('f0','')
        if len ( ftablesXdynamic55_f0 ):
            db.dftablesXdynamic55.insert( **ftablesXdynamic55.vars )
            dftablesXdynamic55_rows = db( db.dftablesXdynamic55 ).select()
            print (f'insert: \"{ftablesXdynamic55.vars.f0}\" in db.dftablesXdynamic55.f0; dftablesXdynamic55: {len(dftablesXdynamic55_rows)} rows' )

    dftablesXdynamic56_rows=''
    ftablesXdynamic56= Form(db.dftablesXdynamic56, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic56.vars is None:  
        ftablesXdynamic56_f0 = ftablesXdynamic56.vars.get('f0','')
        if len ( ftablesXdynamic56_f0 ):
            db.dftablesXdynamic56.insert( **ftablesXdynamic56.vars )
            dftablesXdynamic56_rows = db( db.dftablesXdynamic56 ).select()
            print (f'insert: \"{ftablesXdynamic56.vars.f0}\" in db.dftablesXdynamic56.f0; dftablesXdynamic56: {len(dftablesXdynamic56_rows)} rows' )

    dftablesXdynamic57_rows=''
    ftablesXdynamic57= Form(db.dftablesXdynamic57, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic57.vars is None:  
        ftablesXdynamic57_f0 = ftablesXdynamic57.vars.get('f0','')
        if len ( ftablesXdynamic57_f0 ):
            db.dftablesXdynamic57.insert( **ftablesXdynamic57.vars )
            dftablesXdynamic57_rows = db( db.dftablesXdynamic57 ).select()
            print (f'insert: \"{ftablesXdynamic57.vars.f0}\" in db.dftablesXdynamic57.f0; dftablesXdynamic57: {len(dftablesXdynamic57_rows)} rows' )

    dftablesXdynamic58_rows=''
    ftablesXdynamic58= Form(db.dftablesXdynamic58, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not ftablesXdynamic58.vars is None:  
        ftablesXdynamic58_f0 = ftablesXdynamic58.vars.get('f0','')
        if len ( ftablesXdynamic58_f0 ):
            db.dftablesXdynamic58.insert( **ftablesXdynamic58.vars )
            dftablesXdynamic58_rows = db( db.dftablesXdynamic58 ).select()
            print (f'insert: \"{ftablesXdynamic58.vars.f0}\" in db.dftablesXdynamic58.f0; dftablesXdynamic58: {len(dftablesXdynamic58_rows)} rows' )

    return locals()


@action('projectXdetail', method=["GET", "POST"] )
@action.uses(Template('project_detail.html', delimiters='[%[ ]]',), db, session, T, )

def projectXdetail(id=None):
    ctrl_info= "ctrl: projectXdetail, view: project_detail.html"

    dfprojectXdetail0_rows=''
    fprojectXdetail0= Form(db.dfprojectXdetail0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fprojectXdetail0.vars is None:  
        fprojectXdetail0_f0 = fprojectXdetail0.vars.get('f0','')
        if len ( fprojectXdetail0_f0 ):
            db.dfprojectXdetail0.insert( **fprojectXdetail0.vars )
            dfprojectXdetail0_rows = db( db.dfprojectXdetail0 ).select()
            print (f'insert: \"{fprojectXdetail0.vars.f0}\" in db.dfprojectXdetail0.f0; dfprojectXdetail0: {len(dfprojectXdetail0_rows)} rows' )

    return locals()


@action('pricingXtables', method=["GET", "POST"] )
@action.uses(Template('pricing_tables.html', delimiters='[%[ ]]',), db, session, T, )

def pricingXtables(id=None):
    ctrl_info= "ctrl: pricingXtables, view: pricing_tables.html"

    dfpricingXtables0_rows=''
    fpricingXtables0= Form(db.dfpricingXtables0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fpricingXtables0.vars is None:  
        fpricingXtables0_f0 = fpricingXtables0.vars.get('f0','')
        if len ( fpricingXtables0_f0 ):
            db.dfpricingXtables0.insert( **fpricingXtables0.vars )
            dfpricingXtables0_rows = db( db.dfpricingXtables0 ).select()
            print (f'insert: \"{fpricingXtables0.vars.f0}\" in db.dfpricingXtables0.f0; dfpricingXtables0: {len(dfpricingXtables0_rows)} rows' )

    return locals()


@action('formXvalidation', method=["GET", "POST"] )
@action.uses(Template('form_validation.html', delimiters='[%[ ]]',), db, session, T, )

def formXvalidation(id=None):
    ctrl_info= "ctrl: formXvalidation, view: form_validation.html"

    dfformXvalidation0_rows=''
    fformXvalidation0= Form(db.dfformXvalidation0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fformXvalidation0.vars is None:  
        fformXvalidation0_f0 = fformXvalidation0.vars.get('f0','')
        if len ( fformXvalidation0_f0 ):
            db.dfformXvalidation0.insert( **fformXvalidation0.vars )
            dfformXvalidation0_rows = db( db.dfformXvalidation0 ).select()
            print (f'insert: \"{fformXvalidation0.vars.f0}\" in db.dfformXvalidation0.f0; dfformXvalidation0: {len(dfformXvalidation0_rows)} rows' )

    return locals()


@action('generalXelements', method=["GET", "POST"] )
@action.uses(Template('general_elements.html', delimiters='[%[ ]]',), db, session, T, )

def generalXelements(id=None):
    ctrl_info= "ctrl: generalXelements, view: general_elements.html"

    rows_tgeneralXelements0= db(db.tgeneralXelements0).select()
    rows_tgeneralXelements1= db(db.tgeneralXelements1).select()
    dfgeneralXelements0_rows=''
    fgeneralXelements0= Form(db.dfgeneralXelements0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fgeneralXelements0.vars is None:  
        fgeneralXelements0_f0 = fgeneralXelements0.vars.get('f0','')
        if len ( fgeneralXelements0_f0 ):
            db.dfgeneralXelements0.insert( **fgeneralXelements0.vars )
            dfgeneralXelements0_rows = db( db.dfgeneralXelements0 ).select()
            print (f'insert: \"{fgeneralXelements0.vars.f0}\" in db.dfgeneralXelements0.f0; dfgeneralXelements0: {len(dfgeneralXelements0_rows)} rows' )

    dfgeneralXelements1_rows=''
    fgeneralXelements1= Form(db.dfgeneralXelements1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fgeneralXelements1.vars is None:  
        fgeneralXelements1_f0 = fgeneralXelements1.vars.get('f0','')
        if len ( fgeneralXelements1_f0 ):
            db.dfgeneralXelements1.insert( **fgeneralXelements1.vars )
            dfgeneralXelements1_rows = db( db.dfgeneralXelements1 ).select()
            print (f'insert: \"{fgeneralXelements1.vars.f0}\" in db.dfgeneralXelements1.f0; dfgeneralXelements1: {len(dfgeneralXelements1_rows)} rows' )

    dfgeneralXelements2_rows=''
    fgeneralXelements2= Form(db.dfgeneralXelements2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fgeneralXelements2.vars is None:  
        fgeneralXelements2_f0 = fgeneralXelements2.vars.get('f0','')
        if len ( fgeneralXelements2_f0 ):
            db.dfgeneralXelements2.insert( **fgeneralXelements2.vars )
            dfgeneralXelements2_rows = db( db.dfgeneralXelements2 ).select()
            print (f'insert: \"{fgeneralXelements2.vars.f0}\" in db.dfgeneralXelements2.f0; dfgeneralXelements2: {len(dfgeneralXelements2_rows)} rows' )

    dfgeneralXelements3_rows=''
    fgeneralXelements3= Form(db.dfgeneralXelements3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fgeneralXelements3.vars is None:  
        fgeneralXelements3_f0 = fgeneralXelements3.vars.get('f0','')
        if len ( fgeneralXelements3_f0 ):
            db.dfgeneralXelements3.insert( **fgeneralXelements3.vars )
            dfgeneralXelements3_rows = db( db.dfgeneralXelements3 ).select()
            print (f'insert: \"{fgeneralXelements3.vars.f0}\" in db.dfgeneralXelements3.f0; dfgeneralXelements3: {len(dfgeneralXelements3_rows)} rows' )

    dfgeneralXelements4_rows=''
    fgeneralXelements4= Form(db.dfgeneralXelements4, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fgeneralXelements4.vars is None:  
        fgeneralXelements4_f0 = fgeneralXelements4.vars.get('f0','')
        if len ( fgeneralXelements4_f0 ):
            db.dfgeneralXelements4.insert( **fgeneralXelements4.vars )
            dfgeneralXelements4_rows = db( db.dfgeneralXelements4 ).select()
            print (f'insert: \"{fgeneralXelements4.vars.f0}\" in db.dfgeneralXelements4.f0; dfgeneralXelements4: {len(dfgeneralXelements4_rows)} rows' )

    dfgeneralXelements5_rows=''
    fgeneralXelements5= Form(db.dfgeneralXelements5, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fgeneralXelements5.vars is None:  
        fgeneralXelements5_f0 = fgeneralXelements5.vars.get('f0','')
        if len ( fgeneralXelements5_f0 ):
            db.dfgeneralXelements5.insert( **fgeneralXelements5.vars )
            dfgeneralXelements5_rows = db( db.dfgeneralXelements5 ).select()
            print (f'insert: \"{fgeneralXelements5.vars.f0}\" in db.dfgeneralXelements5.f0; dfgeneralXelements5: {len(dfgeneralXelements5_rows)} rows' )

    dfgeneralXelements6_rows=''
    fgeneralXelements6= Form(db.dfgeneralXelements6, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fgeneralXelements6.vars is None:  
        fgeneralXelements6_f0 = fgeneralXelements6.vars.get('f0','')
        if len ( fgeneralXelements6_f0 ):
            db.dfgeneralXelements6.insert( **fgeneralXelements6.vars )
            dfgeneralXelements6_rows = db( db.dfgeneralXelements6 ).select()
            print (f'insert: \"{fgeneralXelements6.vars.f0}\" in db.dfgeneralXelements6.f0; dfgeneralXelements6: {len(dfgeneralXelements6_rows)} rows' )

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
