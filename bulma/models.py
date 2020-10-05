from .common import db, Field
from pydal.validators import *

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
    'dfadmin0',
    Field('f0','string'),
    )

db.define_table(
    'dfadmin1',
    Field('f0','string'),
    )

db.define_table(
    'dfband0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','text'),
    )

db.define_table(
    'dfforum0',
    Field('f0','string'),
    )

db.define_table(
    'dfhelloXparallax0',
    Field('f0','string'),
    )

db.define_table(
    'dfhelloXparallax1',
    Field('f0','string'),
    )

db.define_table(
    'dfinstaAlbum0',
    Field('f0','string'),
    )

db.define_table(
    'dfinstaAlbum1',
    Field('f0','string'),
    )

db.define_table(
    'dfinstaAlbum2',
    Field('f0','string'),
    )

db.define_table(
    'dfinstaAlbum3',
    Field('f0','string'),
    )

db.define_table(
    'dfkanban0',
    Field('f0','string'),
    )

db.define_table(
    'dfkanbanXsearchX0',
    Field('f0','string'),
    )

db.define_table(
    'dflanding0',
    Field('f0','string'),
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
    'dfpersonal0',
    Field('f0','string'),
    )

db.define_table(
    'dfpersonal1',
    Field('f0','string'),
    )

db.define_table(
    'dfpersonal2',
    Field('f0','text'),
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
    'dfcontact0',
    Field('f0','string'),
    )

db.define_table(
    'dfcontact1',
    Field('f0','string'),
    )

db.define_table(
    'dfcontact2',
    Field('f0','text'),
    )

db.define_table(
    'dfblogXtailsaw0',
    Field('f0','string'),
    )

db.define_table(
    'dfblogXtailsaw1',
    Field('f0','string'),
    )

db.define_table(
    'dfsearch0',
    Field('f0','string'),
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
