from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 21.10.2020 16:01:04
#

#import pydal

#from py4web import *
#from apps.myapp.models import db

#if not len( db().select(db.auth_user.id) ):
if not db(db.auth_user).count():
    body = {
        "username": "nil",
        "email": "nil@nil.com",
        "password": str(CRYPT()("xyz12345")[0]),
        #"password": str(pydal.validators.CRYPT()("xyz12345")[0]),
        "first_name": "MainUser",
        "last_name": "MainUserLast",
    }
    db.auth_user.insert(**body)
    db.commit()


db.define_table(
    'test_table',
    Field( 'f0', 'string', label='l0'),
    Field( 'f1', 'string', label='l1'),
    Field( 'f2', 'string', label='l2'),
    )

if not db(db.test_table).count():
    populate(db.test_table, n=10)


db.define_table(
    'dfband0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','text'),
    )

db.define_table(
    'dflogin0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','boolean'),
    )

db.define_table(
    'dfneumorphicXlogin0',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfshowcase0',
    )

db.define_table(
    'dfshowcase1',
    )

db.define_table(
    'dfshowcase2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','text'),
    )

db.define_table(
    'dfregister0',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'tadmin0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tpersonal0',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'ttabs0',
    Field('f0','string'),
    Field('f1','string'),
    )

if not db(db.tadmin0).count():
    db.tadmin0.insert(f0="p4w:len0", f1="p4w:Lorum ipsum dolem aire", f2="p4w:Action")
    db.tadmin0.insert(f0="p4w:len0", f1="p4w:Lorum ipsum dolem aire", f2="p4w:Action")
    db.tadmin0.insert(f0="p4w:len0", f1="p4w:Lorum ipsum dolem aire", f2="p4w:Action")
    db.tadmin0.insert(f0="p4w:len0", f1="p4w:Lorum ipsum dolem aire", f2="p4w:Action")
    db.tadmin0.insert(f0="p4w:len0", f1="p4w:Lorum ipsum dolem aire", f2="p4w:Action")
    db.tadmin0.insert(f0="p4w:len0", f1="p4w:Lorum ipsum dolem aire", f2="p4w:Action")
    db.tadmin0.insert(f0="p4w:len0", f1="p4w:Lorum ipsum dolem aire", f2="p4w:Action")
    db.tadmin0.insert(f0="p4w:len0", f1="p4w:Lorum ipsum dolem aire", f2="p4w:Action")
    db.tadmin0.insert(f0="p4w:len0", f1="p4w:Lorum ipsum dolem aire", f2="p4w:Action")
    db.commit()

if not db(db.tpersonal0).count():
    db.tpersonal0.insert(f0="p4w:len0", f1="p4w:len0")
    db.tpersonal0.insert(f0="p4w:Address:", f1="p4w:Gurus Lab")
    db.tpersonal0.insert(f0="p4w:Phone:", f1="p4w:0123-456789")
    db.tpersonal0.insert(f0="p4w:Email:", f1="p4w:minion@despicable.me")
    db.commit()

if not db(db.ttabs0).count():
    db.ttabs0.insert(f0="p4w:One", f1="p4w:Two")
    db.ttabs0.insert(f0="p4w:Three", f1="p4w:Four")
    db.ttabs0.insert(f0="p4w:Five", f1="p4w:Six")
    db.ttabs0.insert(f0="p4w:Seven", f1="p4w:Eight")
    db.ttabs0.insert(f0="p4w:Nine", f1="p4w:Ten")
    db.ttabs0.insert(f0="p4w:Eleven", f1="p4w:Twelve")
    db.commit()
