#
# py4web app, AI-biorex ported 12.10.2021 08:13:19 UTC+3, src: https://github.com/BulmaTemplates/bulma-templates

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

@action('tabs', method=["GET", "POST"] )
@action.uses(db, session, T, Template('tabs.html', delimiters='[%[ ]]',))

def tabs():
    ctrl_info= { 'c':'tabs', 'v':'tabs.html' }
    messages = ['tabs', 'tabs.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('tabs') 


    rows_ttabs0= db(db.ttabs0).select()
    return locals()

@action('hero', method=["GET", "POST"] )
@action.uses(db, session, T, Template('hero.html', delimiters='[%[ ]]',))

def hero():
    ctrl_info= { 'c':'hero', 'v':'hero.html' }
    messages = ['hero', 'hero.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('hero') 


    return locals()

@action('band', method=["GET", "POST"] )
@action.uses(db, session, T, Template('band.html', delimiters='[%[ ]]',))

def band():
    ctrl_info= { 'c':'band', 'v':'band.html' }
    messages = ['band', 'band.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('band') 


    # 
    fband0= Form(db.dfband0, dbio=False, formstyle=FormStyleBulma)
    if fband0.accepted:
        icon_type ='success' if insert_form_vars(fband0, db.dfband0) else 'info'
        return json2user(mess = str( fband0.form_name ), icon_type=icon_type )
    elif fband0.errors:
        print(f"fband0 has errors: {fband0.errors}")
        return json2user(mess = str(fband0.form_name), icon_type = 'error')

    return locals()

@action('blog', method=["GET", "POST"] )
@action.uses(db, session, T, Template('blog.html', delimiters='[%[ ]]',))

def blog():
    ctrl_info= { 'c':'blog', 'v':'blog.html' }
    messages = ['blog', 'blog.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('blog') 


    return locals()

@action('loginA', method=["GET", "POST"] )
@action.uses(db, session, T, Template('login.html', delimiters='[%[ ]]',))

def loginA():
    ctrl_info= { 'c':'loginA', 'v':'login.html' }
    messages = ['loginA', 'login.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('loginA') 


    # 
    floginA0= Form(db.dfloginA0, dbio=False, formstyle=FormStyleBulma)
    if floginA0.accepted:
        icon_type ='success' if insert_form_vars(floginA0, db.dfloginA0) else 'info'
        return json2user(mess = str( floginA0.form_name ), icon_type=icon_type )
    elif floginA0.errors:
        print(f"floginA0 has errors: {floginA0.errors}")
        return json2user(mess = str(floginA0.form_name), icon_type = 'error')

    return locals()

@action('inbox', method=["GET", "POST"] )
@action.uses(db, session, T, Template('inbox.html', delimiters='[%[ ]]',))

def inbox():
    ctrl_info= { 'c':'inbox', 'v':'inbox.html' }
    messages = ['inbox', 'inbox.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('inbox') 


    return locals()

@action('forum', method=["GET", "POST"] )
@action.uses(db, session, T, Template('forum.html', delimiters='[%[ ]]',))

def forum():
    ctrl_info= { 'c':'forum', 'v':'forum.html' }
    messages = ['forum', 'forum.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('forum') 


    # 
    fforum0= Form(db.dfforum0, dbio=False, formstyle=FormStyleBulma)
    if fforum0.accepted:
        icon_type ='success' if insert_form_vars(fforum0, db.dfforum0) else 'info'
        return json2user(mess = str( fforum0.form_name ), icon_type=icon_type )
    elif fforum0.errors:
        print(f"fforum0 has errors: {fforum0.errors}")
        return json2user(mess = str(fforum0.form_name), icon_type = 'error')

    return locals()

@action('cover', method=["GET", "POST"] )
@action.uses(db, session, T, Template('cover.html', delimiters='[%[ ]]',))

def cover():
    ctrl_info= { 'c':'cover', 'v':'cover.html' }
    messages = ['cover', 'cover.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('cover') 


    return locals()

@action('cards', method=["GET", "POST"] )
@action.uses(db, session, T, Template('cards.html', delimiters='[%[ ]]',))

def cards():
    ctrl_info= { 'c':'cards', 'v':'cards.html' }
    messages = ['cards', 'cards.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('cards') 


    return locals()

@action('admin', method=["GET", "POST"] )
@action.uses(db, session, T, Template('admin.html', delimiters='[%[ ]]',))

def admin():
    ctrl_info= { 'c':'admin', 'v':'admin.html' }
    messages = ['admin', 'admin.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('admin') 


    rows_tadmin0= db(db.tadmin0).select()
    # 
    fadmin0= Form(db.dfadmin0, dbio=False, formstyle=FormStyleBulma)
    if fadmin0.accepted:
        icon_type ='success' if insert_form_vars(fadmin0, db.dfadmin0) else 'info'
        return json2user(mess = str( fadmin0.form_name ), icon_type=icon_type )
    elif fadmin0.errors:
        print(f"fadmin0 has errors: {fadmin0.errors}")
        return json2user(mess = str(fadmin0.form_name), icon_type = 'error')

    # 
    fadmin1= Form(db.dfadmin1, dbio=False, formstyle=FormStyleBulma)
    if fadmin1.accepted:
        icon_type ='success' if insert_form_vars(fadmin1, db.dfadmin1) else 'info'
        return json2user(mess = str( fadmin1.form_name ), icon_type=icon_type )
    elif fadmin1.errors:
        print(f"fadmin1 has errors: {fadmin1.errors}")
        return json2user(mess = str(fadmin1.form_name), icon_type = 'error')

    return locals()

@action('index', method=["GET", "POST"] )
@action.uses(db, session, T, Template('index.html', delimiters='[%[ ]]',))

def index():
    ctrl_info= { 'c':'index', 'v':'index.html' }
    messages = ['index', 'index.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('index') 


    return locals()

@action('search', method=["GET", "POST"] )
@action.uses(db, session, T, Template('search.html', delimiters='[%[ ]]',))

def search():
    ctrl_info= { 'c':'search', 'v':'search.html' }
    messages = ['search', 'search.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('search') 


    # 
    fsearch0= Form(db.dfsearch0, dbio=False, formstyle=FormStyleBulma)
    if fsearch0.accepted:
        icon_type ='success' if insert_form_vars(fsearch0, db.dfsearch0) else 'info'
        return json2user(mess = str( fsearch0.form_name ), icon_type=icon_type )
    elif fsearch0.errors:
        print(f"fsearch0 has errors: {fsearch0.errors}")
        return json2user(mess = str(fsearch0.form_name), icon_type = 'error')

    return locals()

@action('absurd', method=["GET", "POST"] )
@action.uses(db, session, T, Template('absurd.html', delimiters='[%[ ]]',))

def absurd():
    ctrl_info= { 'c':'absurd', 'v':'absurd.html' }
    messages = ['absurd', 'absurd.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('absurd') 


    return locals()

@action('kanban', method=["GET", "POST"] )
@action.uses(db, session, T, Template('kanban.html', delimiters='[%[ ]]',))

def kanban():
    ctrl_info= { 'c':'kanban', 'v':'kanban.html' }
    messages = ['kanban', 'kanban.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('kanban') 


    # 
    fkanban0= Form(db.dfkanban0, dbio=False, formstyle=FormStyleBulma)
    if fkanban0.accepted:
        icon_type ='success' if insert_form_vars(fkanban0, db.dfkanban0) else 'info'
        return json2user(mess = str( fkanban0.form_name ), icon_type=icon_type )
    elif fkanban0.errors:
        print(f"fkanban0 has errors: {fkanban0.errors}")
        return json2user(mess = str(fkanban0.form_name), icon_type = 'error')

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

    # 
    fcontact2= Form(db.dfcontact2, dbio=False, formstyle=FormStyleBulma)
    if fcontact2.accepted:
        icon_type ='success' if insert_form_vars(fcontact2, db.dfcontact2) else 'info'
        return json2user(mess = str( fcontact2.form_name ), icon_type=icon_type )
    elif fcontact2.errors:
        print(f"fcontact2 has errors: {fcontact2.errors}")
        return json2user(mess = str(fcontact2.form_name), icon_type = 'error')

    return locals()

@action('landing', method=["GET", "POST"] )
@action.uses(db, session, T, Template('landing.html', delimiters='[%[ ]]',))

def landing():
    ctrl_info= { 'c':'landing', 'v':'landing.html' }
    messages = ['landing', 'landing.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('landing') 


    # 
    flanding0= Form(db.dflanding0, dbio=False, formstyle=FormStyleBulma)
    if flanding0.accepted:
        icon_type ='success' if insert_form_vars(flanding0, db.dflanding0) else 'info'
        return json2user(mess = str( flanding0.form_name ), icon_type=icon_type )
    elif flanding0.errors:
        print(f"flanding0 has errors: {flanding0.errors}")
        return json2user(mess = str(flanding0.form_name), icon_type = 'error')

    return locals()

@action('showcase', method=["GET", "POST"] )
@action.uses(db, session, T, Template('showcase.html', delimiters='[%[ ]]',))

def showcase():
    ctrl_info= { 'c':'showcase', 'v':'showcase.html' }
    messages = ['showcase', 'showcase.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('showcase') 


    # 
    fshowcase0= Form(db.dfshowcase0, dbio=False, formstyle=FormStyleBulma)
    if fshowcase0.accepted:
        icon_type ='success' if insert_form_vars(fshowcase0, db.dfshowcase0) else 'info'
        return json2user(mess = str( fshowcase0.form_name ), icon_type=icon_type )
    elif fshowcase0.errors:
        print(f"fshowcase0 has errors: {fshowcase0.errors}")
        return json2user(mess = str(fshowcase0.form_name), icon_type = 'error')

    # 
    fshowcase1= Form(db.dfshowcase1, dbio=False, formstyle=FormStyleBulma)
    if fshowcase1.accepted:
        icon_type ='success' if insert_form_vars(fshowcase1, db.dfshowcase1) else 'info'
        return json2user(mess = str( fshowcase1.form_name ), icon_type=icon_type )
    elif fshowcase1.errors:
        print(f"fshowcase1 has errors: {fshowcase1.errors}")
        return json2user(mess = str(fshowcase1.form_name), icon_type = 'error')

    # 
    fshowcase2= Form(db.dfshowcase2, dbio=False, formstyle=FormStyleBulma)
    if fshowcase2.accepted:
        icon_type ='success' if insert_form_vars(fshowcase2, db.dfshowcase2) else 'info'
        return json2user(mess = str( fshowcase2.form_name ), icon_type=icon_type )
    elif fshowcase2.errors:
        print(f"fshowcase2 has errors: {fshowcase2.errors}")
        return json2user(mess = str(fshowcase2.form_name), icon_type = 'error')

    return locals()

@action('registerA', method=["GET", "POST"] )
@action.uses(db, session, T, Template('register.html', delimiters='[%[ ]]',))

def registerA():
    ctrl_info= { 'c':'registerA', 'v':'register.html' }
    messages = ['registerA', 'register.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('registerA') 


    # 
    fregisterA0= Form(db.dfregisterA0, dbio=False, formstyle=FormStyleBulma)
    if fregisterA0.accepted:
        icon_type ='success' if insert_form_vars(fregisterA0, db.dfregisterA0) else 'info'
        return json2user(mess = str( fregisterA0.form_name ), icon_type=icon_type )
    elif fregisterA0.errors:
        print(f"fregisterA0 has errors: {fregisterA0.errors}")
        return json2user(mess = str(fregisterA0.form_name), icon_type = 'error')

    return locals()

@action('personal', method=["GET", "POST"] )
@action.uses(db, session, T, Template('personal.html', delimiters='[%[ ]]',))

def personal():
    ctrl_info= { 'c':'personal', 'v':'personal.html' }
    messages = ['personal', 'personal.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('personal') 


    rows_tpersonal0= db(db.tpersonal0).select()
    # 
    fpersonal0= Form(db.dfpersonal0, dbio=False, formstyle=FormStyleBulma)
    if fpersonal0.accepted:
        icon_type ='success' if insert_form_vars(fpersonal0, db.dfpersonal0) else 'info'
        return json2user(mess = str( fpersonal0.form_name ), icon_type=icon_type )
    elif fpersonal0.errors:
        print(f"fpersonal0 has errors: {fpersonal0.errors}")
        return json2user(mess = str(fpersonal0.form_name), icon_type = 'error')

    # 
    fpersonal1= Form(db.dfpersonal1, dbio=False, formstyle=FormStyleBulma)
    if fpersonal1.accepted:
        icon_type ='success' if insert_form_vars(fpersonal1, db.dfpersonal1) else 'info'
        return json2user(mess = str( fpersonal1.form_name ), icon_type=icon_type )
    elif fpersonal1.errors:
        print(f"fpersonal1 has errors: {fpersonal1.errors}")
        return json2user(mess = str(fpersonal1.form_name), icon_type = 'error')

    # 
    fpersonal2= Form(db.dfpersonal2, dbio=False, formstyle=FormStyleBulma)
    if fpersonal2.accepted:
        icon_type ='success' if insert_form_vars(fpersonal2, db.dfpersonal2) else 'info'
        return json2user(mess = str( fpersonal2.form_name ), icon_type=icon_type )
    elif fpersonal2.errors:
        print(f"fpersonal2 has errors: {fpersonal2.errors}")
        return json2user(mess = str(fpersonal2.form_name), icon_type = 'error')

    return locals()

@action('instaAlbum', method=["GET", "POST"] )
@action.uses(db, session, T, Template('instaAlbum.html', delimiters='[%[ ]]',))

def instaAlbum():
    ctrl_info= { 'c':'instaAlbum', 'v':'instaAlbum.html' }
    messages = ['instaAlbum', 'instaAlbum.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('instaAlbum') 


    # 
    finstaAlbum0= Form(db.dfinstaAlbum0, dbio=False, formstyle=FormStyleBulma)
    if finstaAlbum0.accepted:
        icon_type ='success' if insert_form_vars(finstaAlbum0, db.dfinstaAlbum0) else 'info'
        return json2user(mess = str( finstaAlbum0.form_name ), icon_type=icon_type )
    elif finstaAlbum0.errors:
        print(f"finstaAlbum0 has errors: {finstaAlbum0.errors}")
        return json2user(mess = str(finstaAlbum0.form_name), icon_type = 'error')

    # 
    finstaAlbum1= Form(db.dfinstaAlbum1, dbio=False, formstyle=FormStyleBulma)
    if finstaAlbum1.accepted:
        icon_type ='success' if insert_form_vars(finstaAlbum1, db.dfinstaAlbum1) else 'info'
        return json2user(mess = str( finstaAlbum1.form_name ), icon_type=icon_type )
    elif finstaAlbum1.errors:
        print(f"finstaAlbum1 has errors: {finstaAlbum1.errors}")
        return json2user(mess = str(finstaAlbum1.form_name), icon_type = 'error')

    # 
    finstaAlbum2= Form(db.dfinstaAlbum2, dbio=False, formstyle=FormStyleBulma)
    if finstaAlbum2.accepted:
        icon_type ='success' if insert_form_vars(finstaAlbum2, db.dfinstaAlbum2) else 'info'
        return json2user(mess = str( finstaAlbum2.form_name ), icon_type=icon_type )
    elif finstaAlbum2.errors:
        print(f"finstaAlbum2 has errors: {finstaAlbum2.errors}")
        return json2user(mess = str(finstaAlbum2.form_name), icon_type = 'error')

    # 
    finstaAlbum3= Form(db.dfinstaAlbum3, dbio=False, formstyle=FormStyleBulma)
    if finstaAlbum3.accepted:
        icon_type ='success' if insert_form_vars(finstaAlbum3, db.dfinstaAlbum3) else 'info'
        return json2user(mess = str( finstaAlbum3.form_name ), icon_type=icon_type )
    elif finstaAlbum3.errors:
        print(f"finstaAlbum3 has errors: {finstaAlbum3.errors}")
        return json2user(mess = str(finstaAlbum3.form_name), icon_type = 'error')

    return locals()

@action('ghostXblog', method=["GET", "POST"] )
@action.uses(db, session, T, Template('ghost-blog.html', delimiters='[%[ ]]',))

def ghostXblog():
    ctrl_info= { 'c':'ghostXblog', 'v':'ghost-blog.html' }
    messages = ['ghostXblog', 'ghost-blog.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('ghostXblog') 


    return locals()

@action('cheatsheet', method=["GET", "POST"] )
@action.uses(db, session, T, Template('cheatsheet.html', delimiters='[%[ ]]',))

def cheatsheet():
    ctrl_info= { 'c':'cheatsheet', 'v':'cheatsheet.html' }
    messages = ['cheatsheet', 'cheatsheet.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('cheatsheet') 


    return locals()

@action('modalXcards', method=["GET", "POST"] )
@action.uses(db, session, T, Template('modal-cards.html', delimiters='[%[ ]]',))

def modalXcards():
    ctrl_info= { 'c':'modalXcards', 'v':'modal-cards.html' }
    messages = ['modalXcards', 'modal-cards.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('modalXcards') 


    return locals()

@action('blogXtailsaw', method=["GET", "POST"] )
@action.uses(db, session, T, Template('blog-tailsaw.html', delimiters='[%[ ]]',))

def blogXtailsaw():
    ctrl_info= { 'c':'blogXtailsaw', 'v':'blog-tailsaw.html' }
    messages = ['blogXtailsaw', 'blog-tailsaw.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('blogXtailsaw') 


    # 
    fblogXtailsaw0= Form(db.dfblogXtailsaw0, dbio=False, formstyle=FormStyleBulma)
    if fblogXtailsaw0.accepted:
        icon_type ='success' if insert_form_vars(fblogXtailsaw0, db.dfblogXtailsaw0) else 'info'
        return json2user(mess = str( fblogXtailsaw0.form_name ), icon_type=icon_type )
    elif fblogXtailsaw0.errors:
        print(f"fblogXtailsaw0 has errors: {fblogXtailsaw0.errors}")
        return json2user(mess = str(fblogXtailsaw0.form_name), icon_type = 'error')

    # 
    fblogXtailsaw1= Form(db.dfblogXtailsaw1, dbio=False, formstyle=FormStyleBulma)
    if fblogXtailsaw1.accepted:
        icon_type ='success' if insert_form_vars(fblogXtailsaw1, db.dfblogXtailsaw1) else 'info'
        return json2user(mess = str( fblogXtailsaw1.form_name ), icon_type=icon_type )
    elif fblogXtailsaw1.errors:
        print(f"fblogXtailsaw1 has errors: {fblogXtailsaw1.errors}")
        return json2user(mess = str(fblogXtailsaw1.form_name), icon_type = 'error')

    return locals()

@action('documentation', method=["GET", "POST"] )
@action.uses(db, session, T, Template('documentation.html', delimiters='[%[ ]]',))

def documentation():
    ctrl_info= { 'c':'documentation', 'v':'documentation.html' }
    messages = ['documentation', 'documentation.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('documentation') 


    # 
    fdocumentation0= Form(db.dfdocumentation0, dbio=False, formstyle=FormStyleBulma)
    if fdocumentation0.accepted:
        icon_type ='success' if insert_form_vars(fdocumentation0, db.dfdocumentation0) else 'info'
        return json2user(mess = str( fdocumentation0.form_name ), icon_type=icon_type )
    elif fdocumentation0.errors:
        print(f"fdocumentation0 has errors: {fdocumentation0.errors}")
        return json2user(mess = str(fdocumentation0.form_name), icon_type = 'error')

    return locals()

@action('kanbanXsearchX', method=["GET", "POST"] )
@action.uses(db, session, T, Template('kanban[search].html', delimiters='[%[ ]]',))

def kanbanXsearchX():
    ctrl_info= { 'c':'kanbanXsearchX', 'v':'kanban[search].html' }
    messages = ['kanbanXsearchX', 'kanban[search].html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('kanbanXsearchX') 


    # 
    fkanbanXsearchX0= Form(db.dfkanbanXsearchX0, dbio=False, formstyle=FormStyleBulma)
    if fkanbanXsearchX0.accepted:
        icon_type ='success' if insert_form_vars(fkanbanXsearchX0, db.dfkanbanXsearchX0) else 'info'
        return json2user(mess = str( fkanbanXsearchX0.form_name ), icon_type=icon_type )
    elif fkanbanXsearchX0.errors:
        print(f"fkanbanXsearchX0 has errors: {fkanbanXsearchX0.errors}")
        return json2user(mess = str(fkanbanXsearchX0.form_name), icon_type = 'error')

    return locals()

@action('helloXparallax', method=["GET", "POST"] )
@action.uses(db, session, T, Template('hello-parallax.html', delimiters='[%[ ]]',))

def helloXparallax():
    ctrl_info= { 'c':'helloXparallax', 'v':'hello-parallax.html' }
    messages = ['helloXparallax', 'hello-parallax.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('helloXparallax') 


    # 
    fhelloXparallax0= Form(db.dfhelloXparallax0, dbio=False, formstyle=FormStyleBulma)
    if fhelloXparallax0.accepted:
        icon_type ='success' if insert_form_vars(fhelloXparallax0, db.dfhelloXparallax0) else 'info'
        return json2user(mess = str( fhelloXparallax0.form_name ), icon_type=icon_type )
    elif fhelloXparallax0.errors:
        print(f"fhelloXparallax0 has errors: {fhelloXparallax0.errors}")
        return json2user(mess = str(fhelloXparallax0.form_name), icon_type = 'error')

    # 
    fhelloXparallax1= Form(db.dfhelloXparallax1, dbio=False, formstyle=FormStyleBulma)
    if fhelloXparallax1.accepted:
        icon_type ='success' if insert_form_vars(fhelloXparallax1, db.dfhelloXparallax1) else 'info'
        return json2user(mess = str( fhelloXparallax1.form_name ), icon_type=icon_type )
    elif fhelloXparallax1.errors:
        print(f"fhelloXparallax1 has errors: {fhelloXparallax1.errors}")
        return json2user(mess = str(fhelloXparallax1.form_name), icon_type = 'error')

    return locals()

@action('neumorphicXlogin', method=["GET", "POST"] )
@action.uses(db, session, T, Template('neumorphic-login.html', delimiters='[%[ ]]',))

def neumorphicXlogin():
    ctrl_info= { 'c':'neumorphicXlogin', 'v':'neumorphic-login.html' }
    messages = ['neumorphicXlogin', 'neumorphic-login.html']

    ctrl_tabinfo_url =  get_ctrl_url('tabinfo') 
    ctrl_template_url = get_ctrl_url('neumorphicXlogin') 


    # 
    fneumorphicXlogin0= Form(db.dfneumorphicXlogin0, dbio=False, formstyle=FormStyleBulma)
    if fneumorphicXlogin0.accepted:
        icon_type ='success' if insert_form_vars(fneumorphicXlogin0, db.dfneumorphicXlogin0) else 'info'
        return json2user(mess = str( fneumorphicXlogin0.form_name ), icon_type=icon_type )
    elif fneumorphicXlogin0.errors:
        print(f"fneumorphicXlogin0 has errors: {fneumorphicXlogin0.errors}")
        return json2user(mess = str(fneumorphicXlogin0.form_name), icon_type = 'error')

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
# curl -X  GET   http://localhost:8000/bulma/api/test_table/
# curl -X  GET   http://localhost:8000/bulma/api/test_table/9
# curl -X DELETE  http://localhost:8000/bulma/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/bulma/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/bulma/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/bulma/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/bulma/api/test_table/
#  http         localhost:8000/bulma/api/test_table/9
#  http -f POST localhost:8000/bulma/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/bulma/api/test_table/2
#  http -f PUT localhost:8000/bulma/api/test_table/2 f0=111111 f1=2222222 f2=333333

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

