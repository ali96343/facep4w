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



@action('blog', method=["GET", "POST"] )
@action.uses(Template('blog.html', delimiters='[%[ ]]',), db, session, T, )

def blog(id=None):
    ctrl_info= "ctrl: blog, view: blog.html"

    return locals()


@action('hero', method=["GET", "POST"] )
@action.uses(Template('hero.html', delimiters='[%[ ]]',), db, session, T, )

def hero(id=None):
    ctrl_info= "ctrl: hero, view: hero.html"

    return locals()


@action('band', method=["GET", "POST"] )
@action.uses(Template('band.html', delimiters='[%[ ]]',), db, session, T, )

def band(id=None):
    ctrl_info= "ctrl: band, view: band.html"

    dfband0_rows=''
    fband0= Form(db.dfband0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fband0.vars is None:  
        fband0_f0 = fband0.vars.get('f0','')
        if len ( fband0_f0 ):
            db.dfband0.insert( **fband0.vars )
            dfband0_rows = db( db.dfband0 ).select()
            print (f'insert: \"{fband0.vars.f0}\" in db.dfband0; dfband0: {len(dfband0_rows)} rows' )

    return locals()


@action('tabs', method=["GET", "POST"] )
@action.uses(Template('tabs.html', delimiters='[%[ ]]',), db, session, T, )

def tabs(id=None):
    ctrl_info= "ctrl: tabs, view: tabs.html"

    rows_ttabs0= db(db.ttabs0).select()
    return locals()


@action('admin', method=["GET", "POST"] )
@action.uses(Template('admin.html', delimiters='[%[ ]]',), db, session, T, )

def admin(id=None):
    ctrl_info= "ctrl: admin, view: admin.html"

    rows_tadmin0= db(db.tadmin0).select()
    dfadmin0_rows=''
    fadmin0= Form(db.dfadmin0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fadmin0.vars is None:  
        fadmin0_f0 = fadmin0.vars.get('f0','')
        if len ( fadmin0_f0 ):
            db.dfadmin0.insert( **fadmin0.vars )
            dfadmin0_rows = db( db.dfadmin0 ).select()
            print (f'insert: \"{fadmin0.vars.f0}\" in db.dfadmin0; dfadmin0: {len(dfadmin0_rows)} rows' )

    dfadmin1_rows=''
    fadmin1= Form(db.dfadmin1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fadmin1.vars is None:  
        fadmin1_f0 = fadmin1.vars.get('f0','')
        if len ( fadmin1_f0 ):
            db.dfadmin1.insert( **fadmin1.vars )
            dfadmin1_rows = db( db.dfadmin1 ).select()
            print (f'insert: \"{fadmin1.vars.f0}\" in db.dfadmin1; dfadmin1: {len(dfadmin1_rows)} rows' )

    return locals()


@action('inbox', method=["GET", "POST"] )
@action.uses(Template('inbox.html', delimiters='[%[ ]]',), db, session, T, )

def inbox(id=None):
    ctrl_info= "ctrl: inbox, view: inbox.html"

    return locals()


@action('forum', method=["GET", "POST"] )
@action.uses(Template('forum.html', delimiters='[%[ ]]',), db, session, T, )

def forum(id=None):
    ctrl_info= "ctrl: forum, view: forum.html"

    dfforum0_rows=''
    fforum0= Form(db.dfforum0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fforum0.vars is None:  
        fforum0_f0 = fforum0.vars.get('f0','')
        if len ( fforum0_f0 ):
            db.dfforum0.insert( **fforum0.vars )
            dfforum0_rows = db( db.dfforum0 ).select()
            print (f'insert: \"{fforum0.vars.f0}\" in db.dfforum0; dfforum0: {len(dfforum0_rows)} rows' )

    return locals()


@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T, )

def index(id=None):
    ctrl_info= "ctrl: index, view: index.html"

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


@action('cards', method=["GET", "POST"] )
@action.uses(Template('cards.html', delimiters='[%[ ]]',), db, session, T, )

def cards(id=None):
    ctrl_info= "ctrl: cards, view: cards.html"

    return locals()


@action('cover', method=["GET", "POST"] )
@action.uses(Template('cover.html', delimiters='[%[ ]]',), db, session, T, )

def cover(id=None):
    ctrl_info= "ctrl: cover, view: cover.html"

    return locals()


@action('kanban', method=["GET", "POST"] )
@action.uses(Template('kanban.html', delimiters='[%[ ]]',), db, session, T, )

def kanban(id=None):
    ctrl_info= "ctrl: kanban, view: kanban.html"

    dfkanban0_rows=''
    fkanban0= Form(db.dfkanban0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fkanban0.vars is None:  
        fkanban0_f0 = fkanban0.vars.get('f0','')
        if len ( fkanban0_f0 ):
            db.dfkanban0.insert( **fkanban0.vars )
            dfkanban0_rows = db( db.dfkanban0 ).select()
            print (f'insert: \"{fkanban0.vars.f0}\" in db.dfkanban0; dfkanban0: {len(dfkanban0_rows)} rows' )

    return locals()


@action('search', method=["GET", "POST"] )
@action.uses(Template('search.html', delimiters='[%[ ]]',), db, session, T, )

def search(id=None):
    ctrl_info= "ctrl: search, view: search.html"

    dfsearch0_rows=''
    fsearch0= Form(db.dfsearch0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fsearch0.vars is None:  
        fsearch0_f0 = fsearch0.vars.get('f0','')
        if len ( fsearch0_f0 ):
            db.dfsearch0.insert( **fsearch0.vars )
            dfsearch0_rows = db( db.dfsearch0 ).select()
            print (f'insert: \"{fsearch0.vars.f0}\" in db.dfsearch0; dfsearch0: {len(dfsearch0_rows)} rows' )

    return locals()


@action('landing', method=["GET", "POST"] )
@action.uses(Template('landing.html', delimiters='[%[ ]]',), db, session, T, )

def landing(id=None):
    ctrl_info= "ctrl: landing, view: landing.html"

    dflanding0_rows=''
    flanding0= Form(db.dflanding0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not flanding0.vars is None:  
        flanding0_f0 = flanding0.vars.get('f0','')
        if len ( flanding0_f0 ):
            db.dflanding0.insert( **flanding0.vars )
            dflanding0_rows = db( db.dflanding0 ).select()
            print (f'insert: \"{flanding0.vars.f0}\" in db.dflanding0; dflanding0: {len(dflanding0_rows)} rows' )

    return locals()


@action('contact', method=["GET", "POST"] )
@action.uses(Template('contact.html', delimiters='[%[ ]]',), db, session, T, )

def contact(id=None):
    ctrl_info= "ctrl: contact, view: contact.html"

    dfcontact0_rows=''
    fcontact0= Form(db.dfcontact0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcontact0.vars is None:  
        fcontact0_f0 = fcontact0.vars.get('f0','')
        if len ( fcontact0_f0 ):
            db.dfcontact0.insert( **fcontact0.vars )
            dfcontact0_rows = db( db.dfcontact0 ).select()
            print (f'insert: \"{fcontact0.vars.f0}\" in db.dfcontact0; dfcontact0: {len(dfcontact0_rows)} rows' )

    dfcontact1_rows=''
    fcontact1= Form(db.dfcontact1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcontact1.vars is None:  
        fcontact1_f0 = fcontact1.vars.get('f0','')
        if len ( fcontact1_f0 ):
            db.dfcontact1.insert( **fcontact1.vars )
            dfcontact1_rows = db( db.dfcontact1 ).select()
            print (f'insert: \"{fcontact1.vars.f0}\" in db.dfcontact1; dfcontact1: {len(dfcontact1_rows)} rows' )

    dfcontact2_rows=''
    fcontact2= Form(db.dfcontact2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fcontact2.vars is None:  
        fcontact2_f0 = fcontact2.vars.get('f0','')
        if len ( fcontact2_f0 ):
            db.dfcontact2.insert( **fcontact2.vars )
            dfcontact2_rows = db( db.dfcontact2 ).select()
            print (f'insert: \"{fcontact2.vars.f0}\" in db.dfcontact2; dfcontact2: {len(dfcontact2_rows)} rows' )

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


@action('personal', method=["GET", "POST"] )
@action.uses(Template('personal.html', delimiters='[%[ ]]',), db, session, T, )

def personal(id=None):
    ctrl_info= "ctrl: personal, view: personal.html"

    rows_tpersonal0= db(db.tpersonal0).select()
    dfpersonal0_rows=''
    fpersonal0= Form(db.dfpersonal0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fpersonal0.vars is None:  
        fpersonal0_f0 = fpersonal0.vars.get('f0','')
        if len ( fpersonal0_f0 ):
            db.dfpersonal0.insert( **fpersonal0.vars )
            dfpersonal0_rows = db( db.dfpersonal0 ).select()
            print (f'insert: \"{fpersonal0.vars.f0}\" in db.dfpersonal0; dfpersonal0: {len(dfpersonal0_rows)} rows' )

    dfpersonal1_rows=''
    fpersonal1= Form(db.dfpersonal1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fpersonal1.vars is None:  
        fpersonal1_f0 = fpersonal1.vars.get('f0','')
        if len ( fpersonal1_f0 ):
            db.dfpersonal1.insert( **fpersonal1.vars )
            dfpersonal1_rows = db( db.dfpersonal1 ).select()
            print (f'insert: \"{fpersonal1.vars.f0}\" in db.dfpersonal1; dfpersonal1: {len(dfpersonal1_rows)} rows' )

    dfpersonal2_rows=''
    fpersonal2= Form(db.dfpersonal2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fpersonal2.vars is None:  
        fpersonal2_f0 = fpersonal2.vars.get('f0','')
        if len ( fpersonal2_f0 ):
            db.dfpersonal2.insert( **fpersonal2.vars )
            dfpersonal2_rows = db( db.dfpersonal2 ).select()
            print (f'insert: \"{fpersonal2.vars.f0}\" in db.dfpersonal2; dfpersonal2: {len(dfpersonal2_rows)} rows' )

    return locals()


@action('showcase', method=["GET", "POST"] )
@action.uses(Template('showcase.html', delimiters='[%[ ]]',), db, session, T, )

def showcase(id=None):
    ctrl_info= "ctrl: showcase, view: showcase.html"

    dfshowcase0_rows=''
    fshowcase0= Form(db.dfshowcase0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fshowcase0.vars is None:  
        fshowcase0_f0 = fshowcase0.vars.get('f0','')
        if len ( fshowcase0_f0 ):
            db.dfshowcase0.insert( **fshowcase0.vars )
            dfshowcase0_rows = db( db.dfshowcase0 ).select()
            print (f'insert: \"{fshowcase0.vars.f0}\" in db.dfshowcase0; dfshowcase0: {len(dfshowcase0_rows)} rows' )

    dfshowcase1_rows=''
    fshowcase1= Form(db.dfshowcase1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fshowcase1.vars is None:  
        fshowcase1_f0 = fshowcase1.vars.get('f0','')
        if len ( fshowcase1_f0 ):
            db.dfshowcase1.insert( **fshowcase1.vars )
            dfshowcase1_rows = db( db.dfshowcase1 ).select()
            print (f'insert: \"{fshowcase1.vars.f0}\" in db.dfshowcase1; dfshowcase1: {len(dfshowcase1_rows)} rows' )

    dfshowcase2_rows=''
    fshowcase2= Form(db.dfshowcase2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fshowcase2.vars is None:  
        fshowcase2_f0 = fshowcase2.vars.get('f0','')
        if len ( fshowcase2_f0 ):
            db.dfshowcase2.insert( **fshowcase2.vars )
            dfshowcase2_rows = db( db.dfshowcase2 ).select()
            print (f'insert: \"{fshowcase2.vars.f0}\" in db.dfshowcase2; dfshowcase2: {len(dfshowcase2_rows)} rows' )

    return locals()


@action('cheatsheet', method=["GET", "POST"] )
@action.uses(Template('cheatsheet.html', delimiters='[%[ ]]',), db, session, T, )

def cheatsheet(id=None):
    ctrl_info= "ctrl: cheatsheet, view: cheatsheet.html"

    return locals()


@action('instaAlbum', method=["GET", "POST"] )
@action.uses(Template('instaAlbum.html', delimiters='[%[ ]]',), db, session, T, )

def instaAlbum(id=None):
    ctrl_info= "ctrl: instaAlbum, view: instaAlbum.html"

    dfinstaAlbum0_rows=''
    finstaAlbum0= Form(db.dfinstaAlbum0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not finstaAlbum0.vars is None:  
        finstaAlbum0_f0 = finstaAlbum0.vars.get('f0','')
        if len ( finstaAlbum0_f0 ):
            db.dfinstaAlbum0.insert( **finstaAlbum0.vars )
            dfinstaAlbum0_rows = db( db.dfinstaAlbum0 ).select()
            print (f'insert: \"{finstaAlbum0.vars.f0}\" in db.dfinstaAlbum0; dfinstaAlbum0: {len(dfinstaAlbum0_rows)} rows' )

    dfinstaAlbum1_rows=''
    finstaAlbum1= Form(db.dfinstaAlbum1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not finstaAlbum1.vars is None:  
        finstaAlbum1_f0 = finstaAlbum1.vars.get('f0','')
        if len ( finstaAlbum1_f0 ):
            db.dfinstaAlbum1.insert( **finstaAlbum1.vars )
            dfinstaAlbum1_rows = db( db.dfinstaAlbum1 ).select()
            print (f'insert: \"{finstaAlbum1.vars.f0}\" in db.dfinstaAlbum1; dfinstaAlbum1: {len(dfinstaAlbum1_rows)} rows' )

    dfinstaAlbum2_rows=''
    finstaAlbum2= Form(db.dfinstaAlbum2, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not finstaAlbum2.vars is None:  
        finstaAlbum2_f0 = finstaAlbum2.vars.get('f0','')
        if len ( finstaAlbum2_f0 ):
            db.dfinstaAlbum2.insert( **finstaAlbum2.vars )
            dfinstaAlbum2_rows = db( db.dfinstaAlbum2 ).select()
            print (f'insert: \"{finstaAlbum2.vars.f0}\" in db.dfinstaAlbum2; dfinstaAlbum2: {len(dfinstaAlbum2_rows)} rows' )

    dfinstaAlbum3_rows=''
    finstaAlbum3= Form(db.dfinstaAlbum3, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not finstaAlbum3.vars is None:  
        finstaAlbum3_f0 = finstaAlbum3.vars.get('f0','')
        if len ( finstaAlbum3_f0 ):
            db.dfinstaAlbum3.insert( **finstaAlbum3.vars )
            dfinstaAlbum3_rows = db( db.dfinstaAlbum3 ).select()
            print (f'insert: \"{finstaAlbum3.vars.f0}\" in db.dfinstaAlbum3; dfinstaAlbum3: {len(dfinstaAlbum3_rows)} rows' )

    return locals()


@action('ghostXblog', method=["GET", "POST"] )
@action.uses(Template('ghost-blog.html', delimiters='[%[ ]]',), db, session, T, )

def ghostXblog(id=None):
    ctrl_info= "ctrl: ghostXblog, view: ghost-blog.html"

    return locals()


@action('modalXcards', method=["GET", "POST"] )
@action.uses(Template('modal-cards.html', delimiters='[%[ ]]',), db, session, T, )

def modalXcards(id=None):
    ctrl_info= "ctrl: modalXcards, view: modal-cards.html"

    return locals()


@action('blogXtailsaw', method=["GET", "POST"] )
@action.uses(Template('blog-tailsaw.html', delimiters='[%[ ]]',), db, session, T, )

def blogXtailsaw(id=None):
    ctrl_info= "ctrl: blogXtailsaw, view: blog-tailsaw.html"

    dfblogXtailsaw0_rows=''
    fblogXtailsaw0= Form(db.dfblogXtailsaw0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fblogXtailsaw0.vars is None:  
        fblogXtailsaw0_f0 = fblogXtailsaw0.vars.get('f0','')
        if len ( fblogXtailsaw0_f0 ):
            db.dfblogXtailsaw0.insert( **fblogXtailsaw0.vars )
            dfblogXtailsaw0_rows = db( db.dfblogXtailsaw0 ).select()
            print (f'insert: \"{fblogXtailsaw0.vars.f0}\" in db.dfblogXtailsaw0; dfblogXtailsaw0: {len(dfblogXtailsaw0_rows)} rows' )

    dfblogXtailsaw1_rows=''
    fblogXtailsaw1= Form(db.dfblogXtailsaw1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fblogXtailsaw1.vars is None:  
        fblogXtailsaw1_f0 = fblogXtailsaw1.vars.get('f0','')
        if len ( fblogXtailsaw1_f0 ):
            db.dfblogXtailsaw1.insert( **fblogXtailsaw1.vars )
            dfblogXtailsaw1_rows = db( db.dfblogXtailsaw1 ).select()
            print (f'insert: \"{fblogXtailsaw1.vars.f0}\" in db.dfblogXtailsaw1; dfblogXtailsaw1: {len(dfblogXtailsaw1_rows)} rows' )

    return locals()


@action('kanbanXsearchX', method=["GET", "POST"] )
@action.uses(Template('kanban[search].html', delimiters='[%[ ]]',), db, session, T, )

def kanbanXsearchX(id=None):
    ctrl_info= "ctrl: kanbanXsearchX, view: kanban[search].html"

    dfkanbanXsearchX0_rows=''
    fkanbanXsearchX0= Form(db.dfkanbanXsearchX0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fkanbanXsearchX0.vars is None:  
        fkanbanXsearchX0_f0 = fkanbanXsearchX0.vars.get('f0','')
        if len ( fkanbanXsearchX0_f0 ):
            db.dfkanbanXsearchX0.insert( **fkanbanXsearchX0.vars )
            dfkanbanXsearchX0_rows = db( db.dfkanbanXsearchX0 ).select()
            print (f'insert: \"{fkanbanXsearchX0.vars.f0}\" in db.dfkanbanXsearchX0; dfkanbanXsearchX0: {len(dfkanbanXsearchX0_rows)} rows' )

    return locals()


@action('helloXparallax', method=["GET", "POST"] )
@action.uses(Template('hello-parallax.html', delimiters='[%[ ]]',), db, session, T, )

def helloXparallax(id=None):
    ctrl_info= "ctrl: helloXparallax, view: hello-parallax.html"

    dfhelloXparallax0_rows=''
    fhelloXparallax0= Form(db.dfhelloXparallax0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fhelloXparallax0.vars is None:  
        fhelloXparallax0_f0 = fhelloXparallax0.vars.get('f0','')
        if len ( fhelloXparallax0_f0 ):
            db.dfhelloXparallax0.insert( **fhelloXparallax0.vars )
            dfhelloXparallax0_rows = db( db.dfhelloXparallax0 ).select()
            print (f'insert: \"{fhelloXparallax0.vars.f0}\" in db.dfhelloXparallax0; dfhelloXparallax0: {len(dfhelloXparallax0_rows)} rows' )

    dfhelloXparallax1_rows=''
    fhelloXparallax1= Form(db.dfhelloXparallax1, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fhelloXparallax1.vars is None:  
        fhelloXparallax1_f0 = fhelloXparallax1.vars.get('f0','')
        if len ( fhelloXparallax1_f0 ):
            db.dfhelloXparallax1.insert( **fhelloXparallax1.vars )
            dfhelloXparallax1_rows = db( db.dfhelloXparallax1 ).select()
            print (f'insert: \"{fhelloXparallax1.vars.f0}\" in db.dfhelloXparallax1; dfhelloXparallax1: {len(dfhelloXparallax1_rows)} rows' )

    return locals()


@action('neumorphicXlogin', method=["GET", "POST"] )
@action.uses(Template('neumorphic-login.html', delimiters='[%[ ]]',), db, session, T, )

def neumorphicXlogin(id=None):
    ctrl_info= "ctrl: neumorphicXlogin, view: neumorphic-login.html"

    dfneumorphicXlogin0_rows=''
    fneumorphicXlogin0= Form(db.dfneumorphicXlogin0, id, deletable=False, dbio = False, formstyle=FormStyleBulma )
    if not fneumorphicXlogin0.vars is None:  
        fneumorphicXlogin0_f0 = fneumorphicXlogin0.vars.get('f0','')
        if len ( fneumorphicXlogin0_f0 ):
            db.dfneumorphicXlogin0.insert( **fneumorphicXlogin0.vars )
            dfneumorphicXlogin0_rows = db( db.dfneumorphicXlogin0 ).select()
            print (f'insert: \"{fneumorphicXlogin0.vars.f0}\" in db.dfneumorphicXlogin0; dfneumorphicXlogin0: {len(dfneumorphicXlogin0_rows)} rows' )

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
