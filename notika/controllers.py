#!/usr/bin/env python3

#
# py4web app, AI-biorex ported 27.10.2020 12:50:51
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


Glb= {'debug': True , 'my_app_name': "notika", 'tte_path': '/static/tte' }



@action('X404', method=["GET", "POST"] )
@action.uses(Template('404.html', delimiters='[%[ ]]',), db, session,  T, )

def X404(id=None):
    ctrl_info= "ctrl: X404, view: 404.html"
    messages = []

    return locals()


@action('tabs', method=["GET", "POST"] )
@action.uses(Template('tabs.html', delimiters='[%[ ]]',), db, session,  T, )

def tabs(id=None):
    ctrl_info= "ctrl: tabs, view: tabs.html"
    messages = []

    dftabs0_row= None
    id_dftabs0 = None
    ftabs0= Form(db.dftabs0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftabs0",  formstyle=FormStyleBulma )
   
    if ftabs0.accepted:

        Glb['debug'] and print("     ftabs0 accepted with: %s " % (ftabs0.vars))
        ftabs0_f0 = ftabs0.vars.get('f0','')
        if len ( ftabs0_f0 ):
            id_dftabs0 = db.dftabs0.insert( **ftabs0.vars )
            db.commit()

            if not id_dftabs0 is None:
                dftabs0_row = db.dftabs0(id_dftabs0 )

                if not dftabs0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftabs0.vars.f0}\" into db.dftabs0.f0, id = {id_dftabs0}' )
                         print(f"     found db.dftabs0.f0: \"{dftabs0_row.f0}\", id = {id_dftabs0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftabs0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftabs0.vars.items() ]
                print()
   
    elif ftabs0.errors:
        print("ftabs0 has errors: %s " % (ftabs0.errors))
 

    dftabs1_row= None
    id_dftabs1 = None
    ftabs1= Form(db.dftabs1, id, deletable=False, dbio = False, keep_values = False, form_name = "ftabs1",  formstyle=FormStyleBulma )
   
    if ftabs1.accepted:

        Glb['debug'] and print("     ftabs1 accepted with: %s " % (ftabs1.vars))
        ftabs1_f0 = ftabs1.vars.get('f0','')
        if len ( ftabs1_f0 ):
            id_dftabs1 = db.dftabs1.insert( **ftabs1.vars )
            db.commit()

            if not id_dftabs1 is None:
                dftabs1_row = db.dftabs1(id_dftabs1 )

                if not dftabs1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftabs1.vars.f0}\" into db.dftabs1.f0, id = {id_dftabs1}' )
                         print(f"     found db.dftabs1.f0: \"{dftabs1_row.f0}\", id = {id_dftabs1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftabs1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftabs1.vars.items() ]
                print()
   
    elif ftabs1.errors:
        print("ftabs1 has errors: %s " % (ftabs1.errors))
 

    return locals()


@action('inbox', method=["GET", "POST"] )
@action.uses(Template('inbox.html', delimiters='[%[ ]]',), db, session,  T, )

def inbox(id=None):
    ctrl_info= "ctrl: inbox, view: inbox.html"
    messages = []

    rows_tinbox0= db(db.tinbox0).select()
    dfinbox0_row= None
    id_dfinbox0 = None
    finbox0= Form(db.dfinbox0, id, deletable=False, dbio = False, keep_values = False, form_name = "finbox0",  formstyle=FormStyleBulma )
   
    if finbox0.accepted:

        Glb['debug'] and print("     finbox0 accepted with: %s " % (finbox0.vars))
        finbox0_f0 = finbox0.vars.get('f0','')
        if len ( finbox0_f0 ):
            id_dfinbox0 = db.dfinbox0.insert( **finbox0.vars )
            db.commit()

            if not id_dfinbox0 is None:
                dfinbox0_row = db.dfinbox0(id_dfinbox0 )

                if not dfinbox0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finbox0.vars.f0}\" into db.dfinbox0.f0, id = {id_dfinbox0}' )
                         print(f"     found db.dfinbox0.f0: \"{dfinbox0_row.f0}\", id = {id_dfinbox0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finbox0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finbox0.vars.items() ]
                print()
   
    elif finbox0.errors:
        print("finbox0 has errors: %s " % (finbox0.errors))
 

    dfinbox1_row= None
    id_dfinbox1 = None
    finbox1= Form(db.dfinbox1, id, deletable=False, dbio = False, keep_values = False, form_name = "finbox1",  formstyle=FormStyleBulma )
   
    if finbox1.accepted:

        Glb['debug'] and print("     finbox1 accepted with: %s " % (finbox1.vars))
        finbox1_f0 = finbox1.vars.get('f0','')
        if len ( finbox1_f0 ):
            id_dfinbox1 = db.dfinbox1.insert( **finbox1.vars )
            db.commit()

            if not id_dfinbox1 is None:
                dfinbox1_row = db.dfinbox1(id_dfinbox1 )

                if not dfinbox1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finbox1.vars.f0}\" into db.dfinbox1.f0, id = {id_dfinbox1}' )
                         print(f"     found db.dfinbox1.f0: \"{dfinbox1_row.f0}\", id = {id_dfinbox1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finbox1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finbox1.vars.items() ]
                print()
   
    elif finbox1.errors:
        print("finbox1 has errors: %s " % (finbox1.errors))
 

    dfinbox2_row= None
    id_dfinbox2 = None
    finbox2= Form(db.dfinbox2, id, deletable=False, dbio = False, keep_values = False, form_name = "finbox2",  formstyle=FormStyleBulma )
   
    if finbox2.accepted:

        Glb['debug'] and print("     finbox2 accepted with: %s " % (finbox2.vars))
        finbox2_f0 = finbox2.vars.get('f0','')
        if len ( finbox2_f0 ):
            id_dfinbox2 = db.dfinbox2.insert( **finbox2.vars )
            db.commit()

            if not id_dfinbox2 is None:
                dfinbox2_row = db.dfinbox2(id_dfinbox2 )

                if not dfinbox2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finbox2.vars.f0}\" into db.dfinbox2.f0, id = {id_dfinbox2}' )
                         print(f"     found db.dfinbox2.f0: \"{dfinbox2_row.f0}\", id = {id_dfinbox2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finbox2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finbox2.vars.items() ]
                print()
   
    elif finbox2.errors:
        print("finbox2 has errors: %s " % (finbox2.errors))
 

    dfinbox3_row= None
    id_dfinbox3 = None
    finbox3= Form(db.dfinbox3, id, deletable=False, dbio = False, keep_values = False, form_name = "finbox3",  formstyle=FormStyleBulma )
   
    if finbox3.accepted:

        Glb['debug'] and print("     finbox3 accepted with: %s " % (finbox3.vars))
        finbox3_f0 = finbox3.vars.get('f0','')
        if len ( finbox3_f0 ):
            id_dfinbox3 = db.dfinbox3.insert( **finbox3.vars )
            db.commit()

            if not id_dfinbox3 is None:
                dfinbox3_row = db.dfinbox3(id_dfinbox3 )

                if not dfinbox3_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finbox3.vars.f0}\" into db.dfinbox3.f0, id = {id_dfinbox3}' )
                         print(f"     found db.dfinbox3.f0: \"{dfinbox3_row.f0}\", id = {id_dfinbox3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finbox3_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finbox3.vars.items() ]
                print()
   
    elif finbox3.errors:
        print("finbox3 has errors: %s " % (finbox3.errors))
 

    dfinbox4_row= None
    id_dfinbox4 = None
    finbox4= Form(db.dfinbox4, id, deletable=False, dbio = False, keep_values = False, form_name = "finbox4",  formstyle=FormStyleBulma )
   
    if finbox4.accepted:

        Glb['debug'] and print("     finbox4 accepted with: %s " % (finbox4.vars))
        finbox4_f0 = finbox4.vars.get('f0','')
        if len ( finbox4_f0 ):
            id_dfinbox4 = db.dfinbox4.insert( **finbox4.vars )
            db.commit()

            if not id_dfinbox4 is None:
                dfinbox4_row = db.dfinbox4(id_dfinbox4 )

                if not dfinbox4_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finbox4.vars.f0}\" into db.dfinbox4.f0, id = {id_dfinbox4}' )
                         print(f"     found db.dfinbox4.f0: \"{dfinbox4_row.f0}\", id = {id_dfinbox4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finbox4_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finbox4.vars.items() ]
                print()
   
    elif finbox4.errors:
        print("finbox4 has errors: %s " % (finbox4.errors))
 

    dfinbox5_row= None
    id_dfinbox5 = None
    finbox5= Form(db.dfinbox5, id, deletable=False, dbio = False, keep_values = False, form_name = "finbox5",  formstyle=FormStyleBulma )
   
    if finbox5.accepted:

        Glb['debug'] and print("     finbox5 accepted with: %s " % (finbox5.vars))
        finbox5_f0 = finbox5.vars.get('f0','')
        if len ( finbox5_f0 ):
            id_dfinbox5 = db.dfinbox5.insert( **finbox5.vars )
            db.commit()

            if not id_dfinbox5 is None:
                dfinbox5_row = db.dfinbox5(id_dfinbox5 )

                if not dfinbox5_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finbox5.vars.f0}\" into db.dfinbox5.f0, id = {id_dfinbox5}' )
                         print(f"     found db.dfinbox5.f0: \"{dfinbox5_row.f0}\", id = {id_dfinbox5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finbox5_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finbox5.vars.items() ]
                print()
   
    elif finbox5.errors:
        print("finbox5 has errors: %s " % (finbox5.errors))
 

    dfinbox6_row= None
    id_dfinbox6 = None
    finbox6= Form(db.dfinbox6, id, deletable=False, dbio = False, keep_values = False, form_name = "finbox6",  formstyle=FormStyleBulma )
   
    if finbox6.accepted:

        Glb['debug'] and print("     finbox6 accepted with: %s " % (finbox6.vars))
        finbox6_f0 = finbox6.vars.get('f0','')
        if len ( finbox6_f0 ):
            id_dfinbox6 = db.dfinbox6.insert( **finbox6.vars )
            db.commit()

            if not id_dfinbox6 is None:
                dfinbox6_row = db.dfinbox6(id_dfinbox6 )

                if not dfinbox6_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finbox6.vars.f0}\" into db.dfinbox6.f0, id = {id_dfinbox6}' )
                         print(f"     found db.dfinbox6.f0: \"{dfinbox6_row.f0}\", id = {id_dfinbox6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finbox6_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finbox6.vars.items() ]
                print()
   
    elif finbox6.errors:
        print("finbox6 has errors: %s " % (finbox6.errors))
 

    dfinbox7_row= None
    id_dfinbox7 = None
    finbox7= Form(db.dfinbox7, id, deletable=False, dbio = False, keep_values = False, form_name = "finbox7",  formstyle=FormStyleBulma )
   
    if finbox7.accepted:

        Glb['debug'] and print("     finbox7 accepted with: %s " % (finbox7.vars))
        finbox7_f0 = finbox7.vars.get('f0','')
        if len ( finbox7_f0 ):
            id_dfinbox7 = db.dfinbox7.insert( **finbox7.vars )
            db.commit()

            if not id_dfinbox7 is None:
                dfinbox7_row = db.dfinbox7(id_dfinbox7 )

                if not dfinbox7_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finbox7.vars.f0}\" into db.dfinbox7.f0, id = {id_dfinbox7}' )
                         print(f"     found db.dfinbox7.f0: \"{dfinbox7_row.f0}\", id = {id_dfinbox7}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finbox7_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finbox7.vars.items() ]
                print()
   
    elif finbox7.errors:
        print("finbox7 has errors: %s " % (finbox7.errors))
 

    dfinbox8_row= None
    id_dfinbox8 = None
    finbox8= Form(db.dfinbox8, id, deletable=False, dbio = False, keep_values = False, form_name = "finbox8",  formstyle=FormStyleBulma )
   
    if finbox8.accepted:

        Glb['debug'] and print("     finbox8 accepted with: %s " % (finbox8.vars))
        finbox8_f0 = finbox8.vars.get('f0','')
        if len ( finbox8_f0 ):
            id_dfinbox8 = db.dfinbox8.insert( **finbox8.vars )
            db.commit()

            if not id_dfinbox8 is None:
                dfinbox8_row = db.dfinbox8(id_dfinbox8 )

                if not dfinbox8_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finbox8.vars.f0}\" into db.dfinbox8.f0, id = {id_dfinbox8}' )
                         print(f"     found db.dfinbox8.f0: \"{dfinbox8_row.f0}\", id = {id_dfinbox8}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finbox8_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finbox8.vars.items() ]
                print()
   
    elif finbox8.errors:
        print("finbox8 has errors: %s " % (finbox8.errors))
 

    dfinbox9_row= None
    id_dfinbox9 = None
    finbox9= Form(db.dfinbox9, id, deletable=False, dbio = False, keep_values = False, form_name = "finbox9",  formstyle=FormStyleBulma )
   
    if finbox9.accepted:

        Glb['debug'] and print("     finbox9 accepted with: %s " % (finbox9.vars))
        finbox9_f0 = finbox9.vars.get('f0','')
        if len ( finbox9_f0 ):
            id_dfinbox9 = db.dfinbox9.insert( **finbox9.vars )
            db.commit()

            if not id_dfinbox9 is None:
                dfinbox9_row = db.dfinbox9(id_dfinbox9 )

                if not dfinbox9_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finbox9.vars.f0}\" into db.dfinbox9.f0, id = {id_dfinbox9}' )
                         print(f"     found db.dfinbox9.f0: \"{dfinbox9_row.f0}\", id = {id_dfinbox9}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finbox9_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finbox9.vars.items() ]
                print()
   
    elif finbox9.errors:
        print("finbox9 has errors: %s " % (finbox9.errors))
 

    dfinbox10_row= None
    id_dfinbox10 = None
    finbox10= Form(db.dfinbox10, id, deletable=False, dbio = False, keep_values = False, form_name = "finbox10",  formstyle=FormStyleBulma )
   
    if finbox10.accepted:

        Glb['debug'] and print("     finbox10 accepted with: %s " % (finbox10.vars))
        finbox10_f0 = finbox10.vars.get('f0','')
        if len ( finbox10_f0 ):
            id_dfinbox10 = db.dfinbox10.insert( **finbox10.vars )
            db.commit()

            if not id_dfinbox10 is None:
                dfinbox10_row = db.dfinbox10(id_dfinbox10 )

                if not dfinbox10_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finbox10.vars.f0}\" into db.dfinbox10.f0, id = {id_dfinbox10}' )
                         print(f"     found db.dfinbox10.f0: \"{dfinbox10_row.f0}\", id = {id_dfinbox10}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finbox10_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finbox10.vars.items() ]
                print()
   
    elif finbox10.errors:
        print("finbox10 has errors: %s " % (finbox10.errors))
 

    return locals()


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
 

    dfindex2_row= None
    id_dfindex2 = None
    findex2= Form(db.dfindex2, id, deletable=False, dbio = False, keep_values = False, form_name = "findex2",  formstyle=FormStyleBulma )
   
    if findex2.accepted:

        Glb['debug'] and print("     findex2 accepted with: %s " % (findex2.vars))
        findex2_f0 = findex2.vars.get('f0','')
        if len ( findex2_f0 ):
            id_dfindex2 = db.dfindex2.insert( **findex2.vars )
            db.commit()

            if not id_dfindex2 is None:
                dfindex2_row = db.dfindex2(id_dfindex2 )

                if not dfindex2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex2.vars.f0}\" into db.dfindex2.f0, id = {id_dfindex2}' )
                         print(f"     found db.dfindex2.f0: \"{dfindex2_row.f0}\", id = {id_dfindex2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findex2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findex2.vars.items() ]
                print()
   
    elif findex2.errors:
        print("findex2 has errors: %s " % (findex2.errors))
 

    dfindex3_row= None
    id_dfindex3 = None
    findex3= Form(db.dfindex3, id, deletable=False, dbio = False, keep_values = False, form_name = "findex3",  formstyle=FormStyleBulma )
   
    if findex3.accepted:

        Glb['debug'] and print("     findex3 accepted with: %s " % (findex3.vars))
        findex3_f0 = findex3.vars.get('f0','')
        if len ( findex3_f0 ):
            id_dfindex3 = db.dfindex3.insert( **findex3.vars )
            db.commit()

            if not id_dfindex3 is None:
                dfindex3_row = db.dfindex3(id_dfindex3 )

                if not dfindex3_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex3.vars.f0}\" into db.dfindex3.f0, id = {id_dfindex3}' )
                         print(f"     found db.dfindex3.f0: \"{dfindex3_row.f0}\", id = {id_dfindex3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findex3_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findex3.vars.items() ]
                print()
   
    elif findex3.errors:
        print("findex3 has errors: %s " % (findex3.errors))
 

    dfindex4_row= None
    id_dfindex4 = None
    findex4= Form(db.dfindex4, id, deletable=False, dbio = False, keep_values = False, form_name = "findex4",  formstyle=FormStyleBulma )
   
    if findex4.accepted:

        Glb['debug'] and print("     findex4 accepted with: %s " % (findex4.vars))
        findex4_f0 = findex4.vars.get('f0','')
        if len ( findex4_f0 ):
            id_dfindex4 = db.dfindex4.insert( **findex4.vars )
            db.commit()

            if not id_dfindex4 is None:
                dfindex4_row = db.dfindex4(id_dfindex4 )

                if not dfindex4_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex4.vars.f0}\" into db.dfindex4.f0, id = {id_dfindex4}' )
                         print(f"     found db.dfindex4.f0: \"{dfindex4_row.f0}\", id = {id_dfindex4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findex4_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findex4.vars.items() ]
                print()
   
    elif findex4.errors:
        print("findex4 has errors: %s " % (findex4.errors))
 

    dfindex5_row= None
    id_dfindex5 = None
    findex5= Form(db.dfindex5, id, deletable=False, dbio = False, keep_values = False, form_name = "findex5",  formstyle=FormStyleBulma )
   
    if findex5.accepted:

        Glb['debug'] and print("     findex5 accepted with: %s " % (findex5.vars))
        findex5_f0 = findex5.vars.get('f0','')
        if len ( findex5_f0 ):
            id_dfindex5 = db.dfindex5.insert( **findex5.vars )
            db.commit()

            if not id_dfindex5 is None:
                dfindex5_row = db.dfindex5(id_dfindex5 )

                if not dfindex5_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex5.vars.f0}\" into db.dfindex5.f0, id = {id_dfindex5}' )
                         print(f"     found db.dfindex5.f0: \"{dfindex5_row.f0}\", id = {id_dfindex5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findex5_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findex5.vars.items() ]
                print()
   
    elif findex5.errors:
        print("findex5 has errors: %s " % (findex5.errors))
 

    dfindex6_row= None
    id_dfindex6 = None
    findex6= Form(db.dfindex6, id, deletable=False, dbio = False, keep_values = False, form_name = "findex6",  formstyle=FormStyleBulma )
   
    if findex6.accepted:

        Glb['debug'] and print("     findex6 accepted with: %s " % (findex6.vars))
        findex6_f0 = findex6.vars.get('f0','')
        if len ( findex6_f0 ):
            id_dfindex6 = db.dfindex6.insert( **findex6.vars )
            db.commit()

            if not id_dfindex6 is None:
                dfindex6_row = db.dfindex6(id_dfindex6 )

                if not dfindex6_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex6.vars.f0}\" into db.dfindex6.f0, id = {id_dfindex6}' )
                         print(f"     found db.dfindex6.f0: \"{dfindex6_row.f0}\", id = {id_dfindex6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findex6_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findex6.vars.items() ]
                print()
   
    elif findex6.errors:
        print("findex6 has errors: %s " % (findex6.errors))
 

    dfindex7_row= None
    id_dfindex7 = None
    findex7= Form(db.dfindex7, id, deletable=False, dbio = False, keep_values = False, form_name = "findex7",  formstyle=FormStyleBulma )
   
    if findex7.accepted:

        Glb['debug'] and print("     findex7 accepted with: %s " % (findex7.vars))
        findex7_f0 = findex7.vars.get('f0','')
        if len ( findex7_f0 ):
            id_dfindex7 = db.dfindex7.insert( **findex7.vars )
            db.commit()

            if not id_dfindex7 is None:
                dfindex7_row = db.dfindex7(id_dfindex7 )

                if not dfindex7_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findex7.vars.f0}\" into db.dfindex7.f0, id = {id_dfindex7}' )
                         print(f"     found db.dfindex7.f0: \"{dfindex7_row.f0}\", id = {id_dfindex7}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findex7_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findex7.vars.items() ]
                print()
   
    elif findex7.errors:
        print("findex7 has errors: %s " % (findex7.errors))
 

    return locals()


@action('color', method=["GET", "POST"] )
@action.uses(Template('color.html', delimiters='[%[ ]]',), db, session,  T, )

def color(id=None):
    ctrl_info= "ctrl: color, view: color.html"
    messages = []

    dfcolor0_row= None
    id_dfcolor0 = None
    fcolor0= Form(db.dfcolor0, id, deletable=False, dbio = False, keep_values = False, form_name = "fcolor0",  formstyle=FormStyleBulma )
   
    if fcolor0.accepted:

        Glb['debug'] and print("     fcolor0 accepted with: %s " % (fcolor0.vars))
        fcolor0_f0 = fcolor0.vars.get('f0','')
        if len ( fcolor0_f0 ):
            id_dfcolor0 = db.dfcolor0.insert( **fcolor0.vars )
            db.commit()

            if not id_dfcolor0 is None:
                dfcolor0_row = db.dfcolor0(id_dfcolor0 )

                if not dfcolor0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcolor0.vars.f0}\" into db.dfcolor0.f0, id = {id_dfcolor0}' )
                         print(f"     found db.dfcolor0.f0: \"{dfcolor0_row.f0}\", id = {id_dfcolor0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fcolor0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fcolor0.vars.items() ]
                print()
   
    elif fcolor0.errors:
        print("fcolor0 has errors: %s " % (fcolor0.errors))
 

    dfcolor1_row= None
    id_dfcolor1 = None
    fcolor1= Form(db.dfcolor1, id, deletable=False, dbio = False, keep_values = False, form_name = "fcolor1",  formstyle=FormStyleBulma )
   
    if fcolor1.accepted:

        Glb['debug'] and print("     fcolor1 accepted with: %s " % (fcolor1.vars))
        fcolor1_f0 = fcolor1.vars.get('f0','')
        if len ( fcolor1_f0 ):
            id_dfcolor1 = db.dfcolor1.insert( **fcolor1.vars )
            db.commit()

            if not id_dfcolor1 is None:
                dfcolor1_row = db.dfcolor1(id_dfcolor1 )

                if not dfcolor1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcolor1.vars.f0}\" into db.dfcolor1.f0, id = {id_dfcolor1}' )
                         print(f"     found db.dfcolor1.f0: \"{dfcolor1_row.f0}\", id = {id_dfcolor1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fcolor1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fcolor1.vars.items() ]
                print()
   
    elif fcolor1.errors:
        print("fcolor1 has errors: %s " % (fcolor1.errors))
 

    return locals()


@action('alert', method=["GET", "POST"] )
@action.uses(Template('alert.html', delimiters='[%[ ]]',), db, session,  T, )

def alert(id=None):
    ctrl_info= "ctrl: alert, view: alert.html"
    messages = []

    dfalert0_row= None
    id_dfalert0 = None
    falert0= Form(db.dfalert0, id, deletable=False, dbio = False, keep_values = False, form_name = "falert0",  formstyle=FormStyleBulma )
   
    if falert0.accepted:

        Glb['debug'] and print("     falert0 accepted with: %s " % (falert0.vars))
        falert0_f0 = falert0.vars.get('f0','')
        if len ( falert0_f0 ):
            id_dfalert0 = db.dfalert0.insert( **falert0.vars )
            db.commit()

            if not id_dfalert0 is None:
                dfalert0_row = db.dfalert0(id_dfalert0 )

                if not dfalert0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{falert0.vars.f0}\" into db.dfalert0.f0, id = {id_dfalert0}' )
                         print(f"     found db.dfalert0.f0: \"{dfalert0_row.f0}\", id = {id_dfalert0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(falert0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in falert0.vars.items() ]
                print()
   
    elif falert0.errors:
        print("falert0 has errors: %s " % (falert0.errors))
 

    dfalert1_row= None
    id_dfalert1 = None
    falert1= Form(db.dfalert1, id, deletable=False, dbio = False, keep_values = False, form_name = "falert1",  formstyle=FormStyleBulma )
   
    if falert1.accepted:

        Glb['debug'] and print("     falert1 accepted with: %s " % (falert1.vars))
        falert1_f0 = falert1.vars.get('f0','')
        if len ( falert1_f0 ):
            id_dfalert1 = db.dfalert1.insert( **falert1.vars )
            db.commit()

            if not id_dfalert1 is None:
                dfalert1_row = db.dfalert1(id_dfalert1 )

                if not dfalert1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{falert1.vars.f0}\" into db.dfalert1.f0, id = {id_dfalert1}' )
                         print(f"     found db.dfalert1.f0: \"{dfalert1_row.f0}\", id = {id_dfalert1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(falert1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in falert1.vars.items() ]
                print()
   
    elif falert1.errors:
        print("falert1 has errors: %s " % (falert1.errors))
 

    return locals()


@action('wizard', method=["GET", "POST"] )
@action.uses(Template('wizard.html', delimiters='[%[ ]]',), db, session,  T, )

def wizard(id=None):
    ctrl_info= "ctrl: wizard, view: wizard.html"
    messages = []

    dfwizard0_row= None
    id_dfwizard0 = None
    fwizard0= Form(db.dfwizard0, id, deletable=False, dbio = False, keep_values = False, form_name = "fwizard0",  formstyle=FormStyleBulma )
   
    if fwizard0.accepted:

        Glb['debug'] and print("     fwizard0 accepted with: %s " % (fwizard0.vars))
        fwizard0_f0 = fwizard0.vars.get('f0','')
        if len ( fwizard0_f0 ):
            id_dfwizard0 = db.dfwizard0.insert( **fwizard0.vars )
            db.commit()

            if not id_dfwizard0 is None:
                dfwizard0_row = db.dfwizard0(id_dfwizard0 )

                if not dfwizard0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwizard0.vars.f0}\" into db.dfwizard0.f0, id = {id_dfwizard0}' )
                         print(f"     found db.dfwizard0.f0: \"{dfwizard0_row.f0}\", id = {id_dfwizard0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fwizard0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fwizard0.vars.items() ]
                print()
   
    elif fwizard0.errors:
        print("fwizard0 has errors: %s " % (fwizard0.errors))
 

    dfwizard1_row= None
    id_dfwizard1 = None
    fwizard1= Form(db.dfwizard1, id, deletable=False, dbio = False, keep_values = False, form_name = "fwizard1",  formstyle=FormStyleBulma )
   
    if fwizard1.accepted:

        Glb['debug'] and print("     fwizard1 accepted with: %s " % (fwizard1.vars))
        fwizard1_f0 = fwizard1.vars.get('f0','')
        if len ( fwizard1_f0 ):
            id_dfwizard1 = db.dfwizard1.insert( **fwizard1.vars )
            db.commit()

            if not id_dfwizard1 is None:
                dfwizard1_row = db.dfwizard1(id_dfwizard1 )

                if not dfwizard1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwizard1.vars.f0}\" into db.dfwizard1.f0, id = {id_dfwizard1}' )
                         print(f"     found db.dfwizard1.f0: \"{dfwizard1_row.f0}\", id = {id_dfwizard1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fwizard1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fwizard1.vars.items() ]
                print()
   
    elif fwizard1.errors:
        print("fwizard1 has errors: %s " % (fwizard1.errors))
 

    return locals()


@action('modals', method=["GET", "POST"] )
@action.uses(Template('modals.html', delimiters='[%[ ]]',), db, session,  T, )

def modals(id=None):
    ctrl_info= "ctrl: modals, view: modals.html"
    messages = []

    dfmodals0_row= None
    id_dfmodals0 = None
    fmodals0= Form(db.dfmodals0, id, deletable=False, dbio = False, keep_values = False, form_name = "fmodals0",  formstyle=FormStyleBulma )
   
    if fmodals0.accepted:

        Glb['debug'] and print("     fmodals0 accepted with: %s " % (fmodals0.vars))
        fmodals0_f0 = fmodals0.vars.get('f0','')
        if len ( fmodals0_f0 ):
            id_dfmodals0 = db.dfmodals0.insert( **fmodals0.vars )
            db.commit()

            if not id_dfmodals0 is None:
                dfmodals0_row = db.dfmodals0(id_dfmodals0 )

                if not dfmodals0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmodals0.vars.f0}\" into db.dfmodals0.f0, id = {id_dfmodals0}' )
                         print(f"     found db.dfmodals0.f0: \"{dfmodals0_row.f0}\", id = {id_dfmodals0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmodals0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmodals0.vars.items() ]
                print()
   
    elif fmodals0.errors:
        print("fmodals0 has errors: %s " % (fmodals0.errors))
 

    dfmodals1_row= None
    id_dfmodals1 = None
    fmodals1= Form(db.dfmodals1, id, deletable=False, dbio = False, keep_values = False, form_name = "fmodals1",  formstyle=FormStyleBulma )
   
    if fmodals1.accepted:

        Glb['debug'] and print("     fmodals1 accepted with: %s " % (fmodals1.vars))
        fmodals1_f0 = fmodals1.vars.get('f0','')
        if len ( fmodals1_f0 ):
            id_dfmodals1 = db.dfmodals1.insert( **fmodals1.vars )
            db.commit()

            if not id_dfmodals1 is None:
                dfmodals1_row = db.dfmodals1(id_dfmodals1 )

                if not dfmodals1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fmodals1.vars.f0}\" into db.dfmodals1.f0, id = {id_dfmodals1}' )
                         print(f"     found db.dfmodals1.f0: \"{dfmodals1_row.f0}\", id = {id_dfmodals1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fmodals1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fmodals1.vars.items() ]
                print()
   
    elif fmodals1.errors:
        print("fmodals1 has errors: %s " % (fmodals1.errors))
 

    return locals()


@action('dialog', method=["GET", "POST"] )
@action.uses(Template('dialog.html', delimiters='[%[ ]]',), db, session,  T, )

def dialog(id=None):
    ctrl_info= "ctrl: dialog, view: dialog.html"
    messages = []

    dfdialog0_row= None
    id_dfdialog0 = None
    fdialog0= Form(db.dfdialog0, id, deletable=False, dbio = False, keep_values = False, form_name = "fdialog0",  formstyle=FormStyleBulma )
   
    if fdialog0.accepted:

        Glb['debug'] and print("     fdialog0 accepted with: %s " % (fdialog0.vars))
        fdialog0_f0 = fdialog0.vars.get('f0','')
        if len ( fdialog0_f0 ):
            id_dfdialog0 = db.dfdialog0.insert( **fdialog0.vars )
            db.commit()

            if not id_dfdialog0 is None:
                dfdialog0_row = db.dfdialog0(id_dfdialog0 )

                if not dfdialog0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fdialog0.vars.f0}\" into db.dfdialog0.f0, id = {id_dfdialog0}' )
                         print(f"     found db.dfdialog0.f0: \"{dfdialog0_row.f0}\", id = {id_dfdialog0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fdialog0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fdialog0.vars.items() ]
                print()
   
    elif fdialog0.errors:
        print("fdialog0 has errors: %s " % (fdialog0.errors))
 

    dfdialog1_row= None
    id_dfdialog1 = None
    fdialog1= Form(db.dfdialog1, id, deletable=False, dbio = False, keep_values = False, form_name = "fdialog1",  formstyle=FormStyleBulma )
   
    if fdialog1.accepted:

        Glb['debug'] and print("     fdialog1 accepted with: %s " % (fdialog1.vars))
        fdialog1_f0 = fdialog1.vars.get('f0','')
        if len ( fdialog1_f0 ):
            id_dfdialog1 = db.dfdialog1.insert( **fdialog1.vars )
            db.commit()

            if not id_dfdialog1 is None:
                dfdialog1_row = db.dfdialog1(id_dfdialog1 )

                if not dfdialog1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fdialog1.vars.f0}\" into db.dfdialog1.f0, id = {id_dfdialog1}' )
                         print(f"     found db.dfdialog1.f0: \"{dfdialog1_row.f0}\", id = {id_dfdialog1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fdialog1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fdialog1.vars.items() ]
                print()
   
    elif fdialog1.errors:
        print("fdialog1 has errors: %s " % (fdialog1.errors))
 

    return locals()


@action('widgets', method=["GET", "POST"] )
@action.uses(Template('widgets.html', delimiters='[%[ ]]',), db, session,  T, )

def widgets(id=None):
    ctrl_info= "ctrl: widgets, view: widgets.html"
    messages = []

    dfwidgets0_row= None
    id_dfwidgets0 = None
    fwidgets0= Form(db.dfwidgets0, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets0",  formstyle=FormStyleBulma )
   
    if fwidgets0.accepted:

        Glb['debug'] and print("     fwidgets0 accepted with: %s " % (fwidgets0.vars))
        fwidgets0_f0 = fwidgets0.vars.get('f0','')
        if len ( fwidgets0_f0 ):
            id_dfwidgets0 = db.dfwidgets0.insert( **fwidgets0.vars )
            db.commit()

            if not id_dfwidgets0 is None:
                dfwidgets0_row = db.dfwidgets0(id_dfwidgets0 )

                if not dfwidgets0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets0.vars.f0}\" into db.dfwidgets0.f0, id = {id_dfwidgets0}' )
                         print(f"     found db.dfwidgets0.f0: \"{dfwidgets0_row.f0}\", id = {id_dfwidgets0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fwidgets0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets0.vars.items() ]
                print()
   
    elif fwidgets0.errors:
        print("fwidgets0 has errors: %s " % (fwidgets0.errors))
 

    dfwidgets1_row= None
    id_dfwidgets1 = None
    fwidgets1= Form(db.dfwidgets1, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets1",  formstyle=FormStyleBulma )
   
    if fwidgets1.accepted:

        Glb['debug'] and print("     fwidgets1 accepted with: %s " % (fwidgets1.vars))
        fwidgets1_f0 = fwidgets1.vars.get('f0','')
        if len ( fwidgets1_f0 ):
            id_dfwidgets1 = db.dfwidgets1.insert( **fwidgets1.vars )
            db.commit()

            if not id_dfwidgets1 is None:
                dfwidgets1_row = db.dfwidgets1(id_dfwidgets1 )

                if not dfwidgets1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets1.vars.f0}\" into db.dfwidgets1.f0, id = {id_dfwidgets1}' )
                         print(f"     found db.dfwidgets1.f0: \"{dfwidgets1_row.f0}\", id = {id_dfwidgets1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fwidgets1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets1.vars.items() ]
                print()
   
    elif fwidgets1.errors:
        print("fwidgets1 has errors: %s " % (fwidgets1.errors))
 

    dfwidgets2_row= None
    id_dfwidgets2 = None
    fwidgets2= Form(db.dfwidgets2, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets2",  formstyle=FormStyleBulma )
   
    if fwidgets2.accepted:

        Glb['debug'] and print("     fwidgets2 accepted with: %s " % (fwidgets2.vars))
        fwidgets2_f0 = fwidgets2.vars.get('f0','')
        if len ( fwidgets2_f0 ):
            id_dfwidgets2 = db.dfwidgets2.insert( **fwidgets2.vars )
            db.commit()

            if not id_dfwidgets2 is None:
                dfwidgets2_row = db.dfwidgets2(id_dfwidgets2 )

                if not dfwidgets2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets2.vars.f0}\" into db.dfwidgets2.f0, id = {id_dfwidgets2}' )
                         print(f"     found db.dfwidgets2.f0: \"{dfwidgets2_row.f0}\", id = {id_dfwidgets2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fwidgets2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets2.vars.items() ]
                print()
   
    elif fwidgets2.errors:
        print("fwidgets2 has errors: %s " % (fwidgets2.errors))
 

    dfwidgets3_row= None
    id_dfwidgets3 = None
    fwidgets3= Form(db.dfwidgets3, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets3",  formstyle=FormStyleBulma )
   
    if fwidgets3.accepted:

        Glb['debug'] and print("     fwidgets3 accepted with: %s " % (fwidgets3.vars))
        fwidgets3_f0 = fwidgets3.vars.get('f0','')
        if len ( fwidgets3_f0 ):
            id_dfwidgets3 = db.dfwidgets3.insert( **fwidgets3.vars )
            db.commit()

            if not id_dfwidgets3 is None:
                dfwidgets3_row = db.dfwidgets3(id_dfwidgets3 )

                if not dfwidgets3_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets3.vars.f0}\" into db.dfwidgets3.f0, id = {id_dfwidgets3}' )
                         print(f"     found db.dfwidgets3.f0: \"{dfwidgets3_row.f0}\", id = {id_dfwidgets3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fwidgets3_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets3.vars.items() ]
                print()
   
    elif fwidgets3.errors:
        print("fwidgets3 has errors: %s " % (fwidgets3.errors))
 

    dfwidgets4_row= None
    id_dfwidgets4 = None
    fwidgets4= Form(db.dfwidgets4, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets4",  formstyle=FormStyleBulma )
   
    if fwidgets4.accepted:

        Glb['debug'] and print("     fwidgets4 accepted with: %s " % (fwidgets4.vars))
        fwidgets4_f0 = fwidgets4.vars.get('f0','')
        if len ( fwidgets4_f0 ):
            id_dfwidgets4 = db.dfwidgets4.insert( **fwidgets4.vars )
            db.commit()

            if not id_dfwidgets4 is None:
                dfwidgets4_row = db.dfwidgets4(id_dfwidgets4 )

                if not dfwidgets4_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets4.vars.f0}\" into db.dfwidgets4.f0, id = {id_dfwidgets4}' )
                         print(f"     found db.dfwidgets4.f0: \"{dfwidgets4_row.f0}\", id = {id_dfwidgets4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fwidgets4_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets4.vars.items() ]
                print()
   
    elif fwidgets4.errors:
        print("fwidgets4 has errors: %s " % (fwidgets4.errors))
 

    dfwidgets5_row= None
    id_dfwidgets5 = None
    fwidgets5= Form(db.dfwidgets5, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets5",  formstyle=FormStyleBulma )
   
    if fwidgets5.accepted:

        Glb['debug'] and print("     fwidgets5 accepted with: %s " % (fwidgets5.vars))
        fwidgets5_f0 = fwidgets5.vars.get('f0','')
        if len ( fwidgets5_f0 ):
            id_dfwidgets5 = db.dfwidgets5.insert( **fwidgets5.vars )
            db.commit()

            if not id_dfwidgets5 is None:
                dfwidgets5_row = db.dfwidgets5(id_dfwidgets5 )

                if not dfwidgets5_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets5.vars.f0}\" into db.dfwidgets5.f0, id = {id_dfwidgets5}' )
                         print(f"     found db.dfwidgets5.f0: \"{dfwidgets5_row.f0}\", id = {id_dfwidgets5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fwidgets5_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets5.vars.items() ]
                print()
   
    elif fwidgets5.errors:
        print("fwidgets5 has errors: %s " % (fwidgets5.errors))
 

    dfwidgets6_row= None
    id_dfwidgets6 = None
    fwidgets6= Form(db.dfwidgets6, id, deletable=False, dbio = False, keep_values = False, form_name = "fwidgets6",  formstyle=FormStyleBulma )
   
    if fwidgets6.accepted:

        Glb['debug'] and print("     fwidgets6 accepted with: %s " % (fwidgets6.vars))
        fwidgets6_f0 = fwidgets6.vars.get('f0','')
        if len ( fwidgets6_f0 ):
            id_dfwidgets6 = db.dfwidgets6.insert( **fwidgets6.vars )
            db.commit()

            if not id_dfwidgets6 is None:
                dfwidgets6_row = db.dfwidgets6(id_dfwidgets6 )

                if not dfwidgets6_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fwidgets6.vars.f0}\" into db.dfwidgets6.f0, id = {id_dfwidgets6}' )
                         print(f"     found db.dfwidgets6.f0: \"{dfwidgets6_row.f0}\", id = {id_dfwidgets6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fwidgets6_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fwidgets6.vars.items() ]
                print()
   
    elif fwidgets6.errors:
        print("fwidgets6 has errors: %s " % (fwidgets6.errors))
 

    return locals()


@action('indexX3', method=["GET", "POST"] )
@action.uses(Template('index-3.html', delimiters='[%[ ]]',), db, session,  T, )

def indexX3(id=None):
    ctrl_info= "ctrl: indexX3, view: index-3.html"
    messages = []

    rows_tindexX30= db(db.tindexX30).select()
    dfindexX30_row= None
    id_dfindexX30 = None
    findexX30= Form(db.dfindexX30, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX30",  formstyle=FormStyleBulma )
   
    if findexX30.accepted:

        Glb['debug'] and print("     findexX30 accepted with: %s " % (findexX30.vars))
        findexX30_f0 = findexX30.vars.get('f0','')
        if len ( findexX30_f0 ):
            id_dfindexX30 = db.dfindexX30.insert( **findexX30.vars )
            db.commit()

            if not id_dfindexX30 is None:
                dfindexX30_row = db.dfindexX30(id_dfindexX30 )

                if not dfindexX30_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX30.vars.f0}\" into db.dfindexX30.f0, id = {id_dfindexX30}' )
                         print(f"     found db.dfindexX30.f0: \"{dfindexX30_row.f0}\", id = {id_dfindexX30}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX30_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX30.vars.items() ]
                print()
   
    elif findexX30.errors:
        print("findexX30 has errors: %s " % (findexX30.errors))
 

    dfindexX31_row= None
    id_dfindexX31 = None
    findexX31= Form(db.dfindexX31, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX31",  formstyle=FormStyleBulma )
   
    if findexX31.accepted:

        Glb['debug'] and print("     findexX31 accepted with: %s " % (findexX31.vars))
        findexX31_f0 = findexX31.vars.get('f0','')
        if len ( findexX31_f0 ):
            id_dfindexX31 = db.dfindexX31.insert( **findexX31.vars )
            db.commit()

            if not id_dfindexX31 is None:
                dfindexX31_row = db.dfindexX31(id_dfindexX31 )

                if not dfindexX31_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX31.vars.f0}\" into db.dfindexX31.f0, id = {id_dfindexX31}' )
                         print(f"     found db.dfindexX31.f0: \"{dfindexX31_row.f0}\", id = {id_dfindexX31}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX31_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX31.vars.items() ]
                print()
   
    elif findexX31.errors:
        print("findexX31 has errors: %s " % (findexX31.errors))
 

    dfindexX32_row= None
    id_dfindexX32 = None
    findexX32= Form(db.dfindexX32, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX32",  formstyle=FormStyleBulma )
   
    if findexX32.accepted:

        Glb['debug'] and print("     findexX32 accepted with: %s " % (findexX32.vars))
        findexX32_f0 = findexX32.vars.get('f0','')
        if len ( findexX32_f0 ):
            id_dfindexX32 = db.dfindexX32.insert( **findexX32.vars )
            db.commit()

            if not id_dfindexX32 is None:
                dfindexX32_row = db.dfindexX32(id_dfindexX32 )

                if not dfindexX32_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX32.vars.f0}\" into db.dfindexX32.f0, id = {id_dfindexX32}' )
                         print(f"     found db.dfindexX32.f0: \"{dfindexX32_row.f0}\", id = {id_dfindexX32}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX32_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX32.vars.items() ]
                print()
   
    elif findexX32.errors:
        print("findexX32 has errors: %s " % (findexX32.errors))
 

    dfindexX33_row= None
    id_dfindexX33 = None
    findexX33= Form(db.dfindexX33, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX33",  formstyle=FormStyleBulma )
   
    if findexX33.accepted:

        Glb['debug'] and print("     findexX33 accepted with: %s " % (findexX33.vars))
        findexX33_f0 = findexX33.vars.get('f0','')
        if len ( findexX33_f0 ):
            id_dfindexX33 = db.dfindexX33.insert( **findexX33.vars )
            db.commit()

            if not id_dfindexX33 is None:
                dfindexX33_row = db.dfindexX33(id_dfindexX33 )

                if not dfindexX33_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX33.vars.f0}\" into db.dfindexX33.f0, id = {id_dfindexX33}' )
                         print(f"     found db.dfindexX33.f0: \"{dfindexX33_row.f0}\", id = {id_dfindexX33}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX33_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX33.vars.items() ]
                print()
   
    elif findexX33.errors:
        print("findexX33 has errors: %s " % (findexX33.errors))
 

    dfindexX34_row= None
    id_dfindexX34 = None
    findexX34= Form(db.dfindexX34, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX34",  formstyle=FormStyleBulma )
   
    if findexX34.accepted:

        Glb['debug'] and print("     findexX34 accepted with: %s " % (findexX34.vars))
        findexX34_f0 = findexX34.vars.get('f0','')
        if len ( findexX34_f0 ):
            id_dfindexX34 = db.dfindexX34.insert( **findexX34.vars )
            db.commit()

            if not id_dfindexX34 is None:
                dfindexX34_row = db.dfindexX34(id_dfindexX34 )

                if not dfindexX34_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX34.vars.f0}\" into db.dfindexX34.f0, id = {id_dfindexX34}' )
                         print(f"     found db.dfindexX34.f0: \"{dfindexX34_row.f0}\", id = {id_dfindexX34}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX34_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX34.vars.items() ]
                print()
   
    elif findexX34.errors:
        print("findexX34 has errors: %s " % (findexX34.errors))
 

    dfindexX35_row= None
    id_dfindexX35 = None
    findexX35= Form(db.dfindexX35, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX35",  formstyle=FormStyleBulma )
   
    if findexX35.accepted:

        Glb['debug'] and print("     findexX35 accepted with: %s " % (findexX35.vars))
        findexX35_f0 = findexX35.vars.get('f0','')
        if len ( findexX35_f0 ):
            id_dfindexX35 = db.dfindexX35.insert( **findexX35.vars )
            db.commit()

            if not id_dfindexX35 is None:
                dfindexX35_row = db.dfindexX35(id_dfindexX35 )

                if not dfindexX35_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX35.vars.f0}\" into db.dfindexX35.f0, id = {id_dfindexX35}' )
                         print(f"     found db.dfindexX35.f0: \"{dfindexX35_row.f0}\", id = {id_dfindexX35}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX35_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX35.vars.items() ]
                print()
   
    elif findexX35.errors:
        print("findexX35 has errors: %s " % (findexX35.errors))
 

    dfindexX36_row= None
    id_dfindexX36 = None
    findexX36= Form(db.dfindexX36, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX36",  formstyle=FormStyleBulma )
   
    if findexX36.accepted:

        Glb['debug'] and print("     findexX36 accepted with: %s " % (findexX36.vars))
        findexX36_f0 = findexX36.vars.get('f0','')
        if len ( findexX36_f0 ):
            id_dfindexX36 = db.dfindexX36.insert( **findexX36.vars )
            db.commit()

            if not id_dfindexX36 is None:
                dfindexX36_row = db.dfindexX36(id_dfindexX36 )

                if not dfindexX36_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX36.vars.f0}\" into db.dfindexX36.f0, id = {id_dfindexX36}' )
                         print(f"     found db.dfindexX36.f0: \"{dfindexX36_row.f0}\", id = {id_dfindexX36}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX36_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX36.vars.items() ]
                print()
   
    elif findexX36.errors:
        print("findexX36 has errors: %s " % (findexX36.errors))
 

    dfindexX37_row= None
    id_dfindexX37 = None
    findexX37= Form(db.dfindexX37, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX37",  formstyle=FormStyleBulma )
   
    if findexX37.accepted:

        Glb['debug'] and print("     findexX37 accepted with: %s " % (findexX37.vars))
        findexX37_f0 = findexX37.vars.get('f0','')
        if len ( findexX37_f0 ):
            id_dfindexX37 = db.dfindexX37.insert( **findexX37.vars )
            db.commit()

            if not id_dfindexX37 is None:
                dfindexX37_row = db.dfindexX37(id_dfindexX37 )

                if not dfindexX37_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX37.vars.f0}\" into db.dfindexX37.f0, id = {id_dfindexX37}' )
                         print(f"     found db.dfindexX37.f0: \"{dfindexX37_row.f0}\", id = {id_dfindexX37}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX37_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX37.vars.items() ]
                print()
   
    elif findexX37.errors:
        print("findexX37 has errors: %s " % (findexX37.errors))
 

    return locals()


@action('invoice', method=["GET", "POST"] )
@action.uses(Template('invoice.html', delimiters='[%[ ]]',), db, session,  T, )

def invoice(id=None):
    ctrl_info= "ctrl: invoice, view: invoice.html"
    messages = []

    rows_tinvoice0= db(db.tinvoice0).select()
    dfinvoice0_row= None
    id_dfinvoice0 = None
    finvoice0= Form(db.dfinvoice0, id, deletable=False, dbio = False, keep_values = False, form_name = "finvoice0",  formstyle=FormStyleBulma )
   
    if finvoice0.accepted:

        Glb['debug'] and print("     finvoice0 accepted with: %s " % (finvoice0.vars))
        finvoice0_f0 = finvoice0.vars.get('f0','')
        if len ( finvoice0_f0 ):
            id_dfinvoice0 = db.dfinvoice0.insert( **finvoice0.vars )
            db.commit()

            if not id_dfinvoice0 is None:
                dfinvoice0_row = db.dfinvoice0(id_dfinvoice0 )

                if not dfinvoice0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finvoice0.vars.f0}\" into db.dfinvoice0.f0, id = {id_dfinvoice0}' )
                         print(f"     found db.dfinvoice0.f0: \"{dfinvoice0_row.f0}\", id = {id_dfinvoice0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finvoice0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finvoice0.vars.items() ]
                print()
   
    elif finvoice0.errors:
        print("finvoice0 has errors: %s " % (finvoice0.errors))
 

    dfinvoice1_row= None
    id_dfinvoice1 = None
    finvoice1= Form(db.dfinvoice1, id, deletable=False, dbio = False, keep_values = False, form_name = "finvoice1",  formstyle=FormStyleBulma )
   
    if finvoice1.accepted:

        Glb['debug'] and print("     finvoice1 accepted with: %s " % (finvoice1.vars))
        finvoice1_f0 = finvoice1.vars.get('f0','')
        if len ( finvoice1_f0 ):
            id_dfinvoice1 = db.dfinvoice1.insert( **finvoice1.vars )
            db.commit()

            if not id_dfinvoice1 is None:
                dfinvoice1_row = db.dfinvoice1(id_dfinvoice1 )

                if not dfinvoice1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{finvoice1.vars.f0}\" into db.dfinvoice1.f0, id = {id_dfinvoice1}' )
                         print(f"     found db.dfinvoice1.f0: \"{dfinvoice1_row.f0}\", id = {id_dfinvoice1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(finvoice1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in finvoice1.vars.items() ]
                print()
   
    elif finvoice1.errors:
        print("finvoice1 has errors: %s " % (finvoice1.errors))
 

    return locals()


@action('indexX4', method=["GET", "POST"] )
@action.uses(Template('index-4.html', delimiters='[%[ ]]',), db, session,  T, )

def indexX4(id=None):
    ctrl_info= "ctrl: indexX4, view: index-4.html"
    messages = []

    rows_tindexX40= db(db.tindexX40).select()
    dfindexX40_row= None
    id_dfindexX40 = None
    findexX40= Form(db.dfindexX40, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX40",  formstyle=FormStyleBulma )
   
    if findexX40.accepted:

        Glb['debug'] and print("     findexX40 accepted with: %s " % (findexX40.vars))
        findexX40_f0 = findexX40.vars.get('f0','')
        if len ( findexX40_f0 ):
            id_dfindexX40 = db.dfindexX40.insert( **findexX40.vars )
            db.commit()

            if not id_dfindexX40 is None:
                dfindexX40_row = db.dfindexX40(id_dfindexX40 )

                if not dfindexX40_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX40.vars.f0}\" into db.dfindexX40.f0, id = {id_dfindexX40}' )
                         print(f"     found db.dfindexX40.f0: \"{dfindexX40_row.f0}\", id = {id_dfindexX40}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX40_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX40.vars.items() ]
                print()
   
    elif findexX40.errors:
        print("findexX40 has errors: %s " % (findexX40.errors))
 

    dfindexX41_row= None
    id_dfindexX41 = None
    findexX41= Form(db.dfindexX41, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX41",  formstyle=FormStyleBulma )
   
    if findexX41.accepted:

        Glb['debug'] and print("     findexX41 accepted with: %s " % (findexX41.vars))
        findexX41_f0 = findexX41.vars.get('f0','')
        if len ( findexX41_f0 ):
            id_dfindexX41 = db.dfindexX41.insert( **findexX41.vars )
            db.commit()

            if not id_dfindexX41 is None:
                dfindexX41_row = db.dfindexX41(id_dfindexX41 )

                if not dfindexX41_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX41.vars.f0}\" into db.dfindexX41.f0, id = {id_dfindexX41}' )
                         print(f"     found db.dfindexX41.f0: \"{dfindexX41_row.f0}\", id = {id_dfindexX41}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX41_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX41.vars.items() ]
                print()
   
    elif findexX41.errors:
        print("findexX41 has errors: %s " % (findexX41.errors))
 

    dfindexX42_row= None
    id_dfindexX42 = None
    findexX42= Form(db.dfindexX42, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX42",  formstyle=FormStyleBulma )
   
    if findexX42.accepted:

        Glb['debug'] and print("     findexX42 accepted with: %s " % (findexX42.vars))
        findexX42_f0 = findexX42.vars.get('f0','')
        if len ( findexX42_f0 ):
            id_dfindexX42 = db.dfindexX42.insert( **findexX42.vars )
            db.commit()

            if not id_dfindexX42 is None:
                dfindexX42_row = db.dfindexX42(id_dfindexX42 )

                if not dfindexX42_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX42.vars.f0}\" into db.dfindexX42.f0, id = {id_dfindexX42}' )
                         print(f"     found db.dfindexX42.f0: \"{dfindexX42_row.f0}\", id = {id_dfindexX42}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX42_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX42.vars.items() ]
                print()
   
    elif findexX42.errors:
        print("findexX42 has errors: %s " % (findexX42.errors))
 

    dfindexX43_row= None
    id_dfindexX43 = None
    findexX43= Form(db.dfindexX43, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX43",  formstyle=FormStyleBulma )
   
    if findexX43.accepted:

        Glb['debug'] and print("     findexX43 accepted with: %s " % (findexX43.vars))
        findexX43_f0 = findexX43.vars.get('f0','')
        if len ( findexX43_f0 ):
            id_dfindexX43 = db.dfindexX43.insert( **findexX43.vars )
            db.commit()

            if not id_dfindexX43 is None:
                dfindexX43_row = db.dfindexX43(id_dfindexX43 )

                if not dfindexX43_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX43.vars.f0}\" into db.dfindexX43.f0, id = {id_dfindexX43}' )
                         print(f"     found db.dfindexX43.f0: \"{dfindexX43_row.f0}\", id = {id_dfindexX43}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX43_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX43.vars.items() ]
                print()
   
    elif findexX43.errors:
        print("findexX43 has errors: %s " % (findexX43.errors))
 

    dfindexX44_row= None
    id_dfindexX44 = None
    findexX44= Form(db.dfindexX44, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX44",  formstyle=FormStyleBulma )
   
    if findexX44.accepted:

        Glb['debug'] and print("     findexX44 accepted with: %s " % (findexX44.vars))
        findexX44_f0 = findexX44.vars.get('f0','')
        if len ( findexX44_f0 ):
            id_dfindexX44 = db.dfindexX44.insert( **findexX44.vars )
            db.commit()

            if not id_dfindexX44 is None:
                dfindexX44_row = db.dfindexX44(id_dfindexX44 )

                if not dfindexX44_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX44.vars.f0}\" into db.dfindexX44.f0, id = {id_dfindexX44}' )
                         print(f"     found db.dfindexX44.f0: \"{dfindexX44_row.f0}\", id = {id_dfindexX44}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX44_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX44.vars.items() ]
                print()
   
    elif findexX44.errors:
        print("findexX44 has errors: %s " % (findexX44.errors))
 

    dfindexX45_row= None
    id_dfindexX45 = None
    findexX45= Form(db.dfindexX45, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX45",  formstyle=FormStyleBulma )
   
    if findexX45.accepted:

        Glb['debug'] and print("     findexX45 accepted with: %s " % (findexX45.vars))
        findexX45_f0 = findexX45.vars.get('f0','')
        if len ( findexX45_f0 ):
            id_dfindexX45 = db.dfindexX45.insert( **findexX45.vars )
            db.commit()

            if not id_dfindexX45 is None:
                dfindexX45_row = db.dfindexX45(id_dfindexX45 )

                if not dfindexX45_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX45.vars.f0}\" into db.dfindexX45.f0, id = {id_dfindexX45}' )
                         print(f"     found db.dfindexX45.f0: \"{dfindexX45_row.f0}\", id = {id_dfindexX45}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX45_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX45.vars.items() ]
                print()
   
    elif findexX45.errors:
        print("findexX45 has errors: %s " % (findexX45.errors))
 

    dfindexX46_row= None
    id_dfindexX46 = None
    findexX46= Form(db.dfindexX46, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX46",  formstyle=FormStyleBulma )
   
    if findexX46.accepted:

        Glb['debug'] and print("     findexX46 accepted with: %s " % (findexX46.vars))
        findexX46_f0 = findexX46.vars.get('f0','')
        if len ( findexX46_f0 ):
            id_dfindexX46 = db.dfindexX46.insert( **findexX46.vars )
            db.commit()

            if not id_dfindexX46 is None:
                dfindexX46_row = db.dfindexX46(id_dfindexX46 )

                if not dfindexX46_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX46.vars.f0}\" into db.dfindexX46.f0, id = {id_dfindexX46}' )
                         print(f"     found db.dfindexX46.f0: \"{dfindexX46_row.f0}\", id = {id_dfindexX46}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX46_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX46.vars.items() ]
                print()
   
    elif findexX46.errors:
        print("findexX46 has errors: %s " % (findexX46.errors))
 

    dfindexX47_row= None
    id_dfindexX47 = None
    findexX47= Form(db.dfindexX47, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX47",  formstyle=FormStyleBulma )
   
    if findexX47.accepted:

        Glb['debug'] and print("     findexX47 accepted with: %s " % (findexX47.vars))
        findexX47_f0 = findexX47.vars.get('f0','')
        if len ( findexX47_f0 ):
            id_dfindexX47 = db.dfindexX47.insert( **findexX47.vars )
            db.commit()

            if not id_dfindexX47 is None:
                dfindexX47_row = db.dfindexX47(id_dfindexX47 )

                if not dfindexX47_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX47.vars.f0}\" into db.dfindexX47.f0, id = {id_dfindexX47}' )
                         print(f"     found db.dfindexX47.f0: \"{dfindexX47_row.f0}\", id = {id_dfindexX47}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX47_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX47.vars.items() ]
                print()
   
    elif findexX47.errors:
        print("findexX47 has errors: %s " % (findexX47.errors))
 

    return locals()


@action('indexX2', method=["GET", "POST"] )
@action.uses(Template('index-2.html', delimiters='[%[ ]]',), db, session,  T, )

def indexX2(id=None):
    ctrl_info= "ctrl: indexX2, view: index-2.html"
    messages = []

    rows_tindexX20= db(db.tindexX20).select()
    dfindexX20_row= None
    id_dfindexX20 = None
    findexX20= Form(db.dfindexX20, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX20",  formstyle=FormStyleBulma )
   
    if findexX20.accepted:

        Glb['debug'] and print("     findexX20 accepted with: %s " % (findexX20.vars))
        findexX20_f0 = findexX20.vars.get('f0','')
        if len ( findexX20_f0 ):
            id_dfindexX20 = db.dfindexX20.insert( **findexX20.vars )
            db.commit()

            if not id_dfindexX20 is None:
                dfindexX20_row = db.dfindexX20(id_dfindexX20 )

                if not dfindexX20_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX20.vars.f0}\" into db.dfindexX20.f0, id = {id_dfindexX20}' )
                         print(f"     found db.dfindexX20.f0: \"{dfindexX20_row.f0}\", id = {id_dfindexX20}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX20_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX20.vars.items() ]
                print()
   
    elif findexX20.errors:
        print("findexX20 has errors: %s " % (findexX20.errors))
 

    dfindexX21_row= None
    id_dfindexX21 = None
    findexX21= Form(db.dfindexX21, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX21",  formstyle=FormStyleBulma )
   
    if findexX21.accepted:

        Glb['debug'] and print("     findexX21 accepted with: %s " % (findexX21.vars))
        findexX21_f0 = findexX21.vars.get('f0','')
        if len ( findexX21_f0 ):
            id_dfindexX21 = db.dfindexX21.insert( **findexX21.vars )
            db.commit()

            if not id_dfindexX21 is None:
                dfindexX21_row = db.dfindexX21(id_dfindexX21 )

                if not dfindexX21_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX21.vars.f0}\" into db.dfindexX21.f0, id = {id_dfindexX21}' )
                         print(f"     found db.dfindexX21.f0: \"{dfindexX21_row.f0}\", id = {id_dfindexX21}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX21_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX21.vars.items() ]
                print()
   
    elif findexX21.errors:
        print("findexX21 has errors: %s " % (findexX21.errors))
 

    dfindexX22_row= None
    id_dfindexX22 = None
    findexX22= Form(db.dfindexX22, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX22",  formstyle=FormStyleBulma )
   
    if findexX22.accepted:

        Glb['debug'] and print("     findexX22 accepted with: %s " % (findexX22.vars))
        findexX22_f0 = findexX22.vars.get('f0','')
        if len ( findexX22_f0 ):
            id_dfindexX22 = db.dfindexX22.insert( **findexX22.vars )
            db.commit()

            if not id_dfindexX22 is None:
                dfindexX22_row = db.dfindexX22(id_dfindexX22 )

                if not dfindexX22_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX22.vars.f0}\" into db.dfindexX22.f0, id = {id_dfindexX22}' )
                         print(f"     found db.dfindexX22.f0: \"{dfindexX22_row.f0}\", id = {id_dfindexX22}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX22_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX22.vars.items() ]
                print()
   
    elif findexX22.errors:
        print("findexX22 has errors: %s " % (findexX22.errors))
 

    dfindexX23_row= None
    id_dfindexX23 = None
    findexX23= Form(db.dfindexX23, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX23",  formstyle=FormStyleBulma )
   
    if findexX23.accepted:

        Glb['debug'] and print("     findexX23 accepted with: %s " % (findexX23.vars))
        findexX23_f0 = findexX23.vars.get('f0','')
        if len ( findexX23_f0 ):
            id_dfindexX23 = db.dfindexX23.insert( **findexX23.vars )
            db.commit()

            if not id_dfindexX23 is None:
                dfindexX23_row = db.dfindexX23(id_dfindexX23 )

                if not dfindexX23_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX23.vars.f0}\" into db.dfindexX23.f0, id = {id_dfindexX23}' )
                         print(f"     found db.dfindexX23.f0: \"{dfindexX23_row.f0}\", id = {id_dfindexX23}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX23_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX23.vars.items() ]
                print()
   
    elif findexX23.errors:
        print("findexX23 has errors: %s " % (findexX23.errors))
 

    dfindexX24_row= None
    id_dfindexX24 = None
    findexX24= Form(db.dfindexX24, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX24",  formstyle=FormStyleBulma )
   
    if findexX24.accepted:

        Glb['debug'] and print("     findexX24 accepted with: %s " % (findexX24.vars))
        findexX24_f0 = findexX24.vars.get('f0','')
        if len ( findexX24_f0 ):
            id_dfindexX24 = db.dfindexX24.insert( **findexX24.vars )
            db.commit()

            if not id_dfindexX24 is None:
                dfindexX24_row = db.dfindexX24(id_dfindexX24 )

                if not dfindexX24_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX24.vars.f0}\" into db.dfindexX24.f0, id = {id_dfindexX24}' )
                         print(f"     found db.dfindexX24.f0: \"{dfindexX24_row.f0}\", id = {id_dfindexX24}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX24_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX24.vars.items() ]
                print()
   
    elif findexX24.errors:
        print("findexX24 has errors: %s " % (findexX24.errors))
 

    dfindexX25_row= None
    id_dfindexX25 = None
    findexX25= Form(db.dfindexX25, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX25",  formstyle=FormStyleBulma )
   
    if findexX25.accepted:

        Glb['debug'] and print("     findexX25 accepted with: %s " % (findexX25.vars))
        findexX25_f0 = findexX25.vars.get('f0','')
        if len ( findexX25_f0 ):
            id_dfindexX25 = db.dfindexX25.insert( **findexX25.vars )
            db.commit()

            if not id_dfindexX25 is None:
                dfindexX25_row = db.dfindexX25(id_dfindexX25 )

                if not dfindexX25_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX25.vars.f0}\" into db.dfindexX25.f0, id = {id_dfindexX25}' )
                         print(f"     found db.dfindexX25.f0: \"{dfindexX25_row.f0}\", id = {id_dfindexX25}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX25_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX25.vars.items() ]
                print()
   
    elif findexX25.errors:
        print("findexX25 has errors: %s " % (findexX25.errors))
 

    dfindexX26_row= None
    id_dfindexX26 = None
    findexX26= Form(db.dfindexX26, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX26",  formstyle=FormStyleBulma )
   
    if findexX26.accepted:

        Glb['debug'] and print("     findexX26 accepted with: %s " % (findexX26.vars))
        findexX26_f0 = findexX26.vars.get('f0','')
        if len ( findexX26_f0 ):
            id_dfindexX26 = db.dfindexX26.insert( **findexX26.vars )
            db.commit()

            if not id_dfindexX26 is None:
                dfindexX26_row = db.dfindexX26(id_dfindexX26 )

                if not dfindexX26_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX26.vars.f0}\" into db.dfindexX26.f0, id = {id_dfindexX26}' )
                         print(f"     found db.dfindexX26.f0: \"{dfindexX26_row.f0}\", id = {id_dfindexX26}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX26_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX26.vars.items() ]
                print()
   
    elif findexX26.errors:
        print("findexX26 has errors: %s " % (findexX26.errors))
 

    dfindexX27_row= None
    id_dfindexX27 = None
    findexX27= Form(db.dfindexX27, id, deletable=False, dbio = False, keep_values = False, form_name = "findexX27",  formstyle=FormStyleBulma )
   
    if findexX27.accepted:

        Glb['debug'] and print("     findexX27 accepted with: %s " % (findexX27.vars))
        findexX27_f0 = findexX27.vars.get('f0','')
        if len ( findexX27_f0 ):
            id_dfindexX27 = db.dfindexX27.insert( **findexX27.vars )
            db.commit()

            if not id_dfindexX27 is None:
                dfindexX27_row = db.dfindexX27(id_dfindexX27 )

                if not dfindexX27_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{findexX27.vars.f0}\" into db.dfindexX27.f0, id = {id_dfindexX27}' )
                         print(f"     found db.dfindexX27.f0: \"{dfindexX27_row.f0}\", id = {id_dfindexX27}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(findexX27_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in findexX27.vars.items() ]
                print()
   
    elif findexX27.errors:
        print("findexX27 has errors: %s " % (findexX27.errors))
 

    return locals()


@action('contact', method=["GET", "POST"] )
@action.uses(Template('contact.html', delimiters='[%[ ]]',), db, session,  T, )

def contact(id=None):
    ctrl_info= "ctrl: contact, view: contact.html"
    messages = []

    dfcontact0_row= None
    id_dfcontact0 = None
    fcontact0= Form(db.dfcontact0, id, deletable=False, dbio = False, keep_values = False, form_name = "fcontact0",  formstyle=FormStyleBulma )
   
    if fcontact0.accepted:

        Glb['debug'] and print("     fcontact0 accepted with: %s " % (fcontact0.vars))
        fcontact0_f0 = fcontact0.vars.get('f0','')
        if len ( fcontact0_f0 ):
            id_dfcontact0 = db.dfcontact0.insert( **fcontact0.vars )
            db.commit()

            if not id_dfcontact0 is None:
                dfcontact0_row = db.dfcontact0(id_dfcontact0 )

                if not dfcontact0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcontact0.vars.f0}\" into db.dfcontact0.f0, id = {id_dfcontact0}' )
                         print(f"     found db.dfcontact0.f0: \"{dfcontact0_row.f0}\", id = {id_dfcontact0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fcontact0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fcontact0.vars.items() ]
                print()
   
    elif fcontact0.errors:
        print("fcontact0 has errors: %s " % (fcontact0.errors))
 

    dfcontact1_row= None
    id_dfcontact1 = None
    fcontact1= Form(db.dfcontact1, id, deletable=False, dbio = False, keep_values = False, form_name = "fcontact1",  formstyle=FormStyleBulma )
   
    if fcontact1.accepted:

        Glb['debug'] and print("     fcontact1 accepted with: %s " % (fcontact1.vars))
        fcontact1_f0 = fcontact1.vars.get('f0','')
        if len ( fcontact1_f0 ):
            id_dfcontact1 = db.dfcontact1.insert( **fcontact1.vars )
            db.commit()

            if not id_dfcontact1 is None:
                dfcontact1_row = db.dfcontact1(id_dfcontact1 )

                if not dfcontact1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcontact1.vars.f0}\" into db.dfcontact1.f0, id = {id_dfcontact1}' )
                         print(f"     found db.dfcontact1.f0: \"{dfcontact1_row.f0}\", id = {id_dfcontact1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fcontact1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fcontact1.vars.items() ]
                print()
   
    elif fcontact1.errors:
        print("fcontact1 has errors: %s " % (fcontact1.errors))
 

    return locals()


@action('buttons', method=["GET", "POST"] )
@action.uses(Template('buttons.html', delimiters='[%[ ]]',), db, session,  T, )

def buttons(id=None):
    ctrl_info= "ctrl: buttons, view: buttons.html"
    messages = []

    dfbuttons0_row= None
    id_dfbuttons0 = None
    fbuttons0= Form(db.dfbuttons0, id, deletable=False, dbio = False, keep_values = False, form_name = "fbuttons0",  formstyle=FormStyleBulma )
   
    if fbuttons0.accepted:

        Glb['debug'] and print("     fbuttons0 accepted with: %s " % (fbuttons0.vars))
        fbuttons0_f0 = fbuttons0.vars.get('f0','')
        if len ( fbuttons0_f0 ):
            id_dfbuttons0 = db.dfbuttons0.insert( **fbuttons0.vars )
            db.commit()

            if not id_dfbuttons0 is None:
                dfbuttons0_row = db.dfbuttons0(id_dfbuttons0 )

                if not dfbuttons0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fbuttons0.vars.f0}\" into db.dfbuttons0.f0, id = {id_dfbuttons0}' )
                         print(f"     found db.dfbuttons0.f0: \"{dfbuttons0_row.f0}\", id = {id_dfbuttons0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fbuttons0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fbuttons0.vars.items() ]
                print()
   
    elif fbuttons0.errors:
        print("fbuttons0 has errors: %s " % (fbuttons0.errors))
 

    dfbuttons1_row= None
    id_dfbuttons1 = None
    fbuttons1= Form(db.dfbuttons1, id, deletable=False, dbio = False, keep_values = False, form_name = "fbuttons1",  formstyle=FormStyleBulma )
   
    if fbuttons1.accepted:

        Glb['debug'] and print("     fbuttons1 accepted with: %s " % (fbuttons1.vars))
        fbuttons1_f0 = fbuttons1.vars.get('f0','')
        if len ( fbuttons1_f0 ):
            id_dfbuttons1 = db.dfbuttons1.insert( **fbuttons1.vars )
            db.commit()

            if not id_dfbuttons1 is None:
                dfbuttons1_row = db.dfbuttons1(id_dfbuttons1 )

                if not dfbuttons1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fbuttons1.vars.f0}\" into db.dfbuttons1.f0, id = {id_dfbuttons1}' )
                         print(f"     found db.dfbuttons1.f0: \"{dfbuttons1_row.f0}\", id = {id_dfbuttons1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fbuttons1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fbuttons1.vars.items() ]
                print()
   
    elif fbuttons1.errors:
        print("fbuttons1 has errors: %s " % (fbuttons1.errors))
 

    return locals()


@action('tooltips', method=["GET", "POST"] )
@action.uses(Template('tooltips.html', delimiters='[%[ ]]',), db, session,  T, )

def tooltips(id=None):
    ctrl_info= "ctrl: tooltips, view: tooltips.html"
    messages = []

    dftooltips0_row= None
    id_dftooltips0 = None
    ftooltips0= Form(db.dftooltips0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftooltips0",  formstyle=FormStyleBulma )
   
    if ftooltips0.accepted:

        Glb['debug'] and print("     ftooltips0 accepted with: %s " % (ftooltips0.vars))
        ftooltips0_f0 = ftooltips0.vars.get('f0','')
        if len ( ftooltips0_f0 ):
            id_dftooltips0 = db.dftooltips0.insert( **ftooltips0.vars )
            db.commit()

            if not id_dftooltips0 is None:
                dftooltips0_row = db.dftooltips0(id_dftooltips0 )

                if not dftooltips0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftooltips0.vars.f0}\" into db.dftooltips0.f0, id = {id_dftooltips0}' )
                         print(f"     found db.dftooltips0.f0: \"{dftooltips0_row.f0}\", id = {id_dftooltips0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftooltips0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftooltips0.vars.items() ]
                print()
   
    elif ftooltips0.errors:
        print("ftooltips0 has errors: %s " % (ftooltips0.errors))
 

    dftooltips1_row= None
    id_dftooltips1 = None
    ftooltips1= Form(db.dftooltips1, id, deletable=False, dbio = False, keep_values = False, form_name = "ftooltips1",  formstyle=FormStyleBulma )
   
    if ftooltips1.accepted:

        Glb['debug'] and print("     ftooltips1 accepted with: %s " % (ftooltips1.vars))
        ftooltips1_f0 = ftooltips1.vars.get('f0','')
        if len ( ftooltips1_f0 ):
            id_dftooltips1 = db.dftooltips1.insert( **ftooltips1.vars )
            db.commit()

            if not id_dftooltips1 is None:
                dftooltips1_row = db.dftooltips1(id_dftooltips1 )

                if not dftooltips1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftooltips1.vars.f0}\" into db.dftooltips1.f0, id = {id_dftooltips1}' )
                         print(f"     found db.dftooltips1.f0: \"{dftooltips1_row.f0}\", id = {id_dftooltips1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftooltips1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftooltips1.vars.items() ]
                print()
   
    elif ftooltips1.errors:
        print("ftooltips1 has errors: %s " % (ftooltips1.errors))
 

    return locals()


@action('popovers', method=["GET", "POST"] )
@action.uses(Template('popovers.html', delimiters='[%[ ]]',), db, session,  T, )

def popovers(id=None):
    ctrl_info= "ctrl: popovers, view: popovers.html"
    messages = []

    dfpopovers0_row= None
    id_dfpopovers0 = None
    fpopovers0= Form(db.dfpopovers0, id, deletable=False, dbio = False, keep_values = False, form_name = "fpopovers0",  formstyle=FormStyleBulma )
   
    if fpopovers0.accepted:

        Glb['debug'] and print("     fpopovers0 accepted with: %s " % (fpopovers0.vars))
        fpopovers0_f0 = fpopovers0.vars.get('f0','')
        if len ( fpopovers0_f0 ):
            id_dfpopovers0 = db.dfpopovers0.insert( **fpopovers0.vars )
            db.commit()

            if not id_dfpopovers0 is None:
                dfpopovers0_row = db.dfpopovers0(id_dfpopovers0 )

                if not dfpopovers0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpopovers0.vars.f0}\" into db.dfpopovers0.f0, id = {id_dfpopovers0}' )
                         print(f"     found db.dfpopovers0.f0: \"{dfpopovers0_row.f0}\", id = {id_dfpopovers0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpopovers0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpopovers0.vars.items() ]
                print()
   
    elif fpopovers0.errors:
        print("fpopovers0 has errors: %s " % (fpopovers0.errors))
 

    dfpopovers1_row= None
    id_dfpopovers1 = None
    fpopovers1= Form(db.dfpopovers1, id, deletable=False, dbio = False, keep_values = False, form_name = "fpopovers1",  formstyle=FormStyleBulma )
   
    if fpopovers1.accepted:

        Glb['debug'] and print("     fpopovers1 accepted with: %s " % (fpopovers1.vars))
        fpopovers1_f0 = fpopovers1.vars.get('f0','')
        if len ( fpopovers1_f0 ):
            id_dfpopovers1 = db.dfpopovers1.insert( **fpopovers1.vars )
            db.commit()

            if not id_dfpopovers1 is None:
                dfpopovers1_row = db.dfpopovers1(id_dfpopovers1 )

                if not dfpopovers1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fpopovers1.vars.f0}\" into db.dfpopovers1.f0, id = {id_dfpopovers1}' )
                         print(f"     found db.dfpopovers1.f0: \"{dfpopovers1_row.f0}\", id = {id_dfpopovers1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fpopovers1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fpopovers1.vars.items() ]
                print()
   
    elif fpopovers1.errors:
        print("fpopovers1 has errors: %s " % (fpopovers1.errors))
 

    return locals()


@action('dropdown', method=["GET", "POST"] )
@action.uses(Template('dropdown.html', delimiters='[%[ ]]',), db, session,  T, )

def dropdown(id=None):
    ctrl_info= "ctrl: dropdown, view: dropdown.html"
    messages = []

    dfdropdown0_row= None
    id_dfdropdown0 = None
    fdropdown0= Form(db.dfdropdown0, id, deletable=False, dbio = False, keep_values = False, form_name = "fdropdown0",  formstyle=FormStyleBulma )
   
    if fdropdown0.accepted:

        Glb['debug'] and print("     fdropdown0 accepted with: %s " % (fdropdown0.vars))
        fdropdown0_f0 = fdropdown0.vars.get('f0','')
        if len ( fdropdown0_f0 ):
            id_dfdropdown0 = db.dfdropdown0.insert( **fdropdown0.vars )
            db.commit()

            if not id_dfdropdown0 is None:
                dfdropdown0_row = db.dfdropdown0(id_dfdropdown0 )

                if not dfdropdown0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fdropdown0.vars.f0}\" into db.dfdropdown0.f0, id = {id_dfdropdown0}' )
                         print(f"     found db.dfdropdown0.f0: \"{dfdropdown0_row.f0}\", id = {id_dfdropdown0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fdropdown0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fdropdown0.vars.items() ]
                print()
   
    elif fdropdown0.errors:
        print("fdropdown0 has errors: %s " % (fdropdown0.errors))
 

    dfdropdown1_row= None
    id_dfdropdown1 = None
    fdropdown1= Form(db.dfdropdown1, id, deletable=False, dbio = False, keep_values = False, form_name = "fdropdown1",  formstyle=FormStyleBulma )
   
    if fdropdown1.accepted:

        Glb['debug'] and print("     fdropdown1 accepted with: %s " % (fdropdown1.vars))
        fdropdown1_f0 = fdropdown1.vars.get('f0','')
        if len ( fdropdown1_f0 ):
            id_dfdropdown1 = db.dfdropdown1.insert( **fdropdown1.vars )
            db.commit()

            if not id_dfdropdown1 is None:
                dfdropdown1_row = db.dfdropdown1(id_dfdropdown1 )

                if not dfdropdown1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fdropdown1.vars.f0}\" into db.dfdropdown1.f0, id = {id_dfdropdown1}' )
                         print(f"     found db.dfdropdown1.f0: \"{dfdropdown1_row.f0}\", id = {id_dfdropdown1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fdropdown1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fdropdown1.vars.items() ]
                print()
   
    elif fdropdown1.errors:
        print("fdropdown1 has errors: %s " % (fdropdown1.errors))
 

    return locals()


@action('dataXmap', method=["GET", "POST"] )
@action.uses(Template('data-map.html', delimiters='[%[ ]]',), db, session,  T, )

def dataXmap(id=None):
    ctrl_info= "ctrl: dataXmap, view: data-map.html"
    messages = []

    dfdataXmap0_row= None
    id_dfdataXmap0 = None
    fdataXmap0= Form(db.dfdataXmap0, id, deletable=False, dbio = False, keep_values = False, form_name = "fdataXmap0",  formstyle=FormStyleBulma )
   
    if fdataXmap0.accepted:

        Glb['debug'] and print("     fdataXmap0 accepted with: %s " % (fdataXmap0.vars))
        fdataXmap0_f0 = fdataXmap0.vars.get('f0','')
        if len ( fdataXmap0_f0 ):
            id_dfdataXmap0 = db.dfdataXmap0.insert( **fdataXmap0.vars )
            db.commit()

            if not id_dfdataXmap0 is None:
                dfdataXmap0_row = db.dfdataXmap0(id_dfdataXmap0 )

                if not dfdataXmap0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fdataXmap0.vars.f0}\" into db.dfdataXmap0.f0, id = {id_dfdataXmap0}' )
                         print(f"     found db.dfdataXmap0.f0: \"{dfdataXmap0_row.f0}\", id = {id_dfdataXmap0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fdataXmap0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fdataXmap0.vars.items() ]
                print()
   
    elif fdataXmap0.errors:
        print("fdataXmap0 has errors: %s " % (fdataXmap0.errors))
 

    dfdataXmap1_row= None
    id_dfdataXmap1 = None
    fdataXmap1= Form(db.dfdataXmap1, id, deletable=False, dbio = False, keep_values = False, form_name = "fdataXmap1",  formstyle=FormStyleBulma )
   
    if fdataXmap1.accepted:

        Glb['debug'] and print("     fdataXmap1 accepted with: %s " % (fdataXmap1.vars))
        fdataXmap1_f0 = fdataXmap1.vars.get('f0','')
        if len ( fdataXmap1_f0 ):
            id_dfdataXmap1 = db.dfdataXmap1.insert( **fdataXmap1.vars )
            db.commit()

            if not id_dfdataXmap1 is None:
                dfdataXmap1_row = db.dfdataXmap1(id_dfdataXmap1 )

                if not dfdataXmap1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fdataXmap1.vars.f0}\" into db.dfdataXmap1.f0, id = {id_dfdataXmap1}' )
                         print(f"     found db.dfdataXmap1.f0: \"{dfdataXmap1_row.f0}\", id = {id_dfdataXmap1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fdataXmap1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fdataXmap1.vars.items() ]
                print()
   
    elif fdataXmap1.errors:
        print("fdataXmap1 has errors: %s " % (fdataXmap1.errors))
 

    return locals()


@action('analytics', method=["GET", "POST"] )
@action.uses(Template('analytics.html', delimiters='[%[ ]]',), db, session,  T, )

def analytics(id=None):
    ctrl_info= "ctrl: analytics, view: analytics.html"
    messages = []

    rows_tanalytics0= db(db.tanalytics0).select()
    rows_tanalytics1= db(db.tanalytics1).select()
    rows_tanalytics2= db(db.tanalytics2).select()
    dfanalytics0_row= None
    id_dfanalytics0 = None
    fanalytics0= Form(db.dfanalytics0, id, deletable=False, dbio = False, keep_values = False, form_name = "fanalytics0",  formstyle=FormStyleBulma )
   
    if fanalytics0.accepted:

        Glb['debug'] and print("     fanalytics0 accepted with: %s " % (fanalytics0.vars))
        fanalytics0_f0 = fanalytics0.vars.get('f0','')
        if len ( fanalytics0_f0 ):
            id_dfanalytics0 = db.dfanalytics0.insert( **fanalytics0.vars )
            db.commit()

            if not id_dfanalytics0 is None:
                dfanalytics0_row = db.dfanalytics0(id_dfanalytics0 )

                if not dfanalytics0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fanalytics0.vars.f0}\" into db.dfanalytics0.f0, id = {id_dfanalytics0}' )
                         print(f"     found db.dfanalytics0.f0: \"{dfanalytics0_row.f0}\", id = {id_dfanalytics0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fanalytics0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fanalytics0.vars.items() ]
                print()
   
    elif fanalytics0.errors:
        print("fanalytics0 has errors: %s " % (fanalytics0.errors))
 

    dfanalytics1_row= None
    id_dfanalytics1 = None
    fanalytics1= Form(db.dfanalytics1, id, deletable=False, dbio = False, keep_values = False, form_name = "fanalytics1",  formstyle=FormStyleBulma )
   
    if fanalytics1.accepted:

        Glb['debug'] and print("     fanalytics1 accepted with: %s " % (fanalytics1.vars))
        fanalytics1_f0 = fanalytics1.vars.get('f0','')
        if len ( fanalytics1_f0 ):
            id_dfanalytics1 = db.dfanalytics1.insert( **fanalytics1.vars )
            db.commit()

            if not id_dfanalytics1 is None:
                dfanalytics1_row = db.dfanalytics1(id_dfanalytics1 )

                if not dfanalytics1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fanalytics1.vars.f0}\" into db.dfanalytics1.f0, id = {id_dfanalytics1}' )
                         print(f"     found db.dfanalytics1.f0: \"{dfanalytics1_row.f0}\", id = {id_dfanalytics1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fanalytics1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fanalytics1.vars.items() ]
                print()
   
    elif fanalytics1.errors:
        print("fanalytics1 has errors: %s " % (fanalytics1.errors))
 

    return locals()


@action('accordion', method=["GET", "POST"] )
@action.uses(Template('accordion.html', delimiters='[%[ ]]',), db, session,  T, )

def accordion(id=None):
    ctrl_info= "ctrl: accordion, view: accordion.html"
    messages = []

    dfaccordion0_row= None
    id_dfaccordion0 = None
    faccordion0= Form(db.dfaccordion0, id, deletable=False, dbio = False, keep_values = False, form_name = "faccordion0",  formstyle=FormStyleBulma )
   
    if faccordion0.accepted:

        Glb['debug'] and print("     faccordion0 accepted with: %s " % (faccordion0.vars))
        faccordion0_f0 = faccordion0.vars.get('f0','')
        if len ( faccordion0_f0 ):
            id_dfaccordion0 = db.dfaccordion0.insert( **faccordion0.vars )
            db.commit()

            if not id_dfaccordion0 is None:
                dfaccordion0_row = db.dfaccordion0(id_dfaccordion0 )

                if not dfaccordion0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{faccordion0.vars.f0}\" into db.dfaccordion0.f0, id = {id_dfaccordion0}' )
                         print(f"     found db.dfaccordion0.f0: \"{dfaccordion0_row.f0}\", id = {id_dfaccordion0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(faccordion0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in faccordion0.vars.items() ]
                print()
   
    elif faccordion0.errors:
        print("faccordion0 has errors: %s " % (faccordion0.errors))
 

    dfaccordion1_row= None
    id_dfaccordion1 = None
    faccordion1= Form(db.dfaccordion1, id, deletable=False, dbio = False, keep_values = False, form_name = "faccordion1",  formstyle=FormStyleBulma )
   
    if faccordion1.accepted:

        Glb['debug'] and print("     faccordion1 accepted with: %s " % (faccordion1.vars))
        faccordion1_f0 = faccordion1.vars.get('f0','')
        if len ( faccordion1_f0 ):
            id_dfaccordion1 = db.dfaccordion1.insert( **faccordion1.vars )
            db.commit()

            if not id_dfaccordion1 is None:
                dfaccordion1_row = db.dfaccordion1(id_dfaccordion1 )

                if not dfaccordion1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{faccordion1.vars.f0}\" into db.dfaccordion1.f0, id = {id_dfaccordion1}' )
                         print(f"     found db.dfaccordion1.f0: \"{dfaccordion1_row.f0}\", id = {id_dfaccordion1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(faccordion1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in faccordion1.vars.items() ]
                print()
   
    elif faccordion1.errors:
        print("faccordion1 has errors: %s " % (faccordion1.errors))
 

    return locals()


@action('viewXemail', method=["GET", "POST"] )
@action.uses(Template('view-email.html', delimiters='[%[ ]]',), db, session,  T, )

def viewXemail(id=None):
    ctrl_info= "ctrl: viewXemail, view: view-email.html"
    messages = []

    dfviewXemail0_row= None
    id_dfviewXemail0 = None
    fviewXemail0= Form(db.dfviewXemail0, id, deletable=False, dbio = False, keep_values = False, form_name = "fviewXemail0",  formstyle=FormStyleBulma )
   
    if fviewXemail0.accepted:

        Glb['debug'] and print("     fviewXemail0 accepted with: %s " % (fviewXemail0.vars))
        fviewXemail0_f0 = fviewXemail0.vars.get('f0','')
        if len ( fviewXemail0_f0 ):
            id_dfviewXemail0 = db.dfviewXemail0.insert( **fviewXemail0.vars )
            db.commit()

            if not id_dfviewXemail0 is None:
                dfviewXemail0_row = db.dfviewXemail0(id_dfviewXemail0 )

                if not dfviewXemail0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fviewXemail0.vars.f0}\" into db.dfviewXemail0.f0, id = {id_dfviewXemail0}' )
                         print(f"     found db.dfviewXemail0.f0: \"{dfviewXemail0_row.f0}\", id = {id_dfviewXemail0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fviewXemail0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fviewXemail0.vars.items() ]
                print()
   
    elif fviewXemail0.errors:
        print("fviewXemail0 has errors: %s " % (fviewXemail0.errors))
 

    dfviewXemail1_row= None
    id_dfviewXemail1 = None
    fviewXemail1= Form(db.dfviewXemail1, id, deletable=False, dbio = False, keep_values = False, form_name = "fviewXemail1",  formstyle=FormStyleBulma )
   
    if fviewXemail1.accepted:

        Glb['debug'] and print("     fviewXemail1 accepted with: %s " % (fviewXemail1.vars))
        fviewXemail1_f0 = fviewXemail1.vars.get('f0','')
        if len ( fviewXemail1_f0 ):
            id_dfviewXemail1 = db.dfviewXemail1.insert( **fviewXemail1.vars )
            db.commit()

            if not id_dfviewXemail1 is None:
                dfviewXemail1_row = db.dfviewXemail1(id_dfviewXemail1 )

                if not dfviewXemail1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fviewXemail1.vars.f0}\" into db.dfviewXemail1.f0, id = {id_dfviewXemail1}' )
                         print(f"     found db.dfviewXemail1.f0: \"{dfviewXemail1_row.f0}\", id = {id_dfviewXemail1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fviewXemail1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fviewXemail1.vars.items() ]
                print()
   
    elif fviewXemail1.errors:
        print("fviewXemail1 has errors: %s " % (fviewXemail1.errors))
 

    return locals()


@action('typography', method=["GET", "POST"] )
@action.uses(Template('typography.html', delimiters='[%[ ]]',), db, session,  T, )

def typography(id=None):
    ctrl_info= "ctrl: typography, view: typography.html"
    messages = []

    dftypography0_row= None
    id_dftypography0 = None
    ftypography0= Form(db.dftypography0, id, deletable=False, dbio = False, keep_values = False, form_name = "ftypography0",  formstyle=FormStyleBulma )
   
    if ftypography0.accepted:

        Glb['debug'] and print("     ftypography0 accepted with: %s " % (ftypography0.vars))
        ftypography0_f0 = ftypography0.vars.get('f0','')
        if len ( ftypography0_f0 ):
            id_dftypography0 = db.dftypography0.insert( **ftypography0.vars )
            db.commit()

            if not id_dftypography0 is None:
                dftypography0_row = db.dftypography0(id_dftypography0 )

                if not dftypography0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftypography0.vars.f0}\" into db.dftypography0.f0, id = {id_dftypography0}' )
                         print(f"     found db.dftypography0.f0: \"{dftypography0_row.f0}\", id = {id_dftypography0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftypography0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftypography0.vars.items() ]
                print()
   
    elif ftypography0.errors:
        print("ftypography0 has errors: %s " % (ftypography0.errors))
 

    dftypography1_row= None
    id_dftypography1 = None
    ftypography1= Form(db.dftypography1, id, deletable=False, dbio = False, keep_values = False, form_name = "ftypography1",  formstyle=FormStyleBulma )
   
    if ftypography1.accepted:

        Glb['debug'] and print("     ftypography1 accepted with: %s " % (ftypography1.vars))
        ftypography1_f0 = ftypography1.vars.get('f0','')
        if len ( ftypography1_f0 ):
            id_dftypography1 = db.dftypography1.insert( **ftypography1.vars )
            db.commit()

            if not id_dftypography1 is None:
                dftypography1_row = db.dftypography1(id_dftypography1 )

                if not dftypography1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{ftypography1.vars.f0}\" into db.dftypography1.f0, id = {id_dftypography1}' )
                         print(f"     found db.dftypography1.f0: \"{dftypography1_row.f0}\", id = {id_dftypography1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(ftypography1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in ftypography1.vars.items() ]
                print()
   
    elif ftypography1.errors:
        print("ftypography1 has errors: %s " % (ftypography1.errors))
 

    return locals()


@action('googleXmap', method=["GET", "POST"] )
@action.uses(Template('google-map.html', delimiters='[%[ ]]',), db, session,  T, )

def googleXmap(id=None):
    ctrl_info= "ctrl: googleXmap, view: google-map.html"
    messages = []

    dfgoogleXmap0_row= None
    id_dfgoogleXmap0 = None
    fgoogleXmap0= Form(db.dfgoogleXmap0, id, deletable=False, dbio = False, keep_values = False, form_name = "fgoogleXmap0",  formstyle=FormStyleBulma )
   
    if fgoogleXmap0.accepted:

        Glb['debug'] and print("     fgoogleXmap0 accepted with: %s " % (fgoogleXmap0.vars))
        fgoogleXmap0_f0 = fgoogleXmap0.vars.get('f0','')
        if len ( fgoogleXmap0_f0 ):
            id_dfgoogleXmap0 = db.dfgoogleXmap0.insert( **fgoogleXmap0.vars )
            db.commit()

            if not id_dfgoogleXmap0 is None:
                dfgoogleXmap0_row = db.dfgoogleXmap0(id_dfgoogleXmap0 )

                if not dfgoogleXmap0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fgoogleXmap0.vars.f0}\" into db.dfgoogleXmap0.f0, id = {id_dfgoogleXmap0}' )
                         print(f"     found db.dfgoogleXmap0.f0: \"{dfgoogleXmap0_row.f0}\", id = {id_dfgoogleXmap0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fgoogleXmap0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fgoogleXmap0.vars.items() ]
                print()
   
    elif fgoogleXmap0.errors:
        print("fgoogleXmap0 has errors: %s " % (fgoogleXmap0.errors))
 

    dfgoogleXmap1_row= None
    id_dfgoogleXmap1 = None
    fgoogleXmap1= Form(db.dfgoogleXmap1, id, deletable=False, dbio = False, keep_values = False, form_name = "fgoogleXmap1",  formstyle=FormStyleBulma )
   
    if fgoogleXmap1.accepted:

        Glb['debug'] and print("     fgoogleXmap1 accepted with: %s " % (fgoogleXmap1.vars))
        fgoogleXmap1_f0 = fgoogleXmap1.vars.get('f0','')
        if len ( fgoogleXmap1_f0 ):
            id_dfgoogleXmap1 = db.dfgoogleXmap1.insert( **fgoogleXmap1.vars )
            db.commit()

            if not id_dfgoogleXmap1 is None:
                dfgoogleXmap1_row = db.dfgoogleXmap1(id_dfgoogleXmap1 )

                if not dfgoogleXmap1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fgoogleXmap1.vars.f0}\" into db.dfgoogleXmap1.f0, id = {id_dfgoogleXmap1}' )
                         print(f"     found db.dfgoogleXmap1.f0: \"{dfgoogleXmap1_row.f0}\", id = {id_dfgoogleXmap1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fgoogleXmap1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fgoogleXmap1.vars.items() ]
                print()
   
    elif fgoogleXmap1.errors:
        print("fgoogleXmap1 has errors: %s " % (fgoogleXmap1.errors))
 

    return locals()


@action('dataXtable', method=["GET", "POST"] )
@action.uses(Template('data-table.html', delimiters='[%[ ]]',), db, session,  T, )

def dataXtable(id=None):
    ctrl_info= "ctrl: dataXtable, view: data-table.html"
    messages = []

    rows_tdataXtable0= db(db.tdataXtable0).select()
    dfdataXtable0_row= None
    id_dfdataXtable0 = None
    fdataXtable0= Form(db.dfdataXtable0, id, deletable=False, dbio = False, keep_values = False, form_name = "fdataXtable0",  formstyle=FormStyleBulma )
   
    if fdataXtable0.accepted:

        Glb['debug'] and print("     fdataXtable0 accepted with: %s " % (fdataXtable0.vars))
        fdataXtable0_f0 = fdataXtable0.vars.get('f0','')
        if len ( fdataXtable0_f0 ):
            id_dfdataXtable0 = db.dfdataXtable0.insert( **fdataXtable0.vars )
            db.commit()

            if not id_dfdataXtable0 is None:
                dfdataXtable0_row = db.dfdataXtable0(id_dfdataXtable0 )

                if not dfdataXtable0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fdataXtable0.vars.f0}\" into db.dfdataXtable0.f0, id = {id_dfdataXtable0}' )
                         print(f"     found db.dfdataXtable0.f0: \"{dfdataXtable0_row.f0}\", id = {id_dfdataXtable0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fdataXtable0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fdataXtable0.vars.items() ]
                print()
   
    elif fdataXtable0.errors:
        print("fdataXtable0 has errors: %s " % (fdataXtable0.errors))
 

    dfdataXtable1_row= None
    id_dfdataXtable1 = None
    fdataXtable1= Form(db.dfdataXtable1, id, deletable=False, dbio = False, keep_values = False, form_name = "fdataXtable1",  formstyle=FormStyleBulma )
   
    if fdataXtable1.accepted:

        Glb['debug'] and print("     fdataXtable1 accepted with: %s " % (fdataXtable1.vars))
        fdataXtable1_f0 = fdataXtable1.vars.get('f0','')
        if len ( fdataXtable1_f0 ):
            id_dfdataXtable1 = db.dfdataXtable1.insert( **fdataXtable1.vars )
            db.commit()

            if not id_dfdataXtable1 is None:
                dfdataXtable1_row = db.dfdataXtable1(id_dfdataXtable1 )

                if not dfdataXtable1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fdataXtable1.vars.f0}\" into db.dfdataXtable1.f0, id = {id_dfdataXtable1}' )
                         print(f"     found db.dfdataXtable1.f0: \"{dfdataXtable1_row.f0}\", id = {id_dfdataXtable1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fdataXtable1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fdataXtable1.vars.items() ]
                print()
   
    elif fdataXtable1.errors:
        print("fdataXtable1 has errors: %s " % (fdataXtable1.errors))
 

    return locals()


@action('barXcharts', method=["GET", "POST"] )
@action.uses(Template('bar-charts.html', delimiters='[%[ ]]',), db, session,  T, )

def barXcharts(id=None):
    ctrl_info= "ctrl: barXcharts, view: bar-charts.html"
    messages = []

    dfbarXcharts0_row= None
    id_dfbarXcharts0 = None
    fbarXcharts0= Form(db.dfbarXcharts0, id, deletable=False, dbio = False, keep_values = False, form_name = "fbarXcharts0",  formstyle=FormStyleBulma )
   
    if fbarXcharts0.accepted:

        Glb['debug'] and print("     fbarXcharts0 accepted with: %s " % (fbarXcharts0.vars))
        fbarXcharts0_f0 = fbarXcharts0.vars.get('f0','')
        if len ( fbarXcharts0_f0 ):
            id_dfbarXcharts0 = db.dfbarXcharts0.insert( **fbarXcharts0.vars )
            db.commit()

            if not id_dfbarXcharts0 is None:
                dfbarXcharts0_row = db.dfbarXcharts0(id_dfbarXcharts0 )

                if not dfbarXcharts0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fbarXcharts0.vars.f0}\" into db.dfbarXcharts0.f0, id = {id_dfbarXcharts0}' )
                         print(f"     found db.dfbarXcharts0.f0: \"{dfbarXcharts0_row.f0}\", id = {id_dfbarXcharts0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fbarXcharts0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fbarXcharts0.vars.items() ]
                print()
   
    elif fbarXcharts0.errors:
        print("fbarXcharts0 has errors: %s " % (fbarXcharts0.errors))
 

    dfbarXcharts1_row= None
    id_dfbarXcharts1 = None
    fbarXcharts1= Form(db.dfbarXcharts1, id, deletable=False, dbio = False, keep_values = False, form_name = "fbarXcharts1",  formstyle=FormStyleBulma )
   
    if fbarXcharts1.accepted:

        Glb['debug'] and print("     fbarXcharts1 accepted with: %s " % (fbarXcharts1.vars))
        fbarXcharts1_f0 = fbarXcharts1.vars.get('f0','')
        if len ( fbarXcharts1_f0 ):
            id_dfbarXcharts1 = db.dfbarXcharts1.insert( **fbarXcharts1.vars )
            db.commit()

            if not id_dfbarXcharts1 is None:
                dfbarXcharts1_row = db.dfbarXcharts1(id_dfbarXcharts1 )

                if not dfbarXcharts1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fbarXcharts1.vars.f0}\" into db.dfbarXcharts1.f0, id = {id_dfbarXcharts1}' )
                         print(f"     found db.dfbarXcharts1.f0: \"{dfbarXcharts1_row.f0}\", id = {id_dfbarXcharts1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fbarXcharts1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fbarXcharts1.vars.items() ]
                print()
   
    elif fbarXcharts1.errors:
        print("fbarXcharts1 has errors: %s " % (fbarXcharts1.errors))
 

    return locals()


@action('animations', method=["GET", "POST"] )
@action.uses(Template('animations.html', delimiters='[%[ ]]',), db, session,  T, )

def animations(id=None):
    ctrl_info= "ctrl: animations, view: animations.html"
    messages = []

    dfanimations0_row= None
    id_dfanimations0 = None
    fanimations0= Form(db.dfanimations0, id, deletable=False, dbio = False, keep_values = False, form_name = "fanimations0",  formstyle=FormStyleBulma )
   
    if fanimations0.accepted:

        Glb['debug'] and print("     fanimations0 accepted with: %s " % (fanimations0.vars))
        fanimations0_f0 = fanimations0.vars.get('f0','')
        if len ( fanimations0_f0 ):
            id_dfanimations0 = db.dfanimations0.insert( **fanimations0.vars )
            db.commit()

            if not id_dfanimations0 is None:
                dfanimations0_row = db.dfanimations0(id_dfanimations0 )

                if not dfanimations0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fanimations0.vars.f0}\" into db.dfanimations0.f0, id = {id_dfanimations0}' )
                         print(f"     found db.dfanimations0.f0: \"{dfanimations0_row.f0}\", id = {id_dfanimations0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fanimations0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fanimations0.vars.items() ]
                print()
   
    elif fanimations0.errors:
        print("fanimations0 has errors: %s " % (fanimations0.errors))
 

    dfanimations1_row= None
    id_dfanimations1 = None
    fanimations1= Form(db.dfanimations1, id, deletable=False, dbio = False, keep_values = False, form_name = "fanimations1",  formstyle=FormStyleBulma )
   
    if fanimations1.accepted:

        Glb['debug'] and print("     fanimations1 accepted with: %s " % (fanimations1.vars))
        fanimations1_f0 = fanimations1.vars.get('f0','')
        if len ( fanimations1_f0 ):
            id_dfanimations1 = db.dfanimations1.insert( **fanimations1.vars )
            db.commit()

            if not id_dfanimations1 is None:
                dfanimations1_row = db.dfanimations1(id_dfanimations1 )

                if not dfanimations1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fanimations1.vars.f0}\" into db.dfanimations1.f0, id = {id_dfanimations1}' )
                         print(f"     found db.dfanimations1.f0: \"{dfanimations1_row.f0}\", id = {id_dfanimations1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fanimations1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fanimations1.vars.items() ]
                print()
   
    elif fanimations1.errors:
        print("fanimations1 has errors: %s " % (fanimations1.errors))
 

    return locals()


@action('lineXcharts', method=["GET", "POST"] )
@action.uses(Template('line-charts.html', delimiters='[%[ ]]',), db, session,  T, )

def lineXcharts(id=None):
    ctrl_info= "ctrl: lineXcharts, view: line-charts.html"
    messages = []

    dflineXcharts0_row= None
    id_dflineXcharts0 = None
    flineXcharts0= Form(db.dflineXcharts0, id, deletable=False, dbio = False, keep_values = False, form_name = "flineXcharts0",  formstyle=FormStyleBulma )
   
    if flineXcharts0.accepted:

        Glb['debug'] and print("     flineXcharts0 accepted with: %s " % (flineXcharts0.vars))
        flineXcharts0_f0 = flineXcharts0.vars.get('f0','')
        if len ( flineXcharts0_f0 ):
            id_dflineXcharts0 = db.dflineXcharts0.insert( **flineXcharts0.vars )
            db.commit()

            if not id_dflineXcharts0 is None:
                dflineXcharts0_row = db.dflineXcharts0(id_dflineXcharts0 )

                if not dflineXcharts0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flineXcharts0.vars.f0}\" into db.dflineXcharts0.f0, id = {id_dflineXcharts0}' )
                         print(f"     found db.dflineXcharts0.f0: \"{dflineXcharts0_row.f0}\", id = {id_dflineXcharts0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(flineXcharts0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in flineXcharts0.vars.items() ]
                print()
   
    elif flineXcharts0.errors:
        print("flineXcharts0 has errors: %s " % (flineXcharts0.errors))
 

    dflineXcharts1_row= None
    id_dflineXcharts1 = None
    flineXcharts1= Form(db.dflineXcharts1, id, deletable=False, dbio = False, keep_values = False, form_name = "flineXcharts1",  formstyle=FormStyleBulma )
   
    if flineXcharts1.accepted:

        Glb['debug'] and print("     flineXcharts1 accepted with: %s " % (flineXcharts1.vars))
        flineXcharts1_f0 = flineXcharts1.vars.get('f0','')
        if len ( flineXcharts1_f0 ):
            id_dflineXcharts1 = db.dflineXcharts1.insert( **flineXcharts1.vars )
            db.commit()

            if not id_dflineXcharts1 is None:
                dflineXcharts1_row = db.dflineXcharts1(id_dflineXcharts1 )

                if not dflineXcharts1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{flineXcharts1.vars.f0}\" into db.dflineXcharts1.f0, id = {id_dflineXcharts1}' )
                         print(f"     found db.dflineXcharts1.f0: \"{dflineXcharts1_row.f0}\", id = {id_dflineXcharts1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(flineXcharts1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in flineXcharts1.vars.items() ]
                print()
   
    elif flineXcharts1.errors:
        print("flineXcharts1 has errors: %s " % (flineXcharts1.errors))
 

    return locals()


@action('flotXcharts', method=["GET", "POST"] )
@action.uses(Template('flot-charts.html', delimiters='[%[ ]]',), db, session,  T, )

def flotXcharts(id=None):
    ctrl_info= "ctrl: flotXcharts, view: flot-charts.html"
    messages = []

    dfflotXcharts0_row= None
    id_dfflotXcharts0 = None
    fflotXcharts0= Form(db.dfflotXcharts0, id, deletable=False, dbio = False, keep_values = False, form_name = "fflotXcharts0",  formstyle=FormStyleBulma )
   
    if fflotXcharts0.accepted:

        Glb['debug'] and print("     fflotXcharts0 accepted with: %s " % (fflotXcharts0.vars))
        fflotXcharts0_f0 = fflotXcharts0.vars.get('f0','')
        if len ( fflotXcharts0_f0 ):
            id_dfflotXcharts0 = db.dfflotXcharts0.insert( **fflotXcharts0.vars )
            db.commit()

            if not id_dfflotXcharts0 is None:
                dfflotXcharts0_row = db.dfflotXcharts0(id_dfflotXcharts0 )

                if not dfflotXcharts0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fflotXcharts0.vars.f0}\" into db.dfflotXcharts0.f0, id = {id_dfflotXcharts0}' )
                         print(f"     found db.dfflotXcharts0.f0: \"{dfflotXcharts0_row.f0}\", id = {id_dfflotXcharts0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fflotXcharts0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fflotXcharts0.vars.items() ]
                print()
   
    elif fflotXcharts0.errors:
        print("fflotXcharts0 has errors: %s " % (fflotXcharts0.errors))
 

    dfflotXcharts1_row= None
    id_dfflotXcharts1 = None
    fflotXcharts1= Form(db.dfflotXcharts1, id, deletable=False, dbio = False, keep_values = False, form_name = "fflotXcharts1",  formstyle=FormStyleBulma )
   
    if fflotXcharts1.accepted:

        Glb['debug'] and print("     fflotXcharts1 accepted with: %s " % (fflotXcharts1.vars))
        fflotXcharts1_f0 = fflotXcharts1.vars.get('f0','')
        if len ( fflotXcharts1_f0 ):
            id_dfflotXcharts1 = db.dfflotXcharts1.insert( **fflotXcharts1.vars )
            db.commit()

            if not id_dfflotXcharts1 is None:
                dfflotXcharts1_row = db.dfflotXcharts1(id_dfflotXcharts1 )

                if not dfflotXcharts1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fflotXcharts1.vars.f0}\" into db.dfflotXcharts1.f0, id = {id_dfflotXcharts1}' )
                         print(f"     found db.dfflotXcharts1.f0: \"{dfflotXcharts1_row.f0}\", id = {id_dfflotXcharts1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fflotXcharts1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fflotXcharts1.vars.items() ]
                print()
   
    elif fflotXcharts1.errors:
        print("fflotXcharts1 has errors: %s " % (fflotXcharts1.errors))
 

    return locals()


@action('areaXcharts', method=["GET", "POST"] )
@action.uses(Template('area-charts.html', delimiters='[%[ ]]',), db, session,  T, )

def areaXcharts(id=None):
    ctrl_info= "ctrl: areaXcharts, view: area-charts.html"
    messages = []

    dfareaXcharts0_row= None
    id_dfareaXcharts0 = None
    fareaXcharts0= Form(db.dfareaXcharts0, id, deletable=False, dbio = False, keep_values = False, form_name = "fareaXcharts0",  formstyle=FormStyleBulma )
   
    if fareaXcharts0.accepted:

        Glb['debug'] and print("     fareaXcharts0 accepted with: %s " % (fareaXcharts0.vars))
        fareaXcharts0_f0 = fareaXcharts0.vars.get('f0','')
        if len ( fareaXcharts0_f0 ):
            id_dfareaXcharts0 = db.dfareaXcharts0.insert( **fareaXcharts0.vars )
            db.commit()

            if not id_dfareaXcharts0 is None:
                dfareaXcharts0_row = db.dfareaXcharts0(id_dfareaXcharts0 )

                if not dfareaXcharts0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fareaXcharts0.vars.f0}\" into db.dfareaXcharts0.f0, id = {id_dfareaXcharts0}' )
                         print(f"     found db.dfareaXcharts0.f0: \"{dfareaXcharts0_row.f0}\", id = {id_dfareaXcharts0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fareaXcharts0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fareaXcharts0.vars.items() ]
                print()
   
    elif fareaXcharts0.errors:
        print("fareaXcharts0 has errors: %s " % (fareaXcharts0.errors))
 

    dfareaXcharts1_row= None
    id_dfareaXcharts1 = None
    fareaXcharts1= Form(db.dfareaXcharts1, id, deletable=False, dbio = False, keep_values = False, form_name = "fareaXcharts1",  formstyle=FormStyleBulma )
   
    if fareaXcharts1.accepted:

        Glb['debug'] and print("     fareaXcharts1 accepted with: %s " % (fareaXcharts1.vars))
        fareaXcharts1_f0 = fareaXcharts1.vars.get('f0','')
        if len ( fareaXcharts1_f0 ):
            id_dfareaXcharts1 = db.dfareaXcharts1.insert( **fareaXcharts1.vars )
            db.commit()

            if not id_dfareaXcharts1 is None:
                dfareaXcharts1_row = db.dfareaXcharts1(id_dfareaXcharts1 )

                if not dfareaXcharts1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fareaXcharts1.vars.f0}\" into db.dfareaXcharts1.f0, id = {id_dfareaXcharts1}' )
                         print(f"     found db.dfareaXcharts1.f0: \"{dfareaXcharts1_row.f0}\", id = {id_dfareaXcharts1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fareaXcharts1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fareaXcharts1.vars.items() ]
                print()
   
    elif fareaXcharts1.errors:
        print("fareaXcharts1 has errors: %s " % (fareaXcharts1.errors))
 

    return locals()


@action('codeXeditor', method=["GET", "POST"] )
@action.uses(Template('code-editor.html', delimiters='[%[ ]]',), db, session,  T, )

def codeXeditor(id=None):
    ctrl_info= "ctrl: codeXeditor, view: code-editor.html"
    messages = []

    dfcodeXeditor0_row= None
    id_dfcodeXeditor0 = None
    fcodeXeditor0= Form(db.dfcodeXeditor0, id, deletable=False, dbio = False, keep_values = False, form_name = "fcodeXeditor0",  formstyle=FormStyleBulma )
   
    if fcodeXeditor0.accepted:

        Glb['debug'] and print("     fcodeXeditor0 accepted with: %s " % (fcodeXeditor0.vars))
        fcodeXeditor0_f0 = fcodeXeditor0.vars.get('f0','')
        if len ( fcodeXeditor0_f0 ):
            id_dfcodeXeditor0 = db.dfcodeXeditor0.insert( **fcodeXeditor0.vars )
            db.commit()

            if not id_dfcodeXeditor0 is None:
                dfcodeXeditor0_row = db.dfcodeXeditor0(id_dfcodeXeditor0 )

                if not dfcodeXeditor0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcodeXeditor0.vars.f0}\" into db.dfcodeXeditor0.f0, id = {id_dfcodeXeditor0}' )
                         print(f"     found db.dfcodeXeditor0.f0: \"{dfcodeXeditor0_row.f0}\", id = {id_dfcodeXeditor0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fcodeXeditor0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fcodeXeditor0.vars.items() ]
                print()
   
    elif fcodeXeditor0.errors:
        print("fcodeXeditor0 has errors: %s " % (fcodeXeditor0.errors))
 

    dfcodeXeditor1_row= None
    id_dfcodeXeditor1 = None
    fcodeXeditor1= Form(db.dfcodeXeditor1, id, deletable=False, dbio = False, keep_values = False, form_name = "fcodeXeditor1",  formstyle=FormStyleBulma )
   
    if fcodeXeditor1.accepted:

        Glb['debug'] and print("     fcodeXeditor1 accepted with: %s " % (fcodeXeditor1.vars))
        fcodeXeditor1_f0 = fcodeXeditor1.vars.get('f0','')
        if len ( fcodeXeditor1_f0 ):
            id_dfcodeXeditor1 = db.dfcodeXeditor1.insert( **fcodeXeditor1.vars )
            db.commit()

            if not id_dfcodeXeditor1 is None:
                dfcodeXeditor1_row = db.dfcodeXeditor1(id_dfcodeXeditor1 )

                if not dfcodeXeditor1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcodeXeditor1.vars.f0}\" into db.dfcodeXeditor1.f0, id = {id_dfcodeXeditor1}' )
                         print(f"     found db.dfcodeXeditor1.f0: \"{dfcodeXeditor1_row.f0}\", id = {id_dfcodeXeditor1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fcodeXeditor1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fcodeXeditor1.vars.items() ]
                print()
   
    elif fcodeXeditor1.errors:
        print("fcodeXeditor1 has errors: %s " % (fcodeXeditor1.errors))
 

    return locals()


@action('normalXtable', method=["GET", "POST"] )
@action.uses(Template('normal-table.html', delimiters='[%[ ]]',), db, session,  T, )

def normalXtable(id=None):
    ctrl_info= "ctrl: normalXtable, view: normal-table.html"
    messages = []

    rows_tnormalXtable0= db(db.tnormalXtable0).select()
    rows_tnormalXtable1= db(db.tnormalXtable1).select()
    rows_tnormalXtable2= db(db.tnormalXtable2).select()
    rows_tnormalXtable3= db(db.tnormalXtable3).select()
    rows_tnormalXtable4= db(db.tnormalXtable4).select()
    rows_tnormalXtable5= db(db.tnormalXtable5).select()
    dfnormalXtable0_row= None
    id_dfnormalXtable0 = None
    fnormalXtable0= Form(db.dfnormalXtable0, id, deletable=False, dbio = False, keep_values = False, form_name = "fnormalXtable0",  formstyle=FormStyleBulma )
   
    if fnormalXtable0.accepted:

        Glb['debug'] and print("     fnormalXtable0 accepted with: %s " % (fnormalXtable0.vars))
        fnormalXtable0_f0 = fnormalXtable0.vars.get('f0','')
        if len ( fnormalXtable0_f0 ):
            id_dfnormalXtable0 = db.dfnormalXtable0.insert( **fnormalXtable0.vars )
            db.commit()

            if not id_dfnormalXtable0 is None:
                dfnormalXtable0_row = db.dfnormalXtable0(id_dfnormalXtable0 )

                if not dfnormalXtable0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnormalXtable0.vars.f0}\" into db.dfnormalXtable0.f0, id = {id_dfnormalXtable0}' )
                         print(f"     found db.dfnormalXtable0.f0: \"{dfnormalXtable0_row.f0}\", id = {id_dfnormalXtable0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fnormalXtable0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fnormalXtable0.vars.items() ]
                print()
   
    elif fnormalXtable0.errors:
        print("fnormalXtable0 has errors: %s " % (fnormalXtable0.errors))
 

    dfnormalXtable1_row= None
    id_dfnormalXtable1 = None
    fnormalXtable1= Form(db.dfnormalXtable1, id, deletable=False, dbio = False, keep_values = False, form_name = "fnormalXtable1",  formstyle=FormStyleBulma )
   
    if fnormalXtable1.accepted:

        Glb['debug'] and print("     fnormalXtable1 accepted with: %s " % (fnormalXtable1.vars))
        fnormalXtable1_f0 = fnormalXtable1.vars.get('f0','')
        if len ( fnormalXtable1_f0 ):
            id_dfnormalXtable1 = db.dfnormalXtable1.insert( **fnormalXtable1.vars )
            db.commit()

            if not id_dfnormalXtable1 is None:
                dfnormalXtable1_row = db.dfnormalXtable1(id_dfnormalXtable1 )

                if not dfnormalXtable1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnormalXtable1.vars.f0}\" into db.dfnormalXtable1.f0, id = {id_dfnormalXtable1}' )
                         print(f"     found db.dfnormalXtable1.f0: \"{dfnormalXtable1_row.f0}\", id = {id_dfnormalXtable1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fnormalXtable1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fnormalXtable1.vars.items() ]
                print()
   
    elif fnormalXtable1.errors:
        print("fnormalXtable1 has errors: %s " % (fnormalXtable1.errors))
 

    return locals()


@action('notification', method=["GET", "POST"] )
@action.uses(Template('notification.html', delimiters='[%[ ]]',), db, session,  T, )

def notification(id=None):
    ctrl_info= "ctrl: notification, view: notification.html"
    messages = []

    dfnotification0_row= None
    id_dfnotification0 = None
    fnotification0= Form(db.dfnotification0, id, deletable=False, dbio = False, keep_values = False, form_name = "fnotification0",  formstyle=FormStyleBulma )
   
    if fnotification0.accepted:

        Glb['debug'] and print("     fnotification0 accepted with: %s " % (fnotification0.vars))
        fnotification0_f0 = fnotification0.vars.get('f0','')
        if len ( fnotification0_f0 ):
            id_dfnotification0 = db.dfnotification0.insert( **fnotification0.vars )
            db.commit()

            if not id_dfnotification0 is None:
                dfnotification0_row = db.dfnotification0(id_dfnotification0 )

                if not dfnotification0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnotification0.vars.f0}\" into db.dfnotification0.f0, id = {id_dfnotification0}' )
                         print(f"     found db.dfnotification0.f0: \"{dfnotification0_row.f0}\", id = {id_dfnotification0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fnotification0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fnotification0.vars.items() ]
                print()
   
    elif fnotification0.errors:
        print("fnotification0 has errors: %s " % (fnotification0.errors))
 

    dfnotification1_row= None
    id_dfnotification1 = None
    fnotification1= Form(db.dfnotification1, id, deletable=False, dbio = False, keep_values = False, form_name = "fnotification1",  formstyle=FormStyleBulma )
   
    if fnotification1.accepted:

        Glb['debug'] and print("     fnotification1 accepted with: %s " % (fnotification1.vars))
        fnotification1_f0 = fnotification1.vars.get('f0','')
        if len ( fnotification1_f0 ):
            id_dfnotification1 = db.dfnotification1.insert( **fnotification1.vars )
            db.commit()

            if not id_dfnotification1 is None:
                dfnotification1_row = db.dfnotification1(id_dfnotification1 )

                if not dfnotification1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fnotification1.vars.f0}\" into db.dfnotification1.f0, id = {id_dfnotification1}' )
                         print(f"     found db.dfnotification1.f0: \"{dfnotification1_row.f0}\", id = {id_dfnotification1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fnotification1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fnotification1.vars.items() ]
                print()
   
    elif fnotification1.errors:
        print("fnotification1 has errors: %s " % (fnotification1.errors))
 

    return locals()


@action('imageXcropper', method=["GET", "POST"] )
@action.uses(Template('image-cropper.html', delimiters='[%[ ]]',), db, session,  T, )

def imageXcropper(id=None):
    ctrl_info= "ctrl: imageXcropper, view: image-cropper.html"
    messages = []

    dfimageXcropper0_row= None
    id_dfimageXcropper0 = None
    fimageXcropper0= Form(db.dfimageXcropper0, id, deletable=False, dbio = False, keep_values = False, form_name = "fimageXcropper0",  formstyle=FormStyleBulma )
   
    if fimageXcropper0.accepted:

        Glb['debug'] and print("     fimageXcropper0 accepted with: %s " % (fimageXcropper0.vars))
        fimageXcropper0_f0 = fimageXcropper0.vars.get('f0','')
        if len ( fimageXcropper0_f0 ):
            id_dfimageXcropper0 = db.dfimageXcropper0.insert( **fimageXcropper0.vars )
            db.commit()

            if not id_dfimageXcropper0 is None:
                dfimageXcropper0_row = db.dfimageXcropper0(id_dfimageXcropper0 )

                if not dfimageXcropper0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fimageXcropper0.vars.f0}\" into db.dfimageXcropper0.f0, id = {id_dfimageXcropper0}' )
                         print(f"     found db.dfimageXcropper0.f0: \"{dfimageXcropper0_row.f0}\", id = {id_dfimageXcropper0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fimageXcropper0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fimageXcropper0.vars.items() ]
                print()
   
    elif fimageXcropper0.errors:
        print("fimageXcropper0 has errors: %s " % (fimageXcropper0.errors))
 

    dfimageXcropper1_row= None
    id_dfimageXcropper1 = None
    fimageXcropper1= Form(db.dfimageXcropper1, id, deletable=False, dbio = False, keep_values = False, form_name = "fimageXcropper1",  formstyle=FormStyleBulma )
   
    if fimageXcropper1.accepted:

        Glb['debug'] and print("     fimageXcropper1 accepted with: %s " % (fimageXcropper1.vars))
        fimageXcropper1_f0 = fimageXcropper1.vars.get('f0','')
        if len ( fimageXcropper1_f0 ):
            id_dfimageXcropper1 = db.dfimageXcropper1.insert( **fimageXcropper1.vars )
            db.commit()

            if not id_dfimageXcropper1 is None:
                dfimageXcropper1_row = db.dfimageXcropper1(id_dfimageXcropper1 )

                if not dfimageXcropper1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fimageXcropper1.vars.f0}\" into db.dfimageXcropper1.f0, id = {id_dfimageXcropper1}' )
                         print(f"     found db.dfimageXcropper1.f0: \"{dfimageXcropper1_row.f0}\", id = {id_dfimageXcropper1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fimageXcropper1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fimageXcropper1.vars.items() ]
                print()
   
    elif fimageXcropper1.errors:
        print("fimageXcropper1 has errors: %s " % (fimageXcropper1.errors))
 

    return locals()


@action('formXexamples', method=["GET", "POST"] )
@action.uses(Template('form-examples.html', delimiters='[%[ ]]',), db, session,  T, )

def formXexamples(id=None):
    ctrl_info= "ctrl: formXexamples, view: form-examples.html"
    messages = []

    dfformXexamples0_row= None
    id_dfformXexamples0 = None
    fformXexamples0= Form(db.dfformXexamples0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXexamples0",  formstyle=FormStyleBulma )
   
    if fformXexamples0.accepted:

        Glb['debug'] and print("     fformXexamples0 accepted with: %s " % (fformXexamples0.vars))
        fformXexamples0_f0 = fformXexamples0.vars.get('f0','')
        if len ( fformXexamples0_f0 ):
            id_dfformXexamples0 = db.dfformXexamples0.insert( **fformXexamples0.vars )
            db.commit()

            if not id_dfformXexamples0 is None:
                dfformXexamples0_row = db.dfformXexamples0(id_dfformXexamples0 )

                if not dfformXexamples0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXexamples0.vars.f0}\" into db.dfformXexamples0.f0, id = {id_dfformXexamples0}' )
                         print(f"     found db.dfformXexamples0.f0: \"{dfformXexamples0_row.f0}\", id = {id_dfformXexamples0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXexamples0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXexamples0.vars.items() ]
                print()
   
    elif fformXexamples0.errors:
        print("fformXexamples0 has errors: %s " % (fformXexamples0.errors))
 

    dfformXexamples1_row= None
    id_dfformXexamples1 = None
    fformXexamples1= Form(db.dfformXexamples1, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXexamples1",  formstyle=FormStyleBulma )
   
    if fformXexamples1.accepted:

        Glb['debug'] and print("     fformXexamples1 accepted with: %s " % (fformXexamples1.vars))
        fformXexamples1_f0 = fformXexamples1.vars.get('f0','')
        if len ( fformXexamples1_f0 ):
            id_dfformXexamples1 = db.dfformXexamples1.insert( **fformXexamples1.vars )
            db.commit()

            if not id_dfformXexamples1 is None:
                dfformXexamples1_row = db.dfformXexamples1(id_dfformXexamples1 )

                if not dfformXexamples1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXexamples1.vars.f0}\" into db.dfformXexamples1.f0, id = {id_dfformXexamples1}' )
                         print(f"     found db.dfformXexamples1.f0: \"{dfformXexamples1_row.f0}\", id = {id_dfformXexamples1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXexamples1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXexamples1.vars.items() ]
                print()
   
    elif fformXexamples1.errors:
        print("fformXexamples1 has errors: %s " % (fformXexamples1.errors))
 

    dfformXexamples2_row= None
    id_dfformXexamples2 = None
    fformXexamples2= Form(db.dfformXexamples2, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXexamples2",  formstyle=FormStyleBulma )
   
    if fformXexamples2.accepted:

        Glb['debug'] and print("     fformXexamples2 accepted with: %s " % (fformXexamples2.vars))
        fformXexamples2_f0 = fformXexamples2.vars.get('f0','')
        if len ( fformXexamples2_f0 ):
            id_dfformXexamples2 = db.dfformXexamples2.insert( **fformXexamples2.vars )
            db.commit()

            if not id_dfformXexamples2 is None:
                dfformXexamples2_row = db.dfformXexamples2(id_dfformXexamples2 )

                if not dfformXexamples2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXexamples2.vars.f0}\" into db.dfformXexamples2.f0, id = {id_dfformXexamples2}' )
                         print(f"     found db.dfformXexamples2.f0: \"{dfformXexamples2_row.f0}\", id = {id_dfformXexamples2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXexamples2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXexamples2.vars.items() ]
                print()
   
    elif fformXexamples2.errors:
        print("fformXexamples2 has errors: %s " % (fformXexamples2.errors))
 

    dfformXexamples3_row= None
    id_dfformXexamples3 = None
    fformXexamples3= Form(db.dfformXexamples3, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXexamples3",  formstyle=FormStyleBulma )
   
    if fformXexamples3.accepted:

        Glb['debug'] and print("     fformXexamples3 accepted with: %s " % (fformXexamples3.vars))
        fformXexamples3_f0 = fformXexamples3.vars.get('f0','')
        if len ( fformXexamples3_f0 ):
            id_dfformXexamples3 = db.dfformXexamples3.insert( **fformXexamples3.vars )
            db.commit()

            if not id_dfformXexamples3 is None:
                dfformXexamples3_row = db.dfformXexamples3(id_dfformXexamples3 )

                if not dfformXexamples3_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXexamples3.vars.f0}\" into db.dfformXexamples3.f0, id = {id_dfformXexamples3}' )
                         print(f"     found db.dfformXexamples3.f0: \"{dfformXexamples3_row.f0}\", id = {id_dfformXexamples3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXexamples3_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXexamples3.vars.items() ]
                print()
   
    elif fformXexamples3.errors:
        print("fformXexamples3 has errors: %s " % (fformXexamples3.errors))
 

    dfformXexamples4_row= None
    id_dfformXexamples4 = None
    fformXexamples4= Form(db.dfformXexamples4, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXexamples4",  formstyle=FormStyleBulma )
   
    if fformXexamples4.accepted:

        Glb['debug'] and print("     fformXexamples4 accepted with: %s " % (fformXexamples4.vars))
        fformXexamples4_f0 = fformXexamples4.vars.get('f0','')
        if len ( fformXexamples4_f0 ):
            id_dfformXexamples4 = db.dfformXexamples4.insert( **fformXexamples4.vars )
            db.commit()

            if not id_dfformXexamples4 is None:
                dfformXexamples4_row = db.dfformXexamples4(id_dfformXexamples4 )

                if not dfformXexamples4_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXexamples4.vars.f0}\" into db.dfformXexamples4.f0, id = {id_dfformXexamples4}' )
                         print(f"     found db.dfformXexamples4.f0: \"{dfformXexamples4_row.f0}\", id = {id_dfformXexamples4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXexamples4_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXexamples4.vars.items() ]
                print()
   
    elif fformXexamples4.errors:
        print("fformXexamples4 has errors: %s " % (fformXexamples4.errors))
 

    dfformXexamples5_row= None
    id_dfformXexamples5 = None
    fformXexamples5= Form(db.dfformXexamples5, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXexamples5",  formstyle=FormStyleBulma )
   
    if fformXexamples5.accepted:

        Glb['debug'] and print("     fformXexamples5 accepted with: %s " % (fformXexamples5.vars))
        fformXexamples5_f0 = fformXexamples5.vars.get('f0','')
        if len ( fformXexamples5_f0 ):
            id_dfformXexamples5 = db.dfformXexamples5.insert( **fformXexamples5.vars )
            db.commit()

            if not id_dfformXexamples5 is None:
                dfformXexamples5_row = db.dfformXexamples5(id_dfformXexamples5 )

                if not dfformXexamples5_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXexamples5.vars.f0}\" into db.dfformXexamples5.f0, id = {id_dfformXexamples5}' )
                         print(f"     found db.dfformXexamples5.f0: \"{dfformXexamples5_row.f0}\", id = {id_dfformXexamples5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXexamples5_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXexamples5.vars.items() ]
                print()
   
    elif fformXexamples5.errors:
        print("fformXexamples5 has errors: %s " % (fformXexamples5.errors))
 

    dfformXexamples6_row= None
    id_dfformXexamples6 = None
    fformXexamples6= Form(db.dfformXexamples6, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXexamples6",  formstyle=FormStyleBulma )
   
    if fformXexamples6.accepted:

        Glb['debug'] and print("     fformXexamples6 accepted with: %s " % (fformXexamples6.vars))
        fformXexamples6_f0 = fformXexamples6.vars.get('f0','')
        if len ( fformXexamples6_f0 ):
            id_dfformXexamples6 = db.dfformXexamples6.insert( **fformXexamples6.vars )
            db.commit()

            if not id_dfformXexamples6 is None:
                dfformXexamples6_row = db.dfformXexamples6(id_dfformXexamples6 )

                if not dfformXexamples6_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXexamples6.vars.f0}\" into db.dfformXexamples6.f0, id = {id_dfformXexamples6}' )
                         print(f"     found db.dfformXexamples6.f0: \"{dfformXexamples6_row.f0}\", id = {id_dfformXexamples6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXexamples6_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXexamples6.vars.items() ]
                print()
   
    elif fformXexamples6.errors:
        print("fformXexamples6 has errors: %s " % (fformXexamples6.errors))
 

    dfformXexamples7_row= None
    id_dfformXexamples7 = None
    fformXexamples7= Form(db.dfformXexamples7, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXexamples7",  formstyle=FormStyleBulma )
   
    if fformXexamples7.accepted:

        Glb['debug'] and print("     fformXexamples7 accepted with: %s " % (fformXexamples7.vars))
        fformXexamples7_f0 = fformXexamples7.vars.get('f0','')
        if len ( fformXexamples7_f0 ):
            id_dfformXexamples7 = db.dfformXexamples7.insert( **fformXexamples7.vars )
            db.commit()

            if not id_dfformXexamples7 is None:
                dfformXexamples7_row = db.dfformXexamples7(id_dfformXexamples7 )

                if not dfformXexamples7_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXexamples7.vars.f0}\" into db.dfformXexamples7.f0, id = {id_dfformXexamples7}' )
                         print(f"     found db.dfformXexamples7.f0: \"{dfformXexamples7_row.f0}\", id = {id_dfformXexamples7}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXexamples7_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXexamples7.vars.items() ]
                print()
   
    elif fformXexamples7.errors:
        print("fformXexamples7 has errors: %s " % (fformXexamples7.errors))
 

    dfformXexamples8_row= None
    id_dfformXexamples8 = None
    fformXexamples8= Form(db.dfformXexamples8, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXexamples8",  formstyle=FormStyleBulma )
   
    if fformXexamples8.accepted:

        Glb['debug'] and print("     fformXexamples8 accepted with: %s " % (fformXexamples8.vars))
        fformXexamples8_f0 = fformXexamples8.vars.get('f0','')
        if len ( fformXexamples8_f0 ):
            id_dfformXexamples8 = db.dfformXexamples8.insert( **fformXexamples8.vars )
            db.commit()

            if not id_dfformXexamples8 is None:
                dfformXexamples8_row = db.dfformXexamples8(id_dfformXexamples8 )

                if not dfformXexamples8_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXexamples8.vars.f0}\" into db.dfformXexamples8.f0, id = {id_dfformXexamples8}' )
                         print(f"     found db.dfformXexamples8.f0: \"{dfformXexamples8_row.f0}\", id = {id_dfformXexamples8}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXexamples8_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXexamples8.vars.items() ]
                print()
   
    elif fformXexamples8.errors:
        print("fformXexamples8 has errors: %s " % (fformXexamples8.errors))
 

    dfformXexamples9_row= None
    id_dfformXexamples9 = None
    fformXexamples9= Form(db.dfformXexamples9, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXexamples9",  formstyle=FormStyleBulma )
   
    if fformXexamples9.accepted:

        Glb['debug'] and print("     fformXexamples9 accepted with: %s " % (fformXexamples9.vars))
        fformXexamples9_f0 = fformXexamples9.vars.get('f0','')
        if len ( fformXexamples9_f0 ):
            id_dfformXexamples9 = db.dfformXexamples9.insert( **fformXexamples9.vars )
            db.commit()

            if not id_dfformXexamples9 is None:
                dfformXexamples9_row = db.dfformXexamples9(id_dfformXexamples9 )

                if not dfformXexamples9_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXexamples9.vars.f0}\" into db.dfformXexamples9.f0, id = {id_dfformXexamples9}' )
                         print(f"     found db.dfformXexamples9.f0: \"{dfformXexamples9_row.f0}\", id = {id_dfformXexamples9}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXexamples9_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXexamples9.vars.items() ]
                print()
   
    elif fformXexamples9.errors:
        print("fformXexamples9 has errors: %s " % (fformXexamples9.errors))
 

    dfformXexamples10_row= None
    id_dfformXexamples10 = None
    fformXexamples10= Form(db.dfformXexamples10, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXexamples10",  formstyle=FormStyleBulma )
   
    if fformXexamples10.accepted:

        Glb['debug'] and print("     fformXexamples10 accepted with: %s " % (fformXexamples10.vars))
        fformXexamples10_f0 = fformXexamples10.vars.get('f0','')
        if len ( fformXexamples10_f0 ):
            id_dfformXexamples10 = db.dfformXexamples10.insert( **fformXexamples10.vars )
            db.commit()

            if not id_dfformXexamples10 is None:
                dfformXexamples10_row = db.dfformXexamples10(id_dfformXexamples10 )

                if not dfformXexamples10_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXexamples10.vars.f0}\" into db.dfformXexamples10.f0, id = {id_dfformXexamples10}' )
                         print(f"     found db.dfformXexamples10.f0: \"{dfformXexamples10_row.f0}\", id = {id_dfformXexamples10}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXexamples10_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXexamples10.vars.items() ]
                print()
   
    elif fformXexamples10.errors:
        print("fformXexamples10 has errors: %s " % (fformXexamples10.errors))
 

    return locals()


@action('formXelements', method=["GET", "POST"] )
@action.uses(Template('form-elements.html', delimiters='[%[ ]]',), db, session,  T, )

def formXelements(id=None):
    ctrl_info= "ctrl: formXelements, view: form-elements.html"
    messages = []

    dfformXelements0_row= None
    id_dfformXelements0 = None
    fformXelements0= Form(db.dfformXelements0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements0",  formstyle=FormStyleBulma )
   
    if fformXelements0.accepted:

        Glb['debug'] and print("     fformXelements0 accepted with: %s " % (fformXelements0.vars))
        fformXelements0_f0 = fformXelements0.vars.get('f0','')
        if len ( fformXelements0_f0 ):
            id_dfformXelements0 = db.dfformXelements0.insert( **fformXelements0.vars )
            db.commit()

            if not id_dfformXelements0 is None:
                dfformXelements0_row = db.dfformXelements0(id_dfformXelements0 )

                if not dfformXelements0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements0.vars.f0}\" into db.dfformXelements0.f0, id = {id_dfformXelements0}' )
                         print(f"     found db.dfformXelements0.f0: \"{dfformXelements0_row.f0}\", id = {id_dfformXelements0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements0.vars.items() ]
                print()
   
    elif fformXelements0.errors:
        print("fformXelements0 has errors: %s " % (fformXelements0.errors))
 

    dfformXelements1_row= None
    id_dfformXelements1 = None
    fformXelements1= Form(db.dfformXelements1, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements1",  formstyle=FormStyleBulma )
   
    if fformXelements1.accepted:

        Glb['debug'] and print("     fformXelements1 accepted with: %s " % (fformXelements1.vars))
        fformXelements1_f0 = fformXelements1.vars.get('f0','')
        if len ( fformXelements1_f0 ):
            id_dfformXelements1 = db.dfformXelements1.insert( **fformXelements1.vars )
            db.commit()

            if not id_dfformXelements1 is None:
                dfformXelements1_row = db.dfformXelements1(id_dfformXelements1 )

                if not dfformXelements1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements1.vars.f0}\" into db.dfformXelements1.f0, id = {id_dfformXelements1}' )
                         print(f"     found db.dfformXelements1.f0: \"{dfformXelements1_row.f0}\", id = {id_dfformXelements1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements1.vars.items() ]
                print()
   
    elif fformXelements1.errors:
        print("fformXelements1 has errors: %s " % (fformXelements1.errors))
 

    dfformXelements2_row= None
    id_dfformXelements2 = None
    fformXelements2= Form(db.dfformXelements2, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements2",  formstyle=FormStyleBulma )
   
    if fformXelements2.accepted:

        Glb['debug'] and print("     fformXelements2 accepted with: %s " % (fformXelements2.vars))
        fformXelements2_f0 = fformXelements2.vars.get('f0','')
        if len ( fformXelements2_f0 ):
            id_dfformXelements2 = db.dfformXelements2.insert( **fformXelements2.vars )
            db.commit()

            if not id_dfformXelements2 is None:
                dfformXelements2_row = db.dfformXelements2(id_dfformXelements2 )

                if not dfformXelements2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements2.vars.f0}\" into db.dfformXelements2.f0, id = {id_dfformXelements2}' )
                         print(f"     found db.dfformXelements2.f0: \"{dfformXelements2_row.f0}\", id = {id_dfformXelements2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements2.vars.items() ]
                print()
   
    elif fformXelements2.errors:
        print("fformXelements2 has errors: %s " % (fformXelements2.errors))
 

    dfformXelements3_row= None
    id_dfformXelements3 = None
    fformXelements3= Form(db.dfformXelements3, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements3",  formstyle=FormStyleBulma )
   
    if fformXelements3.accepted:

        Glb['debug'] and print("     fformXelements3 accepted with: %s " % (fformXelements3.vars))
        fformXelements3_f0 = fformXelements3.vars.get('f0','')
        if len ( fformXelements3_f0 ):
            id_dfformXelements3 = db.dfformXelements3.insert( **fformXelements3.vars )
            db.commit()

            if not id_dfformXelements3 is None:
                dfformXelements3_row = db.dfformXelements3(id_dfformXelements3 )

                if not dfformXelements3_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements3.vars.f0}\" into db.dfformXelements3.f0, id = {id_dfformXelements3}' )
                         print(f"     found db.dfformXelements3.f0: \"{dfformXelements3_row.f0}\", id = {id_dfformXelements3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements3_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements3.vars.items() ]
                print()
   
    elif fformXelements3.errors:
        print("fformXelements3 has errors: %s " % (fformXelements3.errors))
 

    dfformXelements4_row= None
    id_dfformXelements4 = None
    fformXelements4= Form(db.dfformXelements4, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements4",  formstyle=FormStyleBulma )
   
    if fformXelements4.accepted:

        Glb['debug'] and print("     fformXelements4 accepted with: %s " % (fformXelements4.vars))
        fformXelements4_f0 = fformXelements4.vars.get('f0','')
        if len ( fformXelements4_f0 ):
            id_dfformXelements4 = db.dfformXelements4.insert( **fformXelements4.vars )
            db.commit()

            if not id_dfformXelements4 is None:
                dfformXelements4_row = db.dfformXelements4(id_dfformXelements4 )

                if not dfformXelements4_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements4.vars.f0}\" into db.dfformXelements4.f0, id = {id_dfformXelements4}' )
                         print(f"     found db.dfformXelements4.f0: \"{dfformXelements4_row.f0}\", id = {id_dfformXelements4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements4_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements4.vars.items() ]
                print()
   
    elif fformXelements4.errors:
        print("fformXelements4 has errors: %s " % (fformXelements4.errors))
 

    dfformXelements5_row= None
    id_dfformXelements5 = None
    fformXelements5= Form(db.dfformXelements5, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements5",  formstyle=FormStyleBulma )
   
    if fformXelements5.accepted:

        Glb['debug'] and print("     fformXelements5 accepted with: %s " % (fformXelements5.vars))
        fformXelements5_f0 = fformXelements5.vars.get('f0','')
        if len ( fformXelements5_f0 ):
            id_dfformXelements5 = db.dfformXelements5.insert( **fformXelements5.vars )
            db.commit()

            if not id_dfformXelements5 is None:
                dfformXelements5_row = db.dfformXelements5(id_dfformXelements5 )

                if not dfformXelements5_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements5.vars.f0}\" into db.dfformXelements5.f0, id = {id_dfformXelements5}' )
                         print(f"     found db.dfformXelements5.f0: \"{dfformXelements5_row.f0}\", id = {id_dfformXelements5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements5_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements5.vars.items() ]
                print()
   
    elif fformXelements5.errors:
        print("fformXelements5 has errors: %s " % (fformXelements5.errors))
 

    dfformXelements6_row= None
    id_dfformXelements6 = None
    fformXelements6= Form(db.dfformXelements6, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements6",  formstyle=FormStyleBulma )
   
    if fformXelements6.accepted:

        Glb['debug'] and print("     fformXelements6 accepted with: %s " % (fformXelements6.vars))
        fformXelements6_f0 = fformXelements6.vars.get('f0','')
        if len ( fformXelements6_f0 ):
            id_dfformXelements6 = db.dfformXelements6.insert( **fformXelements6.vars )
            db.commit()

            if not id_dfformXelements6 is None:
                dfformXelements6_row = db.dfformXelements6(id_dfformXelements6 )

                if not dfformXelements6_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements6.vars.f0}\" into db.dfformXelements6.f0, id = {id_dfformXelements6}' )
                         print(f"     found db.dfformXelements6.f0: \"{dfformXelements6_row.f0}\", id = {id_dfformXelements6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements6_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements6.vars.items() ]
                print()
   
    elif fformXelements6.errors:
        print("fformXelements6 has errors: %s " % (fformXelements6.errors))
 

    dfformXelements7_row= None
    id_dfformXelements7 = None
    fformXelements7= Form(db.dfformXelements7, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements7",  formstyle=FormStyleBulma )
   
    if fformXelements7.accepted:

        Glb['debug'] and print("     fformXelements7 accepted with: %s " % (fformXelements7.vars))
        fformXelements7_f0 = fformXelements7.vars.get('f0','')
        if len ( fformXelements7_f0 ):
            id_dfformXelements7 = db.dfformXelements7.insert( **fformXelements7.vars )
            db.commit()

            if not id_dfformXelements7 is None:
                dfformXelements7_row = db.dfformXelements7(id_dfformXelements7 )

                if not dfformXelements7_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements7.vars.f0}\" into db.dfformXelements7.f0, id = {id_dfformXelements7}' )
                         print(f"     found db.dfformXelements7.f0: \"{dfformXelements7_row.f0}\", id = {id_dfformXelements7}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements7_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements7.vars.items() ]
                print()
   
    elif fformXelements7.errors:
        print("fformXelements7 has errors: %s " % (fformXelements7.errors))
 

    dfformXelements8_row= None
    id_dfformXelements8 = None
    fformXelements8= Form(db.dfformXelements8, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements8",  formstyle=FormStyleBulma )
   
    if fformXelements8.accepted:

        Glb['debug'] and print("     fformXelements8 accepted with: %s " % (fformXelements8.vars))
        fformXelements8_f0 = fformXelements8.vars.get('f0','')
        if len ( fformXelements8_f0 ):
            id_dfformXelements8 = db.dfformXelements8.insert( **fformXelements8.vars )
            db.commit()

            if not id_dfformXelements8 is None:
                dfformXelements8_row = db.dfformXelements8(id_dfformXelements8 )

                if not dfformXelements8_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements8.vars.f0}\" into db.dfformXelements8.f0, id = {id_dfformXelements8}' )
                         print(f"     found db.dfformXelements8.f0: \"{dfformXelements8_row.f0}\", id = {id_dfformXelements8}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements8_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements8.vars.items() ]
                print()
   
    elif fformXelements8.errors:
        print("fformXelements8 has errors: %s " % (fformXelements8.errors))
 

    dfformXelements9_row= None
    id_dfformXelements9 = None
    fformXelements9= Form(db.dfformXelements9, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements9",  formstyle=FormStyleBulma )
   
    if fformXelements9.accepted:

        Glb['debug'] and print("     fformXelements9 accepted with: %s " % (fformXelements9.vars))
        fformXelements9_f0 = fformXelements9.vars.get('f0','')
        if len ( fformXelements9_f0 ):
            id_dfformXelements9 = db.dfformXelements9.insert( **fformXelements9.vars )
            db.commit()

            if not id_dfformXelements9 is None:
                dfformXelements9_row = db.dfformXelements9(id_dfformXelements9 )

                if not dfformXelements9_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements9.vars.f0}\" into db.dfformXelements9.f0, id = {id_dfformXelements9}' )
                         print(f"     found db.dfformXelements9.f0: \"{dfformXelements9_row.f0}\", id = {id_dfformXelements9}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements9_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements9.vars.items() ]
                print()
   
    elif fformXelements9.errors:
        print("fformXelements9 has errors: %s " % (fformXelements9.errors))
 

    dfformXelements10_row= None
    id_dfformXelements10 = None
    fformXelements10= Form(db.dfformXelements10, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements10",  formstyle=FormStyleBulma )
   
    if fformXelements10.accepted:

        Glb['debug'] and print("     fformXelements10 accepted with: %s " % (fformXelements10.vars))
        fformXelements10_f0 = fformXelements10.vars.get('f0','')
        if len ( fformXelements10_f0 ):
            id_dfformXelements10 = db.dfformXelements10.insert( **fformXelements10.vars )
            db.commit()

            if not id_dfformXelements10 is None:
                dfformXelements10_row = db.dfformXelements10(id_dfformXelements10 )

                if not dfformXelements10_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements10.vars.f0}\" into db.dfformXelements10.f0, id = {id_dfformXelements10}' )
                         print(f"     found db.dfformXelements10.f0: \"{dfformXelements10_row.f0}\", id = {id_dfformXelements10}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements10_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements10.vars.items() ]
                print()
   
    elif fformXelements10.errors:
        print("fformXelements10 has errors: %s " % (fformXelements10.errors))
 

    dfformXelements11_row= None
    id_dfformXelements11 = None
    fformXelements11= Form(db.dfformXelements11, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements11",  formstyle=FormStyleBulma )
   
    if fformXelements11.accepted:

        Glb['debug'] and print("     fformXelements11 accepted with: %s " % (fformXelements11.vars))
        fformXelements11_f0 = fformXelements11.vars.get('f0','')
        if len ( fformXelements11_f0 ):
            id_dfformXelements11 = db.dfformXelements11.insert( **fformXelements11.vars )
            db.commit()

            if not id_dfformXelements11 is None:
                dfformXelements11_row = db.dfformXelements11(id_dfformXelements11 )

                if not dfformXelements11_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements11.vars.f0}\" into db.dfformXelements11.f0, id = {id_dfformXelements11}' )
                         print(f"     found db.dfformXelements11.f0: \"{dfformXelements11_row.f0}\", id = {id_dfformXelements11}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements11_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements11.vars.items() ]
                print()
   
    elif fformXelements11.errors:
        print("fformXelements11 has errors: %s " % (fformXelements11.errors))
 

    dfformXelements12_row= None
    id_dfformXelements12 = None
    fformXelements12= Form(db.dfformXelements12, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements12",  formstyle=FormStyleBulma )
   
    if fformXelements12.accepted:

        Glb['debug'] and print("     fformXelements12 accepted with: %s " % (fformXelements12.vars))
        fformXelements12_f0 = fformXelements12.vars.get('f0','')
        if len ( fformXelements12_f0 ):
            id_dfformXelements12 = db.dfformXelements12.insert( **fformXelements12.vars )
            db.commit()

            if not id_dfformXelements12 is None:
                dfformXelements12_row = db.dfformXelements12(id_dfformXelements12 )

                if not dfformXelements12_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements12.vars.f0}\" into db.dfformXelements12.f0, id = {id_dfformXelements12}' )
                         print(f"     found db.dfformXelements12.f0: \"{dfformXelements12_row.f0}\", id = {id_dfformXelements12}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements12_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements12.vars.items() ]
                print()
   
    elif fformXelements12.errors:
        print("fformXelements12 has errors: %s " % (fformXelements12.errors))
 

    dfformXelements13_row= None
    id_dfformXelements13 = None
    fformXelements13= Form(db.dfformXelements13, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements13",  formstyle=FormStyleBulma )
   
    if fformXelements13.accepted:

        Glb['debug'] and print("     fformXelements13 accepted with: %s " % (fformXelements13.vars))
        fformXelements13_f0 = fformXelements13.vars.get('f0','')
        if len ( fformXelements13_f0 ):
            id_dfformXelements13 = db.dfformXelements13.insert( **fformXelements13.vars )
            db.commit()

            if not id_dfformXelements13 is None:
                dfformXelements13_row = db.dfformXelements13(id_dfformXelements13 )

                if not dfformXelements13_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements13.vars.f0}\" into db.dfformXelements13.f0, id = {id_dfformXelements13}' )
                         print(f"     found db.dfformXelements13.f0: \"{dfformXelements13_row.f0}\", id = {id_dfformXelements13}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements13_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements13.vars.items() ]
                print()
   
    elif fformXelements13.errors:
        print("fformXelements13 has errors: %s " % (fformXelements13.errors))
 

    dfformXelements14_row= None
    id_dfformXelements14 = None
    fformXelements14= Form(db.dfformXelements14, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements14",  formstyle=FormStyleBulma )
   
    if fformXelements14.accepted:

        Glb['debug'] and print("     fformXelements14 accepted with: %s " % (fformXelements14.vars))
        fformXelements14_f0 = fformXelements14.vars.get('f0','')
        if len ( fformXelements14_f0 ):
            id_dfformXelements14 = db.dfformXelements14.insert( **fformXelements14.vars )
            db.commit()

            if not id_dfformXelements14 is None:
                dfformXelements14_row = db.dfformXelements14(id_dfformXelements14 )

                if not dfformXelements14_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements14.vars.f0}\" into db.dfformXelements14.f0, id = {id_dfformXelements14}' )
                         print(f"     found db.dfformXelements14.f0: \"{dfformXelements14_row.f0}\", id = {id_dfformXelements14}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements14_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements14.vars.items() ]
                print()
   
    elif fformXelements14.errors:
        print("fformXelements14 has errors: %s " % (fformXelements14.errors))
 

    dfformXelements15_row= None
    id_dfformXelements15 = None
    fformXelements15= Form(db.dfformXelements15, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements15",  formstyle=FormStyleBulma )
   
    if fformXelements15.accepted:

        Glb['debug'] and print("     fformXelements15 accepted with: %s " % (fformXelements15.vars))
        fformXelements15_f0 = fformXelements15.vars.get('f0','')
        if len ( fformXelements15_f0 ):
            id_dfformXelements15 = db.dfformXelements15.insert( **fformXelements15.vars )
            db.commit()

            if not id_dfformXelements15 is None:
                dfformXelements15_row = db.dfformXelements15(id_dfformXelements15 )

                if not dfformXelements15_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements15.vars.f0}\" into db.dfformXelements15.f0, id = {id_dfformXelements15}' )
                         print(f"     found db.dfformXelements15.f0: \"{dfformXelements15_row.f0}\", id = {id_dfformXelements15}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements15_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements15.vars.items() ]
                print()
   
    elif fformXelements15.errors:
        print("fformXelements15 has errors: %s " % (fformXelements15.errors))
 

    dfformXelements16_row= None
    id_dfformXelements16 = None
    fformXelements16= Form(db.dfformXelements16, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements16",  formstyle=FormStyleBulma )
   
    if fformXelements16.accepted:

        Glb['debug'] and print("     fformXelements16 accepted with: %s " % (fformXelements16.vars))
        fformXelements16_f0 = fformXelements16.vars.get('f0','')
        if len ( fformXelements16_f0 ):
            id_dfformXelements16 = db.dfformXelements16.insert( **fformXelements16.vars )
            db.commit()

            if not id_dfformXelements16 is None:
                dfformXelements16_row = db.dfformXelements16(id_dfformXelements16 )

                if not dfformXelements16_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements16.vars.f0}\" into db.dfformXelements16.f0, id = {id_dfformXelements16}' )
                         print(f"     found db.dfformXelements16.f0: \"{dfformXelements16_row.f0}\", id = {id_dfformXelements16}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements16_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements16.vars.items() ]
                print()
   
    elif fformXelements16.errors:
        print("fformXelements16 has errors: %s " % (fformXelements16.errors))
 

    dfformXelements17_row= None
    id_dfformXelements17 = None
    fformXelements17= Form(db.dfformXelements17, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements17",  formstyle=FormStyleBulma )
   
    if fformXelements17.accepted:

        Glb['debug'] and print("     fformXelements17 accepted with: %s " % (fformXelements17.vars))
        fformXelements17_f0 = fformXelements17.vars.get('f0','')
        if len ( fformXelements17_f0 ):
            id_dfformXelements17 = db.dfformXelements17.insert( **fformXelements17.vars )
            db.commit()

            if not id_dfformXelements17 is None:
                dfformXelements17_row = db.dfformXelements17(id_dfformXelements17 )

                if not dfformXelements17_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements17.vars.f0}\" into db.dfformXelements17.f0, id = {id_dfformXelements17}' )
                         print(f"     found db.dfformXelements17.f0: \"{dfformXelements17_row.f0}\", id = {id_dfformXelements17}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements17_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements17.vars.items() ]
                print()
   
    elif fformXelements17.errors:
        print("fformXelements17 has errors: %s " % (fformXelements17.errors))
 

    dfformXelements18_row= None
    id_dfformXelements18 = None
    fformXelements18= Form(db.dfformXelements18, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements18",  formstyle=FormStyleBulma )
   
    if fformXelements18.accepted:

        Glb['debug'] and print("     fformXelements18 accepted with: %s " % (fformXelements18.vars))
        fformXelements18_f0 = fformXelements18.vars.get('f0','')
        if len ( fformXelements18_f0 ):
            id_dfformXelements18 = db.dfformXelements18.insert( **fformXelements18.vars )
            db.commit()

            if not id_dfformXelements18 is None:
                dfformXelements18_row = db.dfformXelements18(id_dfformXelements18 )

                if not dfformXelements18_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements18.vars.f0}\" into db.dfformXelements18.f0, id = {id_dfformXelements18}' )
                         print(f"     found db.dfformXelements18.f0: \"{dfformXelements18_row.f0}\", id = {id_dfformXelements18}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements18_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements18.vars.items() ]
                print()
   
    elif fformXelements18.errors:
        print("fformXelements18 has errors: %s " % (fformXelements18.errors))
 

    dfformXelements19_row= None
    id_dfformXelements19 = None
    fformXelements19= Form(db.dfformXelements19, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements19",  formstyle=FormStyleBulma )
   
    if fformXelements19.accepted:

        Glb['debug'] and print("     fformXelements19 accepted with: %s " % (fformXelements19.vars))
        fformXelements19_f0 = fformXelements19.vars.get('f0','')
        if len ( fformXelements19_f0 ):
            id_dfformXelements19 = db.dfformXelements19.insert( **fformXelements19.vars )
            db.commit()

            if not id_dfformXelements19 is None:
                dfformXelements19_row = db.dfformXelements19(id_dfformXelements19 )

                if not dfformXelements19_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements19.vars.f0}\" into db.dfformXelements19.f0, id = {id_dfformXelements19}' )
                         print(f"     found db.dfformXelements19.f0: \"{dfformXelements19_row.f0}\", id = {id_dfformXelements19}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements19_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements19.vars.items() ]
                print()
   
    elif fformXelements19.errors:
        print("fformXelements19 has errors: %s " % (fformXelements19.errors))
 

    dfformXelements20_row= None
    id_dfformXelements20 = None
    fformXelements20= Form(db.dfformXelements20, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements20",  formstyle=FormStyleBulma )
   
    if fformXelements20.accepted:

        Glb['debug'] and print("     fformXelements20 accepted with: %s " % (fformXelements20.vars))
        fformXelements20_f0 = fformXelements20.vars.get('f0','')
        if len ( fformXelements20_f0 ):
            id_dfformXelements20 = db.dfformXelements20.insert( **fformXelements20.vars )
            db.commit()

            if not id_dfformXelements20 is None:
                dfformXelements20_row = db.dfformXelements20(id_dfformXelements20 )

                if not dfformXelements20_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements20.vars.f0}\" into db.dfformXelements20.f0, id = {id_dfformXelements20}' )
                         print(f"     found db.dfformXelements20.f0: \"{dfformXelements20_row.f0}\", id = {id_dfformXelements20}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements20_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements20.vars.items() ]
                print()
   
    elif fformXelements20.errors:
        print("fformXelements20 has errors: %s " % (fformXelements20.errors))
 

    dfformXelements21_row= None
    id_dfformXelements21 = None
    fformXelements21= Form(db.dfformXelements21, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements21",  formstyle=FormStyleBulma )
   
    if fformXelements21.accepted:

        Glb['debug'] and print("     fformXelements21 accepted with: %s " % (fformXelements21.vars))
        fformXelements21_f0 = fformXelements21.vars.get('f0','')
        if len ( fformXelements21_f0 ):
            id_dfformXelements21 = db.dfformXelements21.insert( **fformXelements21.vars )
            db.commit()

            if not id_dfformXelements21 is None:
                dfformXelements21_row = db.dfformXelements21(id_dfformXelements21 )

                if not dfformXelements21_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements21.vars.f0}\" into db.dfformXelements21.f0, id = {id_dfformXelements21}' )
                         print(f"     found db.dfformXelements21.f0: \"{dfformXelements21_row.f0}\", id = {id_dfformXelements21}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements21_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements21.vars.items() ]
                print()
   
    elif fformXelements21.errors:
        print("fformXelements21 has errors: %s " % (fformXelements21.errors))
 

    dfformXelements22_row= None
    id_dfformXelements22 = None
    fformXelements22= Form(db.dfformXelements22, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements22",  formstyle=FormStyleBulma )
   
    if fformXelements22.accepted:

        Glb['debug'] and print("     fformXelements22 accepted with: %s " % (fformXelements22.vars))
        fformXelements22_f0 = fformXelements22.vars.get('f0','')
        if len ( fformXelements22_f0 ):
            id_dfformXelements22 = db.dfformXelements22.insert( **fformXelements22.vars )
            db.commit()

            if not id_dfformXelements22 is None:
                dfformXelements22_row = db.dfformXelements22(id_dfformXelements22 )

                if not dfformXelements22_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements22.vars.f0}\" into db.dfformXelements22.f0, id = {id_dfformXelements22}' )
                         print(f"     found db.dfformXelements22.f0: \"{dfformXelements22_row.f0}\", id = {id_dfformXelements22}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements22_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements22.vars.items() ]
                print()
   
    elif fformXelements22.errors:
        print("fformXelements22 has errors: %s " % (fformXelements22.errors))
 

    dfformXelements23_row= None
    id_dfformXelements23 = None
    fformXelements23= Form(db.dfformXelements23, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements23",  formstyle=FormStyleBulma )
   
    if fformXelements23.accepted:

        Glb['debug'] and print("     fformXelements23 accepted with: %s " % (fformXelements23.vars))
        fformXelements23_f0 = fformXelements23.vars.get('f0','')
        if len ( fformXelements23_f0 ):
            id_dfformXelements23 = db.dfformXelements23.insert( **fformXelements23.vars )
            db.commit()

            if not id_dfformXelements23 is None:
                dfformXelements23_row = db.dfformXelements23(id_dfformXelements23 )

                if not dfformXelements23_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements23.vars.f0}\" into db.dfformXelements23.f0, id = {id_dfformXelements23}' )
                         print(f"     found db.dfformXelements23.f0: \"{dfformXelements23_row.f0}\", id = {id_dfformXelements23}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements23_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements23.vars.items() ]
                print()
   
    elif fformXelements23.errors:
        print("fformXelements23 has errors: %s " % (fformXelements23.errors))
 

    dfformXelements24_row= None
    id_dfformXelements24 = None
    fformXelements24= Form(db.dfformXelements24, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements24",  formstyle=FormStyleBulma )
   
    if fformXelements24.accepted:

        Glb['debug'] and print("     fformXelements24 accepted with: %s " % (fformXelements24.vars))
        fformXelements24_f0 = fformXelements24.vars.get('f0','')
        if len ( fformXelements24_f0 ):
            id_dfformXelements24 = db.dfformXelements24.insert( **fformXelements24.vars )
            db.commit()

            if not id_dfformXelements24 is None:
                dfformXelements24_row = db.dfformXelements24(id_dfformXelements24 )

                if not dfformXelements24_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements24.vars.f0}\" into db.dfformXelements24.f0, id = {id_dfformXelements24}' )
                         print(f"     found db.dfformXelements24.f0: \"{dfformXelements24_row.f0}\", id = {id_dfformXelements24}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements24_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements24.vars.items() ]
                print()
   
    elif fformXelements24.errors:
        print("fformXelements24 has errors: %s " % (fformXelements24.errors))
 

    dfformXelements25_row= None
    id_dfformXelements25 = None
    fformXelements25= Form(db.dfformXelements25, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements25",  formstyle=FormStyleBulma )
   
    if fformXelements25.accepted:

        Glb['debug'] and print("     fformXelements25 accepted with: %s " % (fformXelements25.vars))
        fformXelements25_f0 = fformXelements25.vars.get('f0','')
        if len ( fformXelements25_f0 ):
            id_dfformXelements25 = db.dfformXelements25.insert( **fformXelements25.vars )
            db.commit()

            if not id_dfformXelements25 is None:
                dfformXelements25_row = db.dfformXelements25(id_dfformXelements25 )

                if not dfformXelements25_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements25.vars.f0}\" into db.dfformXelements25.f0, id = {id_dfformXelements25}' )
                         print(f"     found db.dfformXelements25.f0: \"{dfformXelements25_row.f0}\", id = {id_dfformXelements25}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements25_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements25.vars.items() ]
                print()
   
    elif fformXelements25.errors:
        print("fformXelements25 has errors: %s " % (fformXelements25.errors))
 

    dfformXelements26_row= None
    id_dfformXelements26 = None
    fformXelements26= Form(db.dfformXelements26, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements26",  formstyle=FormStyleBulma )
   
    if fformXelements26.accepted:

        Glb['debug'] and print("     fformXelements26 accepted with: %s " % (fformXelements26.vars))
        fformXelements26_f0 = fformXelements26.vars.get('f0','')
        if len ( fformXelements26_f0 ):
            id_dfformXelements26 = db.dfformXelements26.insert( **fformXelements26.vars )
            db.commit()

            if not id_dfformXelements26 is None:
                dfformXelements26_row = db.dfformXelements26(id_dfformXelements26 )

                if not dfformXelements26_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements26.vars.f0}\" into db.dfformXelements26.f0, id = {id_dfformXelements26}' )
                         print(f"     found db.dfformXelements26.f0: \"{dfformXelements26_row.f0}\", id = {id_dfformXelements26}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements26_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements26.vars.items() ]
                print()
   
    elif fformXelements26.errors:
        print("fformXelements26 has errors: %s " % (fformXelements26.errors))
 

    dfformXelements27_row= None
    id_dfformXelements27 = None
    fformXelements27= Form(db.dfformXelements27, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXelements27",  formstyle=FormStyleBulma )
   
    if fformXelements27.accepted:

        Glb['debug'] and print("     fformXelements27 accepted with: %s " % (fformXelements27.vars))
        fformXelements27_f0 = fformXelements27.vars.get('f0','')
        if len ( fformXelements27_f0 ):
            id_dfformXelements27 = db.dfformXelements27.insert( **fformXelements27.vars )
            db.commit()

            if not id_dfformXelements27 is None:
                dfformXelements27_row = db.dfformXelements27(id_dfformXelements27 )

                if not dfformXelements27_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXelements27.vars.f0}\" into db.dfformXelements27.f0, id = {id_dfformXelements27}' )
                         print(f"     found db.dfformXelements27.f0: \"{dfformXelements27_row.f0}\", id = {id_dfformXelements27}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXelements27_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXelements27.vars.items() ]
                print()
   
    elif fformXelements27.errors:
        print("fformXelements27 has errors: %s " % (fformXelements27.errors))
 

    return locals()


@action('composeXemail', method=["GET", "POST"] )
@action.uses(Template('compose-email.html', delimiters='[%[ ]]',), db, session,  T, )

def composeXemail(id=None):
    ctrl_info= "ctrl: composeXemail, view: compose-email.html"
    messages = []

    dfcomposeXemail0_row= None
    id_dfcomposeXemail0 = None
    fcomposeXemail0= Form(db.dfcomposeXemail0, id, deletable=False, dbio = False, keep_values = False, form_name = "fcomposeXemail0",  formstyle=FormStyleBulma )
   
    if fcomposeXemail0.accepted:

        Glb['debug'] and print("     fcomposeXemail0 accepted with: %s " % (fcomposeXemail0.vars))
        fcomposeXemail0_f0 = fcomposeXemail0.vars.get('f0','')
        if len ( fcomposeXemail0_f0 ):
            id_dfcomposeXemail0 = db.dfcomposeXemail0.insert( **fcomposeXemail0.vars )
            db.commit()

            if not id_dfcomposeXemail0 is None:
                dfcomposeXemail0_row = db.dfcomposeXemail0(id_dfcomposeXemail0 )

                if not dfcomposeXemail0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fcomposeXemail0.vars.f0}\" into db.dfcomposeXemail0.f0, id = {id_dfcomposeXemail0}' )
                         print(f"     found db.dfcomposeXemail0.f0: \"{dfcomposeXemail0_row.f0}\", id = {id_dfcomposeXemail0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fcomposeXemail0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fcomposeXemail0.vars.items() ]
                print()
   
    elif fcomposeXemail0.errors:
        print("fcomposeXemail0 has errors: %s " % (fcomposeXemail0.errors))
 

    return locals()


@action('loginXregister', method=["GET", "POST"] )
@action.uses(Template('login-register.html', delimiters='[%[ ]]',), db, session,  T, )

def loginXregister(id=None):
    ctrl_info= "ctrl: loginXregister, view: login-register.html"
    messages = []

    dfloginXregister0_row= None
    id_dfloginXregister0 = None
    floginXregister0= Form(db.dfloginXregister0, id, deletable=False, dbio = False, keep_values = False, form_name = "floginXregister0",  formstyle=FormStyleBulma )
   
    if floginXregister0.accepted:

        Glb['debug'] and print("     floginXregister0 accepted with: %s " % (floginXregister0.vars))
        floginXregister0_f0 = floginXregister0.vars.get('f0','')
        if len ( floginXregister0_f0 ):
            id_dfloginXregister0 = db.dfloginXregister0.insert( **floginXregister0.vars )
            db.commit()

            if not id_dfloginXregister0 is None:
                dfloginXregister0_row = db.dfloginXregister0(id_dfloginXregister0 )

                if not dfloginXregister0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{floginXregister0.vars.f0}\" into db.dfloginXregister0.f0, id = {id_dfloginXregister0}' )
                         print(f"     found db.dfloginXregister0.f0: \"{dfloginXregister0_row.f0}\", id = {id_dfloginXregister0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(floginXregister0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in floginXregister0.vars.items() ]
                print()
   
    elif floginXregister0.errors:
        print("floginXregister0 has errors: %s " % (floginXregister0.errors))
 

    dfloginXregister1_row= None
    id_dfloginXregister1 = None
    floginXregister1= Form(db.dfloginXregister1, id, deletable=False, dbio = False, keep_values = False, form_name = "floginXregister1",  formstyle=FormStyleBulma )
   
    if floginXregister1.accepted:

        Glb['debug'] and print("     floginXregister1 accepted with: %s " % (floginXregister1.vars))
        floginXregister1_f0 = floginXregister1.vars.get('f0','')
        if len ( floginXregister1_f0 ):
            id_dfloginXregister1 = db.dfloginXregister1.insert( **floginXregister1.vars )
            db.commit()

            if not id_dfloginXregister1 is None:
                dfloginXregister1_row = db.dfloginXregister1(id_dfloginXregister1 )

                if not dfloginXregister1_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{floginXregister1.vars.f0}\" into db.dfloginXregister1.f0, id = {id_dfloginXregister1}' )
                         print(f"     found db.dfloginXregister1.f0: \"{dfloginXregister1_row.f0}\", id = {id_dfloginXregister1}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(floginXregister1_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in floginXregister1.vars.items() ]
                print()
   
    elif floginXregister1.errors:
        print("floginXregister1 has errors: %s " % (floginXregister1.errors))
 

    dfloginXregister2_row= None
    id_dfloginXregister2 = None
    floginXregister2= Form(db.dfloginXregister2, id, deletable=False, dbio = False, keep_values = False, form_name = "floginXregister2",  formstyle=FormStyleBulma )
   
    if floginXregister2.accepted:

        Glb['debug'] and print("     floginXregister2 accepted with: %s " % (floginXregister2.vars))
        floginXregister2_f0 = floginXregister2.vars.get('f0','')
        if len ( floginXregister2_f0 ):
            id_dfloginXregister2 = db.dfloginXregister2.insert( **floginXregister2.vars )
            db.commit()

            if not id_dfloginXregister2 is None:
                dfloginXregister2_row = db.dfloginXregister2(id_dfloginXregister2 )

                if not dfloginXregister2_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{floginXregister2.vars.f0}\" into db.dfloginXregister2.f0, id = {id_dfloginXregister2}' )
                         print(f"     found db.dfloginXregister2.f0: \"{dfloginXregister2_row.f0}\", id = {id_dfloginXregister2}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(floginXregister2_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in floginXregister2.vars.items() ]
                print()
   
    elif floginXregister2.errors:
        print("floginXregister2 has errors: %s " % (floginXregister2.errors))
 

    dfloginXregister3_row= None
    id_dfloginXregister3 = None
    floginXregister3= Form(db.dfloginXregister3, id, deletable=False, dbio = False, keep_values = False, form_name = "floginXregister3",  formstyle=FormStyleBulma )
   
    if floginXregister3.accepted:

        Glb['debug'] and print("     floginXregister3 accepted with: %s " % (floginXregister3.vars))
        floginXregister3_f0 = floginXregister3.vars.get('f0','')
        if len ( floginXregister3_f0 ):
            id_dfloginXregister3 = db.dfloginXregister3.insert( **floginXregister3.vars )
            db.commit()

            if not id_dfloginXregister3 is None:
                dfloginXregister3_row = db.dfloginXregister3(id_dfloginXregister3 )

                if not dfloginXregister3_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{floginXregister3.vars.f0}\" into db.dfloginXregister3.f0, id = {id_dfloginXregister3}' )
                         print(f"     found db.dfloginXregister3.f0: \"{dfloginXregister3_row.f0}\", id = {id_dfloginXregister3}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(floginXregister3_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in floginXregister3.vars.items() ]
                print()
   
    elif floginXregister3.errors:
        print("floginXregister3 has errors: %s " % (floginXregister3.errors))
 

    dfloginXregister4_row= None
    id_dfloginXregister4 = None
    floginXregister4= Form(db.dfloginXregister4, id, deletable=False, dbio = False, keep_values = False, form_name = "floginXregister4",  formstyle=FormStyleBulma )
   
    if floginXregister4.accepted:

        Glb['debug'] and print("     floginXregister4 accepted with: %s " % (floginXregister4.vars))
        floginXregister4_f0 = floginXregister4.vars.get('f0','')
        if len ( floginXregister4_f0 ):
            id_dfloginXregister4 = db.dfloginXregister4.insert( **floginXregister4.vars )
            db.commit()

            if not id_dfloginXregister4 is None:
                dfloginXregister4_row = db.dfloginXregister4(id_dfloginXregister4 )

                if not dfloginXregister4_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{floginXregister4.vars.f0}\" into db.dfloginXregister4.f0, id = {id_dfloginXregister4}' )
                         print(f"     found db.dfloginXregister4.f0: \"{dfloginXregister4_row.f0}\", id = {id_dfloginXregister4}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(floginXregister4_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in floginXregister4.vars.items() ]
                print()
   
    elif floginXregister4.errors:
        print("floginXregister4 has errors: %s " % (floginXregister4.errors))
 

    dfloginXregister5_row= None
    id_dfloginXregister5 = None
    floginXregister5= Form(db.dfloginXregister5, id, deletable=False, dbio = False, keep_values = False, form_name = "floginXregister5",  formstyle=FormStyleBulma )
   
    if floginXregister5.accepted:

        Glb['debug'] and print("     floginXregister5 accepted with: %s " % (floginXregister5.vars))
        floginXregister5_f0 = floginXregister5.vars.get('f0','')
        if len ( floginXregister5_f0 ):
            id_dfloginXregister5 = db.dfloginXregister5.insert( **floginXregister5.vars )
            db.commit()

            if not id_dfloginXregister5 is None:
                dfloginXregister5_row = db.dfloginXregister5(id_dfloginXregister5 )

                if not dfloginXregister5_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{floginXregister5.vars.f0}\" into db.dfloginXregister5.f0, id = {id_dfloginXregister5}' )
                         print(f"     found db.dfloginXregister5.f0: \"{dfloginXregister5_row.f0}\", id = {id_dfloginXregister5}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(floginXregister5_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in floginXregister5.vars.items() ]
                print()
   
    elif floginXregister5.errors:
        print("floginXregister5 has errors: %s " % (floginXregister5.errors))
 

    dfloginXregister6_row= None
    id_dfloginXregister6 = None
    floginXregister6= Form(db.dfloginXregister6, id, deletable=False, dbio = False, keep_values = False, form_name = "floginXregister6",  formstyle=FormStyleBulma )
   
    if floginXregister6.accepted:

        Glb['debug'] and print("     floginXregister6 accepted with: %s " % (floginXregister6.vars))
        floginXregister6_f0 = floginXregister6.vars.get('f0','')
        if len ( floginXregister6_f0 ):
            id_dfloginXregister6 = db.dfloginXregister6.insert( **floginXregister6.vars )
            db.commit()

            if not id_dfloginXregister6 is None:
                dfloginXregister6_row = db.dfloginXregister6(id_dfloginXregister6 )

                if not dfloginXregister6_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{floginXregister6.vars.f0}\" into db.dfloginXregister6.f0, id = {id_dfloginXregister6}' )
                         print(f"     found db.dfloginXregister6.f0: \"{dfloginXregister6_row.f0}\", id = {id_dfloginXregister6}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(floginXregister6_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in floginXregister6.vars.items() ]
                print()
   
    elif floginXregister6.errors:
        print("floginXregister6 has errors: %s " % (floginXregister6.errors))
 

    return locals()


@action('formXcomponents', method=["GET", "POST"] )
@action.uses(Template('form-components.html', delimiters='[%[ ]]',), db, session,  T, )

def formXcomponents(id=None):
    ctrl_info= "ctrl: formXcomponents, view: form-components.html"
    messages = []

    dfformXcomponents0_row= None
    id_dfformXcomponents0 = None
    fformXcomponents0= Form(db.dfformXcomponents0, id, deletable=False, dbio = False, keep_values = False, form_name = "fformXcomponents0",  formstyle=FormStyleBulma )
   
    if fformXcomponents0.accepted:

        Glb['debug'] and print("     fformXcomponents0 accepted with: %s " % (fformXcomponents0.vars))
        fformXcomponents0_f0 = fformXcomponents0.vars.get('f0','')
        if len ( fformXcomponents0_f0 ):
            id_dfformXcomponents0 = db.dfformXcomponents0.insert( **fformXcomponents0.vars )
            db.commit()

            if not id_dfformXcomponents0 is None:
                dfformXcomponents0_row = db.dfformXcomponents0(id_dfformXcomponents0 )

                if not dfformXcomponents0_row is None:
                    if Glb['debug'] == True:
                         print(f"app: {Glb['my_app_name']}")
                         print(f'     inserted: \"{fformXcomponents0.vars.f0}\" into db.dfformXcomponents0.f0, id = {id_dfformXcomponents0}' )
                         print(f"     found db.dfformXcomponents0.f0: \"{dfformXcomponents0_row.f0}\", id = {id_dfformXcomponents0}" )
                         print ()
        else:
            if Glb['debug'] == True:
                print("app:",Glb['my_app_name'])
                print(f"     no entry inserted: len(fformXcomponents0_f0)=0")  
                _ = [ print (f'     {k}: {v}') for k,v in fformXcomponents0.vars.items() ]
                print()
   
    elif fformXcomponents0.errors:
        print("fformXcomponents0 has errors: %s " % (fformXcomponents0.errors))
 

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

