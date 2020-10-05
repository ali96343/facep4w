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



@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',),  db, session, T,  )
def index():
    message= "ctrl: index, view: index.html"


    findex0= Form(db.dfindex0, formstyle=FormStyleBulma )

    findex1= Form(db.dfindex1, formstyle=FormStyleBulma )

    return locals()


@action('widgets', method=["GET", "POST"] )
@action.uses(Template('widgets.html', delimiters='[%[ ]]',),  db, session, T,  )
def widgets():
    message= "ctrl: widgets, view: widgets.html"


    fwidgets0= Form(db.dfwidgets0, formstyle=FormStyleBulma )

    return locals()


@action('morris', method=["GET", "POST"] )
@action.uses(Template('morris.html', delimiters='[%[ ]]',),  db, session, T,  )
def morris():
    message= "ctrl: morris, view: morris.html"


    fmorris0= Form(db.dfmorris0, formstyle=FormStyleBulma )

    return locals()


@action('flot', method=["GET", "POST"] )
@action.uses(Template('flot.html', delimiters='[%[ ]]',),  db, session, T,  )
def flot():
    message= "ctrl: flot, view: flot.html"


    fflot0= Form(db.dfflot0, formstyle=FormStyleBulma )

    return locals()


@action('inline', method=["GET", "POST"] )
@action.uses(Template('inline.html', delimiters='[%[ ]]',),  db, session, T,  )
def inline():
    message= "ctrl: inline, view: inline.html"


    finline0= Form(db.dfinline0, formstyle=FormStyleBulma )

    return locals()


@action('general', method=["GET", "POST"] )
@action.uses(Template('general.html', delimiters='[%[ ]]',),  db, session, T,  )
def general():
    message= "ctrl: general, view: general.html"


    fgeneral0= Form(db.dfgeneral0, formstyle=FormStyleBulma )

    return locals()


@action('icons', method=["GET", "POST"] )
@action.uses(Template('icons.html', delimiters='[%[ ]]',),  db, session, T,  )
def icons():
    message= "ctrl: icons, view: icons.html"


    ficons0= Form(db.dficons0, formstyle=FormStyleBulma )

    return locals()


@action('buttons', method=["GET", "POST"] )
@action.uses(Template('buttons.html', delimiters='[%[ ]]',),  db, session, T,  )
def buttons():
    message= "ctrl: buttons, view: buttons.html"


    rows_tbuttons0= db(db.tbuttons0).select()

    rows_tbuttons1= db(db.tbuttons1).select()

    rows_tbuttons2= db(db.tbuttons2).select()

    fbuttons0= Form(db.dfbuttons0, formstyle=FormStyleBulma )

    return locals()


@action('sliders', method=["GET", "POST"] )
@action.uses(Template('sliders.html', delimiters='[%[ ]]',),  db, session, T,  )
def sliders():
    message= "ctrl: sliders, view: sliders.html"


    fsliders0= Form(db.dfsliders0, formstyle=FormStyleBulma )

    return locals()


@action('timeline', method=["GET", "POST"] )
@action.uses(Template('timeline.html', delimiters='[%[ ]]',),  db, session, T,  )
def timeline():
    message= "ctrl: timeline, view: timeline.html"


    ftimeline0= Form(db.dftimeline0, formstyle=FormStyleBulma )

    return locals()


@action('advanced', method=["GET", "POST"] )
@action.uses(Template('advanced.html', delimiters='[%[ ]]',),  db, session, T,  )
def advanced():
    message= "ctrl: advanced, view: advanced.html"


    fadvanced0= Form(db.dfadvanced0, formstyle=FormStyleBulma )

    return locals()


@action('editors', method=["GET", "POST"] )
@action.uses(Template('editors.html', delimiters='[%[ ]]',),  db, session, T,  )
def editors():
    message= "ctrl: editors, view: editors.html"


    feditors0= Form(db.dfeditors0, formstyle=FormStyleBulma )

    feditors1= Form(db.dfeditors1, formstyle=FormStyleBulma )

    feditors2= Form(db.dfeditors2, formstyle=FormStyleBulma )

    return locals()


@action('simple', method=["GET", "POST"] )
@action.uses(Template('simple.html', delimiters='[%[ ]]',),  db, session, T,  )
def simple():
    message= "ctrl: simple, view: simple.html"


    rows_tsimple0= db(db.tsimple0).select()

    rows_tsimple1= db(db.tsimple1).select()

    rows_tsimple2= db(db.tsimple2).select()

    rows_tsimple3= db(db.tsimple3).select()

    rows_tsimple4= db(db.tsimple4).select()

    fsimple0= Form(db.dfsimple0, formstyle=FormStyleBulma )

    return locals()


@action('data', method=["GET", "POST"] )
@action.uses(Template('data.html', delimiters='[%[ ]]',),  db, session, T,  )
def data():
    message= "ctrl: data, view: data.html"


    rows_tdata0= db(db.tdata0).select()

    rows_tdata1= db(db.tdata1).select()

    fdata0= Form(db.dfdata0, formstyle=FormStyleBulma )

    return locals()


@action('calendar', method=["GET", "POST"] )
@action.uses(Template('calendar.html', delimiters='[%[ ]]',),  db, session, T,  )
def calendar():
    message= "ctrl: calendar, view: calendar.html"


    fcalendar0= Form(db.dfcalendar0, formstyle=FormStyleBulma )

    return locals()


@action('mailbox', method=["GET", "POST"] )
@action.uses(Template('mailbox.html', delimiters='[%[ ]]',),  db, session, T,  )
def mailbox():
    message= "ctrl: mailbox, view: mailbox.html"


    rows_tmailbox0= db(db.tmailbox0).select()

    fmailbox0= Form(db.dfmailbox0, formstyle=FormStyleBulma )

    fmailbox1= Form(db.dfmailbox1, formstyle=FormStyleBulma )

    fmailbox2= Form(db.dfmailbox2, formstyle=FormStyleBulma )

    return locals()


@action('invoice', method=["GET", "POST"] )
@action.uses(Template('invoice.html', delimiters='[%[ ]]',),  db, session, T,  )
def invoice():
    message= "ctrl: invoice, view: invoice.html"


    rows_tinvoice0= db(db.tinvoice0).select()

    rows_tinvoice1= db(db.tinvoice1).select()

    finvoice0= Form(db.dfinvoice0, formstyle=FormStyleBulma )

    return locals()


@action('login', method=["GET", "POST"] )
@action.uses(Template('login.html', delimiters='[%[ ]]',),  db, session, T,  )
def login():
    message= "ctrl: login, view: login.html"


    flogin0= Form(db.dflogin0, formstyle=FormStyleBulma )

    return locals()


@action('register', method=["GET", "POST"] )
@action.uses(Template('register.html', delimiters='[%[ ]]',),  db, session, T,  )
def register():
    message= "ctrl: register, view: register.html"


    fregister0= Form(db.dfregister0, formstyle=FormStyleBulma )

    return locals()


@action('lockscreen', method=["GET", "POST"] )
@action.uses(Template('lockscreen.html', delimiters='[%[ ]]',),  db, session, T,  )
def lockscreen():
    message= "ctrl: lockscreen, view: lockscreen.html"


    return locals()


@action('X404', method=["GET", "POST"] )
@action.uses(Template('404.html', delimiters='[%[ ]]',),  db, session, T,  )
def X404():
    message= "ctrl: X404, view: 404.html"


    fX4040= Form(db.dfX4040, formstyle=FormStyleBulma )

    fX4041= Form(db.dfX4041, formstyle=FormStyleBulma )

    return locals()


@action('X500', method=["GET", "POST"] )
@action.uses(Template('500.html', delimiters='[%[ ]]',),  db, session, T,  )
def X500():
    message= "ctrl: X500, view: 500.html"


    fX5000= Form(db.dfX5000, formstyle=FormStyleBulma )

    fX5001= Form(db.dfX5001, formstyle=FormStyleBulma )

    return locals()


@action('blank', method=["GET", "POST"] )
@action.uses(Template('blank.html', delimiters='[%[ ]]',),  db, session, T,  )
def blank():
    message= "ctrl: blank, view: blank.html"


    fblank0= Form(db.dfblank0, formstyle=FormStyleBulma )

    return locals()
