#
# py4web app, AI-biorex ported 19.12.2020 12:15:25 UTC+3, src: https://github.com/adminkit/adminkit

# https://github.com/ali96343/facep4w
#

import os, json
from py4web.core import bottle

from py4web import action, request, response,  abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from py4web.core import Template, Reloader
from py4web.utils.dbstore import DBStore

#from yatl.helpers import INPUT, H1, HTML, BODY, A
from .common import db, session, T, cache, authenticated, unauthenticated, auth
from .settings import APP_NAME

 
# ---------------------- Global -----------------------------------------------------

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)

#db_sess = DAL('sqlite:memory')
#session =  Session(storage=DBStore(db_sess))

Glb= {'debug': True , 'my_app_name': APP_NAME, 'tte_path': '/static/tte' }

# ---------------------- Utils -------------------------------------------------------

def prn_form_vars(myform, mydb,):

        id_db = None; row_db = None; f0_fld = None; inserted = False

        if Glb['debug'] == True:
            print("app:",Glb['my_app_name'])
            _ = [ print (f'     {k}: {v}') for k,v in myform.vars.items() if k != '_formkey']

        f0_fld = myform.vars.get('f0', None )
        if (not f0_fld is None) and len(f0_fld):
            id_db = mydb.insert(**mydb._filter_fields(myform.vars))
            db.commit()

            if not id_db is None:
                row_db = mydb(id_db )

                if not row_db is None:
                    if Glb['debug'] == True:
                         print(f'     inserted: \"{myform.vars.f0}\" into {mydb.f0}, id = {id_db}' )
                         print(f"     select  : \"{row_db.f0}\" from {mydb.f0}, id = {id_db}" )
                         print ()
                    inserted =True
        else:
            if Glb['debug'] == True:
                print(f"     no entry inserted: (f0_fld is None) or (len(f0_fld) == 0)")
                print()

        return inserted
            
def put_json_messages(mess='mymess'):
    response.headers["Content-Type"] = "application/json"
    return json.dumps( {'messages' : f'{mess}'})
    
# ---------------------- Controllers  ------------------------------------------------

@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T,)

def index():
    ctrl_info= "ctrl: index, view: index.html"
    page_url = "\'" + URL('index' ) + "\'"
    messages = []

    rows_tindex0= db(db.tindex0).select()
    rows_tindex1= db(db.tindex1).select()
    findex0= Form(db.dfindex0, dbio=False, formstyle=FormStyleBulma)

    if findex0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( findex0, db.dfindex0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( findex0.form_name ))
    elif findex0.errors:
        print("findex0 has errors: %s" % (findex0.errors))
        return put_json_messages('error: ' + str( findex0.form_name ))
 

    return locals()

@action('uiXgrid', method=["GET", "POST"] )
@action.uses(Template('ui-grid.html', delimiters='[%[ ]]',), db, session, T,)

def uiXgrid():
    ctrl_info= "ctrl: uiXgrid, view: ui-grid.html"
    page_url = "\'" + URL('uiXgrid' ) + "\'"
    messages = []

    fuiXgrid0= Form(db.dfuiXgrid0, dbio=False, formstyle=FormStyleBulma)

    if fuiXgrid0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXgrid0, db.dfuiXgrid0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXgrid0.form_name ))
    elif fuiXgrid0.errors:
        print("fuiXgrid0 has errors: %s" % (fuiXgrid0.errors))
        return put_json_messages('error: ' + str( fuiXgrid0.form_name ))
 

    return locals()

@action('uiXcards', method=["GET", "POST"] )
@action.uses(Template('ui-cards.html', delimiters='[%[ ]]',), db, session, T,)

def uiXcards():
    ctrl_info= "ctrl: uiXcards, view: ui-cards.html"
    page_url = "\'" + URL('uiXcards' ) + "\'"
    messages = []

    fuiXcards0= Form(db.dfuiXcards0, dbio=False, formstyle=FormStyleBulma)

    if fuiXcards0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXcards0, db.dfuiXcards0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXcards0.form_name ))
    elif fuiXcards0.errors:
        print("fuiXcards0 has errors: %s" % (fuiXcards0.errors))
        return put_json_messages('error: ' + str( fuiXcards0.form_name ))
 

    return locals()

@action('uiXmodals', method=["GET", "POST"] )
@action.uses(Template('ui-modals.html', delimiters='[%[ ]]',), db, session, T,)

def uiXmodals():
    ctrl_info= "ctrl: uiXmodals, view: ui-modals.html"
    page_url = "\'" + URL('uiXmodals' ) + "\'"
    messages = []

    fuiXmodals0= Form(db.dfuiXmodals0, dbio=False, formstyle=FormStyleBulma)

    if fuiXmodals0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXmodals0, db.dfuiXmodals0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXmodals0.form_name ))
    elif fuiXmodals0.errors:
        print("fuiXmodals0 has errors: %s" % (fuiXmodals0.errors))
        return put_json_messages('error: ' + str( fuiXmodals0.form_name ))
 

    return locals()

@action('uiXalerts', method=["GET", "POST"] )
@action.uses(Template('ui-alerts.html', delimiters='[%[ ]]',), db, session, T,)

def uiXalerts():
    ctrl_info= "ctrl: uiXalerts, view: ui-alerts.html"
    page_url = "\'" + URL('uiXalerts' ) + "\'"
    messages = []

    fuiXalerts0= Form(db.dfuiXalerts0, dbio=False, formstyle=FormStyleBulma)

    if fuiXalerts0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXalerts0, db.dfuiXalerts0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXalerts0.form_name ))
    elif fuiXalerts0.errors:
        print("fuiXalerts0 has errors: %s" % (fuiXalerts0.errors))
        return put_json_messages('error: ' + str( fuiXalerts0.form_name ))
 

    return locals()

@action('uiXgeneral', method=["GET", "POST"] )
@action.uses(Template('ui-general.html', delimiters='[%[ ]]',), db, session, T,)

def uiXgeneral():
    ctrl_info= "ctrl: uiXgeneral, view: ui-general.html"
    page_url = "\'" + URL('uiXgeneral' ) + "\'"
    messages = []

    fuiXgeneral0= Form(db.dfuiXgeneral0, dbio=False, formstyle=FormStyleBulma)

    if fuiXgeneral0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXgeneral0, db.dfuiXgeneral0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXgeneral0.form_name ))
    elif fuiXgeneral0.errors:
        print("fuiXgeneral0 has errors: %s" % (fuiXgeneral0.errors))
        return put_json_messages('error: ' + str( fuiXgeneral0.form_name ))
 

    return locals()

@action('uiXbuttons', method=["GET", "POST"] )
@action.uses(Template('ui-buttons.html', delimiters='[%[ ]]',), db, session, T,)

def uiXbuttons():
    ctrl_info= "ctrl: uiXbuttons, view: ui-buttons.html"
    page_url = "\'" + URL('uiXbuttons' ) + "\'"
    messages = []

    fuiXbuttons0= Form(db.dfuiXbuttons0, dbio=False, formstyle=FormStyleBulma)

    if fuiXbuttons0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXbuttons0, db.dfuiXbuttons0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXbuttons0.form_name ))
    elif fuiXbuttons0.errors:
        print("fuiXbuttons0 has errors: %s" % (fuiXbuttons0.errors))
        return put_json_messages('error: ' + str( fuiXbuttons0.form_name ))
 

    return locals()

@action('pagesXblank', method=["GET", "POST"] )
@action.uses(Template('pages-blank.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXblank():
    ctrl_info= "ctrl: pagesXblank, view: pages-blank.html"
    page_url = "\'" + URL('pagesXblank' ) + "\'"
    messages = []

    fpagesXblank0= Form(db.dfpagesXblank0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXblank0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXblank0, db.dfpagesXblank0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXblank0.form_name ))
    elif fpagesXblank0.errors:
        print("fpagesXblank0 has errors: %s" % (fpagesXblank0.errors))
        return put_json_messages('error: ' + str( fpagesXblank0.form_name ))
 

    return locals()

@action('mapsXgoogle', method=["GET", "POST"] )
@action.uses(Template('maps-google.html', delimiters='[%[ ]]',), db, session, T,)

def mapsXgoogle():
    ctrl_info= "ctrl: mapsXgoogle, view: maps-google.html"
    page_url = "\'" + URL('mapsXgoogle' ) + "\'"
    messages = []

    fmapsXgoogle0= Form(db.dfmapsXgoogle0, dbio=False, formstyle=FormStyleBulma)

    if fmapsXgoogle0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fmapsXgoogle0, db.dfmapsXgoogle0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fmapsXgoogle0.form_name ))
    elif fmapsXgoogle0.errors:
        print("fmapsXgoogle0 has errors: %s" % (fmapsXgoogle0.errors))
        return put_json_messages('error: ' + str( fmapsXgoogle0.form_name ))
 

    return locals()

@action('uiXtypography', method=["GET", "POST"] )
@action.uses(Template('ui-typography.html', delimiters='[%[ ]]',), db, session, T,)

def uiXtypography():
    ctrl_info= "ctrl: uiXtypography, view: ui-typography.html"
    page_url = "\'" + URL('uiXtypography' ) + "\'"
    messages = []

    fuiXtypography0= Form(db.dfuiXtypography0, dbio=False, formstyle=FormStyleBulma)

    if fuiXtypography0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fuiXtypography0, db.dfuiXtypography0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fuiXtypography0.form_name ))
    elif fuiXtypography0.errors:
        print("fuiXtypography0 has errors: %s" % (fuiXtypography0.errors))
        return put_json_messages('error: ' + str( fuiXtypography0.form_name ))
 

    return locals()

@action('pagesXsignXup', method=["GET", "POST"] )
@action.uses(Template('pages-sign-up.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXsignXup():
    ctrl_info= "ctrl: pagesXsignXup, view: pages-sign-up.html"
    page_url = "\'" + URL('pagesXsignXup' ) + "\'"
    messages = []

    fpagesXsignXup0= Form(db.dfpagesXsignXup0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXsignXup0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXsignXup0, db.dfpagesXsignXup0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXsignXup0.form_name ))
    elif fpagesXsignXup0.errors:
        print("fpagesXsignXup0 has errors: %s" % (fpagesXsignXup0.errors))
        return put_json_messages('error: ' + str( fpagesXsignXup0.form_name ))
 

    return locals()

@action('pagesXsignXin', method=["GET", "POST"] )
@action.uses(Template('pages-sign-in.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXsignXin():
    ctrl_info= "ctrl: pagesXsignXin, view: pages-sign-in.html"
    page_url = "\'" + URL('pagesXsignXin' ) + "\'"
    messages = []

    fpagesXsignXin0= Form(db.dfpagesXsignXin0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXsignXin0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXsignXin0, db.dfpagesXsignXin0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXsignXin0.form_name ))
    elif fpagesXsignXin0.errors:
        print("fpagesXsignXin0 has errors: %s" % (fpagesXsignXin0.errors))
        return put_json_messages('error: ' + str( fpagesXsignXin0.form_name ))
 

    return locals()

@action('pagesXinvoice', method=["GET", "POST"] )
@action.uses(Template('pages-invoice.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXinvoice():
    ctrl_info= "ctrl: pagesXinvoice, view: pages-invoice.html"
    page_url = "\'" + URL('pagesXinvoice' ) + "\'"
    messages = []

    rows_tpagesXinvoice0= db(db.tpagesXinvoice0).select()
    fpagesXinvoice0= Form(db.dfpagesXinvoice0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXinvoice0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXinvoice0, db.dfpagesXinvoice0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXinvoice0.form_name ))
    elif fpagesXinvoice0.errors:
        print("fpagesXinvoice0 has errors: %s" % (fpagesXinvoice0.errors))
        return put_json_messages('error: ' + str( fpagesXinvoice0.form_name ))
 

    return locals()

@action('pagesXprofile', method=["GET", "POST"] )
@action.uses(Template('pages-profile.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXprofile():
    ctrl_info= "ctrl: pagesXprofile, view: pages-profile.html"
    page_url = "\'" + URL('pagesXprofile' ) + "\'"
    messages = []

    fpagesXprofile0= Form(db.dfpagesXprofile0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXprofile0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXprofile0, db.dfpagesXprofile0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXprofile0.form_name ))
    elif fpagesXprofile0.errors:
        print("fpagesXprofile0 has errors: %s" % (fpagesXprofile0.errors))
        return put_json_messages('error: ' + str( fpagesXprofile0.form_name ))
 

    return locals()

@action('formsXlayouts', method=["GET", "POST"] )
@action.uses(Template('forms-layouts.html', delimiters='[%[ ]]',), db, session, T,)

def formsXlayouts():
    ctrl_info= "ctrl: formsXlayouts, view: forms-layouts.html"
    page_url = "\'" + URL('formsXlayouts' ) + "\'"
    messages = []

    fformsXlayouts0= Form(db.dfformsXlayouts0, dbio=False, formstyle=FormStyleBulma)

    if fformsXlayouts0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXlayouts0, db.dfformsXlayouts0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXlayouts0.form_name ))
    elif fformsXlayouts0.errors:
        print("fformsXlayouts0 has errors: %s" % (fformsXlayouts0.errors))
        return put_json_messages('error: ' + str( fformsXlayouts0.form_name ))
 

    fformsXlayouts1= Form(db.dfformsXlayouts1, dbio=False, formstyle=FormStyleBulma)

    if fformsXlayouts1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXlayouts1, db.dfformsXlayouts1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXlayouts1.form_name ))
    elif fformsXlayouts1.errors:
        print("fformsXlayouts1 has errors: %s" % (fformsXlayouts1.errors))
        return put_json_messages('error: ' + str( fformsXlayouts1.form_name ))
 

    fformsXlayouts2= Form(db.dfformsXlayouts2, dbio=False, formstyle=FormStyleBulma)

    if fformsXlayouts2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXlayouts2, db.dfformsXlayouts2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXlayouts2.form_name ))
    elif fformsXlayouts2.errors:
        print("fformsXlayouts2 has errors: %s" % (fformsXlayouts2.errors))
        return put_json_messages('error: ' + str( fformsXlayouts2.form_name ))
 

    fformsXlayouts3= Form(db.dfformsXlayouts3, dbio=False, formstyle=FormStyleBulma)

    if fformsXlayouts3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXlayouts3, db.dfformsXlayouts3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXlayouts3.form_name ))
    elif fformsXlayouts3.errors:
        print("fformsXlayouts3 has errors: %s" % (fformsXlayouts3.errors))
        return put_json_messages('error: ' + str( fformsXlayouts3.form_name ))
 

    fformsXlayouts4= Form(db.dfformsXlayouts4, dbio=False, formstyle=FormStyleBulma)

    if fformsXlayouts4.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXlayouts4, db.dfformsXlayouts4 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXlayouts4.form_name ))
    elif fformsXlayouts4.errors:
        print("fformsXlayouts4 has errors: %s" % (fformsXlayouts4.errors))
        return put_json_messages('error: ' + str( fformsXlayouts4.form_name ))
 

    return locals()

@action('iconsXfeather', method=["GET", "POST"] )
@action.uses(Template('icons-feather.html', delimiters='[%[ ]]',), db, session, T,)

def iconsXfeather():
    ctrl_info= "ctrl: iconsXfeather, view: icons-feather.html"
    page_url = "\'" + URL('iconsXfeather' ) + "\'"
    messages = []

    ficonsXfeather0= Form(db.dficonsXfeather0, dbio=False, formstyle=FormStyleBulma)

    if ficonsXfeather0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ficonsXfeather0, db.dficonsXfeather0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ficonsXfeather0.form_name ))
    elif ficonsXfeather0.errors:
        print("ficonsXfeather0 has errors: %s" % (ficonsXfeather0.errors))
        return put_json_messages('error: ' + str( ficonsXfeather0.form_name ))
 

    return locals()

@action('pagesXsettings', method=["GET", "POST"] )
@action.uses(Template('pages-settings.html', delimiters='[%[ ]]',), db, session, T,)

def pagesXsettings():
    ctrl_info= "ctrl: pagesXsettings, view: pages-settings.html"
    page_url = "\'" + URL('pagesXsettings' ) + "\'"
    messages = []

    fpagesXsettings0= Form(db.dfpagesXsettings0, dbio=False, formstyle=FormStyleBulma)

    if fpagesXsettings0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXsettings0, db.dfpagesXsettings0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXsettings0.form_name ))
    elif fpagesXsettings0.errors:
        print("fpagesXsettings0 has errors: %s" % (fpagesXsettings0.errors))
        return put_json_messages('error: ' + str( fpagesXsettings0.form_name ))
 

    fpagesXsettings1= Form(db.dfpagesXsettings1, dbio=False, formstyle=FormStyleBulma)

    if fpagesXsettings1.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXsettings1, db.dfpagesXsettings1 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXsettings1.form_name ))
    elif fpagesXsettings1.errors:
        print("fpagesXsettings1 has errors: %s" % (fpagesXsettings1.errors))
        return put_json_messages('error: ' + str( fpagesXsettings1.form_name ))
 

    fpagesXsettings2= Form(db.dfpagesXsettings2, dbio=False, formstyle=FormStyleBulma)

    if fpagesXsettings2.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXsettings2, db.dfpagesXsettings2 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXsettings2.form_name ))
    elif fpagesXsettings2.errors:
        print("fpagesXsettings2 has errors: %s" % (fpagesXsettings2.errors))
        return put_json_messages('error: ' + str( fpagesXsettings2.form_name ))
 

    fpagesXsettings3= Form(db.dfpagesXsettings3, dbio=False, formstyle=FormStyleBulma)

    if fpagesXsettings3.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fpagesXsettings3, db.dfpagesXsettings3 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fpagesXsettings3.form_name ))
    elif fpagesXsettings3.errors:
        print("fpagesXsettings3 has errors: %s" % (fpagesXsettings3.errors))
        return put_json_messages('error: ' + str( fpagesXsettings3.form_name ))
 

    return locals()

@action('chartsXchartjs', method=["GET", "POST"] )
@action.uses(Template('charts-chartjs.html', delimiters='[%[ ]]',), db, session, T,)

def chartsXchartjs():
    ctrl_info= "ctrl: chartsXchartjs, view: charts-chartjs.html"
    page_url = "\'" + URL('chartsXchartjs' ) + "\'"
    messages = []

    fchartsXchartjs0= Form(db.dfchartsXchartjs0, dbio=False, formstyle=FormStyleBulma)

    if fchartsXchartjs0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fchartsXchartjs0, db.dfchartsXchartjs0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fchartsXchartjs0.form_name ))
    elif fchartsXchartjs0.errors:
        print("fchartsXchartjs0 has errors: %s" % (fchartsXchartjs0.errors))
        return put_json_messages('error: ' + str( fchartsXchartjs0.form_name ))
 

    return locals()

@action('tablesXbootstrap', method=["GET", "POST"] )
@action.uses(Template('tables-bootstrap.html', delimiters='[%[ ]]',), db, session, T,)

def tablesXbootstrap():
    ctrl_info= "ctrl: tablesXbootstrap, view: tables-bootstrap.html"
    page_url = "\'" + URL('tablesXbootstrap' ) + "\'"
    messages = []

    rows_ttablesXbootstrap0= db(db.ttablesXbootstrap0).select()
    rows_ttablesXbootstrap1= db(db.ttablesXbootstrap1).select()
    rows_ttablesXbootstrap2= db(db.ttablesXbootstrap2).select()
    rows_ttablesXbootstrap3= db(db.ttablesXbootstrap3).select()
    rows_ttablesXbootstrap4= db(db.ttablesXbootstrap4).select()
    rows_ttablesXbootstrap5= db(db.ttablesXbootstrap5).select()
    rows_ttablesXbootstrap6= db(db.ttablesXbootstrap6).select()
    ftablesXbootstrap0= Form(db.dftablesXbootstrap0, dbio=False, formstyle=FormStyleBulma)

    if ftablesXbootstrap0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( ftablesXbootstrap0, db.dftablesXbootstrap0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( ftablesXbootstrap0.form_name ))
    elif ftablesXbootstrap0.errors:
        print("ftablesXbootstrap0 has errors: %s" % (ftablesXbootstrap0.errors))
        return put_json_messages('error: ' + str( ftablesXbootstrap0.form_name ))
 

    return locals()

@action('formsXbasicXinputs', method=["GET", "POST"] )
@action.uses(Template('forms-basic-inputs.html', delimiters='[%[ ]]',), db, session, T,)

def formsXbasicXinputs():
    ctrl_info= "ctrl: formsXbasicXinputs, view: forms-basic-inputs.html"
    page_url = "\'" + URL('formsXbasicXinputs' ) + "\'"
    messages = []

    fformsXbasicXinputs0= Form(db.dfformsXbasicXinputs0, dbio=False, formstyle=FormStyleBulma)

    if fformsXbasicXinputs0.accepted:
        mess1 = 'accepted: ' if prn_form_vars( fformsXbasicXinputs0, db.dfformsXbasicXinputs0 ) == False else 'inserted: '
        return put_json_messages(mess1 + str( fformsXbasicXinputs0.form_name ))
    elif fformsXbasicXinputs0.errors:
        print("fformsXbasicXinputs0 has errors: %s" % (fformsXbasicXinputs0.errors))
        return put_json_messages('error: ' + str( fformsXbasicXinputs0.form_name ))
 

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
# curl -X  GET   http://localhost:8000/kit/api/test_table/
# curl -X  GET   http://localhost:8000/kit/api/test_table/9
# curl -X DELETE  http://localhost:8000/kit/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/kit/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/kit/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/kit/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/kit/api/test_table/
#  http         localhost:8000/kit/api/test_table/9
#  http -f POST localhost:8000/kit/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/kit/api/test_table/2
#  http -f PUT localhost:8000/kit/api/test_table/2 f0=111111 f1=2222222 f2=333333


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

