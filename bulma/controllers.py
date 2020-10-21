#!/usr/bin/env python3

#
# py4web app, AI-biorex ported 21.10.2020 16:01:04
#

import os
from py4web import action, request, abort, redirect, URL, Field
from yatl.helpers import A
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A
from py4web.core import Template, Reloader

from .common import db, session, T, cache, authenticated, unauthenticated, auth
import bottle

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)

Glb= {'debug': True , 'my_app_name' : "bulma", 'tte_path': '/static/tte' }



@action('tabs', method=["GET", "POST"] )
@action.uses(Template('tabs.html', delimiters='[%[ ]]',), db, session,  T, )

def tabs(id=None):
    ctrl_info= "ctrl: tabs, view: tabs.html"
    messages = []

    rows_ttabs0= db(db.ttabs0).select()
    return locals()


@action('hero', method=["GET", "POST"] )
@action.uses(Template('hero.html', delimiters='[%[ ]]',), db, session,  T, )

def hero(id=None):
    ctrl_info= "ctrl: hero, view: hero.html"
    messages = []

    return locals()


@action('blog', method=["GET", "POST"] )
@action.uses(Template('blog.html', delimiters='[%[ ]]',), db, session,  T, )

def blog(id=None):
    ctrl_info= "ctrl: blog, view: blog.html"
    messages = []

    return locals()


@action('band', method=["GET", "POST"] )
@action.uses(Template('band.html', delimiters='[%[ ]]',), db, session,  T, )

def band(id=None):
    ctrl_info= "ctrl: band, view: band.html"
    messages = []

    dfband0_rows= None
    id_dfband0 = None
    fband0= Form(db.dfband0, id, deletable=False, dbio = False, keep_values = False, form_name = "fband0",  formstyle=FormStyleBulma )
   
    if fband0.accepted:

        Glb['debug'] and print("     fband0 accepted with: %s " % (fband0.vars))
        fband0_f0 = fband0.vars.get('f0','')
        if len ( fband0_f0 ):
            id_dfband0 = db.dfband0.insert( **fband0.vars )
            db.commit()

            if not id_dfband0 is None:
                dfband0_rows = db.dfband0(id_dfband0 )

                if not dfband0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fband0.vars.f0}\" into db.dfband0.f0, id = {id_dfband0}' )
                         print(f"     found db.dfband0.f0: \"{dfband0_rows.f0}\", id = {id_dfband0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fband0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fband0.vars.items() ]
                print()
   
    elif fband0.errors:
        print("fband0 has errors: %s " % (fband0.errors))
 

    return locals()


@action('login', method=["GET", "POST"] )
@action.uses(Template('login.html', delimiters='[%[ ]]',), db, session,  T, )

def login(id=None):
    ctrl_info= "ctrl: login, view: login.html"
    messages = []

    dflogin0_rows= None
    id_dflogin0 = None
    flogin0= Form(db.dflogin0, id, deletable=False, dbio = False, keep_values = False, form_name = "flogin0",  formstyle=FormStyleBulma )
   
    if flogin0.accepted:

        Glb['debug'] and print("     flogin0 accepted with: %s " % (flogin0.vars))
        flogin0_f0 = flogin0.vars.get('f0','')
        if len ( flogin0_f0 ):
            id_dflogin0 = db.dflogin0.insert( **flogin0.vars )
            db.commit()

            if not id_dflogin0 is None:
                dflogin0_rows = db.dflogin0(id_dflogin0 )

                if not dflogin0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flogin0.vars.f0}\" into db.dflogin0.f0, id = {id_dflogin0}' )
                         print(f"     found db.dflogin0.f0: \"{dflogin0_rows.f0}\", id = {id_dflogin0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(flogin0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in flogin0.vars.items() ]
                print()
   
    elif flogin0.errors:
        print("flogin0 has errors: %s " % (flogin0.errors))
 

    return locals()


@action('inbox', method=["GET", "POST"] )
@action.uses(Template('inbox.html', delimiters='[%[ ]]',), db, session,  T, )

def inbox(id=None):
    ctrl_info= "ctrl: inbox, view: inbox.html"
    messages = []

    return locals()


@action('forum', method=["GET", "POST"] )
@action.uses(Template('forum.html', delimiters='[%[ ]]',), db, session,  T, )

def forum(id=None):
    ctrl_info= "ctrl: forum, view: forum.html"
    messages = []

    return locals()


@action('admin', method=["GET", "POST"] )
@action.uses(Template('admin.html', delimiters='[%[ ]]',), db, session,  T, )

def admin(id=None):
    ctrl_info= "ctrl: admin, view: admin.html"
    messages = []

    rows_tadmin0= db(db.tadmin0).select()
    return locals()


@action('cards', method=["GET", "POST"] )
@action.uses(Template('cards.html', delimiters='[%[ ]]',), db, session,  T, )

def cards(id=None):
    ctrl_info= "ctrl: cards, view: cards.html"
    messages = []

    return locals()


@action('cover', method=["GET", "POST"] )
@action.uses(Template('cover.html', delimiters='[%[ ]]',), db, session,  T, )

def cover(id=None):
    ctrl_info= "ctrl: cover, view: cover.html"
    messages = []

    return locals()


@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session,  T, )

def index(id=None):
    ctrl_info= "ctrl: index, view: index.html"
    messages = []

    return locals()


@action('search', method=["GET", "POST"] )
@action.uses(Template('search.html', delimiters='[%[ ]]',), db, session,  T, )

def search(id=None):
    ctrl_info= "ctrl: search, view: search.html"
    messages = []

    return locals()


@action('kanban', method=["GET", "POST"] )
@action.uses(Template('kanban.html', delimiters='[%[ ]]',), db, session,  T, )

def kanban(id=None):
    ctrl_info= "ctrl: kanban, view: kanban.html"
    messages = []

    return locals()


@action('landing', method=["GET", "POST"] )
@action.uses(Template('landing.html', delimiters='[%[ ]]',), db, session,  T, )

def landing(id=None):
    ctrl_info= "ctrl: landing, view: landing.html"
    messages = []

    return locals()


@action('contact', method=["GET", "POST"] )
@action.uses(Template('contact.html', delimiters='[%[ ]]',), db, session,  T, )

def contact(id=None):
    ctrl_info= "ctrl: contact, view: contact.html"
    messages = []

    return locals()


@action('register', method=["GET", "POST"] )
@action.uses(Template('register.html', delimiters='[%[ ]]',), db, session,  T, )

def register(id=None):
    ctrl_info= "ctrl: register, view: register.html"
    messages = []

    dfregister0_rows= None
    id_dfregister0 = None
    fregister0= Form(db.dfregister0, id, deletable=False, dbio = False, keep_values = False, form_name = "fregister0",  formstyle=FormStyleBulma )
   
    if fregister0.accepted:

        Glb['debug'] and print("     fregister0 accepted with: %s " % (fregister0.vars))
        fregister0_f0 = fregister0.vars.get('f0','')
        if len ( fregister0_f0 ):
            id_dfregister0 = db.dfregister0.insert( **fregister0.vars )
            db.commit()

            if not id_dfregister0 is None:
                dfregister0_rows = db.dfregister0(id_dfregister0 )

                if not dfregister0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fregister0.vars.f0}\" into db.dfregister0.f0, id = {id_dfregister0}' )
                         print(f"     found db.dfregister0.f0: \"{dfregister0_rows.f0}\", id = {id_dfregister0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fregister0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fregister0.vars.items() ]
                print()
   
    elif fregister0.errors:
        print("fregister0 has errors: %s " % (fregister0.errors))
 

    return locals()


@action('showcase', method=["GET", "POST"] )
@action.uses(Template('showcase.html', delimiters='[%[ ]]',), db, session,  T, )

def showcase(id=None):
    ctrl_info= "ctrl: showcase, view: showcase.html"
    messages = []

    dfshowcase0_rows= None
    id_dfshowcase0 = None
    fshowcase0= Form(db.dfshowcase0, id, deletable=False, dbio = False, keep_values = False, form_name = "fshowcase0",  formstyle=FormStyleBulma )
   
    if fshowcase0.accepted:

        Glb['debug'] and print("     fshowcase0 accepted with: %s " % (fshowcase0.vars))
        fshowcase0_f0 = fshowcase0.vars.get('f0','')
        if len ( fshowcase0_f0 ):
            id_dfshowcase0 = db.dfshowcase0.insert( **fshowcase0.vars )
            db.commit()

            if not id_dfshowcase0 is None:
                dfshowcase0_rows = db.dfshowcase0(id_dfshowcase0 )

                if not dfshowcase0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fshowcase0.vars.f0}\" into db.dfshowcase0.f0, id = {id_dfshowcase0}' )
                         print(f"     found db.dfshowcase0.f0: \"{dfshowcase0_rows.f0}\", id = {id_dfshowcase0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fshowcase0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fshowcase0.vars.items() ]
                print()
   
    elif fshowcase0.errors:
        print("fshowcase0 has errors: %s " % (fshowcase0.errors))
 

    dfshowcase1_rows= None
    id_dfshowcase1 = None
    fshowcase1= Form(db.dfshowcase1, id, deletable=False, dbio = False, keep_values = False, form_name = "fshowcase1",  formstyle=FormStyleBulma )
   
    if fshowcase1.accepted:

        Glb['debug'] and print("     fshowcase1 accepted with: %s " % (fshowcase1.vars))
        fshowcase1_f0 = fshowcase1.vars.get('f0','')
        if len ( fshowcase1_f0 ):
            id_dfshowcase1 = db.dfshowcase1.insert( **fshowcase1.vars )
            db.commit()

            if not id_dfshowcase1 is None:
                dfshowcase1_rows = db.dfshowcase1(id_dfshowcase1 )

                if not dfshowcase1_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fshowcase1.vars.f0}\" into db.dfshowcase1.f0, id = {id_dfshowcase1}' )
                         print(f"     found db.dfshowcase1.f0: \"{dfshowcase1_rows.f0}\", id = {id_dfshowcase1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fshowcase1_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fshowcase1.vars.items() ]
                print()
   
    elif fshowcase1.errors:
        print("fshowcase1 has errors: %s " % (fshowcase1.errors))
 

    dfshowcase2_rows= None
    id_dfshowcase2 = None
    fshowcase2= Form(db.dfshowcase2, id, deletable=False, dbio = False, keep_values = False, form_name = "fshowcase2",  formstyle=FormStyleBulma )
   
    if fshowcase2.accepted:

        Glb['debug'] and print("     fshowcase2 accepted with: %s " % (fshowcase2.vars))
        fshowcase2_f0 = fshowcase2.vars.get('f0','')
        if len ( fshowcase2_f0 ):
            id_dfshowcase2 = db.dfshowcase2.insert( **fshowcase2.vars )
            db.commit()

            if not id_dfshowcase2 is None:
                dfshowcase2_rows = db.dfshowcase2(id_dfshowcase2 )

                if not dfshowcase2_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fshowcase2.vars.f0}\" into db.dfshowcase2.f0, id = {id_dfshowcase2}' )
                         print(f"     found db.dfshowcase2.f0: \"{dfshowcase2_rows.f0}\", id = {id_dfshowcase2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fshowcase2_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fshowcase2.vars.items() ]
                print()
   
    elif fshowcase2.errors:
        print("fshowcase2 has errors: %s " % (fshowcase2.errors))
 

    return locals()


@action('personal', method=["GET", "POST"] )
@action.uses(Template('personal.html', delimiters='[%[ ]]',), db, session,  T, )

def personal(id=None):
    ctrl_info= "ctrl: personal, view: personal.html"
    messages = []

    rows_tpersonal0= db(db.tpersonal0).select()
    return locals()


@action('instaAlbum', method=["GET", "POST"] )
@action.uses(Template('instaAlbum.html', delimiters='[%[ ]]',), db, session,  T, )

def instaAlbum(id=None):
    ctrl_info= "ctrl: instaAlbum, view: instaAlbum.html"
    messages = []

    return locals()


@action('cheatsheet', method=["GET", "POST"] )
@action.uses(Template('cheatsheet.html', delimiters='[%[ ]]',), db, session,  T, )

def cheatsheet(id=None):
    ctrl_info= "ctrl: cheatsheet, view: cheatsheet.html"
    messages = []

    return locals()


@action('ghostXblog', method=["GET", "POST"] )
@action.uses(Template('ghost-blog.html', delimiters='[%[ ]]',), db, session,  T, )

def ghostXblog(id=None):
    ctrl_info= "ctrl: ghostXblog, view: ghost-blog.html"
    messages = []

    return locals()


@action('modalXcards', method=["GET", "POST"] )
@action.uses(Template('modal-cards.html', delimiters='[%[ ]]',), db, session,  T, )

def modalXcards(id=None):
    ctrl_info= "ctrl: modalXcards, view: modal-cards.html"
    messages = []

    return locals()


@action('blogXtailsaw', method=["GET", "POST"] )
@action.uses(Template('blog-tailsaw.html', delimiters='[%[ ]]',), db, session,  T, )

def blogXtailsaw(id=None):
    ctrl_info= "ctrl: blogXtailsaw, view: blog-tailsaw.html"
    messages = []

    return locals()


@action('kanbanXsearchX', method=["GET", "POST"] )
@action.uses(Template('kanban[search].html', delimiters='[%[ ]]',), db, session,  T, )

def kanbanXsearchX(id=None):
    ctrl_info= "ctrl: kanbanXsearchX, view: kanban[search].html"
    messages = []

    return locals()


@action('helloXparallax', method=["GET", "POST"] )
@action.uses(Template('hello-parallax.html', delimiters='[%[ ]]',), db, session,  T, )

def helloXparallax(id=None):
    ctrl_info= "ctrl: helloXparallax, view: hello-parallax.html"
    messages = []

    return locals()


@action('neumorphicXlogin', method=["GET", "POST"] )
@action.uses(Template('neumorphic-login.html', delimiters='[%[ ]]',), db, session,  T, )

def neumorphicXlogin(id=None):
    ctrl_info= "ctrl: neumorphicXlogin, view: neumorphic-login.html"
    messages = []

    dfneumorphicXlogin0_rows= None
    id_dfneumorphicXlogin0 = None
    fneumorphicXlogin0= Form(db.dfneumorphicXlogin0, id, deletable=False, dbio = False, keep_values = False, form_name = "fneumorphicXlogin0",  formstyle=FormStyleBulma )
   
    if fneumorphicXlogin0.accepted:

        Glb['debug'] and print("     fneumorphicXlogin0 accepted with: %s " % (fneumorphicXlogin0.vars))
        fneumorphicXlogin0_f0 = fneumorphicXlogin0.vars.get('f0','')
        if len ( fneumorphicXlogin0_f0 ):
            id_dfneumorphicXlogin0 = db.dfneumorphicXlogin0.insert( **fneumorphicXlogin0.vars )
            db.commit()

            if not id_dfneumorphicXlogin0 is None:
                dfneumorphicXlogin0_rows = db.dfneumorphicXlogin0(id_dfneumorphicXlogin0 )

                if not dfneumorphicXlogin0_rows is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fneumorphicXlogin0.vars.f0}\" into db.dfneumorphicXlogin0.f0, id = {id_dfneumorphicXlogin0}' )
                         print(f"     found db.dfneumorphicXlogin0.f0: \"{dfneumorphicXlogin0_rows.f0}\", id = {id_dfneumorphicXlogin0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     len(fneumorphicXlogin0_f0)=0, not inserted")  
                _ = [ print (f'     {k}: {v}') for k,v in fneumorphicXlogin0.vars.items() ]
                print()
   
    elif fneumorphicXlogin0.errors:
        print("fneumorphicXlogin0 has errors: %s " % (fneumorphicXlogin0.errors))
 

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

