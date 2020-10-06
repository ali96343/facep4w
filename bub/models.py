from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate


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
    'dfindex0',
    Field('f0','string'),
    )

db.define_table(
    'dflogin0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','boolean'),
    )

db.define_table(
    'dfcharts0',
    Field('f0','string'),
    )

db.define_table(
    'dftables0',
    Field('f0','string'),
    )

db.define_table(
    'dfforms0',
    Field('f0','string'),
    )

db.define_table(
    'dfforms1',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfforms2',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfforms3',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfforms4',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfforms5',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    Field('f7','boolean'),
    Field('f8','string'),
    Field('f9','string'),
    Field('f10','boolean'),
    Field('f11','boolean'),
    Field('f12','boolean'),
    Field('f13','boolean'),
    Field('f14','string'),
    Field('f15','string'),
    Field('f16','string'),
    Field('f17','string'),
    Field('f18','string'),
    Field('f19','string'),
    Field('f20','string'),
    Field('f21','string'),
    Field('f22','string'),
    Field('f23','string'),
    Field('f24','string'),
    Field('f25','string'),
    Field('f26','string'),
    Field('f27','string'),
    Field('f28','string'),
    Field('f29','boolean'),
    Field('f30','string'),
    Field('f31','string'),
    Field('f32','string'),
    Field('f33','string'),
    Field('f34','string'),
    Field('f35','string'),
    )

db.define_table(
    'ttables0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'ttables1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'ttables2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'ttables3',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

if not db(db.ttables0).count():
    db.ttables0.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.ttables0.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttables0.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttables0.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.commit()

if not db(db.ttables1).count():
    db.ttables1.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.ttables1.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttables1.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttables1.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.commit()

if not db(db.ttables2).count():
    db.ttables2.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.ttables2.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttables2.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttables2.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.ttables2.insert(f0="p4w:3", f1="p4w:Sam", f2="p4w:Nevoresky", f3="p4w:@facebook")
    db.commit()

if not db(db.ttables3).count():
    db.ttables3.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.ttables3.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttables3.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttables3.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.ttables3.insert(f0="p4w:4", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttables3.insert(f0="p4w:5", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttables3.insert(f0="p4w:6", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.commit()
