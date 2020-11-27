from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 27.11.2020 15:03:38 UTC+3
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
db.commit()

if not db(db.test_table).count():
    populate(db.test_table, n=10)
    db.commit()


db.define_table(
    'dfindex0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dflogin0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfcharts0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftables0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','boolean',  ),
    Field('f8','string', length=1024, ),
    Field('f9','string', length=1024, ),
    Field('f10','boolean',  ),
    Field('f11','boolean',  ),
    Field('f12','boolean',  ),
    Field('f13','boolean',  ),
    Field('f14','string', length=1024, ),
    Field('f15','string', length=1024, ),
    Field('f16','string', length=1024, ),
    Field('f17','string', length=1024, ),
    Field('f18','string', length=1024, ),
    Field('f19','string', length=1024, ),
    Field('f20','string', length=1024, ),
    Field('f21','string', length=1024, ),
    Field('f22','string', length=1024, ),
    Field('f23','string', length=1024, ),
    Field('f24','string', length=1024, ),
    Field('f25','string', length=1024, ),
    Field('f26','string', length=1024, ),
    Field('f27','string', length=1024, ),
    Field('f28','string', length=1024, ),
    Field('f29','boolean',  ),
    Field('f30','string', length=1024, ),
    Field('f31','string', length=1024, ),
    Field('f32','string', length=1024, ),
    Field('f33','string', length=1024, ),
    Field('f34','string', length=1024, ),
    Field('f35','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttables3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

if not db(db.ttables0).count():
    db.ttables0.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttables0.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttables0.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.ttables1).count():
    db.ttables1.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttables1.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttables1.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.ttables2).count():
    db.ttables2.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttables2.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttables2.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.ttables2.insert(f0="3", f1="Sam", f2="Nevoresky", f3="@facebook")
    db.commit()

if not db(db.ttables3).count():
    db.ttables3.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.ttables3.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttables3.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.ttables3.insert(f0="4", f1="Mark", f2="Otto", f3="@mdo")
    db.ttables3.insert(f0="5", f1="Jacob", f2="Thornton", f3="@fat")
    db.ttables3.insert(f0="6", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()
