#!/usr/bin/env python3

#
# py4web app, AI-biorex ported 27.10.2020 14:00:18
#

import os
from py4web import action, request, abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A
from py4web.core import Template, Reloader
from py4web.utils.dbstore import DBStore

from .common import db, session, T, cache, authenticated, unauthenticated, auth
import bottle

# exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)

#db_sess = DAL('sqlite:memory')
#session =  Session(storage=DBStore(db_sess))


Glb= {'debug': True , 'my_app_name': "octopus", 'tte_path': '/static/tte' }



@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session,  T, )

def index(id=None):
    ctrl_info= "ctrl: index, view: index.html"
    messages = []

    rows_tindex0= db(db.tindex0).select()
    dfindex0_row= None
    id_dfindex0 = None
    findex0= Form(db.dfindex0, id, deletable=False, dbio = False, keep_values = False, form_name = "findex0",  formstyle=FormStyleBulma )
   
    if findex0.accepted:

        Glb['debug'] and print("     findex0 accepted with: %s " % (findex0.vars))
        findex0_f0 = findex0.vars.get('f0','')
        if len ( findex0_f0 ):
            id_dfindex0 = db.dfindex0.insert( **findex0.vars )
            db.commit()

            if not id_dfindex0 is None:
                dfindex0_row = db.dfindex0(id_dfindex0 )

                if not dfindex0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex0.vars.f0}\" into db.dfindex0.f0, id = {id_dfindex0}' )
                         print(f"     found db.dfindex0.f0: \"{dfindex0_row.f0}\", id = {id_dfindex0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findex0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findex0.vars.items() ]
                print()
   
    elif findex0.errors:
        print("findex0 has errors: %s " % (findex0.errors))
 

    dfindex1_row= None
    id_dfindex1 = None
    findex1= Form(db.dfindex1, id, deletable=False, dbio = False, keep_values = False, form_name = "findex1",  formstyle=FormStyleBulma )
   
    if findex1.accepted:

        Glb['debug'] and print("     findex1 accepted with: %s " % (findex1.vars))
        findex1_f0 = findex1.vars.get('f0','')
        if len ( findex1_f0 ):
            id_dfindex1 = db.dfindex1.insert( **findex1.vars )
            db.commit()

            if not id_dfindex1 is None:
                dfindex1_row = db.dfindex1(id_dfindex1 )

                if not dfindex1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex1.vars.f0}\" into db.dfindex1.f0, id = {id_dfindex1}' )
                         print(f"     found db.dfindex1.f0: \"{dfindex1_row.f0}\", id = {id_dfindex1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findex1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findex1.vars.items() ]
                print()
   
    elif findex1.errors:
        print("findex1 has errors: %s " % (findex1.errors))
 

    return locals()


@action('pagesX500', method=["GET", "POST"] )
@action.uses(Template('pages-500.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesX500(id=None):
    ctrl_info= "ctrl: pagesX500, view: pages-500.html"
    messages = []

    return locals()


@action('pagesX404', method=["GET", "POST"] )
@action.uses(Template('pages-404.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesX404(id=None):
    ctrl_info= "ctrl: pagesX404, view: pages-404.html"
    messages = []

    dfpagesX4040_row= None
    id_dfpagesX4040 = None
    fpagesX4040= Form(db.dfpagesX4040, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesX4040",  formstyle=FormStyleBulma )
   
    if fpagesX4040.accepted:

        Glb['debug'] and print("     fpagesX4040 accepted with: %s " % (fpagesX4040.vars))
        fpagesX4040_f0 = fpagesX4040.vars.get('f0','')
        if len ( fpagesX4040_f0 ):
            id_dfpagesX4040 = db.dfpagesX4040.insert( **fpagesX4040.vars )
            db.commit()

            if not id_dfpagesX4040 is None:
                dfpagesX4040_row = db.dfpagesX4040(id_dfpagesX4040 )

                if not dfpagesX4040_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesX4040.vars.f0}\" into db.dfpagesX4040.f0, id = {id_dfpagesX4040}' )
                         print(f"     found db.dfpagesX4040.f0: \"{dfpagesX4040_row.f0}\", id = {id_dfpagesX4040}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesX4040_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesX4040.vars.items() ]
                print()
   
    elif fpagesX4040.errors:
        print("fpagesX4040 has errors: %s " % (fpagesX4040.errors))
 

    return locals()


@action('tablesXajax', method=["GET", "POST"] )
@action.uses(Template('tables-ajax.html', delimiters='[%[ ]]',), db, session,  T, )

def tablesXajax(id=None):
    ctrl_info= "ctrl: tablesXajax, view: tables-ajax.html"
    messages = []

    rows_ttablesXajax0= db(db.ttablesXajax0).select()
    dftablesXajax0_row= None
    id_dftablesXajax0 = None
    ftablesXajax0= Form(db.dftablesXajax0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftablesXajax0",  formstyle=FormStyleBulma )
   
    if ftablesXajax0.accepted:

        Glb['debug'] and print("     ftablesXajax0 accepted with: %s " % (ftablesXajax0.vars))
        ftablesXajax0_f0 = ftablesXajax0.vars.get('f0','')
        if len ( ftablesXajax0_f0 ):
            id_dftablesXajax0 = db.dftablesXajax0.insert( **ftablesXajax0.vars )
            db.commit()

            if not id_dftablesXajax0 is None:
                dftablesXajax0_row = db.dftablesXajax0(id_dftablesXajax0 )

                if not dftablesXajax0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftablesXajax0.vars.f0}\" into db.dftablesXajax0.f0, id = {id_dftablesXajax0}' )
                         print(f"     found db.dftablesXajax0.f0: \"{dftablesXajax0_row.f0}\", id = {id_dftablesXajax0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftablesXajax0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftablesXajax0.vars.items() ]
                print()
   
    elif ftablesXajax0.errors:
        print("ftablesXajax0 has errors: %s " % (ftablesXajax0.errors))
 

    return locals()


@action('mapsXvector', method=["GET", "POST"] )
@action.uses(Template('maps-vector.html', delimiters='[%[ ]]',), db, session,  T, )

def mapsXvector(id=None):
    ctrl_info= "ctrl: mapsXvector, view: maps-vector.html"
    messages = []

    dfmapsXvector0_row= None
    id_dfmapsXvector0 = None
    fmapsXvector0= Form(db.dfmapsXvector0, id, deletable=False, dbio = False, keep_values = False, form_name = "fmapsXvector0",  formstyle=FormStyleBulma )
   
    if fmapsXvector0.accepted:

        Glb['debug'] and print("     fmapsXvector0 accepted with: %s " % (fmapsXvector0.vars))
        fmapsXvector0_f0 = fmapsXvector0.vars.get('f0','')
        if len ( fmapsXvector0_f0 ):
            id_dfmapsXvector0 = db.dfmapsXvector0.insert( **fmapsXvector0.vars )
            db.commit()

            if not id_dfmapsXvector0 is None:
                dfmapsXvector0_row = db.dfmapsXvector0(id_dfmapsXvector0 )

                if not dfmapsXvector0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmapsXvector0.vars.f0}\" into db.dfmapsXvector0.f0, id = {id_dfmapsXvector0}' )
                         print(f"     found db.dfmapsXvector0.f0: \"{dfmapsXvector0_row.f0}\", id = {id_dfmapsXvector0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmapsXvector0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmapsXvector0.vars.items() ]
                print()
   
    elif fmapsXvector0.errors:
        print("fmapsXvector0 has errors: %s " % (fmapsXvector0.errors))
 

    return locals()


@action('pagesXblank', method=["GET", "POST"] )
@action.uses(Template('pages-blank.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXblank(id=None):
    ctrl_info= "ctrl: pagesXblank, view: pages-blank.html"
    messages = []

    dfpagesXblank0_row= None
    id_dfpagesXblank0 = None
    fpagesXblank0= Form(db.dfpagesXblank0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXblank0",  formstyle=FormStyleBulma )
   
    if fpagesXblank0.accepted:

        Glb['debug'] and print("     fpagesXblank0 accepted with: %s " % (fpagesXblank0.vars))
        fpagesXblank0_f0 = fpagesXblank0.vars.get('f0','')
        if len ( fpagesXblank0_f0 ):
            id_dfpagesXblank0 = db.dfpagesXblank0.insert( **fpagesXblank0.vars )
            db.commit()

            if not id_dfpagesXblank0 is None:
                dfpagesXblank0_row = db.dfpagesXblank0(id_dfpagesXblank0 )

                if not dfpagesXblank0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXblank0.vars.f0}\" into db.dfpagesXblank0.f0, id = {id_dfpagesXblank0}' )
                         print(f"     found db.dfpagesXblank0.f0: \"{dfpagesXblank0_row.f0}\", id = {id_dfpagesXblank0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXblank0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXblank0.vars.items() ]
                print()
   
    elif fpagesXblank0.errors:
        print("fpagesXblank0 has errors: %s " % (fpagesXblank0.errors))
 

    return locals()


@action('formsXbasic', method=["GET", "POST"] )
@action.uses(Template('forms-basic.html', delimiters='[%[ ]]',), db, session,  T, )

def formsXbasic(id=None):
    ctrl_info= "ctrl: formsXbasic, view: forms-basic.html"
    messages = []

    dfformsXbasic0_row= None
    id_dfformsXbasic0 = None
    fformsXbasic0= Form(db.dfformsXbasic0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXbasic0",  formstyle=FormStyleBulma )
   
    if fformsXbasic0.accepted:

        Glb['debug'] and print("     fformsXbasic0 accepted with: %s " % (fformsXbasic0.vars))
        fformsXbasic0_f0 = fformsXbasic0.vars.get('f0','')
        if len ( fformsXbasic0_f0 ):
            id_dfformsXbasic0 = db.dfformsXbasic0.insert( **fformsXbasic0.vars )
            db.commit()

            if not id_dfformsXbasic0 is None:
                dfformsXbasic0_row = db.dfformsXbasic0(id_dfformsXbasic0 )

                if not dfformsXbasic0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXbasic0.vars.f0}\" into db.dfformsXbasic0.f0, id = {id_dfformsXbasic0}' )
                         print(f"     found db.dfformsXbasic0.f0: \"{dfformsXbasic0_row.f0}\", id = {id_dfformsXbasic0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXbasic0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXbasic0.vars.items() ]
                print()
   
    elif fformsXbasic0.errors:
        print("fformsXbasic0 has errors: %s " % (fformsXbasic0.errors))
 

    dfformsXbasic1_row= None
    id_dfformsXbasic1 = None
    fformsXbasic1= Form(db.dfformsXbasic1, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXbasic1",  formstyle=FormStyleBulma )
   
    if fformsXbasic1.accepted:

        Glb['debug'] and print("     fformsXbasic1 accepted with: %s " % (fformsXbasic1.vars))
        fformsXbasic1_f0 = fformsXbasic1.vars.get('f0','')
        if len ( fformsXbasic1_f0 ):
            id_dfformsXbasic1 = db.dfformsXbasic1.insert( **fformsXbasic1.vars )
            db.commit()

            if not id_dfformsXbasic1 is None:
                dfformsXbasic1_row = db.dfformsXbasic1(id_dfformsXbasic1 )

                if not dfformsXbasic1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXbasic1.vars.f0}\" into db.dfformsXbasic1.f0, id = {id_dfformsXbasic1}' )
                         print(f"     found db.dfformsXbasic1.f0: \"{dfformsXbasic1_row.f0}\", id = {id_dfformsXbasic1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXbasic1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXbasic1.vars.items() ]
                print()
   
    elif fformsXbasic1.errors:
        print("fformsXbasic1 has errors: %s " % (fformsXbasic1.errors))
 

    dfformsXbasic2_row= None
    id_dfformsXbasic2 = None
    fformsXbasic2= Form(db.dfformsXbasic2, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXbasic2",  formstyle=FormStyleBulma )
   
    if fformsXbasic2.accepted:

        Glb['debug'] and print("     fformsXbasic2 accepted with: %s " % (fformsXbasic2.vars))
        fformsXbasic2_f0 = fformsXbasic2.vars.get('f0','')
        if len ( fformsXbasic2_f0 ):
            id_dfformsXbasic2 = db.dfformsXbasic2.insert( **fformsXbasic2.vars )
            db.commit()

            if not id_dfformsXbasic2 is None:
                dfformsXbasic2_row = db.dfformsXbasic2(id_dfformsXbasic2 )

                if not dfformsXbasic2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXbasic2.vars.f0}\" into db.dfformsXbasic2.f0, id = {id_dfformsXbasic2}' )
                         print(f"     found db.dfformsXbasic2.f0: \"{dfformsXbasic2_row.f0}\", id = {id_dfformsXbasic2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXbasic2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXbasic2.vars.items() ]
                print()
   
    elif fformsXbasic2.errors:
        print("fformsXbasic2 has errors: %s " % (fformsXbasic2.errors))
 

    dfformsXbasic3_row= None
    id_dfformsXbasic3 = None
    fformsXbasic3= Form(db.dfformsXbasic3, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXbasic3",  formstyle=FormStyleBulma )
   
    if fformsXbasic3.accepted:

        Glb['debug'] and print("     fformsXbasic3 accepted with: %s " % (fformsXbasic3.vars))
        fformsXbasic3_f0 = fformsXbasic3.vars.get('f0','')
        if len ( fformsXbasic3_f0 ):
            id_dfformsXbasic3 = db.dfformsXbasic3.insert( **fformsXbasic3.vars )
            db.commit()

            if not id_dfformsXbasic3 is None:
                dfformsXbasic3_row = db.dfformsXbasic3(id_dfformsXbasic3 )

                if not dfformsXbasic3_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXbasic3.vars.f0}\" into db.dfformsXbasic3.f0, id = {id_dfformsXbasic3}' )
                         print(f"     found db.dfformsXbasic3.f0: \"{dfformsXbasic3_row.f0}\", id = {id_dfformsXbasic3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXbasic3_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXbasic3.vars.items() ]
                print()
   
    elif fformsXbasic3.errors:
        print("fformsXbasic3 has errors: %s " % (fformsXbasic3.errors))
 

    dfformsXbasic4_row= None
    id_dfformsXbasic4 = None
    fformsXbasic4= Form(db.dfformsXbasic4, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXbasic4",  formstyle=FormStyleBulma )
   
    if fformsXbasic4.accepted:

        Glb['debug'] and print("     fformsXbasic4 accepted with: %s " % (fformsXbasic4.vars))
        fformsXbasic4_f0 = fformsXbasic4.vars.get('f0','')
        if len ( fformsXbasic4_f0 ):
            id_dfformsXbasic4 = db.dfformsXbasic4.insert( **fformsXbasic4.vars )
            db.commit()

            if not id_dfformsXbasic4 is None:
                dfformsXbasic4_row = db.dfformsXbasic4(id_dfformsXbasic4 )

                if not dfformsXbasic4_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXbasic4.vars.f0}\" into db.dfformsXbasic4.f0, id = {id_dfformsXbasic4}' )
                         print(f"     found db.dfformsXbasic4.f0: \"{dfformsXbasic4_row.f0}\", id = {id_dfformsXbasic4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXbasic4_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXbasic4.vars.items() ]
                print()
   
    elif fformsXbasic4.errors:
        print("fformsXbasic4 has errors: %s " % (fformsXbasic4.errors))
 

    dfformsXbasic5_row= None
    id_dfformsXbasic5 = None
    fformsXbasic5= Form(db.dfformsXbasic5, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXbasic5",  formstyle=FormStyleBulma )
   
    if fformsXbasic5.accepted:

        Glb['debug'] and print("     fformsXbasic5 accepted with: %s " % (fformsXbasic5.vars))
        fformsXbasic5_f0 = fformsXbasic5.vars.get('f0','')
        if len ( fformsXbasic5_f0 ):
            id_dfformsXbasic5 = db.dfformsXbasic5.insert( **fformsXbasic5.vars )
            db.commit()

            if not id_dfformsXbasic5 is None:
                dfformsXbasic5_row = db.dfformsXbasic5(id_dfformsXbasic5 )

                if not dfformsXbasic5_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXbasic5.vars.f0}\" into db.dfformsXbasic5.f0, id = {id_dfformsXbasic5}' )
                         print(f"     found db.dfformsXbasic5.f0: \"{dfformsXbasic5_row.f0}\", id = {id_dfformsXbasic5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXbasic5_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXbasic5.vars.items() ]
                print()
   
    elif fformsXbasic5.errors:
        print("fformsXbasic5 has errors: %s " % (fformsXbasic5.errors))
 

    dfformsXbasic6_row= None
    id_dfformsXbasic6 = None
    fformsXbasic6= Form(db.dfformsXbasic6, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXbasic6",  formstyle=FormStyleBulma )
   
    if fformsXbasic6.accepted:

        Glb['debug'] and print("     fformsXbasic6 accepted with: %s " % (fformsXbasic6.vars))
        fformsXbasic6_f0 = fformsXbasic6.vars.get('f0','')
        if len ( fformsXbasic6_f0 ):
            id_dfformsXbasic6 = db.dfformsXbasic6.insert( **fformsXbasic6.vars )
            db.commit()

            if not id_dfformsXbasic6 is None:
                dfformsXbasic6_row = db.dfformsXbasic6(id_dfformsXbasic6 )

                if not dfformsXbasic6_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXbasic6.vars.f0}\" into db.dfformsXbasic6.f0, id = {id_dfformsXbasic6}' )
                         print(f"     found db.dfformsXbasic6.f0: \"{dfformsXbasic6_row.f0}\", id = {id_dfformsXbasic6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXbasic6_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXbasic6.vars.items() ]
                print()
   
    elif fformsXbasic6.errors:
        print("fformsXbasic6 has errors: %s " % (fformsXbasic6.errors))
 

    dfformsXbasic7_row= None
    id_dfformsXbasic7 = None
    fformsXbasic7= Form(db.dfformsXbasic7, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXbasic7",  formstyle=FormStyleBulma )
   
    if fformsXbasic7.accepted:

        Glb['debug'] and print("     fformsXbasic7 accepted with: %s " % (fformsXbasic7.vars))
        fformsXbasic7_f0 = fformsXbasic7.vars.get('f0','')
        if len ( fformsXbasic7_f0 ):
            id_dfformsXbasic7 = db.dfformsXbasic7.insert( **fformsXbasic7.vars )
            db.commit()

            if not id_dfformsXbasic7 is None:
                dfformsXbasic7_row = db.dfformsXbasic7(id_dfformsXbasic7 )

                if not dfformsXbasic7_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXbasic7.vars.f0}\" into db.dfformsXbasic7.f0, id = {id_dfformsXbasic7}' )
                         print(f"     found db.dfformsXbasic7.f0: \"{dfformsXbasic7_row.f0}\", id = {id_dfformsXbasic7}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXbasic7_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXbasic7.vars.items() ]
                print()
   
    elif fformsXbasic7.errors:
        print("fformsXbasic7 has errors: %s " % (fformsXbasic7.errors))
 

    return locals()


@action('tablesXbasic', method=["GET", "POST"] )
@action.uses(Template('tables-basic.html', delimiters='[%[ ]]',), db, session,  T, )

def tablesXbasic(id=None):
    ctrl_info= "ctrl: tablesXbasic, view: tables-basic.html"
    messages = []

    rows_ttablesXbasic0= db(db.ttablesXbasic0).select()
    rows_ttablesXbasic1= db(db.ttablesXbasic1).select()
    rows_ttablesXbasic2= db(db.ttablesXbasic2).select()
    rows_ttablesXbasic3= db(db.ttablesXbasic3).select()
    rows_ttablesXbasic4= db(db.ttablesXbasic4).select()
    rows_ttablesXbasic5= db(db.ttablesXbasic5).select()
    rows_ttablesXbasic6= db(db.ttablesXbasic6).select()
    rows_ttablesXbasic7= db(db.ttablesXbasic7).select()
    rows_ttablesXbasic8= db(db.ttablesXbasic8).select()
    rows_ttablesXbasic9= db(db.ttablesXbasic9).select()
    dftablesXbasic0_row= None
    id_dftablesXbasic0 = None
    ftablesXbasic0= Form(db.dftablesXbasic0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftablesXbasic0",  formstyle=FormStyleBulma )
   
    if ftablesXbasic0.accepted:

        Glb['debug'] and print("     ftablesXbasic0 accepted with: %s " % (ftablesXbasic0.vars))
        ftablesXbasic0_f0 = ftablesXbasic0.vars.get('f0','')
        if len ( ftablesXbasic0_f0 ):
            id_dftablesXbasic0 = db.dftablesXbasic0.insert( **ftablesXbasic0.vars )
            db.commit()

            if not id_dftablesXbasic0 is None:
                dftablesXbasic0_row = db.dftablesXbasic0(id_dftablesXbasic0 )

                if not dftablesXbasic0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftablesXbasic0.vars.f0}\" into db.dftablesXbasic0.f0, id = {id_dftablesXbasic0}' )
                         print(f"     found db.dftablesXbasic0.f0: \"{dftablesXbasic0_row.f0}\", id = {id_dftablesXbasic0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftablesXbasic0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftablesXbasic0.vars.items() ]
                print()
   
    elif ftablesXbasic0.errors:
        print("ftablesXbasic0 has errors: %s " % (ftablesXbasic0.errors))
 

    return locals()


@action('pagesXsignin', method=["GET", "POST"] )
@action.uses(Template('pages-signin.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXsignin(id=None):
    ctrl_info= "ctrl: pagesXsignin, view: pages-signin.html"
    messages = []

    dfpagesXsignin0_row= None
    id_dfpagesXsignin0 = None
    fpagesXsignin0= Form(db.dfpagesXsignin0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXsignin0",  formstyle=FormStyleBulma )
   
    if fpagesXsignin0.accepted:

        Glb['debug'] and print("     fpagesXsignin0 accepted with: %s " % (fpagesXsignin0.vars))
        fpagesXsignin0_f0 = fpagesXsignin0.vars.get('f0','')
        if len ( fpagesXsignin0_f0 ):
            id_dfpagesXsignin0 = db.dfpagesXsignin0.insert( **fpagesXsignin0.vars )
            db.commit()

            if not id_dfpagesXsignin0 is None:
                dfpagesXsignin0_row = db.dfpagesXsignin0(id_dfpagesXsignin0 )

                if not dfpagesXsignin0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXsignin0.vars.f0}\" into db.dfpagesXsignin0.f0, id = {id_dfpagesXsignin0}' )
                         print(f"     found db.dfpagesXsignin0.f0: \"{dfpagesXsignin0_row.f0}\", id = {id_dfpagesXsignin0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXsignin0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXsignin0.vars.items() ]
                print()
   
    elif fpagesXsignin0.errors:
        print("fpagesXsignin0 has errors: %s " % (fpagesXsignin0.errors))
 

    return locals()


@action('pagesXsignup', method=["GET", "POST"] )
@action.uses(Template('pages-signup.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXsignup(id=None):
    ctrl_info= "ctrl: pagesXsignup, view: pages-signup.html"
    messages = []

    dfpagesXsignup0_row= None
    id_dfpagesXsignup0 = None
    fpagesXsignup0= Form(db.dfpagesXsignup0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXsignup0",  formstyle=FormStyleBulma )
   
    if fpagesXsignup0.accepted:

        Glb['debug'] and print("     fpagesXsignup0 accepted with: %s " % (fpagesXsignup0.vars))
        fpagesXsignup0_f0 = fpagesXsignup0.vars.get('f0','')
        if len ( fpagesXsignup0_f0 ):
            id_dfpagesXsignup0 = db.dfpagesXsignup0.insert( **fpagesXsignup0.vars )
            db.commit()

            if not id_dfpagesXsignup0 is None:
                dfpagesXsignup0_row = db.dfpagesXsignup0(id_dfpagesXsignup0 )

                if not dfpagesXsignup0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXsignup0.vars.f0}\" into db.dfpagesXsignup0.f0, id = {id_dfpagesXsignup0}' )
                         print(f"     found db.dfpagesXsignup0.f0: \"{dfpagesXsignup0_row.f0}\", id = {id_dfpagesXsignup0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXsignup0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXsignup0.vars.items() ]
                print()
   
    elif fpagesXsignup0.errors:
        print("fpagesXsignup0 has errors: %s " % (fpagesXsignup0.errors))
 

    return locals()


@action('formsXwizard', method=["GET", "POST"] )
@action.uses(Template('forms-wizard.html', delimiters='[%[ ]]',), db, session,  T, )

def formsXwizard(id=None):
    ctrl_info= "ctrl: formsXwizard, view: forms-wizard.html"
    messages = []

    dfformsXwizard0_row= None
    id_dfformsXwizard0 = None
    fformsXwizard0= Form(db.dfformsXwizard0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXwizard0",  formstyle=FormStyleBulma )
   
    if fformsXwizard0.accepted:

        Glb['debug'] and print("     fformsXwizard0 accepted with: %s " % (fformsXwizard0.vars))
        fformsXwizard0_f0 = fformsXwizard0.vars.get('f0','')
        if len ( fformsXwizard0_f0 ):
            id_dfformsXwizard0 = db.dfformsXwizard0.insert( **fformsXwizard0.vars )
            db.commit()

            if not id_dfformsXwizard0 is None:
                dfformsXwizard0_row = db.dfformsXwizard0(id_dfformsXwizard0 )

                if not dfformsXwizard0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXwizard0.vars.f0}\" into db.dfformsXwizard0.f0, id = {id_dfformsXwizard0}' )
                         print(f"     found db.dfformsXwizard0.f0: \"{dfformsXwizard0_row.f0}\", id = {id_dfformsXwizard0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXwizard0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXwizard0.vars.items() ]
                print()
   
    elif fformsXwizard0.errors:
        print("fformsXwizard0 has errors: %s " % (fformsXwizard0.errors))
 

    dfformsXwizard1_row= None
    id_dfformsXwizard1 = None
    fformsXwizard1= Form(db.dfformsXwizard1, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXwizard1",  formstyle=FormStyleBulma )
   
    if fformsXwizard1.accepted:

        Glb['debug'] and print("     fformsXwizard1 accepted with: %s " % (fformsXwizard1.vars))
        fformsXwizard1_f0 = fformsXwizard1.vars.get('f0','')
        if len ( fformsXwizard1_f0 ):
            id_dfformsXwizard1 = db.dfformsXwizard1.insert( **fformsXwizard1.vars )
            db.commit()

            if not id_dfformsXwizard1 is None:
                dfformsXwizard1_row = db.dfformsXwizard1(id_dfformsXwizard1 )

                if not dfformsXwizard1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXwizard1.vars.f0}\" into db.dfformsXwizard1.f0, id = {id_dfformsXwizard1}' )
                         print(f"     found db.dfformsXwizard1.f0: \"{dfformsXwizard1_row.f0}\", id = {id_dfformsXwizard1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXwizard1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXwizard1.vars.items() ]
                print()
   
    elif fformsXwizard1.errors:
        print("fformsXwizard1 has errors: %s " % (fformsXwizard1.errors))
 

    dfformsXwizard2_row= None
    id_dfformsXwizard2 = None
    fformsXwizard2= Form(db.dfformsXwizard2, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXwizard2",  formstyle=FormStyleBulma )
   
    if fformsXwizard2.accepted:

        Glb['debug'] and print("     fformsXwizard2 accepted with: %s " % (fformsXwizard2.vars))
        fformsXwizard2_f0 = fformsXwizard2.vars.get('f0','')
        if len ( fformsXwizard2_f0 ):
            id_dfformsXwizard2 = db.dfformsXwizard2.insert( **fformsXwizard2.vars )
            db.commit()

            if not id_dfformsXwizard2 is None:
                dfformsXwizard2_row = db.dfformsXwizard2(id_dfformsXwizard2 )

                if not dfformsXwizard2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXwizard2.vars.f0}\" into db.dfformsXwizard2.f0, id = {id_dfformsXwizard2}' )
                         print(f"     found db.dfformsXwizard2.f0: \"{dfformsXwizard2_row.f0}\", id = {id_dfformsXwizard2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXwizard2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXwizard2.vars.items() ]
                print()
   
    elif fformsXwizard2.errors:
        print("fformsXwizard2 has errors: %s " % (fformsXwizard2.errors))
 

    dfformsXwizard3_row= None
    id_dfformsXwizard3 = None
    fformsXwizard3= Form(db.dfformsXwizard3, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXwizard3",  formstyle=FormStyleBulma )
   
    if fformsXwizard3.accepted:

        Glb['debug'] and print("     fformsXwizard3 accepted with: %s " % (fformsXwizard3.vars))
        fformsXwizard3_f0 = fformsXwizard3.vars.get('f0','')
        if len ( fformsXwizard3_f0 ):
            id_dfformsXwizard3 = db.dfformsXwizard3.insert( **fformsXwizard3.vars )
            db.commit()

            if not id_dfformsXwizard3 is None:
                dfformsXwizard3_row = db.dfformsXwizard3(id_dfformsXwizard3 )

                if not dfformsXwizard3_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXwizard3.vars.f0}\" into db.dfformsXwizard3.f0, id = {id_dfformsXwizard3}' )
                         print(f"     found db.dfformsXwizard3.f0: \"{dfformsXwizard3_row.f0}\", id = {id_dfformsXwizard3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXwizard3_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXwizard3.vars.items() ]
                print()
   
    elif fformsXwizard3.errors:
        print("fformsXwizard3 has errors: %s " % (fformsXwizard3.errors))
 

    dfformsXwizard4_row= None
    id_dfformsXwizard4 = None
    fformsXwizard4= Form(db.dfformsXwizard4, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXwizard4",  formstyle=FormStyleBulma )
   
    if fformsXwizard4.accepted:

        Glb['debug'] and print("     fformsXwizard4 accepted with: %s " % (fformsXwizard4.vars))
        fformsXwizard4_f0 = fformsXwizard4.vars.get('f0','')
        if len ( fformsXwizard4_f0 ):
            id_dfformsXwizard4 = db.dfformsXwizard4.insert( **fformsXwizard4.vars )
            db.commit()

            if not id_dfformsXwizard4 is None:
                dfformsXwizard4_row = db.dfformsXwizard4(id_dfformsXwizard4 )

                if not dfformsXwizard4_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXwizard4.vars.f0}\" into db.dfformsXwizard4.f0, id = {id_dfformsXwizard4}' )
                         print(f"     found db.dfformsXwizard4.f0: \"{dfformsXwizard4_row.f0}\", id = {id_dfformsXwizard4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXwizard4_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXwizard4.vars.items() ]
                print()
   
    elif fformsXwizard4.errors:
        print("fformsXwizard4 has errors: %s " % (fformsXwizard4.errors))
 

    dfformsXwizard5_row= None
    id_dfformsXwizard5 = None
    fformsXwizard5= Form(db.dfformsXwizard5, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXwizard5",  formstyle=FormStyleBulma )
   
    if fformsXwizard5.accepted:

        Glb['debug'] and print("     fformsXwizard5 accepted with: %s " % (fformsXwizard5.vars))
        fformsXwizard5_f0 = fformsXwizard5.vars.get('f0','')
        if len ( fformsXwizard5_f0 ):
            id_dfformsXwizard5 = db.dfformsXwizard5.insert( **fformsXwizard5.vars )
            db.commit()

            if not id_dfformsXwizard5 is None:
                dfformsXwizard5_row = db.dfformsXwizard5(id_dfformsXwizard5 )

                if not dfformsXwizard5_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXwizard5.vars.f0}\" into db.dfformsXwizard5.f0, id = {id_dfformsXwizard5}' )
                         print(f"     found db.dfformsXwizard5.f0: \"{dfformsXwizard5_row.f0}\", id = {id_dfformsXwizard5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXwizard5_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXwizard5.vars.items() ]
                print()
   
    elif fformsXwizard5.errors:
        print("fformsXwizard5 has errors: %s " % (fformsXwizard5.errors))
 

    return locals()


@action('pagesXinvoice', method=["GET", "POST"] )
@action.uses(Template('pages-invoice.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXinvoice(id=None):
    ctrl_info= "ctrl: pagesXinvoice, view: pages-invoice.html"
    messages = []

    rows_tpagesXinvoice0= db(db.tpagesXinvoice0).select()
    rows_tpagesXinvoice1= db(db.tpagesXinvoice1).select()
    dfpagesXinvoice0_row= None
    id_dfpagesXinvoice0 = None
    fpagesXinvoice0= Form(db.dfpagesXinvoice0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXinvoice0",  formstyle=FormStyleBulma )
   
    if fpagesXinvoice0.accepted:

        Glb['debug'] and print("     fpagesXinvoice0 accepted with: %s " % (fpagesXinvoice0.vars))
        fpagesXinvoice0_f0 = fpagesXinvoice0.vars.get('f0','')
        if len ( fpagesXinvoice0_f0 ):
            id_dfpagesXinvoice0 = db.dfpagesXinvoice0.insert( **fpagesXinvoice0.vars )
            db.commit()

            if not id_dfpagesXinvoice0 is None:
                dfpagesXinvoice0_row = db.dfpagesXinvoice0(id_dfpagesXinvoice0 )

                if not dfpagesXinvoice0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXinvoice0.vars.f0}\" into db.dfpagesXinvoice0.f0, id = {id_dfpagesXinvoice0}' )
                         print(f"     found db.dfpagesXinvoice0.f0: \"{dfpagesXinvoice0_row.f0}\", id = {id_dfpagesXinvoice0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXinvoice0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXinvoice0.vars.items() ]
                print()
   
    elif fpagesXinvoice0.errors:
        print("fpagesXinvoice0 has errors: %s " % (fpagesXinvoice0.errors))
 

    return locals()


@action('layoutsXboxed', method=["GET", "POST"] )
@action.uses(Template('layouts-boxed.html', delimiters='[%[ ]]',), db, session,  T, )

def layoutsXboxed(id=None):
    ctrl_info= "ctrl: layoutsXboxed, view: layouts-boxed.html"
    messages = []

    dflayoutsXboxed0_row= None
    id_dflayoutsXboxed0 = None
    flayoutsXboxed0= Form(db.dflayoutsXboxed0, id, deletable=False, dbio = False, keep_values = False, form_name = "flayoutsXboxed0",  formstyle=FormStyleBulma )
   
    if flayoutsXboxed0.accepted:

        Glb['debug'] and print("     flayoutsXboxed0 accepted with: %s " % (flayoutsXboxed0.vars))
        flayoutsXboxed0_f0 = flayoutsXboxed0.vars.get('f0','')
        if len ( flayoutsXboxed0_f0 ):
            id_dflayoutsXboxed0 = db.dflayoutsXboxed0.insert( **flayoutsXboxed0.vars )
            db.commit()

            if not id_dflayoutsXboxed0 is None:
                dflayoutsXboxed0_row = db.dflayoutsXboxed0(id_dflayoutsXboxed0 )

                if not dflayoutsXboxed0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flayoutsXboxed0.vars.f0}\" into db.dflayoutsXboxed0.f0, id = {id_dflayoutsXboxed0}' )
                         print(f"     found db.dflayoutsXboxed0.f0: \"{dflayoutsXboxed0_row.f0}\", id = {id_dflayoutsXboxed0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(flayoutsXboxed0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in flayoutsXboxed0.vars.items() ]
                print()
   
    elif flayoutsXboxed0.errors:
        print("flayoutsXboxed0 has errors: %s " % (flayoutsXboxed0.errors))
 

    return locals()


@action('mailboxXemail', method=["GET", "POST"] )
@action.uses(Template('mailbox-email.html', delimiters='[%[ ]]',), db, session,  T, )

def mailboxXemail(id=None):
    ctrl_info= "ctrl: mailboxXemail, view: mailbox-email.html"
    messages = []

    dfmailboxXemail0_row= None
    id_dfmailboxXemail0 = None
    fmailboxXemail0= Form(db.dfmailboxXemail0, id, deletable=False, dbio = False, keep_values = False, form_name = "fmailboxXemail0",  formstyle=FormStyleBulma )
   
    if fmailboxXemail0.accepted:

        Glb['debug'] and print("     fmailboxXemail0 accepted with: %s " % (fmailboxXemail0.vars))
        fmailboxXemail0_f0 = fmailboxXemail0.vars.get('f0','')
        if len ( fmailboxXemail0_f0 ):
            id_dfmailboxXemail0 = db.dfmailboxXemail0.insert( **fmailboxXemail0.vars )
            db.commit()

            if not id_dfmailboxXemail0 is None:
                dfmailboxXemail0_row = db.dfmailboxXemail0(id_dfmailboxXemail0 )

                if not dfmailboxXemail0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmailboxXemail0.vars.f0}\" into db.dfmailboxXemail0.f0, id = {id_dfmailboxXemail0}' )
                         print(f"     found db.dfmailboxXemail0.f0: \"{dfmailboxXemail0_row.f0}\", id = {id_dfmailboxXemail0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmailboxXemail0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmailboxXemail0.vars.items() ]
                print()
   
    elif fmailboxXemail0.errors:
        print("fmailboxXemail0 has errors: %s " % (fmailboxXemail0.errors))
 

    return locals()


@action('formsXlayouts', method=["GET", "POST"] )
@action.uses(Template('forms-layouts.html', delimiters='[%[ ]]',), db, session,  T, )

def formsXlayouts(id=None):
    ctrl_info= "ctrl: formsXlayouts, view: forms-layouts.html"
    messages = []

    dfformsXlayouts0_row= None
    id_dfformsXlayouts0 = None
    fformsXlayouts0= Form(db.dfformsXlayouts0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXlayouts0",  formstyle=FormStyleBulma )
   
    if fformsXlayouts0.accepted:

        Glb['debug'] and print("     fformsXlayouts0 accepted with: %s " % (fformsXlayouts0.vars))
        fformsXlayouts0_f0 = fformsXlayouts0.vars.get('f0','')
        if len ( fformsXlayouts0_f0 ):
            id_dfformsXlayouts0 = db.dfformsXlayouts0.insert( **fformsXlayouts0.vars )
            db.commit()

            if not id_dfformsXlayouts0 is None:
                dfformsXlayouts0_row = db.dfformsXlayouts0(id_dfformsXlayouts0 )

                if not dfformsXlayouts0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXlayouts0.vars.f0}\" into db.dfformsXlayouts0.f0, id = {id_dfformsXlayouts0}' )
                         print(f"     found db.dfformsXlayouts0.f0: \"{dfformsXlayouts0_row.f0}\", id = {id_dfformsXlayouts0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXlayouts0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXlayouts0.vars.items() ]
                print()
   
    elif fformsXlayouts0.errors:
        print("fformsXlayouts0 has errors: %s " % (fformsXlayouts0.errors))
 

    dfformsXlayouts1_row= None
    id_dfformsXlayouts1 = None
    fformsXlayouts1= Form(db.dfformsXlayouts1, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXlayouts1",  formstyle=FormStyleBulma )
   
    if fformsXlayouts1.accepted:

        Glb['debug'] and print("     fformsXlayouts1 accepted with: %s " % (fformsXlayouts1.vars))
        fformsXlayouts1_f0 = fformsXlayouts1.vars.get('f0','')
        if len ( fformsXlayouts1_f0 ):
            id_dfformsXlayouts1 = db.dfformsXlayouts1.insert( **fformsXlayouts1.vars )
            db.commit()

            if not id_dfformsXlayouts1 is None:
                dfformsXlayouts1_row = db.dfformsXlayouts1(id_dfformsXlayouts1 )

                if not dfformsXlayouts1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXlayouts1.vars.f0}\" into db.dfformsXlayouts1.f0, id = {id_dfformsXlayouts1}' )
                         print(f"     found db.dfformsXlayouts1.f0: \"{dfformsXlayouts1_row.f0}\", id = {id_dfformsXlayouts1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXlayouts1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXlayouts1.vars.items() ]
                print()
   
    elif fformsXlayouts1.errors:
        print("fformsXlayouts1 has errors: %s " % (fformsXlayouts1.errors))
 

    dfformsXlayouts2_row= None
    id_dfformsXlayouts2 = None
    fformsXlayouts2= Form(db.dfformsXlayouts2, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXlayouts2",  formstyle=FormStyleBulma )
   
    if fformsXlayouts2.accepted:

        Glb['debug'] and print("     fformsXlayouts2 accepted with: %s " % (fformsXlayouts2.vars))
        fformsXlayouts2_f0 = fformsXlayouts2.vars.get('f0','')
        if len ( fformsXlayouts2_f0 ):
            id_dfformsXlayouts2 = db.dfformsXlayouts2.insert( **fformsXlayouts2.vars )
            db.commit()

            if not id_dfformsXlayouts2 is None:
                dfformsXlayouts2_row = db.dfformsXlayouts2(id_dfformsXlayouts2 )

                if not dfformsXlayouts2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXlayouts2.vars.f0}\" into db.dfformsXlayouts2.f0, id = {id_dfformsXlayouts2}' )
                         print(f"     found db.dfformsXlayouts2.f0: \"{dfformsXlayouts2_row.f0}\", id = {id_dfformsXlayouts2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXlayouts2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXlayouts2.vars.items() ]
                print()
   
    elif fformsXlayouts2.errors:
        print("fformsXlayouts2 has errors: %s " % (fformsXlayouts2.errors))
 

    dfformsXlayouts3_row= None
    id_dfformsXlayouts3 = None
    fformsXlayouts3= Form(db.dfformsXlayouts3, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXlayouts3",  formstyle=FormStyleBulma )
   
    if fformsXlayouts3.accepted:

        Glb['debug'] and print("     fformsXlayouts3 accepted with: %s " % (fformsXlayouts3.vars))
        fformsXlayouts3_f0 = fformsXlayouts3.vars.get('f0','')
        if len ( fformsXlayouts3_f0 ):
            id_dfformsXlayouts3 = db.dfformsXlayouts3.insert( **fformsXlayouts3.vars )
            db.commit()

            if not id_dfformsXlayouts3 is None:
                dfformsXlayouts3_row = db.dfformsXlayouts3(id_dfformsXlayouts3 )

                if not dfformsXlayouts3_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXlayouts3.vars.f0}\" into db.dfformsXlayouts3.f0, id = {id_dfformsXlayouts3}' )
                         print(f"     found db.dfformsXlayouts3.f0: \"{dfformsXlayouts3_row.f0}\", id = {id_dfformsXlayouts3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXlayouts3_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXlayouts3.vars.items() ]
                print()
   
    elif fformsXlayouts3.errors:
        print("fformsXlayouts3 has errors: %s " % (fformsXlayouts3.errors))
 

    dfformsXlayouts4_row= None
    id_dfformsXlayouts4 = None
    fformsXlayouts4= Form(db.dfformsXlayouts4, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXlayouts4",  formstyle=FormStyleBulma )
   
    if fformsXlayouts4.accepted:

        Glb['debug'] and print("     fformsXlayouts4 accepted with: %s " % (fformsXlayouts4.vars))
        fformsXlayouts4_f0 = fformsXlayouts4.vars.get('f0','')
        if len ( fformsXlayouts4_f0 ):
            id_dfformsXlayouts4 = db.dfformsXlayouts4.insert( **fformsXlayouts4.vars )
            db.commit()

            if not id_dfformsXlayouts4 is None:
                dfformsXlayouts4_row = db.dfformsXlayouts4(id_dfformsXlayouts4 )

                if not dfformsXlayouts4_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXlayouts4.vars.f0}\" into db.dfformsXlayouts4.f0, id = {id_dfformsXlayouts4}' )
                         print(f"     found db.dfformsXlayouts4.f0: \"{dfformsXlayouts4_row.f0}\", id = {id_dfformsXlayouts4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXlayouts4_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXlayouts4.vars.items() ]
                print()
   
    elif fformsXlayouts4.errors:
        print("fformsXlayouts4 has errors: %s " % (fformsXlayouts4.errors))
 

    return locals()


@action('formsXadvanced', method=["GET", "POST"] )
@action.uses(Template('forms-advanced.html', delimiters='[%[ ]]',), db, session,  T, )

def formsXadvanced(id=None):
    ctrl_info= "ctrl: formsXadvanced, view: forms-advanced.html"
    messages = []

    dfformsXadvanced0_row= None
    id_dfformsXadvanced0 = None
    fformsXadvanced0= Form(db.dfformsXadvanced0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced0",  formstyle=FormStyleBulma )
   
    if fformsXadvanced0.accepted:

        Glb['debug'] and print("     fformsXadvanced0 accepted with: %s " % (fformsXadvanced0.vars))
        fformsXadvanced0_f0 = fformsXadvanced0.vars.get('f0','')
        if len ( fformsXadvanced0_f0 ):
            id_dfformsXadvanced0 = db.dfformsXadvanced0.insert( **fformsXadvanced0.vars )
            db.commit()

            if not id_dfformsXadvanced0 is None:
                dfformsXadvanced0_row = db.dfformsXadvanced0(id_dfformsXadvanced0 )

                if not dfformsXadvanced0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced0.vars.f0}\" into db.dfformsXadvanced0.f0, id = {id_dfformsXadvanced0}' )
                         print(f"     found db.dfformsXadvanced0.f0: \"{dfformsXadvanced0_row.f0}\", id = {id_dfformsXadvanced0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced0.vars.items() ]
                print()
   
    elif fformsXadvanced0.errors:
        print("fformsXadvanced0 has errors: %s " % (fformsXadvanced0.errors))
 

    dfformsXadvanced1_row= None
    id_dfformsXadvanced1 = None
    fformsXadvanced1= Form(db.dfformsXadvanced1, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced1",  formstyle=FormStyleBulma )
   
    if fformsXadvanced1.accepted:

        Glb['debug'] and print("     fformsXadvanced1 accepted with: %s " % (fformsXadvanced1.vars))
        fformsXadvanced1_f0 = fformsXadvanced1.vars.get('f0','')
        if len ( fformsXadvanced1_f0 ):
            id_dfformsXadvanced1 = db.dfformsXadvanced1.insert( **fformsXadvanced1.vars )
            db.commit()

            if not id_dfformsXadvanced1 is None:
                dfformsXadvanced1_row = db.dfformsXadvanced1(id_dfformsXadvanced1 )

                if not dfformsXadvanced1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced1.vars.f0}\" into db.dfformsXadvanced1.f0, id = {id_dfformsXadvanced1}' )
                         print(f"     found db.dfformsXadvanced1.f0: \"{dfformsXadvanced1_row.f0}\", id = {id_dfformsXadvanced1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced1.vars.items() ]
                print()
   
    elif fformsXadvanced1.errors:
        print("fformsXadvanced1 has errors: %s " % (fformsXadvanced1.errors))
 

    dfformsXadvanced2_row= None
    id_dfformsXadvanced2 = None
    fformsXadvanced2= Form(db.dfformsXadvanced2, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced2",  formstyle=FormStyleBulma )
   
    if fformsXadvanced2.accepted:

        Glb['debug'] and print("     fformsXadvanced2 accepted with: %s " % (fformsXadvanced2.vars))
        fformsXadvanced2_f0 = fformsXadvanced2.vars.get('f0','')
        if len ( fformsXadvanced2_f0 ):
            id_dfformsXadvanced2 = db.dfformsXadvanced2.insert( **fformsXadvanced2.vars )
            db.commit()

            if not id_dfformsXadvanced2 is None:
                dfformsXadvanced2_row = db.dfformsXadvanced2(id_dfformsXadvanced2 )

                if not dfformsXadvanced2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced2.vars.f0}\" into db.dfformsXadvanced2.f0, id = {id_dfformsXadvanced2}' )
                         print(f"     found db.dfformsXadvanced2.f0: \"{dfformsXadvanced2_row.f0}\", id = {id_dfformsXadvanced2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced2.vars.items() ]
                print()
   
    elif fformsXadvanced2.errors:
        print("fformsXadvanced2 has errors: %s " % (fformsXadvanced2.errors))
 

    dfformsXadvanced3_row= None
    id_dfformsXadvanced3 = None
    fformsXadvanced3= Form(db.dfformsXadvanced3, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced3",  formstyle=FormStyleBulma )
   
    if fformsXadvanced3.accepted:

        Glb['debug'] and print("     fformsXadvanced3 accepted with: %s " % (fformsXadvanced3.vars))
        fformsXadvanced3_f0 = fformsXadvanced3.vars.get('f0','')
        if len ( fformsXadvanced3_f0 ):
            id_dfformsXadvanced3 = db.dfformsXadvanced3.insert( **fformsXadvanced3.vars )
            db.commit()

            if not id_dfformsXadvanced3 is None:
                dfformsXadvanced3_row = db.dfformsXadvanced3(id_dfformsXadvanced3 )

                if not dfformsXadvanced3_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced3.vars.f0}\" into db.dfformsXadvanced3.f0, id = {id_dfformsXadvanced3}' )
                         print(f"     found db.dfformsXadvanced3.f0: \"{dfformsXadvanced3_row.f0}\", id = {id_dfformsXadvanced3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced3_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced3.vars.items() ]
                print()
   
    elif fformsXadvanced3.errors:
        print("fformsXadvanced3 has errors: %s " % (fformsXadvanced3.errors))
 

    dfformsXadvanced4_row= None
    id_dfformsXadvanced4 = None
    fformsXadvanced4= Form(db.dfformsXadvanced4, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced4",  formstyle=FormStyleBulma )
   
    if fformsXadvanced4.accepted:

        Glb['debug'] and print("     fformsXadvanced4 accepted with: %s " % (fformsXadvanced4.vars))
        fformsXadvanced4_f0 = fformsXadvanced4.vars.get('f0','')
        if len ( fformsXadvanced4_f0 ):
            id_dfformsXadvanced4 = db.dfformsXadvanced4.insert( **fformsXadvanced4.vars )
            db.commit()

            if not id_dfformsXadvanced4 is None:
                dfformsXadvanced4_row = db.dfformsXadvanced4(id_dfformsXadvanced4 )

                if not dfformsXadvanced4_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced4.vars.f0}\" into db.dfformsXadvanced4.f0, id = {id_dfformsXadvanced4}' )
                         print(f"     found db.dfformsXadvanced4.f0: \"{dfformsXadvanced4_row.f0}\", id = {id_dfformsXadvanced4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced4_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced4.vars.items() ]
                print()
   
    elif fformsXadvanced4.errors:
        print("fformsXadvanced4 has errors: %s " % (fformsXadvanced4.errors))
 

    dfformsXadvanced5_row= None
    id_dfformsXadvanced5 = None
    fformsXadvanced5= Form(db.dfformsXadvanced5, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced5",  formstyle=FormStyleBulma )
   
    if fformsXadvanced5.accepted:

        Glb['debug'] and print("     fformsXadvanced5 accepted with: %s " % (fformsXadvanced5.vars))
        fformsXadvanced5_f0 = fformsXadvanced5.vars.get('f0','')
        if len ( fformsXadvanced5_f0 ):
            id_dfformsXadvanced5 = db.dfformsXadvanced5.insert( **fformsXadvanced5.vars )
            db.commit()

            if not id_dfformsXadvanced5 is None:
                dfformsXadvanced5_row = db.dfformsXadvanced5(id_dfformsXadvanced5 )

                if not dfformsXadvanced5_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced5.vars.f0}\" into db.dfformsXadvanced5.f0, id = {id_dfformsXadvanced5}' )
                         print(f"     found db.dfformsXadvanced5.f0: \"{dfformsXadvanced5_row.f0}\", id = {id_dfformsXadvanced5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced5_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced5.vars.items() ]
                print()
   
    elif fformsXadvanced5.errors:
        print("fformsXadvanced5 has errors: %s " % (fformsXadvanced5.errors))
 

    dfformsXadvanced6_row= None
    id_dfformsXadvanced6 = None
    fformsXadvanced6= Form(db.dfformsXadvanced6, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced6",  formstyle=FormStyleBulma )
   
    if fformsXadvanced6.accepted:

        Glb['debug'] and print("     fformsXadvanced6 accepted with: %s " % (fformsXadvanced6.vars))
        fformsXadvanced6_f0 = fformsXadvanced6.vars.get('f0','')
        if len ( fformsXadvanced6_f0 ):
            id_dfformsXadvanced6 = db.dfformsXadvanced6.insert( **fformsXadvanced6.vars )
            db.commit()

            if not id_dfformsXadvanced6 is None:
                dfformsXadvanced6_row = db.dfformsXadvanced6(id_dfformsXadvanced6 )

                if not dfformsXadvanced6_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced6.vars.f0}\" into db.dfformsXadvanced6.f0, id = {id_dfformsXadvanced6}' )
                         print(f"     found db.dfformsXadvanced6.f0: \"{dfformsXadvanced6_row.f0}\", id = {id_dfformsXadvanced6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced6_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced6.vars.items() ]
                print()
   
    elif fformsXadvanced6.errors:
        print("fformsXadvanced6 has errors: %s " % (fformsXadvanced6.errors))
 

    dfformsXadvanced7_row= None
    id_dfformsXadvanced7 = None
    fformsXadvanced7= Form(db.dfformsXadvanced7, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced7",  formstyle=FormStyleBulma )
   
    if fformsXadvanced7.accepted:

        Glb['debug'] and print("     fformsXadvanced7 accepted with: %s " % (fformsXadvanced7.vars))
        fformsXadvanced7_f0 = fformsXadvanced7.vars.get('f0','')
        if len ( fformsXadvanced7_f0 ):
            id_dfformsXadvanced7 = db.dfformsXadvanced7.insert( **fformsXadvanced7.vars )
            db.commit()

            if not id_dfformsXadvanced7 is None:
                dfformsXadvanced7_row = db.dfformsXadvanced7(id_dfformsXadvanced7 )

                if not dfformsXadvanced7_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced7.vars.f0}\" into db.dfformsXadvanced7.f0, id = {id_dfformsXadvanced7}' )
                         print(f"     found db.dfformsXadvanced7.f0: \"{dfformsXadvanced7_row.f0}\", id = {id_dfformsXadvanced7}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced7_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced7.vars.items() ]
                print()
   
    elif fformsXadvanced7.errors:
        print("fformsXadvanced7 has errors: %s " % (fformsXadvanced7.errors))
 

    dfformsXadvanced8_row= None
    id_dfformsXadvanced8 = None
    fformsXadvanced8= Form(db.dfformsXadvanced8, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced8",  formstyle=FormStyleBulma )
   
    if fformsXadvanced8.accepted:

        Glb['debug'] and print("     fformsXadvanced8 accepted with: %s " % (fformsXadvanced8.vars))
        fformsXadvanced8_f0 = fformsXadvanced8.vars.get('f0','')
        if len ( fformsXadvanced8_f0 ):
            id_dfformsXadvanced8 = db.dfformsXadvanced8.insert( **fformsXadvanced8.vars )
            db.commit()

            if not id_dfformsXadvanced8 is None:
                dfformsXadvanced8_row = db.dfformsXadvanced8(id_dfformsXadvanced8 )

                if not dfformsXadvanced8_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced8.vars.f0}\" into db.dfformsXadvanced8.f0, id = {id_dfformsXadvanced8}' )
                         print(f"     found db.dfformsXadvanced8.f0: \"{dfformsXadvanced8_row.f0}\", id = {id_dfformsXadvanced8}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced8_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced8.vars.items() ]
                print()
   
    elif fformsXadvanced8.errors:
        print("fformsXadvanced8 has errors: %s " % (fformsXadvanced8.errors))
 

    dfformsXadvanced9_row= None
    id_dfformsXadvanced9 = None
    fformsXadvanced9= Form(db.dfformsXadvanced9, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced9",  formstyle=FormStyleBulma )
   
    if fformsXadvanced9.accepted:

        Glb['debug'] and print("     fformsXadvanced9 accepted with: %s " % (fformsXadvanced9.vars))
        fformsXadvanced9_f0 = fformsXadvanced9.vars.get('f0','')
        if len ( fformsXadvanced9_f0 ):
            id_dfformsXadvanced9 = db.dfformsXadvanced9.insert( **fformsXadvanced9.vars )
            db.commit()

            if not id_dfformsXadvanced9 is None:
                dfformsXadvanced9_row = db.dfformsXadvanced9(id_dfformsXadvanced9 )

                if not dfformsXadvanced9_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced9.vars.f0}\" into db.dfformsXadvanced9.f0, id = {id_dfformsXadvanced9}' )
                         print(f"     found db.dfformsXadvanced9.f0: \"{dfformsXadvanced9_row.f0}\", id = {id_dfformsXadvanced9}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced9_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced9.vars.items() ]
                print()
   
    elif fformsXadvanced9.errors:
        print("fformsXadvanced9 has errors: %s " % (fformsXadvanced9.errors))
 

    dfformsXadvanced10_row= None
    id_dfformsXadvanced10 = None
    fformsXadvanced10= Form(db.dfformsXadvanced10, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced10",  formstyle=FormStyleBulma )
   
    if fformsXadvanced10.accepted:

        Glb['debug'] and print("     fformsXadvanced10 accepted with: %s " % (fformsXadvanced10.vars))
        fformsXadvanced10_f0 = fformsXadvanced10.vars.get('f0','')
        if len ( fformsXadvanced10_f0 ):
            id_dfformsXadvanced10 = db.dfformsXadvanced10.insert( **fformsXadvanced10.vars )
            db.commit()

            if not id_dfformsXadvanced10 is None:
                dfformsXadvanced10_row = db.dfformsXadvanced10(id_dfformsXadvanced10 )

                if not dfformsXadvanced10_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced10.vars.f0}\" into db.dfformsXadvanced10.f0, id = {id_dfformsXadvanced10}' )
                         print(f"     found db.dfformsXadvanced10.f0: \"{dfformsXadvanced10_row.f0}\", id = {id_dfformsXadvanced10}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced10_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced10.vars.items() ]
                print()
   
    elif fformsXadvanced10.errors:
        print("fformsXadvanced10 has errors: %s " % (fformsXadvanced10.errors))
 

    dfformsXadvanced11_row= None
    id_dfformsXadvanced11 = None
    fformsXadvanced11= Form(db.dfformsXadvanced11, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced11",  formstyle=FormStyleBulma )
   
    if fformsXadvanced11.accepted:

        Glb['debug'] and print("     fformsXadvanced11 accepted with: %s " % (fformsXadvanced11.vars))
        fformsXadvanced11_f0 = fformsXadvanced11.vars.get('f0','')
        if len ( fformsXadvanced11_f0 ):
            id_dfformsXadvanced11 = db.dfformsXadvanced11.insert( **fformsXadvanced11.vars )
            db.commit()

            if not id_dfformsXadvanced11 is None:
                dfformsXadvanced11_row = db.dfformsXadvanced11(id_dfformsXadvanced11 )

                if not dfformsXadvanced11_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced11.vars.f0}\" into db.dfformsXadvanced11.f0, id = {id_dfformsXadvanced11}' )
                         print(f"     found db.dfformsXadvanced11.f0: \"{dfformsXadvanced11_row.f0}\", id = {id_dfformsXadvanced11}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced11_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced11.vars.items() ]
                print()
   
    elif fformsXadvanced11.errors:
        print("fformsXadvanced11 has errors: %s " % (fformsXadvanced11.errors))
 

    dfformsXadvanced12_row= None
    id_dfformsXadvanced12 = None
    fformsXadvanced12= Form(db.dfformsXadvanced12, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXadvanced12",  formstyle=FormStyleBulma )
   
    if fformsXadvanced12.accepted:

        Glb['debug'] and print("     fformsXadvanced12 accepted with: %s " % (fformsXadvanced12.vars))
        fformsXadvanced12_f0 = fformsXadvanced12.vars.get('f0','')
        if len ( fformsXadvanced12_f0 ):
            id_dfformsXadvanced12 = db.dfformsXadvanced12.insert( **fformsXadvanced12.vars )
            db.commit()

            if not id_dfformsXadvanced12 is None:
                dfformsXadvanced12_row = db.dfformsXadvanced12(id_dfformsXadvanced12 )

                if not dfformsXadvanced12_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXadvanced12.vars.f0}\" into db.dfformsXadvanced12.f0, id = {id_dfformsXadvanced12}' )
                         print(f"     found db.dfformsXadvanced12.f0: \"{dfformsXadvanced12_row.f0}\", id = {id_dfformsXadvanced12}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXadvanced12_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXadvanced12.vars.items() ]
                print()
   
    elif fformsXadvanced12.errors:
        print("fformsXadvanced12 has errors: %s " % (fformsXadvanced12.errors))
 

    return locals()


@action('tablesXpricing', method=["GET", "POST"] )
@action.uses(Template('tables-pricing.html', delimiters='[%[ ]]',), db, session,  T, )

def tablesXpricing(id=None):
    ctrl_info= "ctrl: tablesXpricing, view: tables-pricing.html"
    messages = []

    dftablesXpricing0_row= None
    id_dftablesXpricing0 = None
    ftablesXpricing0= Form(db.dftablesXpricing0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftablesXpricing0",  formstyle=FormStyleBulma )
   
    if ftablesXpricing0.accepted:

        Glb['debug'] and print("     ftablesXpricing0 accepted with: %s " % (ftablesXpricing0.vars))
        ftablesXpricing0_f0 = ftablesXpricing0.vars.get('f0','')
        if len ( ftablesXpricing0_f0 ):
            id_dftablesXpricing0 = db.dftablesXpricing0.insert( **ftablesXpricing0.vars )
            db.commit()

            if not id_dftablesXpricing0 is None:
                dftablesXpricing0_row = db.dftablesXpricing0(id_dftablesXpricing0 )

                if not dftablesXpricing0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftablesXpricing0.vars.f0}\" into db.dftablesXpricing0.f0, id = {id_dftablesXpricing0}' )
                         print(f"     found db.dftablesXpricing0.f0: \"{dftablesXpricing0_row.f0}\", id = {id_dftablesXpricing0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftablesXpricing0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftablesXpricing0.vars.items() ]
                print()
   
    elif ftablesXpricing0.errors:
        print("ftablesXpricing0 has errors: %s " % (ftablesXpricing0.errors))
 

    return locals()


@action('pagesXtimeline', method=["GET", "POST"] )
@action.uses(Template('pages-timeline.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXtimeline(id=None):
    ctrl_info= "ctrl: pagesXtimeline, view: pages-timeline.html"
    messages = []

    dfpagesXtimeline0_row= None
    id_dfpagesXtimeline0 = None
    fpagesXtimeline0= Form(db.dfpagesXtimeline0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXtimeline0",  formstyle=FormStyleBulma )
   
    if fpagesXtimeline0.accepted:

        Glb['debug'] and print("     fpagesXtimeline0 accepted with: %s " % (fpagesXtimeline0.vars))
        fpagesXtimeline0_f0 = fpagesXtimeline0.vars.get('f0','')
        if len ( fpagesXtimeline0_f0 ):
            id_dfpagesXtimeline0 = db.dfpagesXtimeline0.insert( **fpagesXtimeline0.vars )
            db.commit()

            if not id_dfpagesXtimeline0 is None:
                dfpagesXtimeline0_row = db.dfpagesXtimeline0(id_dfpagesXtimeline0 )

                if not dfpagesXtimeline0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXtimeline0.vars.f0}\" into db.dfpagesXtimeline0.f0, id = {id_dfpagesXtimeline0}' )
                         print(f"     found db.dfpagesXtimeline0.f0: \"{dfpagesXtimeline0_row.f0}\", id = {id_dfpagesXtimeline0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXtimeline0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXtimeline0.vars.items() ]
                print()
   
    elif fpagesXtimeline0.errors:
        print("fpagesXtimeline0 has errors: %s " % (fpagesXtimeline0.errors))
 

    return locals()


@action('pagesXcalendar', method=["GET", "POST"] )
@action.uses(Template('pages-calendar.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXcalendar(id=None):
    ctrl_info= "ctrl: pagesXcalendar, view: pages-calendar.html"
    messages = []

    dfpagesXcalendar0_row= None
    id_dfpagesXcalendar0 = None
    fpagesXcalendar0= Form(db.dfpagesXcalendar0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXcalendar0",  formstyle=FormStyleBulma )
   
    if fpagesXcalendar0.accepted:

        Glb['debug'] and print("     fpagesXcalendar0 accepted with: %s " % (fpagesXcalendar0.vars))
        fpagesXcalendar0_f0 = fpagesXcalendar0.vars.get('f0','')
        if len ( fpagesXcalendar0_f0 ):
            id_dfpagesXcalendar0 = db.dfpagesXcalendar0.insert( **fpagesXcalendar0.vars )
            db.commit()

            if not id_dfpagesXcalendar0 is None:
                dfpagesXcalendar0_row = db.dfpagesXcalendar0(id_dfpagesXcalendar0 )

                if not dfpagesXcalendar0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXcalendar0.vars.f0}\" into db.dfpagesXcalendar0.f0, id = {id_dfpagesXcalendar0}' )
                         print(f"     found db.dfpagesXcalendar0.f0: \"{dfpagesXcalendar0_row.f0}\", id = {id_dfpagesXcalendar0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXcalendar0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXcalendar0.vars.items() ]
                print()
   
    elif fpagesXcalendar0.errors:
        print("fpagesXcalendar0 has errors: %s " % (fpagesXcalendar0.errors))
 

    return locals()


@action('mailboxXfolder', method=["GET", "POST"] )
@action.uses(Template('mailbox-folder.html', delimiters='[%[ ]]',), db, session,  T, )

def mailboxXfolder(id=None):
    ctrl_info= "ctrl: mailboxXfolder, view: mailbox-folder.html"
    messages = []

    dfmailboxXfolder0_row= None
    id_dfmailboxXfolder0 = None
    fmailboxXfolder0= Form(db.dfmailboxXfolder0, id, deletable=False, dbio = False, keep_values = False, form_name = "fmailboxXfolder0",  formstyle=FormStyleBulma )
   
    if fmailboxXfolder0.accepted:

        Glb['debug'] and print("     fmailboxXfolder0 accepted with: %s " % (fmailboxXfolder0.vars))
        fmailboxXfolder0_f0 = fmailboxXfolder0.vars.get('f0','')
        if len ( fmailboxXfolder0_f0 ):
            id_dfmailboxXfolder0 = db.dfmailboxXfolder0.insert( **fmailboxXfolder0.vars )
            db.commit()

            if not id_dfmailboxXfolder0 is None:
                dfmailboxXfolder0_row = db.dfmailboxXfolder0(id_dfmailboxXfolder0 )

                if not dfmailboxXfolder0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmailboxXfolder0.vars.f0}\" into db.dfmailboxXfolder0.f0, id = {id_dfmailboxXfolder0}' )
                         print(f"     found db.dfmailboxXfolder0.f0: \"{dfmailboxXfolder0_row.f0}\", id = {id_dfmailboxXfolder0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmailboxXfolder0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmailboxXfolder0.vars.items() ]
                print()
   
    elif fmailboxXfolder0.errors:
        print("fmailboxXfolder0 has errors: %s " % (fmailboxXfolder0.errors))
 

    return locals()


@action('layoutsXscroll', method=["GET", "POST"] )
@action.uses(Template('layouts-scroll.html', delimiters='[%[ ]]',), db, session,  T, )

def layoutsXscroll(id=None):
    ctrl_info= "ctrl: layoutsXscroll, view: layouts-scroll.html"
    messages = []

    dflayoutsXscroll0_row= None
    id_dflayoutsXscroll0 = None
    flayoutsXscroll0= Form(db.dflayoutsXscroll0, id, deletable=False, dbio = False, keep_values = False, form_name = "flayoutsXscroll0",  formstyle=FormStyleBulma )
   
    if flayoutsXscroll0.accepted:

        Glb['debug'] and print("     flayoutsXscroll0 accepted with: %s " % (flayoutsXscroll0.vars))
        flayoutsXscroll0_f0 = flayoutsXscroll0.vars.get('f0','')
        if len ( flayoutsXscroll0_f0 ):
            id_dflayoutsXscroll0 = db.dflayoutsXscroll0.insert( **flayoutsXscroll0.vars )
            db.commit()

            if not id_dflayoutsXscroll0 is None:
                dflayoutsXscroll0_row = db.dflayoutsXscroll0(id_dflayoutsXscroll0 )

                if not dflayoutsXscroll0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flayoutsXscroll0.vars.f0}\" into db.dflayoutsXscroll0.f0, id = {id_dflayoutsXscroll0}' )
                         print(f"     found db.dflayoutsXscroll0.f0: \"{dflayoutsXscroll0_row.f0}\", id = {id_dflayoutsXscroll0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(flayoutsXscroll0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in flayoutsXscroll0.vars.items() ]
                print()
   
    elif flayoutsXscroll0.errors:
        print("flayoutsXscroll0 has errors: %s " % (flayoutsXscroll0.errors))
 

    return locals()


@action('tablesXeditable', method=["GET", "POST"] )
@action.uses(Template('tables-editable.html', delimiters='[%[ ]]',), db, session,  T, )

def tablesXeditable(id=None):
    ctrl_info= "ctrl: tablesXeditable, view: tables-editable.html"
    messages = []

    rows_ttablesXeditable0= db(db.ttablesXeditable0).select()
    dftablesXeditable0_row= None
    id_dftablesXeditable0 = None
    ftablesXeditable0= Form(db.dftablesXeditable0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftablesXeditable0",  formstyle=FormStyleBulma )
   
    if ftablesXeditable0.accepted:

        Glb['debug'] and print("     ftablesXeditable0 accepted with: %s " % (ftablesXeditable0.vars))
        ftablesXeditable0_f0 = ftablesXeditable0.vars.get('f0','')
        if len ( ftablesXeditable0_f0 ):
            id_dftablesXeditable0 = db.dftablesXeditable0.insert( **ftablesXeditable0.vars )
            db.commit()

            if not id_dftablesXeditable0 is None:
                dftablesXeditable0_row = db.dftablesXeditable0(id_dftablesXeditable0 )

                if not dftablesXeditable0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftablesXeditable0.vars.f0}\" into db.dftablesXeditable0.f0, id = {id_dftablesXeditable0}' )
                         print(f"     found db.dftablesXeditable0.f0: \"{dftablesXeditable0_row.f0}\", id = {id_dftablesXeditable0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftablesXeditable0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftablesXeditable0.vars.items() ]
                print()
   
    elif ftablesXeditable0.errors:
        print("ftablesXeditable0 has errors: %s " % (ftablesXeditable0.errors))
 

    return locals()


@action('tablesXadvanced', method=["GET", "POST"] )
@action.uses(Template('tables-advanced.html', delimiters='[%[ ]]',), db, session,  T, )

def tablesXadvanced(id=None):
    ctrl_info= "ctrl: tablesXadvanced, view: tables-advanced.html"
    messages = []

    rows_ttablesXadvanced0= db(db.ttablesXadvanced0).select()
    rows_ttablesXadvanced1= db(db.ttablesXadvanced1).select()
    rows_ttablesXadvanced2= db(db.ttablesXadvanced2).select()
    dftablesXadvanced0_row= None
    id_dftablesXadvanced0 = None
    ftablesXadvanced0= Form(db.dftablesXadvanced0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftablesXadvanced0",  formstyle=FormStyleBulma )
   
    if ftablesXadvanced0.accepted:

        Glb['debug'] and print("     ftablesXadvanced0 accepted with: %s " % (ftablesXadvanced0.vars))
        ftablesXadvanced0_f0 = ftablesXadvanced0.vars.get('f0','')
        if len ( ftablesXadvanced0_f0 ):
            id_dftablesXadvanced0 = db.dftablesXadvanced0.insert( **ftablesXadvanced0.vars )
            db.commit()

            if not id_dftablesXadvanced0 is None:
                dftablesXadvanced0_row = db.dftablesXadvanced0(id_dftablesXadvanced0 )

                if not dftablesXadvanced0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftablesXadvanced0.vars.f0}\" into db.dftablesXadvanced0.f0, id = {id_dftablesXadvanced0}' )
                         print(f"     found db.dftablesXadvanced0.f0: \"{dftablesXadvanced0_row.f0}\", id = {id_dftablesXadvanced0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftablesXadvanced0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftablesXadvanced0.vars.items() ]
                print()
   
    elif ftablesXadvanced0.errors:
        print("ftablesXadvanced0 has errors: %s " % (ftablesXadvanced0.errors))
 

    return locals()


@action('layoutsXdefault', method=["GET", "POST"] )
@action.uses(Template('layouts-default.html', delimiters='[%[ ]]',), db, session,  T, )

def layoutsXdefault(id=None):
    ctrl_info= "ctrl: layoutsXdefault, view: layouts-default.html"
    messages = []

    dflayoutsXdefault0_row= None
    id_dflayoutsXdefault0 = None
    flayoutsXdefault0= Form(db.dflayoutsXdefault0, id, deletable=False, dbio = False, keep_values = False, form_name = "flayoutsXdefault0",  formstyle=FormStyleBulma )
   
    if flayoutsXdefault0.accepted:

        Glb['debug'] and print("     flayoutsXdefault0 accepted with: %s " % (flayoutsXdefault0.vars))
        flayoutsXdefault0_f0 = flayoutsXdefault0.vars.get('f0','')
        if len ( flayoutsXdefault0_f0 ):
            id_dflayoutsXdefault0 = db.dflayoutsXdefault0.insert( **flayoutsXdefault0.vars )
            db.commit()

            if not id_dflayoutsXdefault0 is None:
                dflayoutsXdefault0_row = db.dflayoutsXdefault0(id_dflayoutsXdefault0 )

                if not dflayoutsXdefault0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flayoutsXdefault0.vars.f0}\" into db.dflayoutsXdefault0.f0, id = {id_dflayoutsXdefault0}' )
                         print(f"     found db.dflayoutsXdefault0.f0: \"{dflayoutsXdefault0_row.f0}\", id = {id_dflayoutsXdefault0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(flayoutsXdefault0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in flayoutsXdefault0.vars.items() ]
                print()
   
    elif flayoutsXdefault0.errors:
        print("flayoutsXdefault0 has errors: %s " % (flayoutsXdefault0.errors))
 

    return locals()


@action('mailboxXcompose', method=["GET", "POST"] )
@action.uses(Template('mailbox-compose.html', delimiters='[%[ ]]',), db, session,  T, )

def mailboxXcompose(id=None):
    ctrl_info= "ctrl: mailboxXcompose, view: mailbox-compose.html"
    messages = []

    dfmailboxXcompose0_row= None
    id_dfmailboxXcompose0 = None
    fmailboxXcompose0= Form(db.dfmailboxXcompose0, id, deletable=False, dbio = False, keep_values = False, form_name = "fmailboxXcompose0",  formstyle=FormStyleBulma )
   
    if fmailboxXcompose0.accepted:

        Glb['debug'] and print("     fmailboxXcompose0 accepted with: %s " % (fmailboxXcompose0.vars))
        fmailboxXcompose0_f0 = fmailboxXcompose0.vars.get('f0','')
        if len ( fmailboxXcompose0_f0 ):
            id_dfmailboxXcompose0 = db.dfmailboxXcompose0.insert( **fmailboxXcompose0.vars )
            db.commit()

            if not id_dfmailboxXcompose0 is None:
                dfmailboxXcompose0_row = db.dfmailboxXcompose0(id_dfmailboxXcompose0 )

                if not dfmailboxXcompose0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmailboxXcompose0.vars.f0}\" into db.dfmailboxXcompose0.f0, id = {id_dfmailboxXcompose0}' )
                         print(f"     found db.dfmailboxXcompose0.f0: \"{dfmailboxXcompose0_row.f0}\", id = {id_dfmailboxXcompose0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmailboxXcompose0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmailboxXcompose0.vars.items() ]
                print()
   
    elif fmailboxXcompose0.errors:
        print("fmailboxXcompose0 has errors: %s " % (fmailboxXcompose0.errors))
 

    dfmailboxXcompose1_row= None
    id_dfmailboxXcompose1 = None
    fmailboxXcompose1= Form(db.dfmailboxXcompose1, id, deletable=False, dbio = False, keep_values = False, form_name = "fmailboxXcompose1",  formstyle=FormStyleBulma )
   
    if fmailboxXcompose1.accepted:

        Glb['debug'] and print("     fmailboxXcompose1 accepted with: %s " % (fmailboxXcompose1.vars))
        fmailboxXcompose1_f0 = fmailboxXcompose1.vars.get('f0','')
        if len ( fmailboxXcompose1_f0 ):
            id_dfmailboxXcompose1 = db.dfmailboxXcompose1.insert( **fmailboxXcompose1.vars )
            db.commit()

            if not id_dfmailboxXcompose1 is None:
                dfmailboxXcompose1_row = db.dfmailboxXcompose1(id_dfmailboxXcompose1 )

                if not dfmailboxXcompose1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmailboxXcompose1.vars.f0}\" into db.dfmailboxXcompose1.f0, id = {id_dfmailboxXcompose1}' )
                         print(f"     found db.dfmailboxXcompose1.f0: \"{dfmailboxXcompose1_row.f0}\", id = {id_dfmailboxXcompose1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmailboxXcompose1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmailboxXcompose1.vars.items() ]
                print()
   
    elif fmailboxXcompose1.errors:
        print("fmailboxXcompose1 has errors: %s " % (fmailboxXcompose1.errors))
 

    return locals()


@action('uiXelementsXtabs', method=["GET", "POST"] )
@action.uses(Template('ui-elements-tabs.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXtabs(id=None):
    ctrl_info= "ctrl: uiXelementsXtabs, view: ui-elements-tabs.html"
    messages = []

    dfuiXelementsXtabs0_row= None
    id_dfuiXelementsXtabs0 = None
    fuiXelementsXtabs0= Form(db.dfuiXelementsXtabs0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXtabs0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXtabs0.accepted:

        Glb['debug'] and print("     fuiXelementsXtabs0 accepted with: %s " % (fuiXelementsXtabs0.vars))
        fuiXelementsXtabs0_f0 = fuiXelementsXtabs0.vars.get('f0','')
        if len ( fuiXelementsXtabs0_f0 ):
            id_dfuiXelementsXtabs0 = db.dfuiXelementsXtabs0.insert( **fuiXelementsXtabs0.vars )
            db.commit()

            if not id_dfuiXelementsXtabs0 is None:
                dfuiXelementsXtabs0_row = db.dfuiXelementsXtabs0(id_dfuiXelementsXtabs0 )

                if not dfuiXelementsXtabs0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXtabs0.vars.f0}\" into db.dfuiXelementsXtabs0.f0, id = {id_dfuiXelementsXtabs0}' )
                         print(f"     found db.dfuiXelementsXtabs0.f0: \"{dfuiXelementsXtabs0_row.f0}\", id = {id_dfuiXelementsXtabs0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXtabs0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXtabs0.vars.items() ]
                print()
   
    elif fuiXelementsXtabs0.errors:
        print("fuiXelementsXtabs0 has errors: %s " % (fuiXelementsXtabs0.errors))
 

    return locals()


@action('pagesXlogXviewer', method=["GET", "POST"] )
@action.uses(Template('pages-log-viewer.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXlogXviewer(id=None):
    ctrl_info= "ctrl: pagesXlogXviewer, view: pages-log-viewer.html"
    messages = []

    rows_tpagesXlogXviewer0= db(db.tpagesXlogXviewer0).select()
    rows_tpagesXlogXviewer1= db(db.tpagesXlogXviewer1).select()
    rows_tpagesXlogXviewer2= db(db.tpagesXlogXviewer2).select()
    dfpagesXlogXviewer0_row= None
    id_dfpagesXlogXviewer0 = None
    fpagesXlogXviewer0= Form(db.dfpagesXlogXviewer0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXlogXviewer0",  formstyle=FormStyleBulma )
   
    if fpagesXlogXviewer0.accepted:

        Glb['debug'] and print("     fpagesXlogXviewer0 accepted with: %s " % (fpagesXlogXviewer0.vars))
        fpagesXlogXviewer0_f0 = fpagesXlogXviewer0.vars.get('f0','')
        if len ( fpagesXlogXviewer0_f0 ):
            id_dfpagesXlogXviewer0 = db.dfpagesXlogXviewer0.insert( **fpagesXlogXviewer0.vars )
            db.commit()

            if not id_dfpagesXlogXviewer0 is None:
                dfpagesXlogXviewer0_row = db.dfpagesXlogXviewer0(id_dfpagesXlogXviewer0 )

                if not dfpagesXlogXviewer0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXlogXviewer0.vars.f0}\" into db.dfpagesXlogXviewer0.f0, id = {id_dfpagesXlogXviewer0}' )
                         print(f"     found db.dfpagesXlogXviewer0.f0: \"{dfpagesXlogXviewer0_row.f0}\", id = {id_dfpagesXlogXviewer0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXlogXviewer0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXlogXviewer0.vars.items() ]
                print()
   
    elif fpagesXlogXviewer0.errors:
        print("fpagesXlogXviewer0 has errors: %s " % (fpagesXlogXviewer0.errors))
 

    return locals()


@action('mapsXgoogleXmaps', method=["GET", "POST"] )
@action.uses(Template('maps-google-maps.html', delimiters='[%[ ]]',), db, session,  T, )

def mapsXgoogleXmaps(id=None):
    ctrl_info= "ctrl: mapsXgoogleXmaps, view: maps-google-maps.html"
    messages = []

    dfmapsXgoogleXmaps0_row= None
    id_dfmapsXgoogleXmaps0 = None
    fmapsXgoogleXmaps0= Form(db.dfmapsXgoogleXmaps0, id, deletable=False, dbio = False, keep_values = False, form_name = "fmapsXgoogleXmaps0",  formstyle=FormStyleBulma )
   
    if fmapsXgoogleXmaps0.accepted:

        Glb['debug'] and print("     fmapsXgoogleXmaps0 accepted with: %s " % (fmapsXgoogleXmaps0.vars))
        fmapsXgoogleXmaps0_f0 = fmapsXgoogleXmaps0.vars.get('f0','')
        if len ( fmapsXgoogleXmaps0_f0 ):
            id_dfmapsXgoogleXmaps0 = db.dfmapsXgoogleXmaps0.insert( **fmapsXgoogleXmaps0.vars )
            db.commit()

            if not id_dfmapsXgoogleXmaps0 is None:
                dfmapsXgoogleXmaps0_row = db.dfmapsXgoogleXmaps0(id_dfmapsXgoogleXmaps0 )

                if not dfmapsXgoogleXmaps0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmapsXgoogleXmaps0.vars.f0}\" into db.dfmapsXgoogleXmaps0.f0, id = {id_dfmapsXgoogleXmaps0}' )
                         print(f"     found db.dfmapsXgoogleXmaps0.f0: \"{dfmapsXgoogleXmaps0_row.f0}\", id = {id_dfmapsXgoogleXmaps0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmapsXgoogleXmaps0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmapsXgoogleXmaps0.vars.items() ]
                print()
   
    elif fmapsXgoogleXmaps0.errors:
        print("fmapsXgoogleXmaps0 has errors: %s " % (fmapsXgoogleXmaps0.errors))
 

    return locals()


@action('formsXvalidation', method=["GET", "POST"] )
@action.uses(Template('forms-validation.html', delimiters='[%[ ]]',), db, session,  T, )

def formsXvalidation(id=None):
    ctrl_info= "ctrl: formsXvalidation, view: forms-validation.html"
    messages = []

    dfformsXvalidation0_row= None
    id_dfformsXvalidation0 = None
    fformsXvalidation0= Form(db.dfformsXvalidation0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXvalidation0",  formstyle=FormStyleBulma )
   
    if fformsXvalidation0.accepted:

        Glb['debug'] and print("     fformsXvalidation0 accepted with: %s " % (fformsXvalidation0.vars))
        fformsXvalidation0_f0 = fformsXvalidation0.vars.get('f0','')
        if len ( fformsXvalidation0_f0 ):
            id_dfformsXvalidation0 = db.dfformsXvalidation0.insert( **fformsXvalidation0.vars )
            db.commit()

            if not id_dfformsXvalidation0 is None:
                dfformsXvalidation0_row = db.dfformsXvalidation0(id_dfformsXvalidation0 )

                if not dfformsXvalidation0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXvalidation0.vars.f0}\" into db.dfformsXvalidation0.f0, id = {id_dfformsXvalidation0}' )
                         print(f"     found db.dfformsXvalidation0.f0: \"{dfformsXvalidation0_row.f0}\", id = {id_dfformsXvalidation0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXvalidation0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXvalidation0.vars.items() ]
                print()
   
    elif fformsXvalidation0.errors:
        print("fformsXvalidation0 has errors: %s " % (fformsXvalidation0.errors))
 

    dfformsXvalidation1_row= None
    id_dfformsXvalidation1 = None
    fformsXvalidation1= Form(db.dfformsXvalidation1, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXvalidation1",  formstyle=FormStyleBulma )
   
    if fformsXvalidation1.accepted:

        Glb['debug'] and print("     fformsXvalidation1 accepted with: %s " % (fformsXvalidation1.vars))
        fformsXvalidation1_f0 = fformsXvalidation1.vars.get('f0','')
        if len ( fformsXvalidation1_f0 ):
            id_dfformsXvalidation1 = db.dfformsXvalidation1.insert( **fformsXvalidation1.vars )
            db.commit()

            if not id_dfformsXvalidation1 is None:
                dfformsXvalidation1_row = db.dfformsXvalidation1(id_dfformsXvalidation1 )

                if not dfformsXvalidation1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXvalidation1.vars.f0}\" into db.dfformsXvalidation1.f0, id = {id_dfformsXvalidation1}' )
                         print(f"     found db.dfformsXvalidation1.f0: \"{dfformsXvalidation1_row.f0}\", id = {id_dfformsXvalidation1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXvalidation1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXvalidation1.vars.items() ]
                print()
   
    elif fformsXvalidation1.errors:
        print("fformsXvalidation1 has errors: %s " % (fformsXvalidation1.errors))
 

    dfformsXvalidation2_row= None
    id_dfformsXvalidation2 = None
    fformsXvalidation2= Form(db.dfformsXvalidation2, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXvalidation2",  formstyle=FormStyleBulma )
   
    if fformsXvalidation2.accepted:

        Glb['debug'] and print("     fformsXvalidation2 accepted with: %s " % (fformsXvalidation2.vars))
        fformsXvalidation2_f0 = fformsXvalidation2.vars.get('f0','')
        if len ( fformsXvalidation2_f0 ):
            id_dfformsXvalidation2 = db.dfformsXvalidation2.insert( **fformsXvalidation2.vars )
            db.commit()

            if not id_dfformsXvalidation2 is None:
                dfformsXvalidation2_row = db.dfformsXvalidation2(id_dfformsXvalidation2 )

                if not dfformsXvalidation2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXvalidation2.vars.f0}\" into db.dfformsXvalidation2.f0, id = {id_dfformsXvalidation2}' )
                         print(f"     found db.dfformsXvalidation2.f0: \"{dfformsXvalidation2_row.f0}\", id = {id_dfformsXvalidation2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXvalidation2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXvalidation2.vars.items() ]
                print()
   
    elif fformsXvalidation2.errors:
        print("fformsXvalidation2 has errors: %s " % (fformsXvalidation2.errors))
 

    dfformsXvalidation3_row= None
    id_dfformsXvalidation3 = None
    fformsXvalidation3= Form(db.dfformsXvalidation3, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXvalidation3",  formstyle=FormStyleBulma )
   
    if fformsXvalidation3.accepted:

        Glb['debug'] and print("     fformsXvalidation3 accepted with: %s " % (fformsXvalidation3.vars))
        fformsXvalidation3_f0 = fformsXvalidation3.vars.get('f0','')
        if len ( fformsXvalidation3_f0 ):
            id_dfformsXvalidation3 = db.dfformsXvalidation3.insert( **fformsXvalidation3.vars )
            db.commit()

            if not id_dfformsXvalidation3 is None:
                dfformsXvalidation3_row = db.dfformsXvalidation3(id_dfformsXvalidation3 )

                if not dfformsXvalidation3_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXvalidation3.vars.f0}\" into db.dfformsXvalidation3.f0, id = {id_dfformsXvalidation3}' )
                         print(f"     found db.dfformsXvalidation3.f0: \"{dfformsXvalidation3_row.f0}\", id = {id_dfformsXvalidation3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXvalidation3_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXvalidation3.vars.items() ]
                print()
   
    elif fformsXvalidation3.errors:
        print("fformsXvalidation3 has errors: %s " % (fformsXvalidation3.errors))
 

    dfformsXvalidation4_row= None
    id_dfformsXvalidation4 = None
    fformsXvalidation4= Form(db.dfformsXvalidation4, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXvalidation4",  formstyle=FormStyleBulma )
   
    if fformsXvalidation4.accepted:

        Glb['debug'] and print("     fformsXvalidation4 accepted with: %s " % (fformsXvalidation4.vars))
        fformsXvalidation4_f0 = fformsXvalidation4.vars.get('f0','')
        if len ( fformsXvalidation4_f0 ):
            id_dfformsXvalidation4 = db.dfformsXvalidation4.insert( **fformsXvalidation4.vars )
            db.commit()

            if not id_dfformsXvalidation4 is None:
                dfformsXvalidation4_row = db.dfformsXvalidation4(id_dfformsXvalidation4 )

                if not dfformsXvalidation4_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXvalidation4.vars.f0}\" into db.dfformsXvalidation4.f0, id = {id_dfformsXvalidation4}' )
                         print(f"     found db.dfformsXvalidation4.f0: \"{dfformsXvalidation4_row.f0}\", id = {id_dfformsXvalidation4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXvalidation4_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXvalidation4.vars.items() ]
                print()
   
    elif fformsXvalidation4.errors:
        print("fformsXvalidation4 has errors: %s " % (fformsXvalidation4.errors))
 

    return locals()


@action('uiXelementsXicons', method=["GET", "POST"] )
@action.uses(Template('ui-elements-icons.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXicons(id=None):
    ctrl_info= "ctrl: uiXelementsXicons, view: ui-elements-icons.html"
    messages = []

    dfuiXelementsXicons0_row= None
    id_dfuiXelementsXicons0 = None
    fuiXelementsXicons0= Form(db.dfuiXelementsXicons0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXicons0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXicons0.accepted:

        Glb['debug'] and print("     fuiXelementsXicons0 accepted with: %s " % (fuiXelementsXicons0.vars))
        fuiXelementsXicons0_f0 = fuiXelementsXicons0.vars.get('f0','')
        if len ( fuiXelementsXicons0_f0 ):
            id_dfuiXelementsXicons0 = db.dfuiXelementsXicons0.insert( **fuiXelementsXicons0.vars )
            db.commit()

            if not id_dfuiXelementsXicons0 is None:
                dfuiXelementsXicons0_row = db.dfuiXelementsXicons0(id_dfuiXelementsXicons0 )

                if not dfuiXelementsXicons0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXicons0.vars.f0}\" into db.dfuiXelementsXicons0.f0, id = {id_dfuiXelementsXicons0}' )
                         print(f"     found db.dfuiXelementsXicons0.f0: \"{dfuiXelementsXicons0_row.f0}\", id = {id_dfuiXelementsXicons0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXicons0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXicons0.vars.items() ]
                print()
   
    elif fuiXelementsXicons0.errors:
        print("fuiXelementsXicons0 has errors: %s " % (fuiXelementsXicons0.errors))
 

    return locals()


@action('uiXelementsXextra', method=["GET", "POST"] )
@action.uses(Template('ui-elements-extra.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXextra(id=None):
    ctrl_info= "ctrl: uiXelementsXextra, view: ui-elements-extra.html"
    messages = []

    dfuiXelementsXextra0_row= None
    id_dfuiXelementsXextra0 = None
    fuiXelementsXextra0= Form(db.dfuiXelementsXextra0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXextra0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXextra0.accepted:

        Glb['debug'] and print("     fuiXelementsXextra0 accepted with: %s " % (fuiXelementsXextra0.vars))
        fuiXelementsXextra0_f0 = fuiXelementsXextra0.vars.get('f0','')
        if len ( fuiXelementsXextra0_f0 ):
            id_dfuiXelementsXextra0 = db.dfuiXelementsXextra0.insert( **fuiXelementsXextra0.vars )
            db.commit()

            if not id_dfuiXelementsXextra0 is None:
                dfuiXelementsXextra0_row = db.dfuiXelementsXextra0(id_dfuiXelementsXextra0 )

                if not dfuiXelementsXextra0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXextra0.vars.f0}\" into db.dfuiXelementsXextra0.f0, id = {id_dfuiXelementsXextra0}' )
                         print(f"     found db.dfuiXelementsXextra0.f0: \"{dfuiXelementsXextra0_row.f0}\", id = {id_dfuiXelementsXextra0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXextra0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXextra0.vars.items() ]
                print()
   
    elif fuiXelementsXextra0.errors:
        print("fuiXelementsXextra0 has errors: %s " % (fuiXelementsXextra0.errors))
 

    return locals()


@action('tablesXresponsive', method=["GET", "POST"] )
@action.uses(Template('tables-responsive.html', delimiters='[%[ ]]',), db, session,  T, )

def tablesXresponsive(id=None):
    ctrl_info= "ctrl: tablesXresponsive, view: tables-responsive.html"
    messages = []

    rows_ttablesXresponsive0= db(db.ttablesXresponsive0).select()
    rows_ttablesXresponsive1= db(db.ttablesXresponsive1).select()
    rows_ttablesXresponsive2= db(db.ttablesXresponsive2).select()
    dftablesXresponsive0_row= None
    id_dftablesXresponsive0 = None
    ftablesXresponsive0= Form(db.dftablesXresponsive0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftablesXresponsive0",  formstyle=FormStyleBulma )
   
    if ftablesXresponsive0.accepted:

        Glb['debug'] and print("     ftablesXresponsive0 accepted with: %s " % (ftablesXresponsive0.vars))
        ftablesXresponsive0_f0 = ftablesXresponsive0.vars.get('f0','')
        if len ( ftablesXresponsive0_f0 ):
            id_dftablesXresponsive0 = db.dftablesXresponsive0.insert( **ftablesXresponsive0.vars )
            db.commit()

            if not id_dftablesXresponsive0 is None:
                dftablesXresponsive0_row = db.dftablesXresponsive0(id_dftablesXresponsive0 )

                if not dftablesXresponsive0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftablesXresponsive0.vars.f0}\" into db.dftablesXresponsive0.f0, id = {id_dftablesXresponsive0}' )
                         print(f"     found db.dftablesXresponsive0.f0: \"{dftablesXresponsive0_row.f0}\", id = {id_dftablesXresponsive0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftablesXresponsive0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftablesXresponsive0.vars.items() ]
                print()
   
    elif ftablesXresponsive0.errors:
        print("ftablesXresponsive0 has errors: %s " % (ftablesXresponsive0.errors))
 

    return locals()


@action('pagesXlockXscreen', method=["GET", "POST"] )
@action.uses(Template('pages-lock-screen.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXlockXscreen(id=None):
    ctrl_info= "ctrl: pagesXlockXscreen, view: pages-lock-screen.html"
    messages = []

    dfpagesXlockXscreen0_row= None
    id_dfpagesXlockXscreen0 = None
    fpagesXlockXscreen0= Form(db.dfpagesXlockXscreen0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXlockXscreen0",  formstyle=FormStyleBulma )
   
    if fpagesXlockXscreen0.accepted:

        Glb['debug'] and print("     fpagesXlockXscreen0 accepted with: %s " % (fpagesXlockXscreen0.vars))
        fpagesXlockXscreen0_f0 = fpagesXlockXscreen0.vars.get('f0','')
        if len ( fpagesXlockXscreen0_f0 ):
            id_dfpagesXlockXscreen0 = db.dfpagesXlockXscreen0.insert( **fpagesXlockXscreen0.vars )
            db.commit()

            if not id_dfpagesXlockXscreen0 is None:
                dfpagesXlockXscreen0_row = db.dfpagesXlockXscreen0(id_dfpagesXlockXscreen0 )

                if not dfpagesXlockXscreen0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXlockXscreen0.vars.f0}\" into db.dfpagesXlockXscreen0.f0, id = {id_dfpagesXlockXscreen0}' )
                         print(f"     found db.dfpagesXlockXscreen0.f0: \"{dfpagesXlockXscreen0_row.f0}\", id = {id_dfpagesXlockXscreen0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXlockXscreen0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXlockXscreen0.vars.items() ]
                print()
   
    elif fpagesXlockXscreen0.errors:
        print("fpagesXlockXscreen0 has errors: %s " % (fpagesXlockXscreen0.errors))
 

    return locals()


@action('formsXcodeXeditor', method=["GET", "POST"] )
@action.uses(Template('forms-code-editor.html', delimiters='[%[ ]]',), db, session,  T, )

def formsXcodeXeditor(id=None):
    ctrl_info= "ctrl: formsXcodeXeditor, view: forms-code-editor.html"
    messages = []

    dfformsXcodeXeditor0_row= None
    id_dfformsXcodeXeditor0 = None
    fformsXcodeXeditor0= Form(db.dfformsXcodeXeditor0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXcodeXeditor0",  formstyle=FormStyleBulma )
   
    if fformsXcodeXeditor0.accepted:

        Glb['debug'] and print("     fformsXcodeXeditor0 accepted with: %s " % (fformsXcodeXeditor0.vars))
        fformsXcodeXeditor0_f0 = fformsXcodeXeditor0.vars.get('f0','')
        if len ( fformsXcodeXeditor0_f0 ):
            id_dfformsXcodeXeditor0 = db.dfformsXcodeXeditor0.insert( **fformsXcodeXeditor0.vars )
            db.commit()

            if not id_dfformsXcodeXeditor0 is None:
                dfformsXcodeXeditor0_row = db.dfformsXcodeXeditor0(id_dfformsXcodeXeditor0 )

                if not dfformsXcodeXeditor0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXcodeXeditor0.vars.f0}\" into db.dfformsXcodeXeditor0.f0, id = {id_dfformsXcodeXeditor0}' )
                         print(f"     found db.dfformsXcodeXeditor0.f0: \"{dfformsXcodeXeditor0_row.f0}\", id = {id_dfformsXcodeXeditor0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXcodeXeditor0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXcodeXeditor0.vars.items() ]
                print()
   
    elif fformsXcodeXeditor0.errors:
        print("fformsXcodeXeditor0 has errors: %s " % (fformsXcodeXeditor0.errors))
 

    dfformsXcodeXeditor1_row= None
    id_dfformsXcodeXeditor1 = None
    fformsXcodeXeditor1= Form(db.dfformsXcodeXeditor1, id, deletable=False, dbio = False, keep_values = False, form_name = "fformsXcodeXeditor1",  formstyle=FormStyleBulma )
   
    if fformsXcodeXeditor1.accepted:

        Glb['debug'] and print("     fformsXcodeXeditor1 accepted with: %s " % (fformsXcodeXeditor1.vars))
        fformsXcodeXeditor1_f0 = fformsXcodeXeditor1.vars.get('f0','')
        if len ( fformsXcodeXeditor1_f0 ):
            id_dfformsXcodeXeditor1 = db.dfformsXcodeXeditor1.insert( **fformsXcodeXeditor1.vars )
            db.commit()

            if not id_dfformsXcodeXeditor1 is None:
                dfformsXcodeXeditor1_row = db.dfformsXcodeXeditor1(id_dfformsXcodeXeditor1 )

                if not dfformsXcodeXeditor1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformsXcodeXeditor1.vars.f0}\" into db.dfformsXcodeXeditor1.f0, id = {id_dfformsXcodeXeditor1}' )
                         print(f"     found db.dfformsXcodeXeditor1.f0: \"{dfformsXcodeXeditor1_row.f0}\", id = {id_dfformsXcodeXeditor1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformsXcodeXeditor1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformsXcodeXeditor1.vars.items() ]
                print()
   
    elif fformsXcodeXeditor1.errors:
        print("fformsXcodeXeditor1 has errors: %s " % (fformsXcodeXeditor1.errors))
 

    return locals()


@action('uiXelementsXmodals', method=["GET", "POST"] )
@action.uses(Template('ui-elements-modals.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXmodals(id=None):
    ctrl_info= "ctrl: uiXelementsXmodals, view: ui-elements-modals.html"
    messages = []

    dfuiXelementsXmodals0_row= None
    id_dfuiXelementsXmodals0 = None
    fuiXelementsXmodals0= Form(db.dfuiXelementsXmodals0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXmodals0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXmodals0.accepted:

        Glb['debug'] and print("     fuiXelementsXmodals0 accepted with: %s " % (fuiXelementsXmodals0.vars))
        fuiXelementsXmodals0_f0 = fuiXelementsXmodals0.vars.get('f0','')
        if len ( fuiXelementsXmodals0_f0 ):
            id_dfuiXelementsXmodals0 = db.dfuiXelementsXmodals0.insert( **fuiXelementsXmodals0.vars )
            db.commit()

            if not id_dfuiXelementsXmodals0 is None:
                dfuiXelementsXmodals0_row = db.dfuiXelementsXmodals0(id_dfuiXelementsXmodals0 )

                if not dfuiXelementsXmodals0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXmodals0.vars.f0}\" into db.dfuiXelementsXmodals0.f0, id = {id_dfuiXelementsXmodals0}' )
                         print(f"     found db.dfuiXelementsXmodals0.f0: \"{dfuiXelementsXmodals0_row.f0}\", id = {id_dfuiXelementsXmodals0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXmodals0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXmodals0.vars.items() ]
                print()
   
    elif fuiXelementsXmodals0.errors:
        print("fuiXelementsXmodals0 has errors: %s " % (fuiXelementsXmodals0.errors))
 

    dfuiXelementsXmodals1_row= None
    id_dfuiXelementsXmodals1 = None
    fuiXelementsXmodals1= Form(db.dfuiXelementsXmodals1, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXmodals1",  formstyle=FormStyleBulma )
   
    if fuiXelementsXmodals1.accepted:

        Glb['debug'] and print("     fuiXelementsXmodals1 accepted with: %s " % (fuiXelementsXmodals1.vars))
        fuiXelementsXmodals1_f0 = fuiXelementsXmodals1.vars.get('f0','')
        if len ( fuiXelementsXmodals1_f0 ):
            id_dfuiXelementsXmodals1 = db.dfuiXelementsXmodals1.insert( **fuiXelementsXmodals1.vars )
            db.commit()

            if not id_dfuiXelementsXmodals1 is None:
                dfuiXelementsXmodals1_row = db.dfuiXelementsXmodals1(id_dfuiXelementsXmodals1 )

                if not dfuiXelementsXmodals1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXmodals1.vars.f0}\" into db.dfuiXelementsXmodals1.f0, id = {id_dfuiXelementsXmodals1}' )
                         print(f"     found db.dfuiXelementsXmodals1.f0: \"{dfuiXelementsXmodals1_row.f0}\", id = {id_dfuiXelementsXmodals1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXmodals1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXmodals1.vars.items() ]
                print()
   
    elif fuiXelementsXmodals1.errors:
        print("fuiXelementsXmodals1 has errors: %s " % (fuiXelementsXmodals1.errors))
 

    return locals()


@action('uiXelementsXpanels', method=["GET", "POST"] )
@action.uses(Template('ui-elements-panels.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXpanels(id=None):
    ctrl_info= "ctrl: uiXelementsXpanels, view: ui-elements-panels.html"
    messages = []

    dfuiXelementsXpanels0_row= None
    id_dfuiXelementsXpanels0 = None
    fuiXelementsXpanels0= Form(db.dfuiXelementsXpanels0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXpanels0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXpanels0.accepted:

        Glb['debug'] and print("     fuiXelementsXpanels0 accepted with: %s " % (fuiXelementsXpanels0.vars))
        fuiXelementsXpanels0_f0 = fuiXelementsXpanels0.vars.get('f0','')
        if len ( fuiXelementsXpanels0_f0 ):
            id_dfuiXelementsXpanels0 = db.dfuiXelementsXpanels0.insert( **fuiXelementsXpanels0.vars )
            db.commit()

            if not id_dfuiXelementsXpanels0 is None:
                dfuiXelementsXpanels0_row = db.dfuiXelementsXpanels0(id_dfuiXelementsXpanels0 )

                if not dfuiXelementsXpanels0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXpanels0.vars.f0}\" into db.dfuiXelementsXpanels0.f0, id = {id_dfuiXelementsXpanels0}' )
                         print(f"     found db.dfuiXelementsXpanels0.f0: \"{dfuiXelementsXpanels0_row.f0}\", id = {id_dfuiXelementsXpanels0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXpanels0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXpanels0.vars.items() ]
                print()
   
    elif fuiXelementsXpanels0.errors:
        print("fuiXelementsXpanels0 has errors: %s " % (fuiXelementsXpanels0.errors))
 

    return locals()


@action('uiXelementsXcharts', method=["GET", "POST"] )
@action.uses(Template('ui-elements-charts.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXcharts(id=None):
    ctrl_info= "ctrl: uiXelementsXcharts, view: ui-elements-charts.html"
    messages = []

    dfuiXelementsXcharts0_row= None
    id_dfuiXelementsXcharts0 = None
    fuiXelementsXcharts0= Form(db.dfuiXelementsXcharts0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXcharts0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXcharts0.accepted:

        Glb['debug'] and print("     fuiXelementsXcharts0 accepted with: %s " % (fuiXelementsXcharts0.vars))
        fuiXelementsXcharts0_f0 = fuiXelementsXcharts0.vars.get('f0','')
        if len ( fuiXelementsXcharts0_f0 ):
            id_dfuiXelementsXcharts0 = db.dfuiXelementsXcharts0.insert( **fuiXelementsXcharts0.vars )
            db.commit()

            if not id_dfuiXelementsXcharts0 is None:
                dfuiXelementsXcharts0_row = db.dfuiXelementsXcharts0(id_dfuiXelementsXcharts0 )

                if not dfuiXelementsXcharts0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXcharts0.vars.f0}\" into db.dfuiXelementsXcharts0.f0, id = {id_dfuiXelementsXcharts0}' )
                         print(f"     found db.dfuiXelementsXcharts0.f0: \"{dfuiXelementsXcharts0_row.f0}\", id = {id_dfuiXelementsXcharts0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXcharts0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXcharts0.vars.items() ]
                print()
   
    elif fuiXelementsXcharts0.errors:
        print("fuiXelementsXcharts0 has errors: %s " % (fuiXelementsXcharts0.errors))
 

    return locals()


@action('uiXelementsXalerts', method=["GET", "POST"] )
@action.uses(Template('ui-elements-alerts.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXalerts(id=None):
    ctrl_info= "ctrl: uiXelementsXalerts, view: ui-elements-alerts.html"
    messages = []

    dfuiXelementsXalerts0_row= None
    id_dfuiXelementsXalerts0 = None
    fuiXelementsXalerts0= Form(db.dfuiXelementsXalerts0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXalerts0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXalerts0.accepted:

        Glb['debug'] and print("     fuiXelementsXalerts0 accepted with: %s " % (fuiXelementsXalerts0.vars))
        fuiXelementsXalerts0_f0 = fuiXelementsXalerts0.vars.get('f0','')
        if len ( fuiXelementsXalerts0_f0 ):
            id_dfuiXelementsXalerts0 = db.dfuiXelementsXalerts0.insert( **fuiXelementsXalerts0.vars )
            db.commit()

            if not id_dfuiXelementsXalerts0 is None:
                dfuiXelementsXalerts0_row = db.dfuiXelementsXalerts0(id_dfuiXelementsXalerts0 )

                if not dfuiXelementsXalerts0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXalerts0.vars.f0}\" into db.dfuiXelementsXalerts0.f0, id = {id_dfuiXelementsXalerts0}' )
                         print(f"     found db.dfuiXelementsXalerts0.f0: \"{dfuiXelementsXalerts0_row.f0}\", id = {id_dfuiXelementsXalerts0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXalerts0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXalerts0.vars.items() ]
                print()
   
    elif fuiXelementsXalerts0.errors:
        print("fuiXelementsXalerts0 has errors: %s " % (fuiXelementsXalerts0.errors))
 

    return locals()


@action('pagesXuserXprofile', method=["GET", "POST"] )
@action.uses(Template('pages-user-profile.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXuserXprofile(id=None):
    ctrl_info= "ctrl: pagesXuserXprofile, view: pages-user-profile.html"
    messages = []

    dfpagesXuserXprofile0_row= None
    id_dfpagesXuserXprofile0 = None
    fpagesXuserXprofile0= Form(db.dfpagesXuserXprofile0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXuserXprofile0",  formstyle=FormStyleBulma )
   
    if fpagesXuserXprofile0.accepted:

        Glb['debug'] and print("     fpagesXuserXprofile0 accepted with: %s " % (fpagesXuserXprofile0.vars))
        fpagesXuserXprofile0_f0 = fpagesXuserXprofile0.vars.get('f0','')
        if len ( fpagesXuserXprofile0_f0 ):
            id_dfpagesXuserXprofile0 = db.dfpagesXuserXprofile0.insert( **fpagesXuserXprofile0.vars )
            db.commit()

            if not id_dfpagesXuserXprofile0 is None:
                dfpagesXuserXprofile0_row = db.dfpagesXuserXprofile0(id_dfpagesXuserXprofile0 )

                if not dfpagesXuserXprofile0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXuserXprofile0.vars.f0}\" into db.dfpagesXuserXprofile0.f0, id = {id_dfpagesXuserXprofile0}' )
                         print(f"     found db.dfpagesXuserXprofile0.f0: \"{dfpagesXuserXprofile0_row.f0}\", id = {id_dfpagesXuserXprofile0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXuserXprofile0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXuserXprofile0.vars.items() ]
                print()
   
    elif fpagesXuserXprofile0.errors:
        print("fpagesXuserXprofile0 has errors: %s " % (fpagesXuserXprofile0.errors))
 

    dfpagesXuserXprofile1_row= None
    id_dfpagesXuserXprofile1 = None
    fpagesXuserXprofile1= Form(db.dfpagesXuserXprofile1, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXuserXprofile1",  formstyle=FormStyleBulma )
   
    if fpagesXuserXprofile1.accepted:

        Glb['debug'] and print("     fpagesXuserXprofile1 accepted with: %s " % (fpagesXuserXprofile1.vars))
        fpagesXuserXprofile1_f0 = fpagesXuserXprofile1.vars.get('f0','')
        if len ( fpagesXuserXprofile1_f0 ):
            id_dfpagesXuserXprofile1 = db.dfpagesXuserXprofile1.insert( **fpagesXuserXprofile1.vars )
            db.commit()

            if not id_dfpagesXuserXprofile1 is None:
                dfpagesXuserXprofile1_row = db.dfpagesXuserXprofile1(id_dfpagesXuserXprofile1 )

                if not dfpagesXuserXprofile1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXuserXprofile1.vars.f0}\" into db.dfpagesXuserXprofile1.f0, id = {id_dfpagesXuserXprofile1}' )
                         print(f"     found db.dfpagesXuserXprofile1.f0: \"{dfpagesXuserXprofile1_row.f0}\", id = {id_dfpagesXuserXprofile1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXuserXprofile1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXuserXprofile1.vars.items() ]
                print()
   
    elif fpagesXuserXprofile1.errors:
        print("fpagesXuserXprofile1 has errors: %s " % (fpagesXuserXprofile1.errors))
 

    dfpagesXuserXprofile2_row= None
    id_dfpagesXuserXprofile2 = None
    fpagesXuserXprofile2= Form(db.dfpagesXuserXprofile2, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXuserXprofile2",  formstyle=FormStyleBulma )
   
    if fpagesXuserXprofile2.accepted:

        Glb['debug'] and print("     fpagesXuserXprofile2 accepted with: %s " % (fpagesXuserXprofile2.vars))
        fpagesXuserXprofile2_f0 = fpagesXuserXprofile2.vars.get('f0','')
        if len ( fpagesXuserXprofile2_f0 ):
            id_dfpagesXuserXprofile2 = db.dfpagesXuserXprofile2.insert( **fpagesXuserXprofile2.vars )
            db.commit()

            if not id_dfpagesXuserXprofile2 is None:
                dfpagesXuserXprofile2_row = db.dfpagesXuserXprofile2(id_dfpagesXuserXprofile2 )

                if not dfpagesXuserXprofile2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXuserXprofile2.vars.f0}\" into db.dfpagesXuserXprofile2.f0, id = {id_dfpagesXuserXprofile2}' )
                         print(f"     found db.dfpagesXuserXprofile2.f0: \"{dfpagesXuserXprofile2_row.f0}\", id = {id_dfpagesXuserXprofile2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXuserXprofile2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXuserXprofile2.vars.items() ]
                print()
   
    elif fpagesXuserXprofile2.errors:
        print("fpagesXuserXprofile2 has errors: %s " % (fpagesXuserXprofile2.errors))
 

    return locals()


@action('uiXelementsXwidgets', method=["GET", "POST"] )
@action.uses(Template('ui-elements-widgets.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXwidgets(id=None):
    ctrl_info= "ctrl: uiXelementsXwidgets, view: ui-elements-widgets.html"
    messages = []

    dfuiXelementsXwidgets0_row= None
    id_dfuiXelementsXwidgets0 = None
    fuiXelementsXwidgets0= Form(db.dfuiXelementsXwidgets0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXwidgets0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXwidgets0.accepted:

        Glb['debug'] and print("     fuiXelementsXwidgets0 accepted with: %s " % (fuiXelementsXwidgets0.vars))
        fuiXelementsXwidgets0_f0 = fuiXelementsXwidgets0.vars.get('f0','')
        if len ( fuiXelementsXwidgets0_f0 ):
            id_dfuiXelementsXwidgets0 = db.dfuiXelementsXwidgets0.insert( **fuiXelementsXwidgets0.vars )
            db.commit()

            if not id_dfuiXelementsXwidgets0 is None:
                dfuiXelementsXwidgets0_row = db.dfuiXelementsXwidgets0(id_dfuiXelementsXwidgets0 )

                if not dfuiXelementsXwidgets0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXwidgets0.vars.f0}\" into db.dfuiXelementsXwidgets0.f0, id = {id_dfuiXelementsXwidgets0}' )
                         print(f"     found db.dfuiXelementsXwidgets0.f0: \"{dfuiXelementsXwidgets0_row.f0}\", id = {id_dfuiXelementsXwidgets0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXwidgets0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXwidgets0.vars.items() ]
                print()
   
    elif fuiXelementsXwidgets0.errors:
        print("fuiXelementsXwidgets0 has errors: %s " % (fuiXelementsXwidgets0.errors))
 

    return locals()


@action('uiXelementsXsliders', method=["GET", "POST"] )
@action.uses(Template('ui-elements-sliders.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXsliders(id=None):
    ctrl_info= "ctrl: uiXelementsXsliders, view: ui-elements-sliders.html"
    messages = []

    dfuiXelementsXsliders0_row= None
    id_dfuiXelementsXsliders0 = None
    fuiXelementsXsliders0= Form(db.dfuiXelementsXsliders0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXsliders0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXsliders0.accepted:

        Glb['debug'] and print("     fuiXelementsXsliders0 accepted with: %s " % (fuiXelementsXsliders0.vars))
        fuiXelementsXsliders0_f0 = fuiXelementsXsliders0.vars.get('f0','')
        if len ( fuiXelementsXsliders0_f0 ):
            id_dfuiXelementsXsliders0 = db.dfuiXelementsXsliders0.insert( **fuiXelementsXsliders0.vars )
            db.commit()

            if not id_dfuiXelementsXsliders0 is None:
                dfuiXelementsXsliders0_row = db.dfuiXelementsXsliders0(id_dfuiXelementsXsliders0 )

                if not dfuiXelementsXsliders0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXsliders0.vars.f0}\" into db.dfuiXelementsXsliders0.f0, id = {id_dfuiXelementsXsliders0}' )
                         print(f"     found db.dfuiXelementsXsliders0.f0: \"{dfuiXelementsXsliders0_row.f0}\", id = {id_dfuiXelementsXsliders0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXsliders0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXsliders0.vars.items() ]
                print()
   
    elif fuiXelementsXsliders0.errors:
        print("fuiXelementsXsliders0 has errors: %s " % (fuiXelementsXsliders0.errors))
 

    return locals()


@action('uiXelementsXbuttons', method=["GET", "POST"] )
@action.uses(Template('ui-elements-buttons.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXbuttons(id=None):
    ctrl_info= "ctrl: uiXelementsXbuttons, view: ui-elements-buttons.html"
    messages = []

    dfuiXelementsXbuttons0_row= None
    id_dfuiXelementsXbuttons0 = None
    fuiXelementsXbuttons0= Form(db.dfuiXelementsXbuttons0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXbuttons0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXbuttons0.accepted:

        Glb['debug'] and print("     fuiXelementsXbuttons0 accepted with: %s " % (fuiXelementsXbuttons0.vars))
        fuiXelementsXbuttons0_f0 = fuiXelementsXbuttons0.vars.get('f0','')
        if len ( fuiXelementsXbuttons0_f0 ):
            id_dfuiXelementsXbuttons0 = db.dfuiXelementsXbuttons0.insert( **fuiXelementsXbuttons0.vars )
            db.commit()

            if not id_dfuiXelementsXbuttons0 is None:
                dfuiXelementsXbuttons0_row = db.dfuiXelementsXbuttons0(id_dfuiXelementsXbuttons0 )

                if not dfuiXelementsXbuttons0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXbuttons0.vars.f0}\" into db.dfuiXelementsXbuttons0.f0, id = {id_dfuiXelementsXbuttons0}' )
                         print(f"     found db.dfuiXelementsXbuttons0.f0: \"{dfuiXelementsXbuttons0_row.f0}\", id = {id_dfuiXelementsXbuttons0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXbuttons0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXbuttons0.vars.items() ]
                print()
   
    elif fuiXelementsXbuttons0.errors:
        print("fuiXelementsXbuttons0 has errors: %s " % (fuiXelementsXbuttons0.errors))
 

    return locals()


@action('pagesXmediaXgallery', method=["GET", "POST"] )
@action.uses(Template('pages-media-gallery.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXmediaXgallery(id=None):
    ctrl_info= "ctrl: pagesXmediaXgallery, view: pages-media-gallery.html"
    messages = []

    dfpagesXmediaXgallery0_row= None
    id_dfpagesXmediaXgallery0 = None
    fpagesXmediaXgallery0= Form(db.dfpagesXmediaXgallery0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXmediaXgallery0",  formstyle=FormStyleBulma )
   
    if fpagesXmediaXgallery0.accepted:

        Glb['debug'] and print("     fpagesXmediaXgallery0 accepted with: %s " % (fpagesXmediaXgallery0.vars))
        fpagesXmediaXgallery0_f0 = fpagesXmediaXgallery0.vars.get('f0','')
        if len ( fpagesXmediaXgallery0_f0 ):
            id_dfpagesXmediaXgallery0 = db.dfpagesXmediaXgallery0.insert( **fpagesXmediaXgallery0.vars )
            db.commit()

            if not id_dfpagesXmediaXgallery0 is None:
                dfpagesXmediaXgallery0_row = db.dfpagesXmediaXgallery0(id_dfpagesXmediaXgallery0 )

                if not dfpagesXmediaXgallery0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXmediaXgallery0.vars.f0}\" into db.dfpagesXmediaXgallery0.f0, id = {id_dfpagesXmediaXgallery0}' )
                         print(f"     found db.dfpagesXmediaXgallery0.f0: \"{dfpagesXmediaXgallery0_row.f0}\", id = {id_dfpagesXmediaXgallery0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXmediaXgallery0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXmediaXgallery0.vars.items() ]
                print()
   
    elif fpagesXmediaXgallery0.errors:
        print("fpagesXmediaXgallery0 has errors: %s " % (fpagesXmediaXgallery0.errors))
 

    return locals()


@action('pagesXinvoiceXprint', method=["GET", "POST"] )
@action.uses(Template('pages-invoice-print.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXinvoiceXprint(id=None):
    ctrl_info= "ctrl: pagesXinvoiceXprint, view: pages-invoice-print.html"
    messages = []

    rows_tpagesXinvoiceXprint0= db(db.tpagesXinvoiceXprint0).select()
    rows_tpagesXinvoiceXprint1= db(db.tpagesXinvoiceXprint1).select()
    return locals()


@action('uiXelementsXportlets', method=["GET", "POST"] )
@action.uses(Template('ui-elements-portlets.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXportlets(id=None):
    ctrl_info= "ctrl: uiXelementsXportlets, view: ui-elements-portlets.html"
    messages = []

    dfuiXelementsXportlets0_row= None
    id_dfuiXelementsXportlets0 = None
    fuiXelementsXportlets0= Form(db.dfuiXelementsXportlets0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXportlets0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXportlets0.accepted:

        Glb['debug'] and print("     fuiXelementsXportlets0 accepted with: %s " % (fuiXelementsXportlets0.vars))
        fuiXelementsXportlets0_f0 = fuiXelementsXportlets0.vars.get('f0','')
        if len ( fuiXelementsXportlets0_f0 ):
            id_dfuiXelementsXportlets0 = db.dfuiXelementsXportlets0.insert( **fuiXelementsXportlets0.vars )
            db.commit()

            if not id_dfuiXelementsXportlets0 is None:
                dfuiXelementsXportlets0_row = db.dfuiXelementsXportlets0(id_dfuiXelementsXportlets0 )

                if not dfuiXelementsXportlets0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXportlets0.vars.f0}\" into db.dfuiXelementsXportlets0.f0, id = {id_dfuiXelementsXportlets0}' )
                         print(f"     found db.dfuiXelementsXportlets0.f0: \"{dfuiXelementsXportlets0_row.f0}\", id = {id_dfuiXelementsXportlets0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXportlets0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXportlets0.vars.items() ]
                print()
   
    elif fuiXelementsXportlets0.errors:
        print("fuiXelementsXportlets0 has errors: %s " % (fuiXelementsXportlets0.errors))
 

    return locals()


@action('uiXelementsXnestable', method=["GET", "POST"] )
@action.uses(Template('ui-elements-nestable.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXnestable(id=None):
    ctrl_info= "ctrl: uiXelementsXnestable, view: ui-elements-nestable.html"
    messages = []

    dfuiXelementsXnestable0_row= None
    id_dfuiXelementsXnestable0 = None
    fuiXelementsXnestable0= Form(db.dfuiXelementsXnestable0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXnestable0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXnestable0.accepted:

        Glb['debug'] and print("     fuiXelementsXnestable0 accepted with: %s " % (fuiXelementsXnestable0.vars))
        fuiXelementsXnestable0_f0 = fuiXelementsXnestable0.vars.get('f0','')
        if len ( fuiXelementsXnestable0_f0 ):
            id_dfuiXelementsXnestable0 = db.dfuiXelementsXnestable0.insert( **fuiXelementsXnestable0.vars )
            db.commit()

            if not id_dfuiXelementsXnestable0 is None:
                dfuiXelementsXnestable0_row = db.dfuiXelementsXnestable0(id_dfuiXelementsXnestable0 )

                if not dfuiXelementsXnestable0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXnestable0.vars.f0}\" into db.dfuiXelementsXnestable0.f0, id = {id_dfuiXelementsXnestable0}' )
                         print(f"     found db.dfuiXelementsXnestable0.f0: \"{dfuiXelementsXnestable0_row.f0}\", id = {id_dfuiXelementsXnestable0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXnestable0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXnestable0.vars.items() ]
                print()
   
    elif fuiXelementsXnestable0.errors:
        print("fuiXelementsXnestable0 has errors: %s " % (fuiXelementsXnestable0.errors))
 

    return locals()


@action('uiXelementsXlightbox', method=["GET", "POST"] )
@action.uses(Template('ui-elements-lightbox.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXlightbox(id=None):
    ctrl_info= "ctrl: uiXelementsXlightbox, view: ui-elements-lightbox.html"
    messages = []

    dfuiXelementsXlightbox0_row= None
    id_dfuiXelementsXlightbox0 = None
    fuiXelementsXlightbox0= Form(db.dfuiXelementsXlightbox0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXlightbox0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXlightbox0.accepted:

        Glb['debug'] and print("     fuiXelementsXlightbox0 accepted with: %s " % (fuiXelementsXlightbox0.vars))
        fuiXelementsXlightbox0_f0 = fuiXelementsXlightbox0.vars.get('f0','')
        if len ( fuiXelementsXlightbox0_f0 ):
            id_dfuiXelementsXlightbox0 = db.dfuiXelementsXlightbox0.insert( **fuiXelementsXlightbox0.vars )
            db.commit()

            if not id_dfuiXelementsXlightbox0 is None:
                dfuiXelementsXlightbox0_row = db.dfuiXelementsXlightbox0(id_dfuiXelementsXlightbox0 )

                if not dfuiXelementsXlightbox0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXlightbox0.vars.f0}\" into db.dfuiXelementsXlightbox0.f0, id = {id_dfuiXelementsXlightbox0}' )
                         print(f"     found db.dfuiXelementsXlightbox0.f0: \"{dfuiXelementsXlightbox0_row.f0}\", id = {id_dfuiXelementsXlightbox0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXlightbox0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXlightbox0.vars.items() ]
                print()
   
    elif fuiXelementsXlightbox0.errors:
        print("fuiXelementsXlightbox0 has errors: %s " % (fuiXelementsXlightbox0.errors))
 

    dfuiXelementsXlightbox1_row= None
    id_dfuiXelementsXlightbox1 = None
    fuiXelementsXlightbox1= Form(db.dfuiXelementsXlightbox1, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXlightbox1",  formstyle=FormStyleBulma )
   
    if fuiXelementsXlightbox1.accepted:

        Glb['debug'] and print("     fuiXelementsXlightbox1 accepted with: %s " % (fuiXelementsXlightbox1.vars))
        fuiXelementsXlightbox1_f0 = fuiXelementsXlightbox1.vars.get('f0','')
        if len ( fuiXelementsXlightbox1_f0 ):
            id_dfuiXelementsXlightbox1 = db.dfuiXelementsXlightbox1.insert( **fuiXelementsXlightbox1.vars )
            db.commit()

            if not id_dfuiXelementsXlightbox1 is None:
                dfuiXelementsXlightbox1_row = db.dfuiXelementsXlightbox1(id_dfuiXelementsXlightbox1 )

                if not dfuiXelementsXlightbox1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXlightbox1.vars.f0}\" into db.dfuiXelementsXlightbox1.f0, id = {id_dfuiXelementsXlightbox1}' )
                         print(f"     found db.dfuiXelementsXlightbox1.f0: \"{dfuiXelementsXlightbox1_row.f0}\", id = {id_dfuiXelementsXlightbox1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXlightbox1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXlightbox1.vars.items() ]
                print()
   
    elif fuiXelementsXlightbox1.errors:
        print("fuiXelementsXlightbox1 has errors: %s " % (fuiXelementsXlightbox1.errors))
 

    return locals()


@action('pagesXsearchXresults', method=["GET", "POST"] )
@action.uses(Template('pages-search-results.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXsearchXresults(id=None):
    ctrl_info= "ctrl: pagesXsearchXresults, view: pages-search-results.html"
    messages = []

    dfpagesXsearchXresults0_row= None
    id_dfpagesXsearchXresults0 = None
    fpagesXsearchXresults0= Form(db.dfpagesXsearchXresults0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXsearchXresults0",  formstyle=FormStyleBulma )
   
    if fpagesXsearchXresults0.accepted:

        Glb['debug'] and print("     fpagesXsearchXresults0 accepted with: %s " % (fpagesXsearchXresults0.vars))
        fpagesXsearchXresults0_f0 = fpagesXsearchXresults0.vars.get('f0','')
        if len ( fpagesXsearchXresults0_f0 ):
            id_dfpagesXsearchXresults0 = db.dfpagesXsearchXresults0.insert( **fpagesXsearchXresults0.vars )
            db.commit()

            if not id_dfpagesXsearchXresults0 is None:
                dfpagesXsearchXresults0_row = db.dfpagesXsearchXresults0(id_dfpagesXsearchXresults0 )

                if not dfpagesXsearchXresults0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXsearchXresults0.vars.f0}\" into db.dfpagesXsearchXresults0.f0, id = {id_dfpagesXsearchXresults0}' )
                         print(f"     found db.dfpagesXsearchXresults0.f0: \"{dfpagesXsearchXresults0_row.f0}\", id = {id_dfpagesXsearchXresults0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXsearchXresults0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXsearchXresults0.vars.items() ]
                print()
   
    elif fpagesXsearchXresults0.errors:
        print("fpagesXsearchXresults0 has errors: %s " % (fpagesXsearchXresults0.errors))
 

    dfpagesXsearchXresults1_row= None
    id_dfpagesXsearchXresults1 = None
    fpagesXsearchXresults1= Form(db.dfpagesXsearchXresults1, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXsearchXresults1",  formstyle=FormStyleBulma )
   
    if fpagesXsearchXresults1.accepted:

        Glb['debug'] and print("     fpagesXsearchXresults1 accepted with: %s " % (fpagesXsearchXresults1.vars))
        fpagesXsearchXresults1_f0 = fpagesXsearchXresults1.vars.get('f0','')
        if len ( fpagesXsearchXresults1_f0 ):
            id_dfpagesXsearchXresults1 = db.dfpagesXsearchXresults1.insert( **fpagesXsearchXresults1.vars )
            db.commit()

            if not id_dfpagesXsearchXresults1 is None:
                dfpagesXsearchXresults1_row = db.dfpagesXsearchXresults1(id_dfpagesXsearchXresults1 )

                if not dfpagesXsearchXresults1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXsearchXresults1.vars.f0}\" into db.dfpagesXsearchXresults1.f0, id = {id_dfpagesXsearchXresults1}' )
                         print(f"     found db.dfpagesXsearchXresults1.f0: \"{dfpagesXsearchXresults1_row.f0}\", id = {id_dfpagesXsearchXresults1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXsearchXresults1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXsearchXresults1.vars.items() ]
                print()
   
    elif fpagesXsearchXresults1.errors:
        print("fpagesXsearchXresults1 has errors: %s " % (fpagesXsearchXresults1.errors))
 

    return locals()


@action('uiXelementsXtreeXview', method=["GET", "POST"] )
@action.uses(Template('ui-elements-tree-view.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXtreeXview(id=None):
    ctrl_info= "ctrl: uiXelementsXtreeXview, view: ui-elements-tree-view.html"
    messages = []

    dfuiXelementsXtreeXview0_row= None
    id_dfuiXelementsXtreeXview0 = None
    fuiXelementsXtreeXview0= Form(db.dfuiXelementsXtreeXview0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXtreeXview0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXtreeXview0.accepted:

        Glb['debug'] and print("     fuiXelementsXtreeXview0 accepted with: %s " % (fuiXelementsXtreeXview0.vars))
        fuiXelementsXtreeXview0_f0 = fuiXelementsXtreeXview0.vars.get('f0','')
        if len ( fuiXelementsXtreeXview0_f0 ):
            id_dfuiXelementsXtreeXview0 = db.dfuiXelementsXtreeXview0.insert( **fuiXelementsXtreeXview0.vars )
            db.commit()

            if not id_dfuiXelementsXtreeXview0 is None:
                dfuiXelementsXtreeXview0_row = db.dfuiXelementsXtreeXview0(id_dfuiXelementsXtreeXview0 )

                if not dfuiXelementsXtreeXview0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXtreeXview0.vars.f0}\" into db.dfuiXelementsXtreeXview0.f0, id = {id_dfuiXelementsXtreeXview0}' )
                         print(f"     found db.dfuiXelementsXtreeXview0.f0: \"{dfuiXelementsXtreeXview0_row.f0}\", id = {id_dfuiXelementsXtreeXview0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXtreeXview0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXtreeXview0.vars.items() ]
                print()
   
    elif fuiXelementsXtreeXview0.errors:
        print("fuiXelementsXtreeXview0 has errors: %s " % (fuiXelementsXtreeXview0.errors))
 

    return locals()


@action('uiXelementsXcarousels', method=["GET", "POST"] )
@action.uses(Template('ui-elements-carousels.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXcarousels(id=None):
    ctrl_info= "ctrl: uiXelementsXcarousels, view: ui-elements-carousels.html"
    messages = []

    dfuiXelementsXcarousels0_row= None
    id_dfuiXelementsXcarousels0 = None
    fuiXelementsXcarousels0= Form(db.dfuiXelementsXcarousels0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXcarousels0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXcarousels0.accepted:

        Glb['debug'] and print("     fuiXelementsXcarousels0 accepted with: %s " % (fuiXelementsXcarousels0.vars))
        fuiXelementsXcarousels0_f0 = fuiXelementsXcarousels0.vars.get('f0','')
        if len ( fuiXelementsXcarousels0_f0 ):
            id_dfuiXelementsXcarousels0 = db.dfuiXelementsXcarousels0.insert( **fuiXelementsXcarousels0.vars )
            db.commit()

            if not id_dfuiXelementsXcarousels0 is None:
                dfuiXelementsXcarousels0_row = db.dfuiXelementsXcarousels0(id_dfuiXelementsXcarousels0 )

                if not dfuiXelementsXcarousels0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXcarousels0.vars.f0}\" into db.dfuiXelementsXcarousels0.f0, id = {id_dfuiXelementsXcarousels0}' )
                         print(f"     found db.dfuiXelementsXcarousels0.f0: \"{dfuiXelementsXcarousels0_row.f0}\", id = {id_dfuiXelementsXcarousels0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXcarousels0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXcarousels0.vars.items() ]
                print()
   
    elif fuiXelementsXcarousels0.errors:
        print("fuiXelementsXcarousels0 has errors: %s " % (fuiXelementsXcarousels0.errors))
 

    return locals()


@action('pagesXsessionXtimeout', method=["GET", "POST"] )
@action.uses(Template('pages-session-timeout.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXsessionXtimeout(id=None):
    ctrl_info= "ctrl: pagesXsessionXtimeout, view: pages-session-timeout.html"
    messages = []

    dfpagesXsessionXtimeout0_row= None
    id_dfpagesXsessionXtimeout0 = None
    fpagesXsessionXtimeout0= Form(db.dfpagesXsessionXtimeout0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXsessionXtimeout0",  formstyle=FormStyleBulma )
   
    if fpagesXsessionXtimeout0.accepted:

        Glb['debug'] and print("     fpagesXsessionXtimeout0 accepted with: %s " % (fpagesXsessionXtimeout0.vars))
        fpagesXsessionXtimeout0_f0 = fpagesXsessionXtimeout0.vars.get('f0','')
        if len ( fpagesXsessionXtimeout0_f0 ):
            id_dfpagesXsessionXtimeout0 = db.dfpagesXsessionXtimeout0.insert( **fpagesXsessionXtimeout0.vars )
            db.commit()

            if not id_dfpagesXsessionXtimeout0 is None:
                dfpagesXsessionXtimeout0_row = db.dfpagesXsessionXtimeout0(id_dfpagesXsessionXtimeout0 )

                if not dfpagesXsessionXtimeout0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXsessionXtimeout0.vars.f0}\" into db.dfpagesXsessionXtimeout0.f0, id = {id_dfpagesXsessionXtimeout0}' )
                         print(f"     found db.dfpagesXsessionXtimeout0.f0: \"{dfpagesXsessionXtimeout0_row.f0}\", id = {id_dfpagesXsessionXtimeout0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXsessionXtimeout0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXsessionXtimeout0.vars.items() ]
                print()
   
    elif fpagesXsessionXtimeout0.errors:
        print("fpagesXsessionXtimeout0 has errors: %s " % (fpagesXsessionXtimeout0.errors))
 

    return locals()


@action('uiXelementsXanimations', method=["GET", "POST"] )
@action.uses(Template('ui-elements-animations.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXanimations(id=None):
    ctrl_info= "ctrl: uiXelementsXanimations, view: ui-elements-animations.html"
    messages = []

    dfuiXelementsXanimations0_row= None
    id_dfuiXelementsXanimations0 = None
    fuiXelementsXanimations0= Form(db.dfuiXelementsXanimations0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXanimations0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXanimations0.accepted:

        Glb['debug'] and print("     fuiXelementsXanimations0 accepted with: %s " % (fuiXelementsXanimations0.vars))
        fuiXelementsXanimations0_f0 = fuiXelementsXanimations0.vars.get('f0','')
        if len ( fuiXelementsXanimations0_f0 ):
            id_dfuiXelementsXanimations0 = db.dfuiXelementsXanimations0.insert( **fuiXelementsXanimations0.vars )
            db.commit()

            if not id_dfuiXelementsXanimations0 is None:
                dfuiXelementsXanimations0_row = db.dfuiXelementsXanimations0(id_dfuiXelementsXanimations0 )

                if not dfuiXelementsXanimations0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXanimations0.vars.f0}\" into db.dfuiXelementsXanimations0.f0, id = {id_dfuiXelementsXanimations0}' )
                         print(f"     found db.dfuiXelementsXanimations0.f0: \"{dfuiXelementsXanimations0_row.f0}\", id = {id_dfuiXelementsXanimations0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXanimations0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXanimations0.vars.items() ]
                print()
   
    elif fuiXelementsXanimations0.errors:
        print("fuiXelementsXanimations0 has errors: %s " % (fuiXelementsXanimations0.errors))
 

    return locals()


@action('uiXelementsXtypography', method=["GET", "POST"] )
@action.uses(Template('ui-elements-typography.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXtypography(id=None):
    ctrl_info= "ctrl: uiXelementsXtypography, view: ui-elements-typography.html"
    messages = []

    dfuiXelementsXtypography0_row= None
    id_dfuiXelementsXtypography0 = None
    fuiXelementsXtypography0= Form(db.dfuiXelementsXtypography0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXtypography0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXtypography0.accepted:

        Glb['debug'] and print("     fuiXelementsXtypography0 accepted with: %s " % (fuiXelementsXtypography0.vars))
        fuiXelementsXtypography0_f0 = fuiXelementsXtypography0.vars.get('f0','')
        if len ( fuiXelementsXtypography0_f0 ):
            id_dfuiXelementsXtypography0 = db.dfuiXelementsXtypography0.insert( **fuiXelementsXtypography0.vars )
            db.commit()

            if not id_dfuiXelementsXtypography0 is None:
                dfuiXelementsXtypography0_row = db.dfuiXelementsXtypography0(id_dfuiXelementsXtypography0 )

                if not dfuiXelementsXtypography0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXtypography0.vars.f0}\" into db.dfuiXelementsXtypography0.f0, id = {id_dfuiXelementsXtypography0}' )
                         print(f"     found db.dfuiXelementsXtypography0.f0: \"{dfuiXelementsXtypography0_row.f0}\", id = {id_dfuiXelementsXtypography0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXtypography0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXtypography0.vars.items() ]
                print()
   
    elif fuiXelementsXtypography0.errors:
        print("fuiXelementsXtypography0 has errors: %s " % (fuiXelementsXtypography0.errors))
 

    return locals()


@action('uiXelementsXaccordions', method=["GET", "POST"] )
@action.uses(Template('ui-elements-accordions.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXaccordions(id=None):
    ctrl_info= "ctrl: uiXelementsXaccordions, view: ui-elements-accordions.html"
    messages = []

    dfuiXelementsXaccordions0_row= None
    id_dfuiXelementsXaccordions0 = None
    fuiXelementsXaccordions0= Form(db.dfuiXelementsXaccordions0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXaccordions0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXaccordions0.accepted:

        Glb['debug'] and print("     fuiXelementsXaccordions0 accepted with: %s " % (fuiXelementsXaccordions0.vars))
        fuiXelementsXaccordions0_f0 = fuiXelementsXaccordions0.vars.get('f0','')
        if len ( fuiXelementsXaccordions0_f0 ):
            id_dfuiXelementsXaccordions0 = db.dfuiXelementsXaccordions0.insert( **fuiXelementsXaccordions0.vars )
            db.commit()

            if not id_dfuiXelementsXaccordions0 is None:
                dfuiXelementsXaccordions0_row = db.dfuiXelementsXaccordions0(id_dfuiXelementsXaccordions0 )

                if not dfuiXelementsXaccordions0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXaccordions0.vars.f0}\" into db.dfuiXelementsXaccordions0.f0, id = {id_dfuiXelementsXaccordions0}' )
                         print(f"     found db.dfuiXelementsXaccordions0.f0: \"{dfuiXelementsXaccordions0_row.f0}\", id = {id_dfuiXelementsXaccordions0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXaccordions0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXaccordions0.vars.items() ]
                print()
   
    elif fuiXelementsXaccordions0.errors:
        print("fuiXelementsXaccordions0 has errors: %s " % (fuiXelementsXaccordions0.errors))
 

    return locals()


@action('pagesXrecoverXpassword', method=["GET", "POST"] )
@action.uses(Template('pages-recover-password.html', delimiters='[%[ ]]',), db, session,  T, )

def pagesXrecoverXpassword(id=None):
    ctrl_info= "ctrl: pagesXrecoverXpassword, view: pages-recover-password.html"
    messages = []

    dfpagesXrecoverXpassword0_row= None
    id_dfpagesXrecoverXpassword0 = None
    fpagesXrecoverXpassword0= Form(db.dfpagesXrecoverXpassword0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpagesXrecoverXpassword0",  formstyle=FormStyleBulma )
   
    if fpagesXrecoverXpassword0.accepted:

        Glb['debug'] and print("     fpagesXrecoverXpassword0 accepted with: %s " % (fpagesXrecoverXpassword0.vars))
        fpagesXrecoverXpassword0_f0 = fpagesXrecoverXpassword0.vars.get('f0','')
        if len ( fpagesXrecoverXpassword0_f0 ):
            id_dfpagesXrecoverXpassword0 = db.dfpagesXrecoverXpassword0.insert( **fpagesXrecoverXpassword0.vars )
            db.commit()

            if not id_dfpagesXrecoverXpassword0 is None:
                dfpagesXrecoverXpassword0_row = db.dfpagesXrecoverXpassword0(id_dfpagesXrecoverXpassword0 )

                if not dfpagesXrecoverXpassword0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpagesXrecoverXpassword0.vars.f0}\" into db.dfpagesXrecoverXpassword0.f0, id = {id_dfpagesXrecoverXpassword0}' )
                         print(f"     found db.dfpagesXrecoverXpassword0.f0: \"{dfpagesXrecoverXpassword0_row.f0}\", id = {id_dfpagesXrecoverXpassword0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpagesXrecoverXpassword0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpagesXrecoverXpassword0.vars.items() ]
                print()
   
    elif fpagesXrecoverXpassword0.errors:
        print("fpagesXrecoverXpassword0 has errors: %s " % (fpagesXrecoverXpassword0.errors))
 

    return locals()


@action('layoutsXmenuXcollapsed', method=["GET", "POST"] )
@action.uses(Template('layouts-menu-collapsed.html', delimiters='[%[ ]]',), db, session,  T, )

def layoutsXmenuXcollapsed(id=None):
    ctrl_info= "ctrl: layoutsXmenuXcollapsed, view: layouts-menu-collapsed.html"
    messages = []

    dflayoutsXmenuXcollapsed0_row= None
    id_dflayoutsXmenuXcollapsed0 = None
    flayoutsXmenuXcollapsed0= Form(db.dflayoutsXmenuXcollapsed0, id, deletable=False, dbio = False, keep_values = False, form_name = "flayoutsXmenuXcollapsed0",  formstyle=FormStyleBulma )
   
    if flayoutsXmenuXcollapsed0.accepted:

        Glb['debug'] and print("     flayoutsXmenuXcollapsed0 accepted with: %s " % (flayoutsXmenuXcollapsed0.vars))
        flayoutsXmenuXcollapsed0_f0 = flayoutsXmenuXcollapsed0.vars.get('f0','')
        if len ( flayoutsXmenuXcollapsed0_f0 ):
            id_dflayoutsXmenuXcollapsed0 = db.dflayoutsXmenuXcollapsed0.insert( **flayoutsXmenuXcollapsed0.vars )
            db.commit()

            if not id_dflayoutsXmenuXcollapsed0 is None:
                dflayoutsXmenuXcollapsed0_row = db.dflayoutsXmenuXcollapsed0(id_dflayoutsXmenuXcollapsed0 )

                if not dflayoutsXmenuXcollapsed0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flayoutsXmenuXcollapsed0.vars.f0}\" into db.dflayoutsXmenuXcollapsed0.f0, id = {id_dflayoutsXmenuXcollapsed0}' )
                         print(f"     found db.dflayoutsXmenuXcollapsed0.f0: \"{dflayoutsXmenuXcollapsed0_row.f0}\", id = {id_dflayoutsXmenuXcollapsed0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(flayoutsXmenuXcollapsed0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in flayoutsXmenuXcollapsed0.vars.items() ]
                print()
   
    elif flayoutsXmenuXcollapsed0.errors:
        print("flayoutsXmenuXcollapsed0 has errors: %s " % (flayoutsXmenuXcollapsed0.errors))
 

    return locals()


@action('uiXelementsXmodalsXajax', method=["GET", "POST"] )
@action.uses(Template('ui-elements-modals-ajax.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXmodalsXajax(id=None):
    ctrl_info= "ctrl: uiXelementsXmodalsXajax, view: ui-elements-modals-ajax.html"
    messages = []

    return locals()


@action('uiXelementsXgridXsystem', method=["GET", "POST"] )
@action.uses(Template('ui-elements-grid-system.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXgridXsystem(id=None):
    ctrl_info= "ctrl: uiXelementsXgridXsystem, view: ui-elements-grid-system.html"
    messages = []

    dfuiXelementsXgridXsystem0_row= None
    id_dfuiXelementsXgridXsystem0 = None
    fuiXelementsXgridXsystem0= Form(db.dfuiXelementsXgridXsystem0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXgridXsystem0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXgridXsystem0.accepted:

        Glb['debug'] and print("     fuiXelementsXgridXsystem0 accepted with: %s " % (fuiXelementsXgridXsystem0.vars))
        fuiXelementsXgridXsystem0_f0 = fuiXelementsXgridXsystem0.vars.get('f0','')
        if len ( fuiXelementsXgridXsystem0_f0 ):
            id_dfuiXelementsXgridXsystem0 = db.dfuiXelementsXgridXsystem0.insert( **fuiXelementsXgridXsystem0.vars )
            db.commit()

            if not id_dfuiXelementsXgridXsystem0 is None:
                dfuiXelementsXgridXsystem0_row = db.dfuiXelementsXgridXsystem0(id_dfuiXelementsXgridXsystem0 )

                if not dfuiXelementsXgridXsystem0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXgridXsystem0.vars.f0}\" into db.dfuiXelementsXgridXsystem0.f0, id = {id_dfuiXelementsXgridXsystem0}' )
                         print(f"     found db.dfuiXelementsXgridXsystem0.f0: \"{dfuiXelementsXgridXsystem0_row.f0}\", id = {id_dfuiXelementsXgridXsystem0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXgridXsystem0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXgridXsystem0.vars.items() ]
                print()
   
    elif fuiXelementsXgridXsystem0.errors:
        print("fuiXelementsXgridXsystem0 has errors: %s " % (fuiXelementsXgridXsystem0.errors))
 

    return locals()


@action('uiXelementsXprogressbars', method=["GET", "POST"] )
@action.uses(Template('ui-elements-progressbars.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXprogressbars(id=None):
    ctrl_info= "ctrl: uiXelementsXprogressbars, view: ui-elements-progressbars.html"
    messages = []

    dfuiXelementsXprogressbars0_row= None
    id_dfuiXelementsXprogressbars0 = None
    fuiXelementsXprogressbars0= Form(db.dfuiXelementsXprogressbars0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXprogressbars0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXprogressbars0.accepted:

        Glb['debug'] and print("     fuiXelementsXprogressbars0 accepted with: %s " % (fuiXelementsXprogressbars0.vars))
        fuiXelementsXprogressbars0_f0 = fuiXelementsXprogressbars0.vars.get('f0','')
        if len ( fuiXelementsXprogressbars0_f0 ):
            id_dfuiXelementsXprogressbars0 = db.dfuiXelementsXprogressbars0.insert( **fuiXelementsXprogressbars0.vars )
            db.commit()

            if not id_dfuiXelementsXprogressbars0 is None:
                dfuiXelementsXprogressbars0_row = db.dfuiXelementsXprogressbars0(id_dfuiXelementsXprogressbars0 )

                if not dfuiXelementsXprogressbars0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXprogressbars0.vars.f0}\" into db.dfuiXelementsXprogressbars0.f0, id = {id_dfuiXelementsXprogressbars0}' )
                         print(f"     found db.dfuiXelementsXprogressbars0.f0: \"{dfuiXelementsXprogressbars0_row.f0}\", id = {id_dfuiXelementsXprogressbars0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXprogressbars0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXprogressbars0.vars.items() ]
                print()
   
    elif fuiXelementsXprogressbars0.errors:
        print("fuiXelementsXprogressbars0 has errors: %s " % (fuiXelementsXprogressbars0.errors))
 

    return locals()


@action('mapsXgoogleXmapsXbuilder', method=["GET", "POST"] )
@action.uses(Template('maps-google-maps-builder.html', delimiters='[%[ ]]',), db, session,  T, )

def mapsXgoogleXmapsXbuilder(id=None):
    ctrl_info= "ctrl: mapsXgoogleXmapsXbuilder, view: maps-google-maps-builder.html"
    messages = []

    dfmapsXgoogleXmapsXbuilder0_row= None
    id_dfmapsXgoogleXmapsXbuilder0 = None
    fmapsXgoogleXmapsXbuilder0= Form(db.dfmapsXgoogleXmapsXbuilder0, id, deletable=False, dbio = False, keep_values = False, form_name = "fmapsXgoogleXmapsXbuilder0",  formstyle=FormStyleBulma )
   
    if fmapsXgoogleXmapsXbuilder0.accepted:

        Glb['debug'] and print("     fmapsXgoogleXmapsXbuilder0 accepted with: %s " % (fmapsXgoogleXmapsXbuilder0.vars))
        fmapsXgoogleXmapsXbuilder0_f0 = fmapsXgoogleXmapsXbuilder0.vars.get('f0','')
        if len ( fmapsXgoogleXmapsXbuilder0_f0 ):
            id_dfmapsXgoogleXmapsXbuilder0 = db.dfmapsXgoogleXmapsXbuilder0.insert( **fmapsXgoogleXmapsXbuilder0.vars )
            db.commit()

            if not id_dfmapsXgoogleXmapsXbuilder0 is None:
                dfmapsXgoogleXmapsXbuilder0_row = db.dfmapsXgoogleXmapsXbuilder0(id_dfmapsXgoogleXmapsXbuilder0 )

                if not dfmapsXgoogleXmapsXbuilder0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmapsXgoogleXmapsXbuilder0.vars.f0}\" into db.dfmapsXgoogleXmapsXbuilder0.f0, id = {id_dfmapsXgoogleXmapsXbuilder0}' )
                         print(f"     found db.dfmapsXgoogleXmapsXbuilder0.f0: \"{dfmapsXgoogleXmapsXbuilder0_row.f0}\", id = {id_dfmapsXgoogleXmapsXbuilder0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmapsXgoogleXmapsXbuilder0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmapsXgoogleXmapsXbuilder0.vars.items() ]
                print()
   
    elif fmapsXgoogleXmapsXbuilder0.errors:
        print("fmapsXgoogleXmapsXbuilder0 has errors: %s " % (fmapsXgoogleXmapsXbuilder0.errors))
 

    dfmapsXgoogleXmapsXbuilder1_row= None
    id_dfmapsXgoogleXmapsXbuilder1 = None
    fmapsXgoogleXmapsXbuilder1= Form(db.dfmapsXgoogleXmapsXbuilder1, id, deletable=False, dbio = False, keep_values = False, form_name = "fmapsXgoogleXmapsXbuilder1",  formstyle=FormStyleBulma )
   
    if fmapsXgoogleXmapsXbuilder1.accepted:

        Glb['debug'] and print("     fmapsXgoogleXmapsXbuilder1 accepted with: %s " % (fmapsXgoogleXmapsXbuilder1.vars))
        fmapsXgoogleXmapsXbuilder1_f0 = fmapsXgoogleXmapsXbuilder1.vars.get('f0','')
        if len ( fmapsXgoogleXmapsXbuilder1_f0 ):
            id_dfmapsXgoogleXmapsXbuilder1 = db.dfmapsXgoogleXmapsXbuilder1.insert( **fmapsXgoogleXmapsXbuilder1.vars )
            db.commit()

            if not id_dfmapsXgoogleXmapsXbuilder1 is None:
                dfmapsXgoogleXmapsXbuilder1_row = db.dfmapsXgoogleXmapsXbuilder1(id_dfmapsXgoogleXmapsXbuilder1 )

                if not dfmapsXgoogleXmapsXbuilder1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmapsXgoogleXmapsXbuilder1.vars.f0}\" into db.dfmapsXgoogleXmapsXbuilder1.f0, id = {id_dfmapsXgoogleXmapsXbuilder1}' )
                         print(f"     found db.dfmapsXgoogleXmapsXbuilder1.f0: \"{dfmapsXgoogleXmapsXbuilder1_row.f0}\", id = {id_dfmapsXgoogleXmapsXbuilder1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmapsXgoogleXmapsXbuilder1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmapsXgoogleXmapsXbuilder1.vars.items() ]
                print()
   
    elif fmapsXgoogleXmapsXbuilder1.errors:
        print("fmapsXgoogleXmapsXbuilder1 has errors: %s " % (fmapsXgoogleXmapsXbuilder1.errors))
 

    return locals()


@action('uiXelementsXlightboxXajax', method=["GET", "POST"] )
@action.uses(Template('ui-elements-lightbox-ajax.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXlightboxXajax(id=None):
    ctrl_info= "ctrl: uiXelementsXlightboxXajax, view: ui-elements-lightbox-ajax.html"
    messages = []

    return locals()


@action('uiXelementsXnotifications', method=["GET", "POST"] )
@action.uses(Template('ui-elements-notifications.html', delimiters='[%[ ]]',), db, session,  T, )

def uiXelementsXnotifications(id=None):
    ctrl_info= "ctrl: uiXelementsXnotifications, view: ui-elements-notifications.html"
    messages = []

    dfuiXelementsXnotifications0_row= None
    id_dfuiXelementsXnotifications0 = None
    fuiXelementsXnotifications0= Form(db.dfuiXelementsXnotifications0, id, deletable=False, dbio = False, keep_values = False, form_name = "fuiXelementsXnotifications0",  formstyle=FormStyleBulma )
   
    if fuiXelementsXnotifications0.accepted:

        Glb['debug'] and print("     fuiXelementsXnotifications0 accepted with: %s " % (fuiXelementsXnotifications0.vars))
        fuiXelementsXnotifications0_f0 = fuiXelementsXnotifications0.vars.get('f0','')
        if len ( fuiXelementsXnotifications0_f0 ):
            id_dfuiXelementsXnotifications0 = db.dfuiXelementsXnotifications0.insert( **fuiXelementsXnotifications0.vars )
            db.commit()

            if not id_dfuiXelementsXnotifications0 is None:
                dfuiXelementsXnotifications0_row = db.dfuiXelementsXnotifications0(id_dfuiXelementsXnotifications0 )

                if not dfuiXelementsXnotifications0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fuiXelementsXnotifications0.vars.f0}\" into db.dfuiXelementsXnotifications0.f0, id = {id_dfuiXelementsXnotifications0}' )
                         print(f"     found db.dfuiXelementsXnotifications0.f0: \"{dfuiXelementsXnotifications0_row.f0}\", id = {id_dfuiXelementsXnotifications0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fuiXelementsXnotifications0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fuiXelementsXnotifications0.vars.items() ]
                print()
   
    elif fuiXelementsXnotifications0.errors:
        print("fuiXelementsXnotifications0 has errors: %s " % (fuiXelementsXnotifications0.errors))
 

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
# curl -X  GET   http://localhost:8000/octopus/api/test_table/
# curl -X  GET   http://localhost:8000/octopus/api/test_table/9
# curl -X DELETE  http://localhost:8000/octopus/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/octopus/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/octopus/api/test_table/9
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/octopus/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/octopus/api/test_table/
#  http         localhost:8000/octopus/api/test_table/9
#  http -f POST localhost:8000/octopus/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/octopus/api/test_table/2
#  http -f PUT localhost:8000/octopus/api/test_table/2 f0=111111 f1=2222222 f2=333333


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
        debug_mess.append(f"     goto_new_path: {location}\\n")
        print("\\n".join(debug_mess))

    bottle.response.status = 303
    bottle.response.set_header("Location", location)

