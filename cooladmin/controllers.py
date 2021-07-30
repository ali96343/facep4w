#
# py4web app, AI-biorex ported 06.05.2021 16:14:35 UTC+3, src: https://github.com/puikinsh/CoolAdmin

#
# https://github.com/ali96343/facep4w py4web apps
#
# http://py4web.com 
# http://py4web.com/_documentation/static/en/index.html 
#
#

import os, json, uuid
from py4web.core import bottle

from py4web import action, request, response,  abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from py4web.core import Template, Reloader
from py4web.utils.dbstore import DBStore
from py4web import Session, Cache, Translator, Flash, DAL

from py4web.utils.url_signer import URLSigner

from yatl.helpers import INPUT, H1, HTML, BODY, A, DIV, SPAN, P
from .common import db, session, T, cache, authenticated, unauthenticated, auth
from .settings import APP_NAME


#
# admin panel at APP_NAME/tabinfo
#
# ---------------------- Global -----------------------------------------------------

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)
url_signer = URLSigner(session)

Glb= {'debug': True , 'my_app_name': APP_NAME, 'tte_path': '/static/tte' }

# ---------------------- Utils -------------------------------------------------------

def insert_form_vars(myform, mytable):

    row_id, table_row, f0_fld = None, None, None

    if Glb['debug'] == True:
        print("app:",Glb['my_app_name'])
        _ = [ print (f'     {k}: {v}') for k,v in myform.vars.items() if k != '_formkey']

    f0_fld = myform.vars.get('f0', None )
    if (not f0_fld is None) and ( type( f0_fld ) in (list, tuple, dict, str, bytes) ) and len(f0_fld):
        row_id = mytable.insert(**mytable._filter_fields(myform.vars))
        db.commit()

        if not row_id is None:
            table_row = mytable(row_id )

            if not table_row is None:
                if Glb['debug'] == True:
                     print( f'     inserted: \"{myform.vars["f0"]}\" into {mytable.f0}, id = {row_id}' )
                     print( f"     selected: \"{table_row.f0}\" from {mytable.f0}, id = {row_id}" )
                     print ()
    else:
        if Glb['debug'] == True:
            print( f"     no entry inserted: (f0_fld is None) or (len(f0_fld) == 0)")
            print()

    return row_id 



@action('callback', method="GET")
# Note that we do not use a template.  This is a JSON API, not a "web page".
@action.uses(url_signer.verify())
def callback():
     print("Called with:", dict(request.params))
     return dict(messages=request.params.echo)

#
def json2user(mess='mymess', icon_type = 'warning', js_alert='sweet2'):
    response.headers["Content-Type"] = "application/json"
    return json.dumps( {'messages' : f'{mess}', 'icon_type': icon_type, 'js_alert': js_alert})

# ---------------------- Controllers  ------------------------------------------------

@action('tab', method=["GET", "POST"] )
@action.uses(db, session, T, Template('tab.html', delimiters='[%[ ]]',))

def tab():
    ctrl_info= { 'c':'tab', 'v':'tab.html' }
    messages = ['tab', 'tab.html']
    #
    ctrl_template_url = "\'" + URL('tab' ) + "\'"

    # 
    ftab0= Form(db.dftab0, dbio=False, formstyle=FormStyleBulma)
    if ftab0.accepted:
        icon_type ='success' if insert_form_vars(ftab0, db.dftab0) else 'info'
        return json2user(mess = str( ftab0.form_name ), icon_type=icon_type )
    elif ftab0.errors:
        print("ftab0 has errors: %s" % (ftab0.errors))
        return json2user(mess = str(ftab0.form_name), icon_type = 'error')

    return locals()

@action('map', method=["GET", "POST"] )
@action.uses(db, session, T, Template('map.html', delimiters='[%[ ]]',))

def map():
    ctrl_info= { 'c':'map', 'v':'map.html' }
    messages = ['map', 'map.html']
    #
    ctrl_template_url = "\'" + URL('map' ) + "\'"

    # 
    fmap0= Form(db.dfmap0, dbio=False, formstyle=FormStyleBulma)
    if fmap0.accepted:
        icon_type ='success' if insert_form_vars(fmap0, db.dfmap0) else 'info'
        return json2user(mess = str( fmap0.form_name ), icon_type=icon_type )
    elif fmap0.errors:
        print("fmap0 has errors: %s" % (fmap0.errors))
        return json2user(mess = str(fmap0.form_name), icon_type = 'error')

    return locals()

@action('form', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form.html', delimiters='[%[ ]]',))

def form():
    ctrl_info= { 'c':'form', 'v':'form.html' }
    messages = ['form', 'form.html']
    #
    ctrl_template_url = "\'" + URL('form' ) + "\'"

    # 
    fform0= Form(db.dfform0, dbio=False, formstyle=FormStyleBulma)
    if fform0.accepted:
        icon_type ='success' if insert_form_vars(fform0, db.dfform0) else 'info'
        return json2user(mess = str( fform0.form_name ), icon_type=icon_type )
    elif fform0.errors:
        print("fform0 has errors: %s" % (fform0.errors))
        return json2user(mess = str(fform0.form_name), icon_type = 'error')

    # 
    fform1= Form(db.dfform1, dbio=False, formstyle=FormStyleBulma)
    if fform1.accepted:
        icon_type ='success' if insert_form_vars(fform1, db.dfform1) else 'info'
        return json2user(mess = str( fform1.form_name ), icon_type=icon_type )
    elif fform1.errors:
        print("fform1 has errors: %s" % (fform1.errors))
        return json2user(mess = str(fform1.form_name), icon_type = 'error')

    # 
    fform2= Form(db.dfform2, dbio=False, formstyle=FormStyleBulma)
    if fform2.accepted:
        icon_type ='success' if insert_form_vars(fform2, db.dfform2) else 'info'
        return json2user(mess = str( fform2.form_name ), icon_type=icon_type )
    elif fform2.errors:
        print("fform2 has errors: %s" % (fform2.errors))
        return json2user(mess = str(fform2.form_name), icon_type = 'error')

    # 
    fform3= Form(db.dfform3, dbio=False, formstyle=FormStyleBulma)
    if fform3.accepted:
        icon_type ='success' if insert_form_vars(fform3, db.dfform3) else 'info'
        return json2user(mess = str( fform3.form_name ), icon_type=icon_type )
    elif fform3.errors:
        print("fform3 has errors: %s" % (fform3.errors))
        return json2user(mess = str(fform3.form_name), icon_type = 'error')

    # 
    fform4= Form(db.dfform4, dbio=False, formstyle=FormStyleBulma)
    if fform4.accepted:
        icon_type ='success' if insert_form_vars(fform4, db.dfform4) else 'info'
        return json2user(mess = str( fform4.form_name ), icon_type=icon_type )
    elif fform4.errors:
        print("fform4 has errors: %s" % (fform4.errors))
        return json2user(mess = str(fform4.form_name), icon_type = 'error')

    # 
    fform5= Form(db.dfform5, dbio=False, formstyle=FormStyleBulma)
    if fform5.accepted:
        icon_type ='success' if insert_form_vars(fform5, db.dfform5) else 'info'
        return json2user(mess = str( fform5.form_name ), icon_type=icon_type )
    elif fform5.errors:
        print("fform5 has errors: %s" % (fform5.errors))
        return json2user(mess = str(fform5.form_name), icon_type = 'error')

    # 
    fform6= Form(db.dfform6, dbio=False, formstyle=FormStyleBulma)
    if fform6.accepted:
        icon_type ='success' if insert_form_vars(fform6, db.dfform6) else 'info'
        return json2user(mess = str( fform6.form_name ), icon_type=icon_type )
    elif fform6.errors:
        print("fform6 has errors: %s" % (fform6.errors))
        return json2user(mess = str(fform6.form_name), icon_type = 'error')

    # 
    fform7= Form(db.dfform7, dbio=False, formstyle=FormStyleBulma)
    if fform7.accepted:
        icon_type ='success' if insert_form_vars(fform7, db.dfform7) else 'info'
        return json2user(mess = str( fform7.form_name ), icon_type=icon_type )
    elif fform7.errors:
        print("fform7 has errors: %s" % (fform7.errors))
        return json2user(mess = str(fform7.form_name), icon_type = 'error')

    # 
    fform8= Form(db.dfform8, dbio=False, formstyle=FormStyleBulma)
    if fform8.accepted:
        icon_type ='success' if insert_form_vars(fform8, db.dfform8) else 'info'
        return json2user(mess = str( fform8.form_name ), icon_type=icon_type )
    elif fform8.errors:
        print("fform8 has errors: %s" % (fform8.errors))
        return json2user(mess = str(fform8.form_name), icon_type = 'error')

    # 
    fform9= Form(db.dfform9, dbio=False, formstyle=FormStyleBulma)
    if fform9.accepted:
        icon_type ='success' if insert_form_vars(fform9, db.dfform9) else 'info'
        return json2user(mess = str( fform9.form_name ), icon_type=icon_type )
    elif fform9.errors:
        print("fform9 has errors: %s" % (fform9.errors))
        return json2user(mess = str(fform9.form_name), icon_type = 'error')

    # 
    fform10= Form(db.dfform10, dbio=False, formstyle=FormStyleBulma)
    if fform10.accepted:
        icon_type ='success' if insert_form_vars(fform10, db.dfform10) else 'info'
        return json2user(mess = str( fform10.form_name ), icon_type=icon_type )
    elif fform10.errors:
        print("fform10 has errors: %s" % (fform10.errors))
        return json2user(mess = str(fform10.form_name), icon_type = 'error')

    # 
    fform11= Form(db.dfform11, dbio=False, formstyle=FormStyleBulma)
    if fform11.accepted:
        icon_type ='success' if insert_form_vars(fform11, db.dfform11) else 'info'
        return json2user(mess = str( fform11.form_name ), icon_type=icon_type )
    elif fform11.errors:
        print("fform11 has errors: %s" % (fform11.errors))
        return json2user(mess = str(fform11.form_name), icon_type = 'error')

    # 
    fform12= Form(db.dfform12, dbio=False, formstyle=FormStyleBulma)
    if fform12.accepted:
        icon_type ='success' if insert_form_vars(fform12, db.dfform12) else 'info'
        return json2user(mess = str( fform12.form_name ), icon_type=icon_type )
    elif fform12.errors:
        print("fform12 has errors: %s" % (fform12.errors))
        return json2user(mess = str(fform12.form_name), icon_type = 'error')

    # 
    fform13= Form(db.dfform13, dbio=False, formstyle=FormStyleBulma)
    if fform13.accepted:
        icon_type ='success' if insert_form_vars(fform13, db.dfform13) else 'info'
        return json2user(mess = str( fform13.form_name ), icon_type=icon_type )
    elif fform13.errors:
        print("fform13 has errors: %s" % (fform13.errors))
        return json2user(mess = str(fform13.form_name), icon_type = 'error')

    # 
    fform14= Form(db.dfform14, dbio=False, formstyle=FormStyleBulma)
    if fform14.accepted:
        icon_type ='success' if insert_form_vars(fform14, db.dfform14) else 'info'
        return json2user(mess = str( fform14.form_name ), icon_type=icon_type )
    elif fform14.errors:
        print("fform14 has errors: %s" % (fform14.errors))
        return json2user(mess = str(fform14.form_name), icon_type = 'error')

    # 
    fform15= Form(db.dfform15, dbio=False, formstyle=FormStyleBulma)
    if fform15.accepted:
        icon_type ='success' if insert_form_vars(fform15, db.dfform15) else 'info'
        return json2user(mess = str( fform15.form_name ), icon_type=icon_type )
    elif fform15.errors:
        print("fform15 has errors: %s" % (fform15.errors))
        return json2user(mess = str(fform15.form_name), icon_type = 'error')

    return locals()

@action('typo', method=["GET", "POST"] )
@action.uses(db, session, T, Template('typo.html', delimiters='[%[ ]]',))

def typo():
    ctrl_info= { 'c':'typo', 'v':'typo.html' }
    messages = ['typo', 'typo.html']
    #
    ctrl_template_url = "\'" + URL('typo' ) + "\'"

    # 
    ftypo0= Form(db.dftypo0, dbio=False, formstyle=FormStyleBulma)
    if ftypo0.accepted:
        icon_type ='success' if insert_form_vars(ftypo0, db.dftypo0) else 'info'
        return json2user(mess = str( ftypo0.form_name ), icon_type=icon_type )
    elif ftypo0.errors:
        print("ftypo0 has errors: %s" % (ftypo0.errors))
        return json2user(mess = str(ftypo0.form_name), icon_type = 'error')

    return locals()

@action('grid', method=["GET", "POST"] )
@action.uses(db, session, T, Template('grid.html', delimiters='[%[ ]]',))

def grid():
    ctrl_info= { 'c':'grid', 'v':'grid.html' }
    messages = ['grid', 'grid.html']
    #
    ctrl_template_url = "\'" + URL('grid' ) + "\'"

    # 
    fgrid0= Form(db.dfgrid0, dbio=False, formstyle=FormStyleBulma)
    if fgrid0.accepted:
        icon_type ='success' if insert_form_vars(fgrid0, db.dfgrid0) else 'info'
        return json2user(mess = str( fgrid0.form_name ), icon_type=icon_type )
    elif fgrid0.errors:
        print("fgrid0 has errors: %s" % (fgrid0.errors))
        return json2user(mess = str(fgrid0.form_name), icon_type = 'error')

    return locals()

@action('card', method=["GET", "POST"] )
@action.uses(db, session, T, Template('card.html', delimiters='[%[ ]]',))

def card():
    ctrl_info= { 'c':'card', 'v':'card.html' }
    messages = ['card', 'card.html']
    #
    ctrl_template_url = "\'" + URL('card' ) + "\'"

    # 
    fcard0= Form(db.dfcard0, dbio=False, formstyle=FormStyleBulma)
    if fcard0.accepted:
        icon_type ='success' if insert_form_vars(fcard0, db.dfcard0) else 'info'
        return json2user(mess = str( fcard0.form_name ), icon_type=icon_type )
    elif fcard0.errors:
        print("fcard0 has errors: %s" % (fcard0.errors))
        return json2user(mess = str(fcard0.form_name), icon_type = 'error')

    return locals()

@action('inbox', method=["GET", "POST"] )
@action.uses(db, session, T, Template('inbox.html', delimiters='[%[ ]]',))

def inbox():
    ctrl_info= { 'c':'inbox', 'v':'inbox.html' }
    messages = ['inbox', 'inbox.html']
    #
    ctrl_template_url = "\'" + URL('inbox' ) + "\'"

    # 
    finbox0= Form(db.dfinbox0, dbio=False, formstyle=FormStyleBulma)
    if finbox0.accepted:
        icon_type ='success' if insert_form_vars(finbox0, db.dfinbox0) else 'info'
        return json2user(mess = str( finbox0.form_name ), icon_type=icon_type )
    elif finbox0.errors:
        print("finbox0 has errors: %s" % (finbox0.errors))
        return json2user(mess = str(finbox0.form_name), icon_type = 'error')

    # 
    finbox1= Form(db.dfinbox1, dbio=False, formstyle=FormStyleBulma)
    if finbox1.accepted:
        icon_type ='success' if insert_form_vars(finbox1, db.dfinbox1) else 'info'
        return json2user(mess = str( finbox1.form_name ), icon_type=icon_type )
    elif finbox1.errors:
        print("finbox1 has errors: %s" % (finbox1.errors))
        return json2user(mess = str(finbox1.form_name), icon_type = 'error')

    # 
    finbox2= Form(db.dfinbox2, dbio=False, formstyle=FormStyleBulma)
    if finbox2.accepted:
        icon_type ='success' if insert_form_vars(finbox2, db.dfinbox2) else 'info'
        return json2user(mess = str( finbox2.form_name ), icon_type=icon_type )
    elif finbox2.errors:
        print("finbox2 has errors: %s" % (finbox2.errors))
        return json2user(mess = str(finbox2.form_name), icon_type = 'error')

    return locals()

@action('table', method=["GET", "POST"] )
@action.uses(db, session, T, Template('table.html', delimiters='[%[ ]]',))

def table():
    ctrl_info= { 'c':'table', 'v':'table.html' }
    messages = ['table', 'table.html']
    #
    ctrl_template_url = "\'" + URL('table' ) + "\'"

    rows_ttable0= db(db.ttable0).select()
    rows_ttable1= db(db.ttable1).select()
    rows_ttable2= db(db.ttable2).select()
    rows_ttable3= db(db.ttable3).select()
    rows_ttable4= db(db.ttable4).select()
    rows_ttable5= db(db.ttable5).select()
    # 
    ftable0= Form(db.dftable0, dbio=False, formstyle=FormStyleBulma)
    if ftable0.accepted:
        icon_type ='success' if insert_form_vars(ftable0, db.dftable0) else 'info'
        return json2user(mess = str( ftable0.form_name ), icon_type=icon_type )
    elif ftable0.errors:
        print("ftable0 has errors: %s" % (ftable0.errors))
        return json2user(mess = str(ftable0.form_name), icon_type = 'error')

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index.html', delimiters='[%[ ]]',))

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    messages = ['index', 'index.html']
    #
    ctrl_template_url = "\'" + URL('index' ) + "\'"

    rows_tindex0= db(db.tindex0).select()
    rows_tindex1= db(db.tindex1).select()
    # 
    findex0= Form(db.dfindex0, dbio=False, formstyle=FormStyleBulma)
    if findex0.accepted:
        icon_type ='success' if insert_form_vars(findex0, db.dfindex0) else 'info'
        return json2user(mess = str( findex0.form_name ), icon_type=icon_type )
    elif findex0.errors:
        print("findex0 has errors: %s" % (findex0.errors))
        return json2user(mess = str(findex0.form_name), icon_type = 'error')

    # 
    findex1= Form(db.dfindex1, dbio=False, formstyle=FormStyleBulma)
    if findex1.accepted:
        icon_type ='success' if insert_form_vars(findex1, db.dfindex1) else 'info'
        return json2user(mess = str( findex1.form_name ), icon_type=icon_type )
    elif findex1.errors:
        print("findex1 has errors: %s" % (findex1.errors))
        return json2user(mess = str(findex1.form_name), icon_type = 'error')

    return locals()

@action('modal', method=["GET", "POST"] )
@action.uses(db, session, T, Template('modal.html', delimiters='[%[ ]]',))

def modal():
    ctrl_info= { 'c':'modal', 'v':'modal.html' }
    messages = ['modal', 'modal.html']
    #
    ctrl_template_url = "\'" + URL('modal' ) + "\'"

    # 
    fmodal0= Form(db.dfmodal0, dbio=False, formstyle=FormStyleBulma)
    if fmodal0.accepted:
        icon_type ='success' if insert_form_vars(fmodal0, db.dfmodal0) else 'info'
        return json2user(mess = str( fmodal0.form_name ), icon_type=icon_type )
    elif fmodal0.errors:
        print("fmodal0 has errors: %s" % (fmodal0.errors))
        return json2user(mess = str(fmodal0.form_name), icon_type = 'error')

    return locals()

@action('loginA', method=["GET", "POST"] )
@action.uses(db, session, T, Template('login.html', delimiters='[%[ ]]',))

def loginA():
    ctrl_info= { 'c':'loginA', 'v':'login.html' }
    messages = ['loginA', 'login.html']
    #
    ctrl_template_url = "\'" + URL('loginA' ) + "\'"

    # 
    floginA0= Form(db.dfloginA0, dbio=False, formstyle=FormStyleBulma)
    if floginA0.accepted:
        icon_type ='success' if insert_form_vars(floginA0, db.dfloginA0) else 'info'
        return json2user(mess = str( floginA0.form_name ), icon_type=icon_type )
    elif floginA0.errors:
        print("floginA0 has errors: %s" % (floginA0.errors))
        return json2user(mess = str(floginA0.form_name), icon_type = 'error')

    return locals()

@action('chart', method=["GET", "POST"] )
@action.uses(db, session, T, Template('chart.html', delimiters='[%[ ]]',))

def chart():
    ctrl_info= { 'c':'chart', 'v':'chart.html' }
    messages = ['chart', 'chart.html']
    #
    ctrl_template_url = "\'" + URL('chart' ) + "\'"

    # 
    fchart0= Form(db.dfchart0, dbio=False, formstyle=FormStyleBulma)
    if fchart0.accepted:
        icon_type ='success' if insert_form_vars(fchart0, db.dfchart0) else 'info'
        return json2user(mess = str( fchart0.form_name ), icon_type=icon_type )
    elif fchart0.errors:
        print("fchart0 has errors: %s" % (fchart0.errors))
        return json2user(mess = str(fchart0.form_name), icon_type = 'error')

    return locals()

@action('badge', method=["GET", "POST"] )
@action.uses(db, session, T, Template('badge.html', delimiters='[%[ ]]',))

def badge():
    ctrl_info= { 'c':'badge', 'v':'badge.html' }
    messages = ['badge', 'badge.html']
    #
    ctrl_template_url = "\'" + URL('badge' ) + "\'"

    # 
    fbadge0= Form(db.dfbadge0, dbio=False, formstyle=FormStyleBulma)
    if fbadge0.accepted:
        icon_type ='success' if insert_form_vars(fbadge0, db.dfbadge0) else 'info'
        return json2user(mess = str( fbadge0.form_name ), icon_type=icon_type )
    elif fbadge0.errors:
        print("fbadge0 has errors: %s" % (fbadge0.errors))
        return json2user(mess = str(fbadge0.form_name), icon_type = 'error')

    return locals()

@action('alert', method=["GET", "POST"] )
@action.uses(db, session, T, Template('alert.html', delimiters='[%[ ]]',))

def alert():
    ctrl_info= { 'c':'alert', 'v':'alert.html' }
    messages = ['alert', 'alert.html']
    #
    ctrl_template_url = "\'" + URL('alert' ) + "\'"

    # 
    falert0= Form(db.dfalert0, dbio=False, formstyle=FormStyleBulma)
    if falert0.accepted:
        icon_type ='success' if insert_form_vars(falert0, db.dfalert0) else 'info'
        return json2user(mess = str( falert0.form_name ), icon_type=icon_type )
    elif falert0.errors:
        print("falert0 has errors: %s" % (falert0.errors))
        return json2user(mess = str(falert0.form_name), icon_type = 'error')

    return locals()

@action('switch', method=["GET", "POST"] )
@action.uses(db, session, T, Template('switch.html', delimiters='[%[ ]]',))

def switch():
    ctrl_info= { 'c':'switch', 'v':'switch.html' }
    messages = ['switch', 'switch.html']
    #
    ctrl_template_url = "\'" + URL('switch' ) + "\'"

    rows_tswitch0= db(db.tswitch0).select()
    # 
    fswitch0= Form(db.dfswitch0, dbio=False, formstyle=FormStyleBulma)
    if fswitch0.accepted:
        icon_type ='success' if insert_form_vars(fswitch0, db.dfswitch0) else 'info'
        return json2user(mess = str( fswitch0.form_name ), icon_type=icon_type )
    elif fswitch0.errors:
        print("fswitch0 has errors: %s" % (fswitch0.errors))
        return json2user(mess = str(fswitch0.form_name), icon_type = 'error')

    return locals()

@action('button', method=["GET", "POST"] )
@action.uses(db, session, T, Template('button.html', delimiters='[%[ ]]',))

def button():
    ctrl_info= { 'c':'button', 'v':'button.html' }
    messages = ['button', 'button.html']
    #
    ctrl_template_url = "\'" + URL('button' ) + "\'"

    # 
    fbutton0= Form(db.dfbutton0, dbio=False, formstyle=FormStyleBulma)
    if fbutton0.accepted:
        icon_type ='success' if insert_form_vars(fbutton0, db.dfbutton0) else 'info'
        return json2user(mess = str( fbutton0.form_name ), icon_type=icon_type )
    elif fbutton0.errors:
        print("fbutton0 has errors: %s" % (fbutton0.errors))
        return json2user(mess = str(fbutton0.form_name), icon_type = 'error')

    return locals()

@action('index4', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index4.html', delimiters='[%[ ]]',))

def index4():
    ctrl_info= { 'c':'index4', 'v':'index4.html' }
    messages = ['index4', 'index4.html']
    #
    ctrl_template_url = "\'" + URL('index4' ) + "\'"

    rows_tindex40= db(db.tindex40).select()
    # 
    findex40= Form(db.dfindex40, dbio=False, formstyle=FormStyleBulma)
    if findex40.accepted:
        icon_type ='success' if insert_form_vars(findex40, db.dfindex40) else 'info'
        return json2user(mess = str( findex40.form_name ), icon_type=icon_type )
    elif findex40.errors:
        print("findex40 has errors: %s" % (findex40.errors))
        return json2user(mess = str(findex40.form_name), icon_type = 'error')

    # 
    findex41= Form(db.dfindex41, dbio=False, formstyle=FormStyleBulma)
    if findex41.accepted:
        icon_type ='success' if insert_form_vars(findex41, db.dfindex41) else 'info'
        return json2user(mess = str( findex41.form_name ), icon_type=icon_type )
    elif findex41.errors:
        print("findex41 has errors: %s" % (findex41.errors))
        return json2user(mess = str(findex41.form_name), icon_type = 'error')

    return locals()

@action('index3', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index3.html', delimiters='[%[ ]]',))

def index3():
    ctrl_info= { 'c':'index3', 'v':'index3.html' }
    messages = ['index3', 'index3.html']
    #
    ctrl_template_url = "\'" + URL('index3' ) + "\'"

    # 
    findex30= Form(db.dfindex30, dbio=False, formstyle=FormStyleBulma)
    if findex30.accepted:
        icon_type ='success' if insert_form_vars(findex30, db.dfindex30) else 'info'
        return json2user(mess = str( findex30.form_name ), icon_type=icon_type )
    elif findex30.errors:
        print("findex30 has errors: %s" % (findex30.errors))
        return json2user(mess = str(findex30.form_name), icon_type = 'error')

    return locals()

@action('index2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index2.html', delimiters='[%[ ]]',))

def index2():
    ctrl_info= { 'c':'index2', 'v':'index2.html' }
    messages = ['index2', 'index2.html']
    #
    ctrl_template_url = "\'" + URL('index2' ) + "\'"

    rows_tindex20= db(db.tindex20).select()
    rows_tindex21= db(db.tindex21).select()
    rows_tindex22= db(db.tindex22).select()
    # 
    findex20= Form(db.dfindex20, dbio=False, formstyle=FormStyleBulma)
    if findex20.accepted:
        icon_type ='success' if insert_form_vars(findex20, db.dfindex20) else 'info'
        return json2user(mess = str( findex20.form_name ), icon_type=icon_type )
    elif findex20.errors:
        print("findex20 has errors: %s" % (findex20.errors))
        return json2user(mess = str(findex20.form_name), icon_type = 'error')

    return locals()

@action('registerA', method=["GET", "POST"] )
@action.uses(db, session, T, Template('register.html', delimiters='[%[ ]]',))

def registerA():
    ctrl_info= { 'c':'registerA', 'v':'register.html' }
    messages = ['registerA', 'register.html']
    #
    ctrl_template_url = "\'" + URL('registerA' ) + "\'"

    # 
    fregisterA0= Form(db.dfregisterA0, dbio=False, formstyle=FormStyleBulma)
    if fregisterA0.accepted:
        icon_type ='success' if insert_form_vars(fregisterA0, db.dfregisterA0) else 'info'
        return json2user(mess = str( fregisterA0.form_name ), icon_type=icon_type )
    elif fregisterA0.errors:
        print("fregisterA0 has errors: %s" % (fregisterA0.errors))
        return json2user(mess = str(fregisterA0.form_name), icon_type = 'error')

    return locals()

@action('calendar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('calendar.html', delimiters='[%[ ]]',))

def calendar():
    ctrl_info= { 'c':'calendar', 'v':'calendar.html' }
    messages = ['calendar', 'calendar.html']
    #
    ctrl_template_url = "\'" + URL('calendar' ) + "\'"

    # 
    fcalendar0= Form(db.dfcalendar0, dbio=False, formstyle=FormStyleBulma)
    if fcalendar0.accepted:
        icon_type ='success' if insert_form_vars(fcalendar0, db.dfcalendar0) else 'info'
        return json2user(mess = str( fcalendar0.form_name ), icon_type=icon_type )
    elif fcalendar0.errors:
        print("fcalendar0 has errors: %s" % (fcalendar0.errors))
        return json2user(mess = str(fcalendar0.form_name), icon_type = 'error')

    return locals()

@action('fontawesome', method=["GET", "POST"] )
@action.uses(db, session, T, Template('fontawesome.html', delimiters='[%[ ]]',))

def fontawesome():
    ctrl_info= { 'c':'fontawesome', 'v':'fontawesome.html' }
    messages = ['fontawesome', 'fontawesome.html']
    #
    ctrl_template_url = "\'" + URL('fontawesome' ) + "\'"

    # 
    ffontawesome0= Form(db.dffontawesome0, dbio=False, formstyle=FormStyleBulma)
    if ffontawesome0.accepted:
        icon_type ='success' if insert_form_vars(ffontawesome0, db.dffontawesome0) else 'info'
        return json2user(mess = str( ffontawesome0.form_name ), icon_type=icon_type )
    elif ffontawesome0.errors:
        print("ffontawesome0 has errors: %s" % (ffontawesome0.errors))
        return json2user(mess = str(ffontawesome0.form_name), icon_type = 'error')

    return locals()

@action('forgetXpass', method=["GET", "POST"] )
@action.uses(db, session, T, Template('forget-pass.html', delimiters='[%[ ]]',))

def forgetXpass():
    ctrl_info= { 'c':'forgetXpass', 'v':'forget-pass.html' }
    messages = ['forgetXpass', 'forget-pass.html']
    #
    ctrl_template_url = "\'" + URL('forgetXpass' ) + "\'"

    # 
    fforgetXpass0= Form(db.dfforgetXpass0, dbio=False, formstyle=FormStyleBulma)
    if fforgetXpass0.accepted:
        icon_type ='success' if insert_form_vars(fforgetXpass0, db.dfforgetXpass0) else 'info'
        return json2user(mess = str( fforgetXpass0.form_name ), icon_type=icon_type )
    elif fforgetXpass0.errors:
        print("fforgetXpass0 has errors: %s" % (fforgetXpass0.errors))
        return json2user(mess = str(fforgetXpass0.form_name), icon_type = 'error')

    return locals()

@action('progressXbar', method=["GET", "POST"] )
@action.uses(db, session, T, Template('progress-bar.html', delimiters='[%[ ]]',))

def progressXbar():
    ctrl_info= { 'c':'progressXbar', 'v':'progress-bar.html' }
    messages = ['progressXbar', 'progress-bar.html']
    #
    ctrl_template_url = "\'" + URL('progressXbar' ) + "\'"

    # 
    fprogressXbar0= Form(db.dfprogressXbar0, dbio=False, formstyle=FormStyleBulma)
    if fprogressXbar0.accepted:
        icon_type ='success' if insert_form_vars(fprogressXbar0, db.dfprogressXbar0) else 'info'
        return json2user(mess = str( fprogressXbar0.form_name ), icon_type=icon_type )
    elif fprogressXbar0.errors:
        print("fprogressXbar0 has errors: %s" % (fprogressXbar0.errors))
        return json2user(mess = str(fprogressXbar0.form_name), icon_type = 'error')

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
# curl -X  GET   http://localhost:8000/cooladmin/api/test_table/
# curl -X  GET   http://localhost:8000/cooladmin/api/test_table/9
# curl -X DELETE  http://localhost:8000/cooladmin/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/cooladmin/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/cooladmin/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/cooladmin/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/cooladmin/api/test_table/
#  http         localhost:8000/cooladmin/api/test_table/9
#  http -f POST localhost:8000/cooladmin/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/cooladmin/api/test_table/2
#  http -f PUT localhost:8000/cooladmin/api/test_table/2 f0=111111 f1=2222222 f2=333333

#------------------------------------------------------------------------------------
#curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://rest-api.io/items
#curl -i -X PUT -H 'Content-Type: application/json' -d '{"name": "Updated item", "year": "2010"}' http://rest-api.io/items/5069b47aa892630aae059584






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

# this code is not necessary for modern py4web 
#
#        files_prefix = location + Glb["tte_path"]
#
#        location_2x = location + location + "/"
#        files_prefix_2x = files_prefix + files_prefix + "/"
#
#        def rm_bad_prefix(bad_prefix):
#            new_location = bottle.request.path.replace(bad_prefix, "", 1)
#            Glb["debug"] and func_mess.append(f"     rm_bad_prefix: {bad_prefix}")
#            return new_location
#
#        if bottle.request.path.startswith(files_prefix_2x):
#            if len(bottle.request.path) > len(files_prefix_2x):
#                location = rm_bad_prefix(files_prefix)
#
#        elif bottle.request.path.startswith(location_2x):
#            if len(bottle.request.path) > len(location_2x):
#                location = rm_bad_prefix(location)

    if Glb["debug"]:
        debug_mess = [  f"404  app=/{Glb['my_app_name']}, err_path={bottle.request.path}",
                        f"     info: {error}", ]
        if len(func_mess):
            debug_mess += func_mess
        debug_mess.append(f"     goto_new_path: {location}\n")
        print("\n".join(debug_mess))

    bottle.response.status = 303
    bottle.response.set_header("Location", location)


# -------------------- tabinfo: my backend ------------------------------------

from .atab_utils import mytab_grid
from .images_utils import ima_grid
from .upload_utils import p4wupload_file
from .tlist_utils import tlist 

@unauthenticated("tabinfo", "tabinfo.html")
def tabinfo():
    user = auth.get_user()
    # simple backand-admin-panel (to be continued)
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    menu = DIV(
               P( SPAN(f"app: {APP_NAME}", _style="color:red"),  " admin-panel"),
               A( "tlist", _role="button", _href=URL('tlist', ),) ,
               A( "app_images", _role="button", _href=URL('ima_grid', ),) ,
               A( "p4wupload_file", _role="button", _href=URL('p4wupload_file', ),) ,
               A( "sql2table", _role="button", _href=URL('mytab_grid', ),) ,
              )
    return dict(message=message, menu=menu)

