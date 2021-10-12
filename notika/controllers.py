#
# py4web app, AI-biorex ported 12.10.2021 15:22:50 UTC+3, src: https://github.com/puikinsh/notika
#
# https://github.com/ali96343/facep4w py4web apps
#
# http://py4web.com 
# http://py4web.com/_documentation/static/en/index.html 
#
#

import os, json, uuid
#
try:
   import ombott as bottle
except ImportError:
   import bottle
   #from py4web.core import bottle

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

Glb= {'debug': True , 'my_app_name': APP_NAME, 'tte_path': '/static/tte', }

# ---------------------- Utils -------------------------------------------------------

def get_ctrl_url(ctrl_nm):
    return "\'" + URL(ctrl_nm) + "\'"

def insert_form_vars(myform, mytable):

    ( row_id, table_row, f0_fld) = ( None, None, None )

    if Glb['debug'] == True:
        print("app:",Glb['my_app_name'])
        _ = [ print (f'     {k}: {v}') for k,v in myform.vars.items() if k != '_formkey']

    f0_name  = [ e for e in mytable.fields if e != 'id' ][0]
    f0_value = myform.vars.get( f0_name  , None )

    if f0_value and ( type( f0_value ) in (str, bytes, list, tuple, dict,) ) and len(f0_value):
        row_id = mytable.insert(**mytable._filter_fields(myform.vars))
        db.commit()

        if row_id:
            table_row = mytable(row_id )

            if table_row:
                if Glb['debug']:
                     print(f'     insert: \"{myform.vars[f0_name]}\" into {mytable[f0_name]}, id = {row_id}' )
                     print(f"     select: \"{table_row[f0_name]}\" from {mytable[f0_name]}, id = {row_id}" )
                     print ()
    else:
        if Glb['debug']:
            print( f"     no entry inserted: (f0_value is None) or (len(f0_value) == 0)")
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

@action('X404', method=["GET", "POST"] )
@action.uses(db, session, T, Template('404.html', delimiters='[%[ ]]',))

def X404():
    ctrl_info= { 'c':'X404', 'v':'404.html' }
    messages = ['X404', '404.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('X404') 


    return locals()

@action('tabs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('tabs.html', delimiters='[%[ ]]',))

def tabs():
    ctrl_info= { 'c':'tabs', 'v':'tabs.html' }
    messages = ['tabs', 'tabs.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('tabs') 


    # 
    ftabs0= Form(db.dftabs0, dbio=False, formstyle=FormStyleBulma)
    if ftabs0.accepted:
        icon_type ='success' if insert_form_vars(ftabs0, db.dftabs0) else 'info'
        return json2user(mess = str( ftabs0.form_name ), icon_type=icon_type )
    elif ftabs0.errors:
        print(f"ftabs0 has errors: {ftabs0.errors}")
        return json2user(mess = str(ftabs0.form_name), icon_type = 'error')

    # 
    ftabs1= Form(db.dftabs1, dbio=False, formstyle=FormStyleBulma)
    if ftabs1.accepted:
        icon_type ='success' if insert_form_vars(ftabs1, db.dftabs1) else 'info'
        return json2user(mess = str( ftabs1.form_name ), icon_type=icon_type )
    elif ftabs1.errors:
        print(f"ftabs1 has errors: {ftabs1.errors}")
        return json2user(mess = str(ftabs1.form_name), icon_type = 'error')

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index.html', delimiters='[%[ ]]',))

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    messages = ['index', 'index.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('index') 


    rows_tindex0= db(db.tindex0).select()
    # 
    findex0= Form(db.dfindex0, dbio=False, formstyle=FormStyleBulma)
    if findex0.accepted:
        icon_type ='success' if insert_form_vars(findex0, db.dfindex0) else 'info'
        return json2user(mess = str( findex0.form_name ), icon_type=icon_type )
    elif findex0.errors:
        print(f"findex0 has errors: {findex0.errors}")
        return json2user(mess = str(findex0.form_name), icon_type = 'error')

    # 
    findex1= Form(db.dfindex1, dbio=False, formstyle=FormStyleBulma)
    if findex1.accepted:
        icon_type ='success' if insert_form_vars(findex1, db.dfindex1) else 'info'
        return json2user(mess = str( findex1.form_name ), icon_type=icon_type )
    elif findex1.errors:
        print(f"findex1 has errors: {findex1.errors}")
        return json2user(mess = str(findex1.form_name), icon_type = 'error')

    # 
    findex2= Form(db.dfindex2, dbio=False, formstyle=FormStyleBulma)
    if findex2.accepted:
        icon_type ='success' if insert_form_vars(findex2, db.dfindex2) else 'info'
        return json2user(mess = str( findex2.form_name ), icon_type=icon_type )
    elif findex2.errors:
        print(f"findex2 has errors: {findex2.errors}")
        return json2user(mess = str(findex2.form_name), icon_type = 'error')

    # 
    findex3= Form(db.dfindex3, dbio=False, formstyle=FormStyleBulma)
    if findex3.accepted:
        icon_type ='success' if insert_form_vars(findex3, db.dfindex3) else 'info'
        return json2user(mess = str( findex3.form_name ), icon_type=icon_type )
    elif findex3.errors:
        print(f"findex3 has errors: {findex3.errors}")
        return json2user(mess = str(findex3.form_name), icon_type = 'error')

    # 
    findex4= Form(db.dfindex4, dbio=False, formstyle=FormStyleBulma)
    if findex4.accepted:
        icon_type ='success' if insert_form_vars(findex4, db.dfindex4) else 'info'
        return json2user(mess = str( findex4.form_name ), icon_type=icon_type )
    elif findex4.errors:
        print(f"findex4 has errors: {findex4.errors}")
        return json2user(mess = str(findex4.form_name), icon_type = 'error')

    # 
    findex5= Form(db.dfindex5, dbio=False, formstyle=FormStyleBulma)
    if findex5.accepted:
        icon_type ='success' if insert_form_vars(findex5, db.dfindex5) else 'info'
        return json2user(mess = str( findex5.form_name ), icon_type=icon_type )
    elif findex5.errors:
        print(f"findex5 has errors: {findex5.errors}")
        return json2user(mess = str(findex5.form_name), icon_type = 'error')

    # 
    findex6= Form(db.dfindex6, dbio=False, formstyle=FormStyleBulma)
    if findex6.accepted:
        icon_type ='success' if insert_form_vars(findex6, db.dfindex6) else 'info'
        return json2user(mess = str( findex6.form_name ), icon_type=icon_type )
    elif findex6.errors:
        print(f"findex6 has errors: {findex6.errors}")
        return json2user(mess = str(findex6.form_name), icon_type = 'error')

    # 
    findex7= Form(db.dfindex7, dbio=False, formstyle=FormStyleBulma)
    if findex7.accepted:
        icon_type ='success' if insert_form_vars(findex7, db.dfindex7) else 'info'
        return json2user(mess = str( findex7.form_name ), icon_type=icon_type )
    elif findex7.errors:
        print(f"findex7 has errors: {findex7.errors}")
        return json2user(mess = str(findex7.form_name), icon_type = 'error')

    return locals()

@action('inbox', method=["GET", "POST"] )
@action.uses(db, session, T, Template('inbox.html', delimiters='[%[ ]]',))

def inbox():
    ctrl_info= { 'c':'inbox', 'v':'inbox.html' }
    messages = ['inbox', 'inbox.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('inbox') 


    rows_tinbox0= db(db.tinbox0).select()
    # 
    finbox0= Form(db.dfinbox0, dbio=False, formstyle=FormStyleBulma)
    if finbox0.accepted:
        icon_type ='success' if insert_form_vars(finbox0, db.dfinbox0) else 'info'
        return json2user(mess = str( finbox0.form_name ), icon_type=icon_type )
    elif finbox0.errors:
        print(f"finbox0 has errors: {finbox0.errors}")
        return json2user(mess = str(finbox0.form_name), icon_type = 'error')

    # 
    finbox1= Form(db.dfinbox1, dbio=False, formstyle=FormStyleBulma)
    if finbox1.accepted:
        icon_type ='success' if insert_form_vars(finbox1, db.dfinbox1) else 'info'
        return json2user(mess = str( finbox1.form_name ), icon_type=icon_type )
    elif finbox1.errors:
        print(f"finbox1 has errors: {finbox1.errors}")
        return json2user(mess = str(finbox1.form_name), icon_type = 'error')

    # 
    finbox2= Form(db.dfinbox2, dbio=False, formstyle=FormStyleBulma)
    if finbox2.accepted:
        icon_type ='success' if insert_form_vars(finbox2, db.dfinbox2) else 'info'
        return json2user(mess = str( finbox2.form_name ), icon_type=icon_type )
    elif finbox2.errors:
        print(f"finbox2 has errors: {finbox2.errors}")
        return json2user(mess = str(finbox2.form_name), icon_type = 'error')

    # 
    finbox3= Form(db.dfinbox3, dbio=False, formstyle=FormStyleBulma)
    if finbox3.accepted:
        icon_type ='success' if insert_form_vars(finbox3, db.dfinbox3) else 'info'
        return json2user(mess = str( finbox3.form_name ), icon_type=icon_type )
    elif finbox3.errors:
        print(f"finbox3 has errors: {finbox3.errors}")
        return json2user(mess = str(finbox3.form_name), icon_type = 'error')

    # 
    finbox4= Form(db.dfinbox4, dbio=False, formstyle=FormStyleBulma)
    if finbox4.accepted:
        icon_type ='success' if insert_form_vars(finbox4, db.dfinbox4) else 'info'
        return json2user(mess = str( finbox4.form_name ), icon_type=icon_type )
    elif finbox4.errors:
        print(f"finbox4 has errors: {finbox4.errors}")
        return json2user(mess = str(finbox4.form_name), icon_type = 'error')

    # 
    finbox5= Form(db.dfinbox5, dbio=False, formstyle=FormStyleBulma)
    if finbox5.accepted:
        icon_type ='success' if insert_form_vars(finbox5, db.dfinbox5) else 'info'
        return json2user(mess = str( finbox5.form_name ), icon_type=icon_type )
    elif finbox5.errors:
        print(f"finbox5 has errors: {finbox5.errors}")
        return json2user(mess = str(finbox5.form_name), icon_type = 'error')

    # 
    finbox6= Form(db.dfinbox6, dbio=False, formstyle=FormStyleBulma)
    if finbox6.accepted:
        icon_type ='success' if insert_form_vars(finbox6, db.dfinbox6) else 'info'
        return json2user(mess = str( finbox6.form_name ), icon_type=icon_type )
    elif finbox6.errors:
        print(f"finbox6 has errors: {finbox6.errors}")
        return json2user(mess = str(finbox6.form_name), icon_type = 'error')

    # 
    finbox7= Form(db.dfinbox7, dbio=False, formstyle=FormStyleBulma)
    if finbox7.accepted:
        icon_type ='success' if insert_form_vars(finbox7, db.dfinbox7) else 'info'
        return json2user(mess = str( finbox7.form_name ), icon_type=icon_type )
    elif finbox7.errors:
        print(f"finbox7 has errors: {finbox7.errors}")
        return json2user(mess = str(finbox7.form_name), icon_type = 'error')

    # 
    finbox8= Form(db.dfinbox8, dbio=False, formstyle=FormStyleBulma)
    if finbox8.accepted:
        icon_type ='success' if insert_form_vars(finbox8, db.dfinbox8) else 'info'
        return json2user(mess = str( finbox8.form_name ), icon_type=icon_type )
    elif finbox8.errors:
        print(f"finbox8 has errors: {finbox8.errors}")
        return json2user(mess = str(finbox8.form_name), icon_type = 'error')

    # 
    finbox9= Form(db.dfinbox9, dbio=False, formstyle=FormStyleBulma)
    if finbox9.accepted:
        icon_type ='success' if insert_form_vars(finbox9, db.dfinbox9) else 'info'
        return json2user(mess = str( finbox9.form_name ), icon_type=icon_type )
    elif finbox9.errors:
        print(f"finbox9 has errors: {finbox9.errors}")
        return json2user(mess = str(finbox9.form_name), icon_type = 'error')

    # 
    finbox10= Form(db.dfinbox10, dbio=False, formstyle=FormStyleBulma)
    if finbox10.accepted:
        icon_type ='success' if insert_form_vars(finbox10, db.dfinbox10) else 'info'
        return json2user(mess = str( finbox10.form_name ), icon_type=icon_type )
    elif finbox10.errors:
        print(f"finbox10 has errors: {finbox10.errors}")
        return json2user(mess = str(finbox10.form_name), icon_type = 'error')

    return locals()

@action('color', method=["GET", "POST"] )
@action.uses(db, session, T, Template('color.html', delimiters='[%[ ]]',))

def color():
    ctrl_info= { 'c':'color', 'v':'color.html' }
    messages = ['color', 'color.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('color') 


    # 
    fcolor0= Form(db.dfcolor0, dbio=False, formstyle=FormStyleBulma)
    if fcolor0.accepted:
        icon_type ='success' if insert_form_vars(fcolor0, db.dfcolor0) else 'info'
        return json2user(mess = str( fcolor0.form_name ), icon_type=icon_type )
    elif fcolor0.errors:
        print(f"fcolor0 has errors: {fcolor0.errors}")
        return json2user(mess = str(fcolor0.form_name), icon_type = 'error')

    # 
    fcolor1= Form(db.dfcolor1, dbio=False, formstyle=FormStyleBulma)
    if fcolor1.accepted:
        icon_type ='success' if insert_form_vars(fcolor1, db.dfcolor1) else 'info'
        return json2user(mess = str( fcolor1.form_name ), icon_type=icon_type )
    elif fcolor1.errors:
        print(f"fcolor1 has errors: {fcolor1.errors}")
        return json2user(mess = str(fcolor1.form_name), icon_type = 'error')

    return locals()

@action('alert', method=["GET", "POST"] )
@action.uses(db, session, T, Template('alert.html', delimiters='[%[ ]]',))

def alert():
    ctrl_info= { 'c':'alert', 'v':'alert.html' }
    messages = ['alert', 'alert.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('alert') 


    # 
    falert0= Form(db.dfalert0, dbio=False, formstyle=FormStyleBulma)
    if falert0.accepted:
        icon_type ='success' if insert_form_vars(falert0, db.dfalert0) else 'info'
        return json2user(mess = str( falert0.form_name ), icon_type=icon_type )
    elif falert0.errors:
        print(f"falert0 has errors: {falert0.errors}")
        return json2user(mess = str(falert0.form_name), icon_type = 'error')

    # 
    falert1= Form(db.dfalert1, dbio=False, formstyle=FormStyleBulma)
    if falert1.accepted:
        icon_type ='success' if insert_form_vars(falert1, db.dfalert1) else 'info'
        return json2user(mess = str( falert1.form_name ), icon_type=icon_type )
    elif falert1.errors:
        print(f"falert1 has errors: {falert1.errors}")
        return json2user(mess = str(falert1.form_name), icon_type = 'error')

    return locals()

@action('wizard', method=["GET", "POST"] )
@action.uses(db, session, T, Template('wizard.html', delimiters='[%[ ]]',))

def wizard():
    ctrl_info= { 'c':'wizard', 'v':'wizard.html' }
    messages = ['wizard', 'wizard.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('wizard') 


    # 
    fwizard0= Form(db.dfwizard0, dbio=False, formstyle=FormStyleBulma)
    if fwizard0.accepted:
        icon_type ='success' if insert_form_vars(fwizard0, db.dfwizard0) else 'info'
        return json2user(mess = str( fwizard0.form_name ), icon_type=icon_type )
    elif fwizard0.errors:
        print(f"fwizard0 has errors: {fwizard0.errors}")
        return json2user(mess = str(fwizard0.form_name), icon_type = 'error')

    # 
    fwizard1= Form(db.dfwizard1, dbio=False, formstyle=FormStyleBulma)
    if fwizard1.accepted:
        icon_type ='success' if insert_form_vars(fwizard1, db.dfwizard1) else 'info'
        return json2user(mess = str( fwizard1.form_name ), icon_type=icon_type )
    elif fwizard1.errors:
        print(f"fwizard1 has errors: {fwizard1.errors}")
        return json2user(mess = str(fwizard1.form_name), icon_type = 'error')

    return locals()

@action('modals', method=["GET", "POST"] )
@action.uses(db, session, T, Template('modals.html', delimiters='[%[ ]]',))

def modals():
    ctrl_info= { 'c':'modals', 'v':'modals.html' }
    messages = ['modals', 'modals.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('modals') 


    # 
    fmodals0= Form(db.dfmodals0, dbio=False, formstyle=FormStyleBulma)
    if fmodals0.accepted:
        icon_type ='success' if insert_form_vars(fmodals0, db.dfmodals0) else 'info'
        return json2user(mess = str( fmodals0.form_name ), icon_type=icon_type )
    elif fmodals0.errors:
        print(f"fmodals0 has errors: {fmodals0.errors}")
        return json2user(mess = str(fmodals0.form_name), icon_type = 'error')

    # 
    fmodals1= Form(db.dfmodals1, dbio=False, formstyle=FormStyleBulma)
    if fmodals1.accepted:
        icon_type ='success' if insert_form_vars(fmodals1, db.dfmodals1) else 'info'
        return json2user(mess = str( fmodals1.form_name ), icon_type=icon_type )
    elif fmodals1.errors:
        print(f"fmodals1 has errors: {fmodals1.errors}")
        return json2user(mess = str(fmodals1.form_name), icon_type = 'error')

    return locals()

@action('dialog', method=["GET", "POST"] )
@action.uses(db, session, T, Template('dialog.html', delimiters='[%[ ]]',))

def dialog():
    ctrl_info= { 'c':'dialog', 'v':'dialog.html' }
    messages = ['dialog', 'dialog.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('dialog') 


    # 
    fdialog0= Form(db.dfdialog0, dbio=False, formstyle=FormStyleBulma)
    if fdialog0.accepted:
        icon_type ='success' if insert_form_vars(fdialog0, db.dfdialog0) else 'info'
        return json2user(mess = str( fdialog0.form_name ), icon_type=icon_type )
    elif fdialog0.errors:
        print(f"fdialog0 has errors: {fdialog0.errors}")
        return json2user(mess = str(fdialog0.form_name), icon_type = 'error')

    # 
    fdialog1= Form(db.dfdialog1, dbio=False, formstyle=FormStyleBulma)
    if fdialog1.accepted:
        icon_type ='success' if insert_form_vars(fdialog1, db.dfdialog1) else 'info'
        return json2user(mess = str( fdialog1.form_name ), icon_type=icon_type )
    elif fdialog1.errors:
        print(f"fdialog1 has errors: {fdialog1.errors}")
        return json2user(mess = str(fdialog1.form_name), icon_type = 'error')

    return locals()

@action('widgets', method=["GET", "POST"] )
@action.uses(db, session, T, Template('widgets.html', delimiters='[%[ ]]',))

def widgets():
    ctrl_info= { 'c':'widgets', 'v':'widgets.html' }
    messages = ['widgets', 'widgets.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('widgets') 


    # 
    fwidgets0= Form(db.dfwidgets0, dbio=False, formstyle=FormStyleBulma)
    if fwidgets0.accepted:
        icon_type ='success' if insert_form_vars(fwidgets0, db.dfwidgets0) else 'info'
        return json2user(mess = str( fwidgets0.form_name ), icon_type=icon_type )
    elif fwidgets0.errors:
        print(f"fwidgets0 has errors: {fwidgets0.errors}")
        return json2user(mess = str(fwidgets0.form_name), icon_type = 'error')

    # 
    fwidgets1= Form(db.dfwidgets1, dbio=False, formstyle=FormStyleBulma)
    if fwidgets1.accepted:
        icon_type ='success' if insert_form_vars(fwidgets1, db.dfwidgets1) else 'info'
        return json2user(mess = str( fwidgets1.form_name ), icon_type=icon_type )
    elif fwidgets1.errors:
        print(f"fwidgets1 has errors: {fwidgets1.errors}")
        return json2user(mess = str(fwidgets1.form_name), icon_type = 'error')

    # 
    fwidgets2= Form(db.dfwidgets2, dbio=False, formstyle=FormStyleBulma)
    if fwidgets2.accepted:
        icon_type ='success' if insert_form_vars(fwidgets2, db.dfwidgets2) else 'info'
        return json2user(mess = str( fwidgets2.form_name ), icon_type=icon_type )
    elif fwidgets2.errors:
        print(f"fwidgets2 has errors: {fwidgets2.errors}")
        return json2user(mess = str(fwidgets2.form_name), icon_type = 'error')

    # 
    fwidgets3= Form(db.dfwidgets3, dbio=False, formstyle=FormStyleBulma)
    if fwidgets3.accepted:
        icon_type ='success' if insert_form_vars(fwidgets3, db.dfwidgets3) else 'info'
        return json2user(mess = str( fwidgets3.form_name ), icon_type=icon_type )
    elif fwidgets3.errors:
        print(f"fwidgets3 has errors: {fwidgets3.errors}")
        return json2user(mess = str(fwidgets3.form_name), icon_type = 'error')

    # 
    fwidgets4= Form(db.dfwidgets4, dbio=False, formstyle=FormStyleBulma)
    if fwidgets4.accepted:
        icon_type ='success' if insert_form_vars(fwidgets4, db.dfwidgets4) else 'info'
        return json2user(mess = str( fwidgets4.form_name ), icon_type=icon_type )
    elif fwidgets4.errors:
        print(f"fwidgets4 has errors: {fwidgets4.errors}")
        return json2user(mess = str(fwidgets4.form_name), icon_type = 'error')

    # 
    fwidgets5= Form(db.dfwidgets5, dbio=False, formstyle=FormStyleBulma)
    if fwidgets5.accepted:
        icon_type ='success' if insert_form_vars(fwidgets5, db.dfwidgets5) else 'info'
        return json2user(mess = str( fwidgets5.form_name ), icon_type=icon_type )
    elif fwidgets5.errors:
        print(f"fwidgets5 has errors: {fwidgets5.errors}")
        return json2user(mess = str(fwidgets5.form_name), icon_type = 'error')

    # 
    fwidgets6= Form(db.dfwidgets6, dbio=False, formstyle=FormStyleBulma)
    if fwidgets6.accepted:
        icon_type ='success' if insert_form_vars(fwidgets6, db.dfwidgets6) else 'info'
        return json2user(mess = str( fwidgets6.form_name ), icon_type=icon_type )
    elif fwidgets6.errors:
        print(f"fwidgets6 has errors: {fwidgets6.errors}")
        return json2user(mess = str(fwidgets6.form_name), icon_type = 'error')

    return locals()

@action('invoice', method=["GET", "POST"] )
@action.uses(db, session, T, Template('invoice.html', delimiters='[%[ ]]',))

def invoice():
    ctrl_info= { 'c':'invoice', 'v':'invoice.html' }
    messages = ['invoice', 'invoice.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('invoice') 


    rows_tinvoice0= db(db.tinvoice0).select()
    # 
    finvoice0= Form(db.dfinvoice0, dbio=False, formstyle=FormStyleBulma)
    if finvoice0.accepted:
        icon_type ='success' if insert_form_vars(finvoice0, db.dfinvoice0) else 'info'
        return json2user(mess = str( finvoice0.form_name ), icon_type=icon_type )
    elif finvoice0.errors:
        print(f"finvoice0 has errors: {finvoice0.errors}")
        return json2user(mess = str(finvoice0.form_name), icon_type = 'error')

    # 
    finvoice1= Form(db.dfinvoice1, dbio=False, formstyle=FormStyleBulma)
    if finvoice1.accepted:
        icon_type ='success' if insert_form_vars(finvoice1, db.dfinvoice1) else 'info'
        return json2user(mess = str( finvoice1.form_name ), icon_type=icon_type )
    elif finvoice1.errors:
        print(f"finvoice1 has errors: {finvoice1.errors}")
        return json2user(mess = str(finvoice1.form_name), icon_type = 'error')

    return locals()

@action('indexX4', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index-4.html', delimiters='[%[ ]]',))

def indexX4():
    ctrl_info= { 'c':'indexX4', 'v':'index-4.html' }
    messages = ['indexX4', 'index-4.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('indexX4') 


    rows_tindexX40= db(db.tindexX40).select()
    # 
    findexX40= Form(db.dfindexX40, dbio=False, formstyle=FormStyleBulma)
    if findexX40.accepted:
        icon_type ='success' if insert_form_vars(findexX40, db.dfindexX40) else 'info'
        return json2user(mess = str( findexX40.form_name ), icon_type=icon_type )
    elif findexX40.errors:
        print(f"findexX40 has errors: {findexX40.errors}")
        return json2user(mess = str(findexX40.form_name), icon_type = 'error')

    # 
    findexX41= Form(db.dfindexX41, dbio=False, formstyle=FormStyleBulma)
    if findexX41.accepted:
        icon_type ='success' if insert_form_vars(findexX41, db.dfindexX41) else 'info'
        return json2user(mess = str( findexX41.form_name ), icon_type=icon_type )
    elif findexX41.errors:
        print(f"findexX41 has errors: {findexX41.errors}")
        return json2user(mess = str(findexX41.form_name), icon_type = 'error')

    # 
    findexX42= Form(db.dfindexX42, dbio=False, formstyle=FormStyleBulma)
    if findexX42.accepted:
        icon_type ='success' if insert_form_vars(findexX42, db.dfindexX42) else 'info'
        return json2user(mess = str( findexX42.form_name ), icon_type=icon_type )
    elif findexX42.errors:
        print(f"findexX42 has errors: {findexX42.errors}")
        return json2user(mess = str(findexX42.form_name), icon_type = 'error')

    # 
    findexX43= Form(db.dfindexX43, dbio=False, formstyle=FormStyleBulma)
    if findexX43.accepted:
        icon_type ='success' if insert_form_vars(findexX43, db.dfindexX43) else 'info'
        return json2user(mess = str( findexX43.form_name ), icon_type=icon_type )
    elif findexX43.errors:
        print(f"findexX43 has errors: {findexX43.errors}")
        return json2user(mess = str(findexX43.form_name), icon_type = 'error')

    # 
    findexX44= Form(db.dfindexX44, dbio=False, formstyle=FormStyleBulma)
    if findexX44.accepted:
        icon_type ='success' if insert_form_vars(findexX44, db.dfindexX44) else 'info'
        return json2user(mess = str( findexX44.form_name ), icon_type=icon_type )
    elif findexX44.errors:
        print(f"findexX44 has errors: {findexX44.errors}")
        return json2user(mess = str(findexX44.form_name), icon_type = 'error')

    # 
    findexX45= Form(db.dfindexX45, dbio=False, formstyle=FormStyleBulma)
    if findexX45.accepted:
        icon_type ='success' if insert_form_vars(findexX45, db.dfindexX45) else 'info'
        return json2user(mess = str( findexX45.form_name ), icon_type=icon_type )
    elif findexX45.errors:
        print(f"findexX45 has errors: {findexX45.errors}")
        return json2user(mess = str(findexX45.form_name), icon_type = 'error')

    # 
    findexX46= Form(db.dfindexX46, dbio=False, formstyle=FormStyleBulma)
    if findexX46.accepted:
        icon_type ='success' if insert_form_vars(findexX46, db.dfindexX46) else 'info'
        return json2user(mess = str( findexX46.form_name ), icon_type=icon_type )
    elif findexX46.errors:
        print(f"findexX46 has errors: {findexX46.errors}")
        return json2user(mess = str(findexX46.form_name), icon_type = 'error')

    # 
    findexX47= Form(db.dfindexX47, dbio=False, formstyle=FormStyleBulma)
    if findexX47.accepted:
        icon_type ='success' if insert_form_vars(findexX47, db.dfindexX47) else 'info'
        return json2user(mess = str( findexX47.form_name ), icon_type=icon_type )
    elif findexX47.errors:
        print(f"findexX47 has errors: {findexX47.errors}")
        return json2user(mess = str(findexX47.form_name), icon_type = 'error')

    return locals()

@action('indexX2', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index-2.html', delimiters='[%[ ]]',))

def indexX2():
    ctrl_info= { 'c':'indexX2', 'v':'index-2.html' }
    messages = ['indexX2', 'index-2.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('indexX2') 


    rows_tindexX20= db(db.tindexX20).select()
    # 
    findexX20= Form(db.dfindexX20, dbio=False, formstyle=FormStyleBulma)
    if findexX20.accepted:
        icon_type ='success' if insert_form_vars(findexX20, db.dfindexX20) else 'info'
        return json2user(mess = str( findexX20.form_name ), icon_type=icon_type )
    elif findexX20.errors:
        print(f"findexX20 has errors: {findexX20.errors}")
        return json2user(mess = str(findexX20.form_name), icon_type = 'error')

    # 
    findexX21= Form(db.dfindexX21, dbio=False, formstyle=FormStyleBulma)
    if findexX21.accepted:
        icon_type ='success' if insert_form_vars(findexX21, db.dfindexX21) else 'info'
        return json2user(mess = str( findexX21.form_name ), icon_type=icon_type )
    elif findexX21.errors:
        print(f"findexX21 has errors: {findexX21.errors}")
        return json2user(mess = str(findexX21.form_name), icon_type = 'error')

    # 
    findexX22= Form(db.dfindexX22, dbio=False, formstyle=FormStyleBulma)
    if findexX22.accepted:
        icon_type ='success' if insert_form_vars(findexX22, db.dfindexX22) else 'info'
        return json2user(mess = str( findexX22.form_name ), icon_type=icon_type )
    elif findexX22.errors:
        print(f"findexX22 has errors: {findexX22.errors}")
        return json2user(mess = str(findexX22.form_name), icon_type = 'error')

    # 
    findexX23= Form(db.dfindexX23, dbio=False, formstyle=FormStyleBulma)
    if findexX23.accepted:
        icon_type ='success' if insert_form_vars(findexX23, db.dfindexX23) else 'info'
        return json2user(mess = str( findexX23.form_name ), icon_type=icon_type )
    elif findexX23.errors:
        print(f"findexX23 has errors: {findexX23.errors}")
        return json2user(mess = str(findexX23.form_name), icon_type = 'error')

    # 
    findexX24= Form(db.dfindexX24, dbio=False, formstyle=FormStyleBulma)
    if findexX24.accepted:
        icon_type ='success' if insert_form_vars(findexX24, db.dfindexX24) else 'info'
        return json2user(mess = str( findexX24.form_name ), icon_type=icon_type )
    elif findexX24.errors:
        print(f"findexX24 has errors: {findexX24.errors}")
        return json2user(mess = str(findexX24.form_name), icon_type = 'error')

    # 
    findexX25= Form(db.dfindexX25, dbio=False, formstyle=FormStyleBulma)
    if findexX25.accepted:
        icon_type ='success' if insert_form_vars(findexX25, db.dfindexX25) else 'info'
        return json2user(mess = str( findexX25.form_name ), icon_type=icon_type )
    elif findexX25.errors:
        print(f"findexX25 has errors: {findexX25.errors}")
        return json2user(mess = str(findexX25.form_name), icon_type = 'error')

    # 
    findexX26= Form(db.dfindexX26, dbio=False, formstyle=FormStyleBulma)
    if findexX26.accepted:
        icon_type ='success' if insert_form_vars(findexX26, db.dfindexX26) else 'info'
        return json2user(mess = str( findexX26.form_name ), icon_type=icon_type )
    elif findexX26.errors:
        print(f"findexX26 has errors: {findexX26.errors}")
        return json2user(mess = str(findexX26.form_name), icon_type = 'error')

    # 
    findexX27= Form(db.dfindexX27, dbio=False, formstyle=FormStyleBulma)
    if findexX27.accepted:
        icon_type ='success' if insert_form_vars(findexX27, db.dfindexX27) else 'info'
        return json2user(mess = str( findexX27.form_name ), icon_type=icon_type )
    elif findexX27.errors:
        print(f"findexX27 has errors: {findexX27.errors}")
        return json2user(mess = str(findexX27.form_name), icon_type = 'error')

    return locals()

@action('indexX3', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index-3.html', delimiters='[%[ ]]',))

def indexX3():
    ctrl_info= { 'c':'indexX3', 'v':'index-3.html' }
    messages = ['indexX3', 'index-3.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('indexX3') 


    rows_tindexX30= db(db.tindexX30).select()
    # 
    findexX30= Form(db.dfindexX30, dbio=False, formstyle=FormStyleBulma)
    if findexX30.accepted:
        icon_type ='success' if insert_form_vars(findexX30, db.dfindexX30) else 'info'
        return json2user(mess = str( findexX30.form_name ), icon_type=icon_type )
    elif findexX30.errors:
        print(f"findexX30 has errors: {findexX30.errors}")
        return json2user(mess = str(findexX30.form_name), icon_type = 'error')

    # 
    findexX31= Form(db.dfindexX31, dbio=False, formstyle=FormStyleBulma)
    if findexX31.accepted:
        icon_type ='success' if insert_form_vars(findexX31, db.dfindexX31) else 'info'
        return json2user(mess = str( findexX31.form_name ), icon_type=icon_type )
    elif findexX31.errors:
        print(f"findexX31 has errors: {findexX31.errors}")
        return json2user(mess = str(findexX31.form_name), icon_type = 'error')

    # 
    findexX32= Form(db.dfindexX32, dbio=False, formstyle=FormStyleBulma)
    if findexX32.accepted:
        icon_type ='success' if insert_form_vars(findexX32, db.dfindexX32) else 'info'
        return json2user(mess = str( findexX32.form_name ), icon_type=icon_type )
    elif findexX32.errors:
        print(f"findexX32 has errors: {findexX32.errors}")
        return json2user(mess = str(findexX32.form_name), icon_type = 'error')

    # 
    findexX33= Form(db.dfindexX33, dbio=False, formstyle=FormStyleBulma)
    if findexX33.accepted:
        icon_type ='success' if insert_form_vars(findexX33, db.dfindexX33) else 'info'
        return json2user(mess = str( findexX33.form_name ), icon_type=icon_type )
    elif findexX33.errors:
        print(f"findexX33 has errors: {findexX33.errors}")
        return json2user(mess = str(findexX33.form_name), icon_type = 'error')

    # 
    findexX34= Form(db.dfindexX34, dbio=False, formstyle=FormStyleBulma)
    if findexX34.accepted:
        icon_type ='success' if insert_form_vars(findexX34, db.dfindexX34) else 'info'
        return json2user(mess = str( findexX34.form_name ), icon_type=icon_type )
    elif findexX34.errors:
        print(f"findexX34 has errors: {findexX34.errors}")
        return json2user(mess = str(findexX34.form_name), icon_type = 'error')

    # 
    findexX35= Form(db.dfindexX35, dbio=False, formstyle=FormStyleBulma)
    if findexX35.accepted:
        icon_type ='success' if insert_form_vars(findexX35, db.dfindexX35) else 'info'
        return json2user(mess = str( findexX35.form_name ), icon_type=icon_type )
    elif findexX35.errors:
        print(f"findexX35 has errors: {findexX35.errors}")
        return json2user(mess = str(findexX35.form_name), icon_type = 'error')

    # 
    findexX36= Form(db.dfindexX36, dbio=False, formstyle=FormStyleBulma)
    if findexX36.accepted:
        icon_type ='success' if insert_form_vars(findexX36, db.dfindexX36) else 'info'
        return json2user(mess = str( findexX36.form_name ), icon_type=icon_type )
    elif findexX36.errors:
        print(f"findexX36 has errors: {findexX36.errors}")
        return json2user(mess = str(findexX36.form_name), icon_type = 'error')

    # 
    findexX37= Form(db.dfindexX37, dbio=False, formstyle=FormStyleBulma)
    if findexX37.accepted:
        icon_type ='success' if insert_form_vars(findexX37, db.dfindexX37) else 'info'
        return json2user(mess = str( findexX37.form_name ), icon_type=icon_type )
    elif findexX37.errors:
        print(f"findexX37 has errors: {findexX37.errors}")
        return json2user(mess = str(findexX37.form_name), icon_type = 'error')

    return locals()

@action('contact', method=["GET", "POST"] )
@action.uses(db, session, T, Template('contact.html', delimiters='[%[ ]]',))

def contact():
    ctrl_info= { 'c':'contact', 'v':'contact.html' }
    messages = ['contact', 'contact.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('contact') 


    # 
    fcontact0= Form(db.dfcontact0, dbio=False, formstyle=FormStyleBulma)
    if fcontact0.accepted:
        icon_type ='success' if insert_form_vars(fcontact0, db.dfcontact0) else 'info'
        return json2user(mess = str( fcontact0.form_name ), icon_type=icon_type )
    elif fcontact0.errors:
        print(f"fcontact0 has errors: {fcontact0.errors}")
        return json2user(mess = str(fcontact0.form_name), icon_type = 'error')

    # 
    fcontact1= Form(db.dfcontact1, dbio=False, formstyle=FormStyleBulma)
    if fcontact1.accepted:
        icon_type ='success' if insert_form_vars(fcontact1, db.dfcontact1) else 'info'
        return json2user(mess = str( fcontact1.form_name ), icon_type=icon_type )
    elif fcontact1.errors:
        print(f"fcontact1 has errors: {fcontact1.errors}")
        return json2user(mess = str(fcontact1.form_name), icon_type = 'error')

    return locals()

@action('buttons', method=["GET", "POST"] )
@action.uses(db, session, T, Template('buttons.html', delimiters='[%[ ]]',))

def buttons():
    ctrl_info= { 'c':'buttons', 'v':'buttons.html' }
    messages = ['buttons', 'buttons.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('buttons') 


    # 
    fbuttons0= Form(db.dfbuttons0, dbio=False, formstyle=FormStyleBulma)
    if fbuttons0.accepted:
        icon_type ='success' if insert_form_vars(fbuttons0, db.dfbuttons0) else 'info'
        return json2user(mess = str( fbuttons0.form_name ), icon_type=icon_type )
    elif fbuttons0.errors:
        print(f"fbuttons0 has errors: {fbuttons0.errors}")
        return json2user(mess = str(fbuttons0.form_name), icon_type = 'error')

    # 
    fbuttons1= Form(db.dfbuttons1, dbio=False, formstyle=FormStyleBulma)
    if fbuttons1.accepted:
        icon_type ='success' if insert_form_vars(fbuttons1, db.dfbuttons1) else 'info'
        return json2user(mess = str( fbuttons1.form_name ), icon_type=icon_type )
    elif fbuttons1.errors:
        print(f"fbuttons1 has errors: {fbuttons1.errors}")
        return json2user(mess = str(fbuttons1.form_name), icon_type = 'error')

    return locals()

@action('tooltips', method=["GET", "POST"] )
@action.uses(db, session, T, Template('tooltips.html', delimiters='[%[ ]]',))

def tooltips():
    ctrl_info= { 'c':'tooltips', 'v':'tooltips.html' }
    messages = ['tooltips', 'tooltips.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('tooltips') 


    # 
    ftooltips0= Form(db.dftooltips0, dbio=False, formstyle=FormStyleBulma)
    if ftooltips0.accepted:
        icon_type ='success' if insert_form_vars(ftooltips0, db.dftooltips0) else 'info'
        return json2user(mess = str( ftooltips0.form_name ), icon_type=icon_type )
    elif ftooltips0.errors:
        print(f"ftooltips0 has errors: {ftooltips0.errors}")
        return json2user(mess = str(ftooltips0.form_name), icon_type = 'error')

    # 
    ftooltips1= Form(db.dftooltips1, dbio=False, formstyle=FormStyleBulma)
    if ftooltips1.accepted:
        icon_type ='success' if insert_form_vars(ftooltips1, db.dftooltips1) else 'info'
        return json2user(mess = str( ftooltips1.form_name ), icon_type=icon_type )
    elif ftooltips1.errors:
        print(f"ftooltips1 has errors: {ftooltips1.errors}")
        return json2user(mess = str(ftooltips1.form_name), icon_type = 'error')

    return locals()

@action('popovers', method=["GET", "POST"] )
@action.uses(db, session, T, Template('popovers.html', delimiters='[%[ ]]',))

def popovers():
    ctrl_info= { 'c':'popovers', 'v':'popovers.html' }
    messages = ['popovers', 'popovers.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('popovers') 


    # 
    fpopovers0= Form(db.dfpopovers0, dbio=False, formstyle=FormStyleBulma)
    if fpopovers0.accepted:
        icon_type ='success' if insert_form_vars(fpopovers0, db.dfpopovers0) else 'info'
        return json2user(mess = str( fpopovers0.form_name ), icon_type=icon_type )
    elif fpopovers0.errors:
        print(f"fpopovers0 has errors: {fpopovers0.errors}")
        return json2user(mess = str(fpopovers0.form_name), icon_type = 'error')

    # 
    fpopovers1= Form(db.dfpopovers1, dbio=False, formstyle=FormStyleBulma)
    if fpopovers1.accepted:
        icon_type ='success' if insert_form_vars(fpopovers1, db.dfpopovers1) else 'info'
        return json2user(mess = str( fpopovers1.form_name ), icon_type=icon_type )
    elif fpopovers1.errors:
        print(f"fpopovers1 has errors: {fpopovers1.errors}")
        return json2user(mess = str(fpopovers1.form_name), icon_type = 'error')

    return locals()

@action('dropdown', method=["GET", "POST"] )
@action.uses(db, session, T, Template('dropdown.html', delimiters='[%[ ]]',))

def dropdown():
    ctrl_info= { 'c':'dropdown', 'v':'dropdown.html' }
    messages = ['dropdown', 'dropdown.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('dropdown') 


    # 
    fdropdown0= Form(db.dfdropdown0, dbio=False, formstyle=FormStyleBulma)
    if fdropdown0.accepted:
        icon_type ='success' if insert_form_vars(fdropdown0, db.dfdropdown0) else 'info'
        return json2user(mess = str( fdropdown0.form_name ), icon_type=icon_type )
    elif fdropdown0.errors:
        print(f"fdropdown0 has errors: {fdropdown0.errors}")
        return json2user(mess = str(fdropdown0.form_name), icon_type = 'error')

    # 
    fdropdown1= Form(db.dfdropdown1, dbio=False, formstyle=FormStyleBulma)
    if fdropdown1.accepted:
        icon_type ='success' if insert_form_vars(fdropdown1, db.dfdropdown1) else 'info'
        return json2user(mess = str( fdropdown1.form_name ), icon_type=icon_type )
    elif fdropdown1.errors:
        print(f"fdropdown1 has errors: {fdropdown1.errors}")
        return json2user(mess = str(fdropdown1.form_name), icon_type = 'error')

    return locals()

@action('dataXmap', method=["GET", "POST"] )
@action.uses(db, session, T, Template('data-map.html', delimiters='[%[ ]]',))

def dataXmap():
    ctrl_info= { 'c':'dataXmap', 'v':'data-map.html' }
    messages = ['dataXmap', 'data-map.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('dataXmap') 


    # 
    fdataXmap0= Form(db.dfdataXmap0, dbio=False, formstyle=FormStyleBulma)
    if fdataXmap0.accepted:
        icon_type ='success' if insert_form_vars(fdataXmap0, db.dfdataXmap0) else 'info'
        return json2user(mess = str( fdataXmap0.form_name ), icon_type=icon_type )
    elif fdataXmap0.errors:
        print(f"fdataXmap0 has errors: {fdataXmap0.errors}")
        return json2user(mess = str(fdataXmap0.form_name), icon_type = 'error')

    # 
    fdataXmap1= Form(db.dfdataXmap1, dbio=False, formstyle=FormStyleBulma)
    if fdataXmap1.accepted:
        icon_type ='success' if insert_form_vars(fdataXmap1, db.dfdataXmap1) else 'info'
        return json2user(mess = str( fdataXmap1.form_name ), icon_type=icon_type )
    elif fdataXmap1.errors:
        print(f"fdataXmap1 has errors: {fdataXmap1.errors}")
        return json2user(mess = str(fdataXmap1.form_name), icon_type = 'error')

    return locals()

@action('analytics', method=["GET", "POST"] )
@action.uses(db, session, T, Template('analytics.html', delimiters='[%[ ]]',))

def analytics():
    ctrl_info= { 'c':'analytics', 'v':'analytics.html' }
    messages = ['analytics', 'analytics.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('analytics') 


    rows_tanalytics0= db(db.tanalytics0).select()
    rows_tanalytics1= db(db.tanalytics1).select()
    rows_tanalytics2= db(db.tanalytics2).select()
    # 
    fanalytics0= Form(db.dfanalytics0, dbio=False, formstyle=FormStyleBulma)
    if fanalytics0.accepted:
        icon_type ='success' if insert_form_vars(fanalytics0, db.dfanalytics0) else 'info'
        return json2user(mess = str( fanalytics0.form_name ), icon_type=icon_type )
    elif fanalytics0.errors:
        print(f"fanalytics0 has errors: {fanalytics0.errors}")
        return json2user(mess = str(fanalytics0.form_name), icon_type = 'error')

    # 
    fanalytics1= Form(db.dfanalytics1, dbio=False, formstyle=FormStyleBulma)
    if fanalytics1.accepted:
        icon_type ='success' if insert_form_vars(fanalytics1, db.dfanalytics1) else 'info'
        return json2user(mess = str( fanalytics1.form_name ), icon_type=icon_type )
    elif fanalytics1.errors:
        print(f"fanalytics1 has errors: {fanalytics1.errors}")
        return json2user(mess = str(fanalytics1.form_name), icon_type = 'error')

    return locals()

@action('accordion', method=["GET", "POST"] )
@action.uses(db, session, T, Template('accordion.html', delimiters='[%[ ]]',))

def accordion():
    ctrl_info= { 'c':'accordion', 'v':'accordion.html' }
    messages = ['accordion', 'accordion.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('accordion') 


    # 
    faccordion0= Form(db.dfaccordion0, dbio=False, formstyle=FormStyleBulma)
    if faccordion0.accepted:
        icon_type ='success' if insert_form_vars(faccordion0, db.dfaccordion0) else 'info'
        return json2user(mess = str( faccordion0.form_name ), icon_type=icon_type )
    elif faccordion0.errors:
        print(f"faccordion0 has errors: {faccordion0.errors}")
        return json2user(mess = str(faccordion0.form_name), icon_type = 'error')

    # 
    faccordion1= Form(db.dfaccordion1, dbio=False, formstyle=FormStyleBulma)
    if faccordion1.accepted:
        icon_type ='success' if insert_form_vars(faccordion1, db.dfaccordion1) else 'info'
        return json2user(mess = str( faccordion1.form_name ), icon_type=icon_type )
    elif faccordion1.errors:
        print(f"faccordion1 has errors: {faccordion1.errors}")
        return json2user(mess = str(faccordion1.form_name), icon_type = 'error')

    return locals()

@action('viewXemail', method=["GET", "POST"] )
@action.uses(db, session, T, Template('view-email.html', delimiters='[%[ ]]',))

def viewXemail():
    ctrl_info= { 'c':'viewXemail', 'v':'view-email.html' }
    messages = ['viewXemail', 'view-email.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('viewXemail') 


    # 
    fviewXemail0= Form(db.dfviewXemail0, dbio=False, formstyle=FormStyleBulma)
    if fviewXemail0.accepted:
        icon_type ='success' if insert_form_vars(fviewXemail0, db.dfviewXemail0) else 'info'
        return json2user(mess = str( fviewXemail0.form_name ), icon_type=icon_type )
    elif fviewXemail0.errors:
        print(f"fviewXemail0 has errors: {fviewXemail0.errors}")
        return json2user(mess = str(fviewXemail0.form_name), icon_type = 'error')

    # 
    fviewXemail1= Form(db.dfviewXemail1, dbio=False, formstyle=FormStyleBulma)
    if fviewXemail1.accepted:
        icon_type ='success' if insert_form_vars(fviewXemail1, db.dfviewXemail1) else 'info'
        return json2user(mess = str( fviewXemail1.form_name ), icon_type=icon_type )
    elif fviewXemail1.errors:
        print(f"fviewXemail1 has errors: {fviewXemail1.errors}")
        return json2user(mess = str(fviewXemail1.form_name), icon_type = 'error')

    return locals()

@action('typography', method=["GET", "POST"] )
@action.uses(db, session, T, Template('typography.html', delimiters='[%[ ]]',))

def typography():
    ctrl_info= { 'c':'typography', 'v':'typography.html' }
    messages = ['typography', 'typography.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('typography') 


    # 
    ftypography0= Form(db.dftypography0, dbio=False, formstyle=FormStyleBulma)
    if ftypography0.accepted:
        icon_type ='success' if insert_form_vars(ftypography0, db.dftypography0) else 'info'
        return json2user(mess = str( ftypography0.form_name ), icon_type=icon_type )
    elif ftypography0.errors:
        print(f"ftypography0 has errors: {ftypography0.errors}")
        return json2user(mess = str(ftypography0.form_name), icon_type = 'error')

    # 
    ftypography1= Form(db.dftypography1, dbio=False, formstyle=FormStyleBulma)
    if ftypography1.accepted:
        icon_type ='success' if insert_form_vars(ftypography1, db.dftypography1) else 'info'
        return json2user(mess = str( ftypography1.form_name ), icon_type=icon_type )
    elif ftypography1.errors:
        print(f"ftypography1 has errors: {ftypography1.errors}")
        return json2user(mess = str(ftypography1.form_name), icon_type = 'error')

    return locals()

@action('googleXmap', method=["GET", "POST"] )
@action.uses(db, session, T, Template('google-map.html', delimiters='[%[ ]]',))

def googleXmap():
    ctrl_info= { 'c':'googleXmap', 'v':'google-map.html' }
    messages = ['googleXmap', 'google-map.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('googleXmap') 


    # 
    fgoogleXmap0= Form(db.dfgoogleXmap0, dbio=False, formstyle=FormStyleBulma)
    if fgoogleXmap0.accepted:
        icon_type ='success' if insert_form_vars(fgoogleXmap0, db.dfgoogleXmap0) else 'info'
        return json2user(mess = str( fgoogleXmap0.form_name ), icon_type=icon_type )
    elif fgoogleXmap0.errors:
        print(f"fgoogleXmap0 has errors: {fgoogleXmap0.errors}")
        return json2user(mess = str(fgoogleXmap0.form_name), icon_type = 'error')

    # 
    fgoogleXmap1= Form(db.dfgoogleXmap1, dbio=False, formstyle=FormStyleBulma)
    if fgoogleXmap1.accepted:
        icon_type ='success' if insert_form_vars(fgoogleXmap1, db.dfgoogleXmap1) else 'info'
        return json2user(mess = str( fgoogleXmap1.form_name ), icon_type=icon_type )
    elif fgoogleXmap1.errors:
        print(f"fgoogleXmap1 has errors: {fgoogleXmap1.errors}")
        return json2user(mess = str(fgoogleXmap1.form_name), icon_type = 'error')

    return locals()

@action('dataXtable', method=["GET", "POST"] )
@action.uses(db, session, T, Template('data-table.html', delimiters='[%[ ]]',))

def dataXtable():
    ctrl_info= { 'c':'dataXtable', 'v':'data-table.html' }
    messages = ['dataXtable', 'data-table.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('dataXtable') 


    rows_tdataXtable0= db(db.tdataXtable0).select()
    # 
    fdataXtable0= Form(db.dfdataXtable0, dbio=False, formstyle=FormStyleBulma)
    if fdataXtable0.accepted:
        icon_type ='success' if insert_form_vars(fdataXtable0, db.dfdataXtable0) else 'info'
        return json2user(mess = str( fdataXtable0.form_name ), icon_type=icon_type )
    elif fdataXtable0.errors:
        print(f"fdataXtable0 has errors: {fdataXtable0.errors}")
        return json2user(mess = str(fdataXtable0.form_name), icon_type = 'error')

    # 
    fdataXtable1= Form(db.dfdataXtable1, dbio=False, formstyle=FormStyleBulma)
    if fdataXtable1.accepted:
        icon_type ='success' if insert_form_vars(fdataXtable1, db.dfdataXtable1) else 'info'
        return json2user(mess = str( fdataXtable1.form_name ), icon_type=icon_type )
    elif fdataXtable1.errors:
        print(f"fdataXtable1 has errors: {fdataXtable1.errors}")
        return json2user(mess = str(fdataXtable1.form_name), icon_type = 'error')

    return locals()

@action('barXcharts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('bar-charts.html', delimiters='[%[ ]]',))

def barXcharts():
    ctrl_info= { 'c':'barXcharts', 'v':'bar-charts.html' }
    messages = ['barXcharts', 'bar-charts.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('barXcharts') 


    # 
    fbarXcharts0= Form(db.dfbarXcharts0, dbio=False, formstyle=FormStyleBulma)
    if fbarXcharts0.accepted:
        icon_type ='success' if insert_form_vars(fbarXcharts0, db.dfbarXcharts0) else 'info'
        return json2user(mess = str( fbarXcharts0.form_name ), icon_type=icon_type )
    elif fbarXcharts0.errors:
        print(f"fbarXcharts0 has errors: {fbarXcharts0.errors}")
        return json2user(mess = str(fbarXcharts0.form_name), icon_type = 'error')

    # 
    fbarXcharts1= Form(db.dfbarXcharts1, dbio=False, formstyle=FormStyleBulma)
    if fbarXcharts1.accepted:
        icon_type ='success' if insert_form_vars(fbarXcharts1, db.dfbarXcharts1) else 'info'
        return json2user(mess = str( fbarXcharts1.form_name ), icon_type=icon_type )
    elif fbarXcharts1.errors:
        print(f"fbarXcharts1 has errors: {fbarXcharts1.errors}")
        return json2user(mess = str(fbarXcharts1.form_name), icon_type = 'error')

    return locals()

@action('animations', method=["GET", "POST"] )
@action.uses(db, session, T, Template('animations.html', delimiters='[%[ ]]',))

def animations():
    ctrl_info= { 'c':'animations', 'v':'animations.html' }
    messages = ['animations', 'animations.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('animations') 


    # 
    fanimations0= Form(db.dfanimations0, dbio=False, formstyle=FormStyleBulma)
    if fanimations0.accepted:
        icon_type ='success' if insert_form_vars(fanimations0, db.dfanimations0) else 'info'
        return json2user(mess = str( fanimations0.form_name ), icon_type=icon_type )
    elif fanimations0.errors:
        print(f"fanimations0 has errors: {fanimations0.errors}")
        return json2user(mess = str(fanimations0.form_name), icon_type = 'error')

    # 
    fanimations1= Form(db.dfanimations1, dbio=False, formstyle=FormStyleBulma)
    if fanimations1.accepted:
        icon_type ='success' if insert_form_vars(fanimations1, db.dfanimations1) else 'info'
        return json2user(mess = str( fanimations1.form_name ), icon_type=icon_type )
    elif fanimations1.errors:
        print(f"fanimations1 has errors: {fanimations1.errors}")
        return json2user(mess = str(fanimations1.form_name), icon_type = 'error')

    return locals()

@action('lineXcharts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('line-charts.html', delimiters='[%[ ]]',))

def lineXcharts():
    ctrl_info= { 'c':'lineXcharts', 'v':'line-charts.html' }
    messages = ['lineXcharts', 'line-charts.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('lineXcharts') 


    # 
    flineXcharts0= Form(db.dflineXcharts0, dbio=False, formstyle=FormStyleBulma)
    if flineXcharts0.accepted:
        icon_type ='success' if insert_form_vars(flineXcharts0, db.dflineXcharts0) else 'info'
        return json2user(mess = str( flineXcharts0.form_name ), icon_type=icon_type )
    elif flineXcharts0.errors:
        print(f"flineXcharts0 has errors: {flineXcharts0.errors}")
        return json2user(mess = str(flineXcharts0.form_name), icon_type = 'error')

    # 
    flineXcharts1= Form(db.dflineXcharts1, dbio=False, formstyle=FormStyleBulma)
    if flineXcharts1.accepted:
        icon_type ='success' if insert_form_vars(flineXcharts1, db.dflineXcharts1) else 'info'
        return json2user(mess = str( flineXcharts1.form_name ), icon_type=icon_type )
    elif flineXcharts1.errors:
        print(f"flineXcharts1 has errors: {flineXcharts1.errors}")
        return json2user(mess = str(flineXcharts1.form_name), icon_type = 'error')

    return locals()

@action('flotXcharts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('flot-charts.html', delimiters='[%[ ]]',))

def flotXcharts():
    ctrl_info= { 'c':'flotXcharts', 'v':'flot-charts.html' }
    messages = ['flotXcharts', 'flot-charts.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('flotXcharts') 


    # 
    fflotXcharts0= Form(db.dfflotXcharts0, dbio=False, formstyle=FormStyleBulma)
    if fflotXcharts0.accepted:
        icon_type ='success' if insert_form_vars(fflotXcharts0, db.dfflotXcharts0) else 'info'
        return json2user(mess = str( fflotXcharts0.form_name ), icon_type=icon_type )
    elif fflotXcharts0.errors:
        print(f"fflotXcharts0 has errors: {fflotXcharts0.errors}")
        return json2user(mess = str(fflotXcharts0.form_name), icon_type = 'error')

    # 
    fflotXcharts1= Form(db.dfflotXcharts1, dbio=False, formstyle=FormStyleBulma)
    if fflotXcharts1.accepted:
        icon_type ='success' if insert_form_vars(fflotXcharts1, db.dfflotXcharts1) else 'info'
        return json2user(mess = str( fflotXcharts1.form_name ), icon_type=icon_type )
    elif fflotXcharts1.errors:
        print(f"fflotXcharts1 has errors: {fflotXcharts1.errors}")
        return json2user(mess = str(fflotXcharts1.form_name), icon_type = 'error')

    return locals()

@action('codeXeditor', method=["GET", "POST"] )
@action.uses(db, session, T, Template('code-editor.html', delimiters='[%[ ]]',))

def codeXeditor():
    ctrl_info= { 'c':'codeXeditor', 'v':'code-editor.html' }
    messages = ['codeXeditor', 'code-editor.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('codeXeditor') 


    # 
    fcodeXeditor0= Form(db.dfcodeXeditor0, dbio=False, formstyle=FormStyleBulma)
    if fcodeXeditor0.accepted:
        icon_type ='success' if insert_form_vars(fcodeXeditor0, db.dfcodeXeditor0) else 'info'
        return json2user(mess = str( fcodeXeditor0.form_name ), icon_type=icon_type )
    elif fcodeXeditor0.errors:
        print(f"fcodeXeditor0 has errors: {fcodeXeditor0.errors}")
        return json2user(mess = str(fcodeXeditor0.form_name), icon_type = 'error')

    # 
    fcodeXeditor1= Form(db.dfcodeXeditor1, dbio=False, formstyle=FormStyleBulma)
    if fcodeXeditor1.accepted:
        icon_type ='success' if insert_form_vars(fcodeXeditor1, db.dfcodeXeditor1) else 'info'
        return json2user(mess = str( fcodeXeditor1.form_name ), icon_type=icon_type )
    elif fcodeXeditor1.errors:
        print(f"fcodeXeditor1 has errors: {fcodeXeditor1.errors}")
        return json2user(mess = str(fcodeXeditor1.form_name), icon_type = 'error')

    return locals()

@action('areaXcharts', method=["GET", "POST"] )
@action.uses(db, session, T, Template('area-charts.html', delimiters='[%[ ]]',))

def areaXcharts():
    ctrl_info= { 'c':'areaXcharts', 'v':'area-charts.html' }
    messages = ['areaXcharts', 'area-charts.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('areaXcharts') 


    # 
    fareaXcharts0= Form(db.dfareaXcharts0, dbio=False, formstyle=FormStyleBulma)
    if fareaXcharts0.accepted:
        icon_type ='success' if insert_form_vars(fareaXcharts0, db.dfareaXcharts0) else 'info'
        return json2user(mess = str( fareaXcharts0.form_name ), icon_type=icon_type )
    elif fareaXcharts0.errors:
        print(f"fareaXcharts0 has errors: {fareaXcharts0.errors}")
        return json2user(mess = str(fareaXcharts0.form_name), icon_type = 'error')

    # 
    fareaXcharts1= Form(db.dfareaXcharts1, dbio=False, formstyle=FormStyleBulma)
    if fareaXcharts1.accepted:
        icon_type ='success' if insert_form_vars(fareaXcharts1, db.dfareaXcharts1) else 'info'
        return json2user(mess = str( fareaXcharts1.form_name ), icon_type=icon_type )
    elif fareaXcharts1.errors:
        print(f"fareaXcharts1 has errors: {fareaXcharts1.errors}")
        return json2user(mess = str(fareaXcharts1.form_name), icon_type = 'error')

    return locals()

@action('normalXtable', method=["GET", "POST"] )
@action.uses(db, session, T, Template('normal-table.html', delimiters='[%[ ]]',))

def normalXtable():
    ctrl_info= { 'c':'normalXtable', 'v':'normal-table.html' }
    messages = ['normalXtable', 'normal-table.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('normalXtable') 


    rows_tnormalXtable0= db(db.tnormalXtable0).select()
    rows_tnormalXtable1= db(db.tnormalXtable1).select()
    rows_tnormalXtable2= db(db.tnormalXtable2).select()
    rows_tnormalXtable3= db(db.tnormalXtable3).select()
    rows_tnormalXtable4= db(db.tnormalXtable4).select()
    rows_tnormalXtable5= db(db.tnormalXtable5).select()
    # 
    fnormalXtable0= Form(db.dfnormalXtable0, dbio=False, formstyle=FormStyleBulma)
    if fnormalXtable0.accepted:
        icon_type ='success' if insert_form_vars(fnormalXtable0, db.dfnormalXtable0) else 'info'
        return json2user(mess = str( fnormalXtable0.form_name ), icon_type=icon_type )
    elif fnormalXtable0.errors:
        print(f"fnormalXtable0 has errors: {fnormalXtable0.errors}")
        return json2user(mess = str(fnormalXtable0.form_name), icon_type = 'error')

    # 
    fnormalXtable1= Form(db.dfnormalXtable1, dbio=False, formstyle=FormStyleBulma)
    if fnormalXtable1.accepted:
        icon_type ='success' if insert_form_vars(fnormalXtable1, db.dfnormalXtable1) else 'info'
        return json2user(mess = str( fnormalXtable1.form_name ), icon_type=icon_type )
    elif fnormalXtable1.errors:
        print(f"fnormalXtable1 has errors: {fnormalXtable1.errors}")
        return json2user(mess = str(fnormalXtable1.form_name), icon_type = 'error')

    return locals()

@action('notification', method=["GET", "POST"] )
@action.uses(db, session, T, Template('notification.html', delimiters='[%[ ]]',))

def notification():
    ctrl_info= { 'c':'notification', 'v':'notification.html' }
    messages = ['notification', 'notification.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('notification') 


    # 
    fnotification0= Form(db.dfnotification0, dbio=False, formstyle=FormStyleBulma)
    if fnotification0.accepted:
        icon_type ='success' if insert_form_vars(fnotification0, db.dfnotification0) else 'info'
        return json2user(mess = str( fnotification0.form_name ), icon_type=icon_type )
    elif fnotification0.errors:
        print(f"fnotification0 has errors: {fnotification0.errors}")
        return json2user(mess = str(fnotification0.form_name), icon_type = 'error')

    # 
    fnotification1= Form(db.dfnotification1, dbio=False, formstyle=FormStyleBulma)
    if fnotification1.accepted:
        icon_type ='success' if insert_form_vars(fnotification1, db.dfnotification1) else 'info'
        return json2user(mess = str( fnotification1.form_name ), icon_type=icon_type )
    elif fnotification1.errors:
        print(f"fnotification1 has errors: {fnotification1.errors}")
        return json2user(mess = str(fnotification1.form_name), icon_type = 'error')

    return locals()

@action('imageXcropper', method=["GET", "POST"] )
@action.uses(db, session, T, Template('image-cropper.html', delimiters='[%[ ]]',))

def imageXcropper():
    ctrl_info= { 'c':'imageXcropper', 'v':'image-cropper.html' }
    messages = ['imageXcropper', 'image-cropper.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('imageXcropper') 


    # 
    fimageXcropper0= Form(db.dfimageXcropper0, dbio=False, formstyle=FormStyleBulma)
    if fimageXcropper0.accepted:
        icon_type ='success' if insert_form_vars(fimageXcropper0, db.dfimageXcropper0) else 'info'
        return json2user(mess = str( fimageXcropper0.form_name ), icon_type=icon_type )
    elif fimageXcropper0.errors:
        print(f"fimageXcropper0 has errors: {fimageXcropper0.errors}")
        return json2user(mess = str(fimageXcropper0.form_name), icon_type = 'error')

    # 
    fimageXcropper1= Form(db.dfimageXcropper1, dbio=False, formstyle=FormStyleBulma)
    if fimageXcropper1.accepted:
        icon_type ='success' if insert_form_vars(fimageXcropper1, db.dfimageXcropper1) else 'info'
        return json2user(mess = str( fimageXcropper1.form_name ), icon_type=icon_type )
    elif fimageXcropper1.errors:
        print(f"fimageXcropper1 has errors: {fimageXcropper1.errors}")
        return json2user(mess = str(fimageXcropper1.form_name), icon_type = 'error')

    return locals()

@action('formXexamples', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form-examples.html', delimiters='[%[ ]]',))

def formXexamples():
    ctrl_info= { 'c':'formXexamples', 'v':'form-examples.html' }
    messages = ['formXexamples', 'form-examples.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('formXexamples') 


    # 
    fformXexamples0= Form(db.dfformXexamples0, dbio=False, formstyle=FormStyleBulma)
    if fformXexamples0.accepted:
        icon_type ='success' if insert_form_vars(fformXexamples0, db.dfformXexamples0) else 'info'
        return json2user(mess = str( fformXexamples0.form_name ), icon_type=icon_type )
    elif fformXexamples0.errors:
        print(f"fformXexamples0 has errors: {fformXexamples0.errors}")
        return json2user(mess = str(fformXexamples0.form_name), icon_type = 'error')

    # 
    fformXexamples1= Form(db.dfformXexamples1, dbio=False, formstyle=FormStyleBulma)
    if fformXexamples1.accepted:
        icon_type ='success' if insert_form_vars(fformXexamples1, db.dfformXexamples1) else 'info'
        return json2user(mess = str( fformXexamples1.form_name ), icon_type=icon_type )
    elif fformXexamples1.errors:
        print(f"fformXexamples1 has errors: {fformXexamples1.errors}")
        return json2user(mess = str(fformXexamples1.form_name), icon_type = 'error')

    # 
    fformXexamples2= Form(db.dfformXexamples2, dbio=False, formstyle=FormStyleBulma)
    if fformXexamples2.accepted:
        icon_type ='success' if insert_form_vars(fformXexamples2, db.dfformXexamples2) else 'info'
        return json2user(mess = str( fformXexamples2.form_name ), icon_type=icon_type )
    elif fformXexamples2.errors:
        print(f"fformXexamples2 has errors: {fformXexamples2.errors}")
        return json2user(mess = str(fformXexamples2.form_name), icon_type = 'error')

    # 
    fformXexamples3= Form(db.dfformXexamples3, dbio=False, formstyle=FormStyleBulma)
    if fformXexamples3.accepted:
        icon_type ='success' if insert_form_vars(fformXexamples3, db.dfformXexamples3) else 'info'
        return json2user(mess = str( fformXexamples3.form_name ), icon_type=icon_type )
    elif fformXexamples3.errors:
        print(f"fformXexamples3 has errors: {fformXexamples3.errors}")
        return json2user(mess = str(fformXexamples3.form_name), icon_type = 'error')

    # 
    fformXexamples4= Form(db.dfformXexamples4, dbio=False, formstyle=FormStyleBulma)
    if fformXexamples4.accepted:
        icon_type ='success' if insert_form_vars(fformXexamples4, db.dfformXexamples4) else 'info'
        return json2user(mess = str( fformXexamples4.form_name ), icon_type=icon_type )
    elif fformXexamples4.errors:
        print(f"fformXexamples4 has errors: {fformXexamples4.errors}")
        return json2user(mess = str(fformXexamples4.form_name), icon_type = 'error')

    # 
    fformXexamples5= Form(db.dfformXexamples5, dbio=False, formstyle=FormStyleBulma)
    if fformXexamples5.accepted:
        icon_type ='success' if insert_form_vars(fformXexamples5, db.dfformXexamples5) else 'info'
        return json2user(mess = str( fformXexamples5.form_name ), icon_type=icon_type )
    elif fformXexamples5.errors:
        print(f"fformXexamples5 has errors: {fformXexamples5.errors}")
        return json2user(mess = str(fformXexamples5.form_name), icon_type = 'error')

    # 
    fformXexamples6= Form(db.dfformXexamples6, dbio=False, formstyle=FormStyleBulma)
    if fformXexamples6.accepted:
        icon_type ='success' if insert_form_vars(fformXexamples6, db.dfformXexamples6) else 'info'
        return json2user(mess = str( fformXexamples6.form_name ), icon_type=icon_type )
    elif fformXexamples6.errors:
        print(f"fformXexamples6 has errors: {fformXexamples6.errors}")
        return json2user(mess = str(fformXexamples6.form_name), icon_type = 'error')

    # 
    fformXexamples7= Form(db.dfformXexamples7, dbio=False, formstyle=FormStyleBulma)
    if fformXexamples7.accepted:
        icon_type ='success' if insert_form_vars(fformXexamples7, db.dfformXexamples7) else 'info'
        return json2user(mess = str( fformXexamples7.form_name ), icon_type=icon_type )
    elif fformXexamples7.errors:
        print(f"fformXexamples7 has errors: {fformXexamples7.errors}")
        return json2user(mess = str(fformXexamples7.form_name), icon_type = 'error')

    # 
    fformXexamples8= Form(db.dfformXexamples8, dbio=False, formstyle=FormStyleBulma)
    if fformXexamples8.accepted:
        icon_type ='success' if insert_form_vars(fformXexamples8, db.dfformXexamples8) else 'info'
        return json2user(mess = str( fformXexamples8.form_name ), icon_type=icon_type )
    elif fformXexamples8.errors:
        print(f"fformXexamples8 has errors: {fformXexamples8.errors}")
        return json2user(mess = str(fformXexamples8.form_name), icon_type = 'error')

    # 
    fformXexamples9= Form(db.dfformXexamples9, dbio=False, formstyle=FormStyleBulma)
    if fformXexamples9.accepted:
        icon_type ='success' if insert_form_vars(fformXexamples9, db.dfformXexamples9) else 'info'
        return json2user(mess = str( fformXexamples9.form_name ), icon_type=icon_type )
    elif fformXexamples9.errors:
        print(f"fformXexamples9 has errors: {fformXexamples9.errors}")
        return json2user(mess = str(fformXexamples9.form_name), icon_type = 'error')

    # 
    fformXexamples10= Form(db.dfformXexamples10, dbio=False, formstyle=FormStyleBulma)
    if fformXexamples10.accepted:
        icon_type ='success' if insert_form_vars(fformXexamples10, db.dfformXexamples10) else 'info'
        return json2user(mess = str( fformXexamples10.form_name ), icon_type=icon_type )
    elif fformXexamples10.errors:
        print(f"fformXexamples10 has errors: {fformXexamples10.errors}")
        return json2user(mess = str(fformXexamples10.form_name), icon_type = 'error')

    return locals()

@action('formXelements', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form-elements.html', delimiters='[%[ ]]',))

def formXelements():
    ctrl_info= { 'c':'formXelements', 'v':'form-elements.html' }
    messages = ['formXelements', 'form-elements.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('formXelements') 


    # 
    fformXelements0= Form(db.dfformXelements0, dbio=False, formstyle=FormStyleBulma)
    if fformXelements0.accepted:
        icon_type ='success' if insert_form_vars(fformXelements0, db.dfformXelements0) else 'info'
        return json2user(mess = str( fformXelements0.form_name ), icon_type=icon_type )
    elif fformXelements0.errors:
        print(f"fformXelements0 has errors: {fformXelements0.errors}")
        return json2user(mess = str(fformXelements0.form_name), icon_type = 'error')

    # 
    fformXelements1= Form(db.dfformXelements1, dbio=False, formstyle=FormStyleBulma)
    if fformXelements1.accepted:
        icon_type ='success' if insert_form_vars(fformXelements1, db.dfformXelements1) else 'info'
        return json2user(mess = str( fformXelements1.form_name ), icon_type=icon_type )
    elif fformXelements1.errors:
        print(f"fformXelements1 has errors: {fformXelements1.errors}")
        return json2user(mess = str(fformXelements1.form_name), icon_type = 'error')

    # 
    fformXelements2= Form(db.dfformXelements2, dbio=False, formstyle=FormStyleBulma)
    if fformXelements2.accepted:
        icon_type ='success' if insert_form_vars(fformXelements2, db.dfformXelements2) else 'info'
        return json2user(mess = str( fformXelements2.form_name ), icon_type=icon_type )
    elif fformXelements2.errors:
        print(f"fformXelements2 has errors: {fformXelements2.errors}")
        return json2user(mess = str(fformXelements2.form_name), icon_type = 'error')

    # 
    fformXelements3= Form(db.dfformXelements3, dbio=False, formstyle=FormStyleBulma)
    if fformXelements3.accepted:
        icon_type ='success' if insert_form_vars(fformXelements3, db.dfformXelements3) else 'info'
        return json2user(mess = str( fformXelements3.form_name ), icon_type=icon_type )
    elif fformXelements3.errors:
        print(f"fformXelements3 has errors: {fformXelements3.errors}")
        return json2user(mess = str(fformXelements3.form_name), icon_type = 'error')

    # 
    fformXelements4= Form(db.dfformXelements4, dbio=False, formstyle=FormStyleBulma)
    if fformXelements4.accepted:
        icon_type ='success' if insert_form_vars(fformXelements4, db.dfformXelements4) else 'info'
        return json2user(mess = str( fformXelements4.form_name ), icon_type=icon_type )
    elif fformXelements4.errors:
        print(f"fformXelements4 has errors: {fformXelements4.errors}")
        return json2user(mess = str(fformXelements4.form_name), icon_type = 'error')

    # 
    fformXelements5= Form(db.dfformXelements5, dbio=False, formstyle=FormStyleBulma)
    if fformXelements5.accepted:
        icon_type ='success' if insert_form_vars(fformXelements5, db.dfformXelements5) else 'info'
        return json2user(mess = str( fformXelements5.form_name ), icon_type=icon_type )
    elif fformXelements5.errors:
        print(f"fformXelements5 has errors: {fformXelements5.errors}")
        return json2user(mess = str(fformXelements5.form_name), icon_type = 'error')

    # 
    fformXelements6= Form(db.dfformXelements6, dbio=False, formstyle=FormStyleBulma)
    if fformXelements6.accepted:
        icon_type ='success' if insert_form_vars(fformXelements6, db.dfformXelements6) else 'info'
        return json2user(mess = str( fformXelements6.form_name ), icon_type=icon_type )
    elif fformXelements6.errors:
        print(f"fformXelements6 has errors: {fformXelements6.errors}")
        return json2user(mess = str(fformXelements6.form_name), icon_type = 'error')

    # 
    fformXelements7= Form(db.dfformXelements7, dbio=False, formstyle=FormStyleBulma)
    if fformXelements7.accepted:
        icon_type ='success' if insert_form_vars(fformXelements7, db.dfformXelements7) else 'info'
        return json2user(mess = str( fformXelements7.form_name ), icon_type=icon_type )
    elif fformXelements7.errors:
        print(f"fformXelements7 has errors: {fformXelements7.errors}")
        return json2user(mess = str(fformXelements7.form_name), icon_type = 'error')

    # 
    fformXelements8= Form(db.dfformXelements8, dbio=False, formstyle=FormStyleBulma)
    if fformXelements8.accepted:
        icon_type ='success' if insert_form_vars(fformXelements8, db.dfformXelements8) else 'info'
        return json2user(mess = str( fformXelements8.form_name ), icon_type=icon_type )
    elif fformXelements8.errors:
        print(f"fformXelements8 has errors: {fformXelements8.errors}")
        return json2user(mess = str(fformXelements8.form_name), icon_type = 'error')

    # 
    fformXelements9= Form(db.dfformXelements9, dbio=False, formstyle=FormStyleBulma)
    if fformXelements9.accepted:
        icon_type ='success' if insert_form_vars(fformXelements9, db.dfformXelements9) else 'info'
        return json2user(mess = str( fformXelements9.form_name ), icon_type=icon_type )
    elif fformXelements9.errors:
        print(f"fformXelements9 has errors: {fformXelements9.errors}")
        return json2user(mess = str(fformXelements9.form_name), icon_type = 'error')

    # 
    fformXelements10= Form(db.dfformXelements10, dbio=False, formstyle=FormStyleBulma)
    if fformXelements10.accepted:
        icon_type ='success' if insert_form_vars(fformXelements10, db.dfformXelements10) else 'info'
        return json2user(mess = str( fformXelements10.form_name ), icon_type=icon_type )
    elif fformXelements10.errors:
        print(f"fformXelements10 has errors: {fformXelements10.errors}")
        return json2user(mess = str(fformXelements10.form_name), icon_type = 'error')

    # 
    fformXelements11= Form(db.dfformXelements11, dbio=False, formstyle=FormStyleBulma)
    if fformXelements11.accepted:
        icon_type ='success' if insert_form_vars(fformXelements11, db.dfformXelements11) else 'info'
        return json2user(mess = str( fformXelements11.form_name ), icon_type=icon_type )
    elif fformXelements11.errors:
        print(f"fformXelements11 has errors: {fformXelements11.errors}")
        return json2user(mess = str(fformXelements11.form_name), icon_type = 'error')

    # 
    fformXelements12= Form(db.dfformXelements12, dbio=False, formstyle=FormStyleBulma)
    if fformXelements12.accepted:
        icon_type ='success' if insert_form_vars(fformXelements12, db.dfformXelements12) else 'info'
        return json2user(mess = str( fformXelements12.form_name ), icon_type=icon_type )
    elif fformXelements12.errors:
        print(f"fformXelements12 has errors: {fformXelements12.errors}")
        return json2user(mess = str(fformXelements12.form_name), icon_type = 'error')

    # 
    fformXelements13= Form(db.dfformXelements13, dbio=False, formstyle=FormStyleBulma)
    if fformXelements13.accepted:
        icon_type ='success' if insert_form_vars(fformXelements13, db.dfformXelements13) else 'info'
        return json2user(mess = str( fformXelements13.form_name ), icon_type=icon_type )
    elif fformXelements13.errors:
        print(f"fformXelements13 has errors: {fformXelements13.errors}")
        return json2user(mess = str(fformXelements13.form_name), icon_type = 'error')

    # 
    fformXelements14= Form(db.dfformXelements14, dbio=False, formstyle=FormStyleBulma)
    if fformXelements14.accepted:
        icon_type ='success' if insert_form_vars(fformXelements14, db.dfformXelements14) else 'info'
        return json2user(mess = str( fformXelements14.form_name ), icon_type=icon_type )
    elif fformXelements14.errors:
        print(f"fformXelements14 has errors: {fformXelements14.errors}")
        return json2user(mess = str(fformXelements14.form_name), icon_type = 'error')

    # 
    fformXelements15= Form(db.dfformXelements15, dbio=False, formstyle=FormStyleBulma)
    if fformXelements15.accepted:
        icon_type ='success' if insert_form_vars(fformXelements15, db.dfformXelements15) else 'info'
        return json2user(mess = str( fformXelements15.form_name ), icon_type=icon_type )
    elif fformXelements15.errors:
        print(f"fformXelements15 has errors: {fformXelements15.errors}")
        return json2user(mess = str(fformXelements15.form_name), icon_type = 'error')

    # 
    fformXelements16= Form(db.dfformXelements16, dbio=False, formstyle=FormStyleBulma)
    if fformXelements16.accepted:
        icon_type ='success' if insert_form_vars(fformXelements16, db.dfformXelements16) else 'info'
        return json2user(mess = str( fformXelements16.form_name ), icon_type=icon_type )
    elif fformXelements16.errors:
        print(f"fformXelements16 has errors: {fformXelements16.errors}")
        return json2user(mess = str(fformXelements16.form_name), icon_type = 'error')

    # 
    fformXelements17= Form(db.dfformXelements17, dbio=False, formstyle=FormStyleBulma)
    if fformXelements17.accepted:
        icon_type ='success' if insert_form_vars(fformXelements17, db.dfformXelements17) else 'info'
        return json2user(mess = str( fformXelements17.form_name ), icon_type=icon_type )
    elif fformXelements17.errors:
        print(f"fformXelements17 has errors: {fformXelements17.errors}")
        return json2user(mess = str(fformXelements17.form_name), icon_type = 'error')

    # 
    fformXelements18= Form(db.dfformXelements18, dbio=False, formstyle=FormStyleBulma)
    if fformXelements18.accepted:
        icon_type ='success' if insert_form_vars(fformXelements18, db.dfformXelements18) else 'info'
        return json2user(mess = str( fformXelements18.form_name ), icon_type=icon_type )
    elif fformXelements18.errors:
        print(f"fformXelements18 has errors: {fformXelements18.errors}")
        return json2user(mess = str(fformXelements18.form_name), icon_type = 'error')

    # 
    fformXelements19= Form(db.dfformXelements19, dbio=False, formstyle=FormStyleBulma)
    if fformXelements19.accepted:
        icon_type ='success' if insert_form_vars(fformXelements19, db.dfformXelements19) else 'info'
        return json2user(mess = str( fformXelements19.form_name ), icon_type=icon_type )
    elif fformXelements19.errors:
        print(f"fformXelements19 has errors: {fformXelements19.errors}")
        return json2user(mess = str(fformXelements19.form_name), icon_type = 'error')

    # 
    fformXelements20= Form(db.dfformXelements20, dbio=False, formstyle=FormStyleBulma)
    if fformXelements20.accepted:
        icon_type ='success' if insert_form_vars(fformXelements20, db.dfformXelements20) else 'info'
        return json2user(mess = str( fformXelements20.form_name ), icon_type=icon_type )
    elif fformXelements20.errors:
        print(f"fformXelements20 has errors: {fformXelements20.errors}")
        return json2user(mess = str(fformXelements20.form_name), icon_type = 'error')

    # 
    fformXelements21= Form(db.dfformXelements21, dbio=False, formstyle=FormStyleBulma)
    if fformXelements21.accepted:
        icon_type ='success' if insert_form_vars(fformXelements21, db.dfformXelements21) else 'info'
        return json2user(mess = str( fformXelements21.form_name ), icon_type=icon_type )
    elif fformXelements21.errors:
        print(f"fformXelements21 has errors: {fformXelements21.errors}")
        return json2user(mess = str(fformXelements21.form_name), icon_type = 'error')

    # 
    fformXelements22= Form(db.dfformXelements22, dbio=False, formstyle=FormStyleBulma)
    if fformXelements22.accepted:
        icon_type ='success' if insert_form_vars(fformXelements22, db.dfformXelements22) else 'info'
        return json2user(mess = str( fformXelements22.form_name ), icon_type=icon_type )
    elif fformXelements22.errors:
        print(f"fformXelements22 has errors: {fformXelements22.errors}")
        return json2user(mess = str(fformXelements22.form_name), icon_type = 'error')

    # 
    fformXelements23= Form(db.dfformXelements23, dbio=False, formstyle=FormStyleBulma)
    if fformXelements23.accepted:
        icon_type ='success' if insert_form_vars(fformXelements23, db.dfformXelements23) else 'info'
        return json2user(mess = str( fformXelements23.form_name ), icon_type=icon_type )
    elif fformXelements23.errors:
        print(f"fformXelements23 has errors: {fformXelements23.errors}")
        return json2user(mess = str(fformXelements23.form_name), icon_type = 'error')

    # 
    fformXelements24= Form(db.dfformXelements24, dbio=False, formstyle=FormStyleBulma)
    if fformXelements24.accepted:
        icon_type ='success' if insert_form_vars(fformXelements24, db.dfformXelements24) else 'info'
        return json2user(mess = str( fformXelements24.form_name ), icon_type=icon_type )
    elif fformXelements24.errors:
        print(f"fformXelements24 has errors: {fformXelements24.errors}")
        return json2user(mess = str(fformXelements24.form_name), icon_type = 'error')

    # 
    fformXelements25= Form(db.dfformXelements25, dbio=False, formstyle=FormStyleBulma)
    if fformXelements25.accepted:
        icon_type ='success' if insert_form_vars(fformXelements25, db.dfformXelements25) else 'info'
        return json2user(mess = str( fformXelements25.form_name ), icon_type=icon_type )
    elif fformXelements25.errors:
        print(f"fformXelements25 has errors: {fformXelements25.errors}")
        return json2user(mess = str(fformXelements25.form_name), icon_type = 'error')

    # 
    fformXelements26= Form(db.dfformXelements26, dbio=False, formstyle=FormStyleBulma)
    if fformXelements26.accepted:
        icon_type ='success' if insert_form_vars(fformXelements26, db.dfformXelements26) else 'info'
        return json2user(mess = str( fformXelements26.form_name ), icon_type=icon_type )
    elif fformXelements26.errors:
        print(f"fformXelements26 has errors: {fformXelements26.errors}")
        return json2user(mess = str(fformXelements26.form_name), icon_type = 'error')

    # 
    fformXelements27= Form(db.dfformXelements27, dbio=False, formstyle=FormStyleBulma)
    if fformXelements27.accepted:
        icon_type ='success' if insert_form_vars(fformXelements27, db.dfformXelements27) else 'info'
        return json2user(mess = str( fformXelements27.form_name ), icon_type=icon_type )
    elif fformXelements27.errors:
        print(f"fformXelements27 has errors: {fformXelements27.errors}")
        return json2user(mess = str(fformXelements27.form_name), icon_type = 'error')

    return locals()

@action('composeXemail', method=["GET", "POST"] )
@action.uses(db, session, T, Template('compose-email.html', delimiters='[%[ ]]',))

def composeXemail():
    ctrl_info= { 'c':'composeXemail', 'v':'compose-email.html' }
    messages = ['composeXemail', 'compose-email.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('composeXemail') 


    # 
    fcomposeXemail0= Form(db.dfcomposeXemail0, dbio=False, formstyle=FormStyleBulma)
    if fcomposeXemail0.accepted:
        icon_type ='success' if insert_form_vars(fcomposeXemail0, db.dfcomposeXemail0) else 'info'
        return json2user(mess = str( fcomposeXemail0.form_name ), icon_type=icon_type )
    elif fcomposeXemail0.errors:
        print(f"fcomposeXemail0 has errors: {fcomposeXemail0.errors}")
        return json2user(mess = str(fcomposeXemail0.form_name), icon_type = 'error')

    return locals()

@action('loginXregister', method=["GET", "POST"] )
@action.uses(db, session, T, Template('login-register.html', delimiters='[%[ ]]',))

def loginXregister():
    ctrl_info= { 'c':'loginXregister', 'v':'login-register.html' }
    messages = ['loginXregister', 'login-register.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('loginXregister') 


    # 
    floginXregister0= Form(db.dfloginXregister0, dbio=False, formstyle=FormStyleBulma)
    if floginXregister0.accepted:
        icon_type ='success' if insert_form_vars(floginXregister0, db.dfloginXregister0) else 'info'
        return json2user(mess = str( floginXregister0.form_name ), icon_type=icon_type )
    elif floginXregister0.errors:
        print(f"floginXregister0 has errors: {floginXregister0.errors}")
        return json2user(mess = str(floginXregister0.form_name), icon_type = 'error')

    # 
    floginXregister1= Form(db.dfloginXregister1, dbio=False, formstyle=FormStyleBulma)
    if floginXregister1.accepted:
        icon_type ='success' if insert_form_vars(floginXregister1, db.dfloginXregister1) else 'info'
        return json2user(mess = str( floginXregister1.form_name ), icon_type=icon_type )
    elif floginXregister1.errors:
        print(f"floginXregister1 has errors: {floginXregister1.errors}")
        return json2user(mess = str(floginXregister1.form_name), icon_type = 'error')

    # 
    floginXregister2= Form(db.dfloginXregister2, dbio=False, formstyle=FormStyleBulma)
    if floginXregister2.accepted:
        icon_type ='success' if insert_form_vars(floginXregister2, db.dfloginXregister2) else 'info'
        return json2user(mess = str( floginXregister2.form_name ), icon_type=icon_type )
    elif floginXregister2.errors:
        print(f"floginXregister2 has errors: {floginXregister2.errors}")
        return json2user(mess = str(floginXregister2.form_name), icon_type = 'error')

    # 
    floginXregister3= Form(db.dfloginXregister3, dbio=False, formstyle=FormStyleBulma)
    if floginXregister3.accepted:
        icon_type ='success' if insert_form_vars(floginXregister3, db.dfloginXregister3) else 'info'
        return json2user(mess = str( floginXregister3.form_name ), icon_type=icon_type )
    elif floginXregister3.errors:
        print(f"floginXregister3 has errors: {floginXregister3.errors}")
        return json2user(mess = str(floginXregister3.form_name), icon_type = 'error')

    # 
    floginXregister4= Form(db.dfloginXregister4, dbio=False, formstyle=FormStyleBulma)
    if floginXregister4.accepted:
        icon_type ='success' if insert_form_vars(floginXregister4, db.dfloginXregister4) else 'info'
        return json2user(mess = str( floginXregister4.form_name ), icon_type=icon_type )
    elif floginXregister4.errors:
        print(f"floginXregister4 has errors: {floginXregister4.errors}")
        return json2user(mess = str(floginXregister4.form_name), icon_type = 'error')

    # 
    floginXregister5= Form(db.dfloginXregister5, dbio=False, formstyle=FormStyleBulma)
    if floginXregister5.accepted:
        icon_type ='success' if insert_form_vars(floginXregister5, db.dfloginXregister5) else 'info'
        return json2user(mess = str( floginXregister5.form_name ), icon_type=icon_type )
    elif floginXregister5.errors:
        print(f"floginXregister5 has errors: {floginXregister5.errors}")
        return json2user(mess = str(floginXregister5.form_name), icon_type = 'error')

    # 
    floginXregister6= Form(db.dfloginXregister6, dbio=False, formstyle=FormStyleBulma)
    if floginXregister6.accepted:
        icon_type ='success' if insert_form_vars(floginXregister6, db.dfloginXregister6) else 'info'
        return json2user(mess = str( floginXregister6.form_name ), icon_type=icon_type )
    elif floginXregister6.errors:
        print(f"floginXregister6 has errors: {floginXregister6.errors}")
        return json2user(mess = str(floginXregister6.form_name), icon_type = 'error')

    return locals()

@action('formXcomponents', method=["GET", "POST"] )
@action.uses(db, session, T, Template('form-components.html', delimiters='[%[ ]]',))

def formXcomponents():
    ctrl_info= { 'c':'formXcomponents', 'v':'form-components.html' }
    messages = ['formXcomponents', 'form-components.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('formXcomponents') 


    # 
    fformXcomponents0= Form(db.dfformXcomponents0, dbio=False, formstyle=FormStyleBulma)
    if fformXcomponents0.accepted:
        icon_type ='success' if insert_form_vars(fformXcomponents0, db.dfformXcomponents0) else 'info'
        return json2user(mess = str( fformXcomponents0.form_name ), icon_type=icon_type )
    elif fformXcomponents0.errors:
        print(f"fformXcomponents0 has errors: {fformXcomponents0.errors}")
        return json2user(mess = str(fformXcomponents0.form_name), icon_type = 'error')

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
# curl -X  GET   http://localhost:8000/notika/api/test_table/
# curl -X  GET   http://localhost:8000/notika/api/test_table/9
# curl -X DELETE  http://localhost:8000/notika/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/notika/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/notika/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/notika/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/notika/api/test_table/
#  http         localhost:8000/notika/api/test_table/9
#  http -f POST localhost:8000/notika/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/notika/api/test_table/2
#  http -f PUT localhost:8000/notika/api/test_table/2 f0=111111 f1=2222222 f2=333333

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

@unauthenticated("tabinfo", "tabinfo.html")
def tabinfo():
    user = auth.get_user()
    # simple backand-admin-panel (to be continued)
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    return dict(message=message, )

