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

    return locals()


@action('inbox', method=["GET", "POST"] )
@action.uses(Template('inbox.html', delimiters='[%[ ]]',), db, session, T, )

def inbox(id=None):
    ctrl_info= "ctrl: inbox, view: inbox.html"

    return locals()


@action('icons', method=["GET", "POST"] )
@action.uses(Template('icons.html', delimiters='[%[ ]]',), db, session, T, )

def icons(id=None):
    ctrl_info= "ctrl: icons, view: icons.html"

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

    return locals()


@action('profile', method=["GET", "POST"] )
@action.uses(Template('profile.html', delimiters='[%[ ]]',), db, session, T, )

def profile(id=None):
    ctrl_info= "ctrl: profile, view: profile.html"

    rows_tprofile0= db(db.tprofile0).select()
    return locals()


@action('morisjs', method=["GET", "POST"] )
@action.uses(Template('morisjs.html', delimiters='[%[ ]]',), db, session, T, )

def morisjs(id=None):
    ctrl_info= "ctrl: morisjs, view: morisjs.html"

    return locals()


@action('invoice', method=["GET", "POST"] )
@action.uses(Template('invoice.html', delimiters='[%[ ]]',), db, session, T, )

def invoice(id=None):
    ctrl_info= "ctrl: invoice, view: invoice.html"

    rows_tinvoice0= db(db.tinvoice0).select()
    rows_tinvoice1= db(db.tinvoice1).select()
    return locals()


@action('echarts', method=["GET", "POST"] )
@action.uses(Template('echarts.html', delimiters='[%[ ]]',), db, session, T, )

def echarts(id=None):
    ctrl_info= "ctrl: echarts, view: echarts.html"

    return locals()


@action('chartjs', method=["GET", "POST"] )
@action.uses(Template('chartjs.html', delimiters='[%[ ]]',), db, session, T, )

def chartjs(id=None):
    ctrl_info= "ctrl: chartjs, view: chartjs.html"

    return locals()


@action('projects', method=["GET", "POST"] )
@action.uses(Template('projects.html', delimiters='[%[ ]]',), db, session, T, )

def projects(id=None):
    ctrl_info= "ctrl: projects, view: projects.html"

    rows_tprojects0= db(db.tprojects0).select()
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

    return locals()


@action('contacts', method=["GET", "POST"] )
@action.uses(Template('contacts.html', delimiters='[%[ ]]',), db, session, T, )

def contacts(id=None):
    ctrl_info= "ctrl: contacts, view: contacts.html"

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

    return locals()


@action('plainXpage', method=["GET", "POST"] )
@action.uses(Template('plain_page.html', delimiters='[%[ ]]',), db, session, T, )

def plainXpage(id=None):
    ctrl_info= "ctrl: plainXpage, view: plain_page.html"

    return locals()


@action('glyphicons', method=["GET", "POST"] )
@action.uses(Template('glyphicons.html', delimiters='[%[ ]]',), db, session, T, )

def glyphicons(id=None):
    ctrl_info= "ctrl: glyphicons, view: glyphicons.html"

    return locals()


@action('eXcommerce', method=["GET", "POST"] )
@action.uses(Template('e_commerce.html', delimiters='[%[ ]]',), db, session, T, )

def eXcommerce(id=None):
    ctrl_info= "ctrl: eXcommerce, view: e_commerce.html"

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
    return locals()


@action('formXbuttons', method=["GET", "POST"] )
@action.uses(Template('form_buttons.html', delimiters='[%[ ]]',), db, session, T, )

def formXbuttons(id=None):
    ctrl_info= "ctrl: formXbuttons, view: form_buttons.html"

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
    return locals()


@action('projectXdetail', method=["GET", "POST"] )
@action.uses(Template('project_detail.html', delimiters='[%[ ]]',), db, session, T, )

def projectXdetail(id=None):
    ctrl_info= "ctrl: projectXdetail, view: project_detail.html"

    return locals()


@action('pricingXtables', method=["GET", "POST"] )
@action.uses(Template('pricing_tables.html', delimiters='[%[ ]]',), db, session, T, )

def pricingXtables(id=None):
    ctrl_info= "ctrl: pricingXtables, view: pricing_tables.html"

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
