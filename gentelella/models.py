from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 21.10.2020 16:07:41
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
    'dfform0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'dfform1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    Field('f7','string'),
    )

db.define_table(
    'dfform2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','boolean'),
    Field('f5','boolean'),
    Field('f6','boolean'),
    Field('f7','boolean'),
    Field('f8','string'),
    Field('f9','text'),
    )

db.define_table(
    'dfform3',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','text'),
    )

db.define_table(
    'dfform4',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'dfform5',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfform6',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfform7',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','boolean'),
    )

db.define_table(
    'dfformXadvanced0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'dfformXadvanced1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'dfformXadvanced2',
    Field('f0','string'),
    )

db.define_table(
    'dfformXadvanced3',
    Field('f0','string'),
    )

db.define_table(
    'dfformXvalidation0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    Field('f7','string'),
    Field('f8','string'),
    Field('f9','string'),
    Field('f10','text'),
    )

db.define_table(
    'dfformXwizards0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'dfformXwizards1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'dfformXupload0',
    )

db.define_table(
    'dfcalendar0',
    Field('f0','string'),
    Field('f1','text'),
    )

db.define_table(
    'dfcalendar1',
    Field('f0','string'),
    Field('f1','text'),
    )

db.define_table(
    'dfpageX4030',
    Field('f0','string'),
    )

db.define_table(
    'dfpageX4040',
    Field('f0','string'),
    )

db.define_table(
    'dfpageX5000',
    Field('f0','string'),
    )

db.define_table(
    'dflogin0',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dflogin1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tformXadvanced0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tformXadvanced1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tformXadvanced2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tformXadvanced3',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tformXadvanced4',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tformXadvanced5',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tformXadvanced6',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tformXadvanced7',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tgeneralXelements0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tgeneralXelements1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tinvoice0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tinvoice1',
    Field('f0','string'),
    Field('f1','string'),
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

db.define_table(
    'ttables4',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    Field('f7','string'),
    Field('f8','string'),
    )

db.define_table(
    'ttablesXdynamic0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'ttablesXdynamic1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    Field('f7','string'),
    )

db.define_table(
    'ttablesXdynamic2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'ttablesXdynamic3',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'ttablesXdynamic4',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'ttablesXdynamic5',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    Field('f7','string'),
    Field('f8','string'),
    )

db.define_table(
    'totherXcharts0',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'tprojects0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'tprofile0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

if not db(db.tformXadvanced0).count():
    db.tformXadvanced0.insert(f0="p4w:len0", f1="p4w:Oct 2016", f2="p4w:len0")
    db.tformXadvanced0.insert(f0="p4w:Su", f1="p4w:Mo", f2="p4w:Tu", f3="p4w:We", f4="p4w:Th", f5="p4w:Fr", f6="p4w:Sa")
    db.tformXadvanced0.insert(f0="p4w:25", f1="p4w:26", f2="p4w:27", f3="p4w:28", f4="p4w:29", f5="p4w:30", f6="p4w:1")
    db.tformXadvanced0.insert(f0="p4w:2", f1="p4w:3", f2="p4w:4", f3="p4w:5", f4="p4w:6", f5="p4w:7", f6="p4w:8")
    db.tformXadvanced0.insert(f0="p4w:9", f1="p4w:10", f2="p4w:11", f3="p4w:12", f4="p4w:13", f5="p4w:14", f6="p4w:15")
    db.tformXadvanced0.insert(f0="p4w:16", f1="p4w:17", f2="p4w:18", f3="p4w:19", f4="p4w:20", f5="p4w:21", f6="p4w:22")
    db.tformXadvanced0.insert(f0="p4w:23", f1="p4w:24", f2="p4w:25", f3="p4w:26", f4="p4w:27", f5="p4w:28", f6="p4w:29")
    db.tformXadvanced0.insert(f0="p4w:30", f1="p4w:31", f2="p4w:1", f3="p4w:2", f4="p4w:3", f5="p4w:4", f6="p4w:5")
    db.commit()

if not db(db.tformXadvanced1).count():
    db.tformXadvanced1.insert(f0="p4w:len0", f1="p4w:Nov 2016", f2="p4w:len0")
    db.tformXadvanced1.insert(f0="p4w:Su", f1="p4w:Mo", f2="p4w:Tu", f3="p4w:We", f4="p4w:Th", f5="p4w:Fr", f6="p4w:Sa")
    db.tformXadvanced1.insert(f0="p4w:30", f1="p4w:31", f2="p4w:1", f3="p4w:2", f4="p4w:3", f5="p4w:4", f6="p4w:5")
    db.tformXadvanced1.insert(f0="p4w:6", f1="p4w:7", f2="p4w:8", f3="p4w:9", f4="p4w:10", f5="p4w:11", f6="p4w:12")
    db.tformXadvanced1.insert(f0="p4w:13", f1="p4w:14", f2="p4w:15", f3="p4w:16", f4="p4w:17", f5="p4w:18", f6="p4w:19")
    db.tformXadvanced1.insert(f0="p4w:20", f1="p4w:21", f2="p4w:22", f3="p4w:23", f4="p4w:24", f5="p4w:25", f6="p4w:26")
    db.tformXadvanced1.insert(f0="p4w:27", f1="p4w:28", f2="p4w:29", f3="p4w:30", f4="p4w:1", f5="p4w:2", f6="p4w:3")
    db.tformXadvanced1.insert(f0="p4w:4", f1="p4w:5", f2="p4w:6", f3="p4w:7", f4="p4w:8", f5="p4w:9", f6="p4w:10")
    db.commit()

if not db(db.tformXadvanced2).count():
    db.tformXadvanced2.insert(f0="p4w:len0", f1="p4w:Oct 2016", f2="p4w:len0")
    db.tformXadvanced2.insert(f0="p4w:Su", f1="p4w:Mo", f2="p4w:Tu", f3="p4w:We", f4="p4w:Th", f5="p4w:Fr", f6="p4w:Sa")
    db.tformXadvanced2.insert(f0="p4w:25", f1="p4w:26", f2="p4w:27", f3="p4w:28", f4="p4w:29", f5="p4w:30", f6="p4w:1")
    db.tformXadvanced2.insert(f0="p4w:2", f1="p4w:3", f2="p4w:4", f3="p4w:5", f4="p4w:6", f5="p4w:7", f6="p4w:8")
    db.tformXadvanced2.insert(f0="p4w:9", f1="p4w:10", f2="p4w:11", f3="p4w:12", f4="p4w:13", f5="p4w:14", f6="p4w:15")
    db.tformXadvanced2.insert(f0="p4w:16", f1="p4w:17", f2="p4w:18", f3="p4w:19", f4="p4w:20", f5="p4w:21", f6="p4w:22")
    db.tformXadvanced2.insert(f0="p4w:23", f1="p4w:24", f2="p4w:25", f3="p4w:26", f4="p4w:27", f5="p4w:28", f6="p4w:29")
    db.tformXadvanced2.insert(f0="p4w:30", f1="p4w:31", f2="p4w:1", f3="p4w:2", f4="p4w:3", f5="p4w:4", f6="p4w:5")
    db.commit()

if not db(db.tformXadvanced3).count():
    db.tformXadvanced3.insert(f0="p4w:len0", f1="p4w:Nov 2016", f2="p4w:len0")
    db.tformXadvanced3.insert(f0="p4w:Su", f1="p4w:Mo", f2="p4w:Tu", f3="p4w:We", f4="p4w:Th", f5="p4w:Fr", f6="p4w:Sa")
    db.tformXadvanced3.insert(f0="p4w:30", f1="p4w:31", f2="p4w:1", f3="p4w:2", f4="p4w:3", f5="p4w:4", f6="p4w:5")
    db.tformXadvanced3.insert(f0="p4w:6", f1="p4w:7", f2="p4w:8", f3="p4w:9", f4="p4w:10", f5="p4w:11", f6="p4w:12")
    db.tformXadvanced3.insert(f0="p4w:13", f1="p4w:14", f2="p4w:15", f3="p4w:16", f4="p4w:17", f5="p4w:18", f6="p4w:19")
    db.tformXadvanced3.insert(f0="p4w:20", f1="p4w:21", f2="p4w:22", f3="p4w:23", f4="p4w:24", f5="p4w:25", f6="p4w:26")
    db.tformXadvanced3.insert(f0="p4w:27", f1="p4w:28", f2="p4w:29", f3="p4w:30", f4="p4w:1", f5="p4w:2", f6="p4w:3")
    db.tformXadvanced3.insert(f0="p4w:4", f1="p4w:5", f2="p4w:6", f3="p4w:7", f4="p4w:8", f5="p4w:9", f6="p4w:10")
    db.commit()

if not db(db.tformXadvanced4).count():
    db.tformXadvanced4.insert(f0="p4w:len0", f1="p4w:Oct 2016", f2="p4w:len0")
    db.tformXadvanced4.insert(f0="p4w:Su", f1="p4w:Mo", f2="p4w:Tu", f3="p4w:We", f4="p4w:Th", f5="p4w:Fr", f6="p4w:Sa")
    db.tformXadvanced4.insert(f0="p4w:25", f1="p4w:26", f2="p4w:27", f3="p4w:28", f4="p4w:29", f5="p4w:30", f6="p4w:1")
    db.tformXadvanced4.insert(f0="p4w:2", f1="p4w:3", f2="p4w:4", f3="p4w:5", f4="p4w:6", f5="p4w:7", f6="p4w:8")
    db.tformXadvanced4.insert(f0="p4w:9", f1="p4w:10", f2="p4w:11", f3="p4w:12", f4="p4w:13", f5="p4w:14", f6="p4w:15")
    db.tformXadvanced4.insert(f0="p4w:16", f1="p4w:17", f2="p4w:18", f3="p4w:19", f4="p4w:20", f5="p4w:21", f6="p4w:22")
    db.tformXadvanced4.insert(f0="p4w:23", f1="p4w:24", f2="p4w:25", f3="p4w:26", f4="p4w:27", f5="p4w:28", f6="p4w:29")
    db.tformXadvanced4.insert(f0="p4w:30", f1="p4w:31", f2="p4w:1", f3="p4w:2", f4="p4w:3", f5="p4w:4", f6="p4w:5")
    db.commit()

if not db(db.tformXadvanced5).count():
    db.tformXadvanced5.insert(f0="p4w:len0", f1="p4w:Nov 2016", f2="p4w:len0")
    db.tformXadvanced5.insert(f0="p4w:Su", f1="p4w:Mo", f2="p4w:Tu", f3="p4w:We", f4="p4w:Th", f5="p4w:Fr", f6="p4w:Sa")
    db.tformXadvanced5.insert(f0="p4w:30", f1="p4w:31", f2="p4w:1", f3="p4w:2", f4="p4w:3", f5="p4w:4", f6="p4w:5")
    db.tformXadvanced5.insert(f0="p4w:6", f1="p4w:7", f2="p4w:8", f3="p4w:9", f4="p4w:10", f5="p4w:11", f6="p4w:12")
    db.tformXadvanced5.insert(f0="p4w:13", f1="p4w:14", f2="p4w:15", f3="p4w:16", f4="p4w:17", f5="p4w:18", f6="p4w:19")
    db.tformXadvanced5.insert(f0="p4w:20", f1="p4w:21", f2="p4w:22", f3="p4w:23", f4="p4w:24", f5="p4w:25", f6="p4w:26")
    db.tformXadvanced5.insert(f0="p4w:27", f1="p4w:28", f2="p4w:29", f3="p4w:30", f4="p4w:1", f5="p4w:2", f6="p4w:3")
    db.tformXadvanced5.insert(f0="p4w:4", f1="p4w:5", f2="p4w:6", f3="p4w:7", f4="p4w:8", f5="p4w:9", f6="p4w:10")
    db.commit()

if not db(db.tformXadvanced6).count():
    db.tformXadvanced6.insert(f0="p4w:len0", f1="p4w:Oct 2016", f2="p4w:len0")
    db.tformXadvanced6.insert(f0="p4w:Su", f1="p4w:Mo", f2="p4w:Tu", f3="p4w:We", f4="p4w:Th", f5="p4w:Fr", f6="p4w:Sa")
    db.tformXadvanced6.insert(f0="p4w:25", f1="p4w:26", f2="p4w:27", f3="p4w:28", f4="p4w:29", f5="p4w:30", f6="p4w:1")
    db.tformXadvanced6.insert(f0="p4w:2", f1="p4w:3", f2="p4w:4", f3="p4w:5", f4="p4w:6", f5="p4w:7", f6="p4w:8")
    db.tformXadvanced6.insert(f0="p4w:9", f1="p4w:10", f2="p4w:11", f3="p4w:12", f4="p4w:13", f5="p4w:14", f6="p4w:15")
    db.tformXadvanced6.insert(f0="p4w:16", f1="p4w:17", f2="p4w:18", f3="p4w:19", f4="p4w:20", f5="p4w:21", f6="p4w:22")
    db.tformXadvanced6.insert(f0="p4w:23", f1="p4w:24", f2="p4w:25", f3="p4w:26", f4="p4w:27", f5="p4w:28", f6="p4w:29")
    db.tformXadvanced6.insert(f0="p4w:30", f1="p4w:31", f2="p4w:1", f3="p4w:2", f4="p4w:3", f5="p4w:4", f6="p4w:5")
    db.commit()

if not db(db.tformXadvanced7).count():
    db.tformXadvanced7.insert(f0="p4w:len0", f1="p4w:Nov 2016", f2="p4w:len0")
    db.tformXadvanced7.insert(f0="p4w:Su", f1="p4w:Mo", f2="p4w:Tu", f3="p4w:We", f4="p4w:Th", f5="p4w:Fr", f6="p4w:Sa")
    db.tformXadvanced7.insert(f0="p4w:30", f1="p4w:31", f2="p4w:1", f3="p4w:2", f4="p4w:3", f5="p4w:4", f6="p4w:5")
    db.tformXadvanced7.insert(f0="p4w:6", f1="p4w:7", f2="p4w:8", f3="p4w:9", f4="p4w:10", f5="p4w:11", f6="p4w:12")
    db.tformXadvanced7.insert(f0="p4w:13", f1="p4w:14", f2="p4w:15", f3="p4w:16", f4="p4w:17", f5="p4w:18", f6="p4w:19")
    db.tformXadvanced7.insert(f0="p4w:20", f1="p4w:21", f2="p4w:22", f3="p4w:23", f4="p4w:24", f5="p4w:25", f6="p4w:26")
    db.tformXadvanced7.insert(f0="p4w:27", f1="p4w:28", f2="p4w:29", f3="p4w:30", f4="p4w:1", f5="p4w:2", f6="p4w:3")
    db.tformXadvanced7.insert(f0="p4w:4", f1="p4w:5", f2="p4w:6", f3="p4w:7", f4="p4w:8", f5="p4w:9", f6="p4w:10")
    db.commit()

if not db(db.tgeneralXelements0).count():
    db.tgeneralXelements0.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.tgeneralXelements0.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.tgeneralXelements0.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.tgeneralXelements0.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.commit()

if not db(db.tgeneralXelements1).count():
    db.tgeneralXelements1.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.tgeneralXelements1.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.tgeneralXelements1.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.tgeneralXelements1.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.commit()

if not db(db.tinvoice0).count():
    db.tinvoice0.insert(f0="p4w:Qty", f1="p4w:Product", f2="p4w:Serial #", f3="p4w:Description", f4="p4w:Subtotal")
    db.tinvoice0.insert(f0="p4w:1", f1="p4w:Call of Duty", f2="p4w:455-981-221", f3="p4w:El snort testosterone trophy driving gloves handsome gerry Richardson helvetica tousled street art master testosterone trophy driving gloves handsome gerry Richardson", f4="p4w:$64.50")
    db.tinvoice0.insert(f0="p4w:1", f1="p4w:Need for Speed IV", f2="p4w:247-925-726", f3="p4w:Wes Anderson umami biodiesel", f4="p4w:$50.00")
    db.tinvoice0.insert(f0="p4w:1", f1="p4w:Monsters DVD", f2="p4w:735-845-642", f3="p4w:Terry Richardson helvetica tousled street art master, El snort testosterone trophy driving gloves handsome letterpress erry Richardson helvetica tousled", f4="p4w:$10.70")
    db.tinvoice0.insert(f0="p4w:1", f1="p4w:Grown Ups Blue Ray", f2="p4w:422-568-642", f3="p4w:Tousled lomo letterpress erry Richardson helvetica tousled street art master helvetica tousled street art master, El snort testosterone", f4="p4w:$25.99")
    db.commit()

if not db(db.tinvoice1).count():
    db.tinvoice1.insert(f0="p4w:Subtotal:", f1="p4w:$250.30")
    db.tinvoice1.insert(f0="p4w:Tax (9.3%)", f1="p4w:$10.34")
    db.tinvoice1.insert(f0="p4w:Shipping:", f1="p4w:$5.80")
    db.tinvoice1.insert(f0="p4w:Total:", f1="p4w:$265.24")
    db.commit()

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
    db.commit()

if not db(db.ttables3).count():
    db.ttables3.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.ttables3.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttables3.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttables3.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.commit()

if not db(db.ttables4).count():
    db.ttables4.insert(f0="p4w:len0", f1="p4w:Invoice", f2="p4w:Invoice Date", f3="p4w:Order", f4="p4w:Bill to Name", f5="p4w:Status", f6="p4w:Amount", f7="p4w:Action", f8="p4w:Bulk Actions ( )")
    db.ttables4.insert(f0="p4w:len0", f1="p4w:121000040", f2="p4w:May 23, 2014 11:47:56 PM", f3="p4w:121000210", f4="p4w:John Blank L", f5="p4w:Paid", f6="p4w:$7.45", f7="p4w:View")
    db.ttables4.insert(f0="p4w:len0", f1="p4w:121000039", f2="p4w:May 23, 2014 11:30:12 PM", f3="p4w:121000208", f4="p4w:John Blank L", f5="p4w:Paid", f6="p4w:$741.20", f7="p4w:View")
    db.ttables4.insert(f0="p4w:len0", f1="p4w:121000038", f2="p4w:May 24, 2014 10:55:33 PM", f3="p4w:121000203", f4="p4w:Mike Smith", f5="p4w:Paid", f6="p4w:$432.26", f7="p4w:View")
    db.ttables4.insert(f0="p4w:len0", f1="p4w:121000037", f2="p4w:May 24, 2014 10:52:44 PM", f3="p4w:121000204", f4="p4w:Mike Smith", f5="p4w:Paid", f6="p4w:$333.21", f7="p4w:View")
    db.ttables4.insert(f0="p4w:len0", f1="p4w:121000040", f2="p4w:May 24, 2014 11:47:56 PM", f3="p4w:121000210", f4="p4w:John Blank L", f5="p4w:Paid", f6="p4w:$7.45", f7="p4w:View")
    db.ttables4.insert(f0="p4w:len0", f1="p4w:121000039", f2="p4w:May 26, 2014 11:30:12 PM", f3="p4w:121000208", f4="p4w:John Blank L", f5="p4w:Paid", f6="p4w:$741.20", f7="p4w:View")
    db.ttables4.insert(f0="p4w:len0", f1="p4w:121000038", f2="p4w:May 26, 2014 10:55:33 PM", f3="p4w:121000203", f4="p4w:Mike Smith", f5="p4w:Paid", f6="p4w:$432.26", f7="p4w:View")
    db.ttables4.insert(f0="p4w:len0", f1="p4w:121000037", f2="p4w:May 26, 2014 10:52:44 PM", f3="p4w:121000204", f4="p4w:Mike Smith", f5="p4w:Paid", f6="p4w:$333.21", f7="p4w:View")
    db.ttables4.insert(f0="p4w:len0", f1="p4w:121000040", f2="p4w:May 27, 2014 11:47:56 PM", f3="p4w:121000210", f4="p4w:John Blank L", f5="p4w:Paid", f6="p4w:$7.45", f7="p4w:View")
    db.ttables4.insert(f0="p4w:len0", f1="p4w:121000039", f2="p4w:May 28, 2014 11:30:12 PM", f3="p4w:121000208", f4="p4w:John Blank L", f5="p4w:Paid", f6="p4w:$741.20", f7="p4w:View")
    db.commit()

if not db(db.ttablesXdynamic0).count():
    db.ttablesXdynamic0.insert(f0="p4w:Name", f1="p4w:Position", f2="p4w:Office", f3="p4w:Age", f4="p4w:Start date", f5="p4w:Salary")
    db.ttablesXdynamic0.insert(f0="p4w:Tiger Nixon", f1="p4w:System Architect", f2="p4w:Edinburgh", f3="p4w:61", f4="p4w:2011/04/25", f5="p4w:$320,800")
    db.ttablesXdynamic0.insert(f0="p4w:Garrett Winters", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:63", f4="p4w:2011/07/25", f5="p4w:$170,750")
    db.ttablesXdynamic0.insert(f0="p4w:Ashton Cox", f1="p4w:Junior Technical Author", f2="p4w:San Francisco", f3="p4w:66", f4="p4w:2009/01/12", f5="p4w:$86,000")
    db.ttablesXdynamic0.insert(f0="p4w:Cedric Kelly", f1="p4w:Senior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2012/03/29", f5="p4w:$433,060")
    db.ttablesXdynamic0.insert(f0="p4w:Airi Satou", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:33", f4="p4w:2008/11/28", f5="p4w:$162,700")
    db.ttablesXdynamic0.insert(f0="p4w:Brielle Williamson", f1="p4w:Integration Specialist", f2="p4w:New York", f3="p4w:61", f4="p4w:2012/12/02", f5="p4w:$372,000")
    db.ttablesXdynamic0.insert(f0="p4w:Herrod Chandler", f1="p4w:Sales Assistant", f2="p4w:San Francisco", f3="p4w:59", f4="p4w:2012/08/06", f5="p4w:$137,500")
    db.ttablesXdynamic0.insert(f0="p4w:Rhona Davidson", f1="p4w:Integration Specialist", f2="p4w:Tokyo", f3="p4w:55", f4="p4w:2010/10/14", f5="p4w:$327,900")
    db.ttablesXdynamic0.insert(f0="p4w:Colleen Hurst", f1="p4w:Javascript Developer", f2="p4w:San Francisco", f3="p4w:39", f4="p4w:2009/09/15", f5="p4w:$205,500")
    db.ttablesXdynamic0.insert(f0="p4w:Sonya Frost", f1="p4w:Software Engineer", f2="p4w:Edinburgh", f3="p4w:23", f4="p4w:2008/12/13", f5="p4w:$103,600")
    db.ttablesXdynamic0.insert(f0="p4w:Jena Gaines", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:30", f4="p4w:2008/12/19", f5="p4w:$90,560")
    db.ttablesXdynamic0.insert(f0="p4w:Quinn Flynn", f1="p4w:Support Lead", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2013/03/03", f5="p4w:$342,000")
    db.ttablesXdynamic0.insert(f0="p4w:Charde Marshall", f1="p4w:Regional Director", f2="p4w:San Francisco", f3="p4w:36", f4="p4w:2008/10/16", f5="p4w:$470,600")
    db.ttablesXdynamic0.insert(f0="p4w:Haley Kennedy", f1="p4w:Senior Marketing Designer", f2="p4w:London", f3="p4w:43", f4="p4w:2012/12/18", f5="p4w:$313,500")
    db.ttablesXdynamic0.insert(f0="p4w:Tatyana Fitzpatrick", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:19", f4="p4w:2010/03/17", f5="p4w:$385,750")
    db.ttablesXdynamic0.insert(f0="p4w:Michael Silva", f1="p4w:Marketing Designer", f2="p4w:London", f3="p4w:66", f4="p4w:2012/11/27", f5="p4w:$198,500")
    db.ttablesXdynamic0.insert(f0="p4w:Paul Byrd", f1="p4w:Chief Financial Officer (CFO)", f2="p4w:New York", f3="p4w:64", f4="p4w:2010/06/09", f5="p4w:$725,000")
    db.ttablesXdynamic0.insert(f0="p4w:Gloria Little", f1="p4w:Systems Administrator", f2="p4w:New York", f3="p4w:59", f4="p4w:2009/04/10", f5="p4w:$237,500")
    db.ttablesXdynamic0.insert(f0="p4w:Bradley Greer", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:41", f4="p4w:2012/10/13", f5="p4w:$132,000")
    db.ttablesXdynamic0.insert(f0="p4w:Dai Rios", f1="p4w:Personnel Lead", f2="p4w:Edinburgh", f3="p4w:35", f4="p4w:2012/09/26", f5="p4w:$217,500")
    db.ttablesXdynamic0.insert(f0="p4w:Jenette Caldwell", f1="p4w:Development Lead", f2="p4w:New York", f3="p4w:30", f4="p4w:2011/09/03", f5="p4w:$345,000")
    db.ttablesXdynamic0.insert(f0="p4w:Yuri Berry", f1="p4w:Chief Marketing Officer (CMO)", f2="p4w:New York", f3="p4w:40", f4="p4w:2009/06/25", f5="p4w:$675,000")
    db.ttablesXdynamic0.insert(f0="p4w:Caesar Vance", f1="p4w:Pre-Sales Support", f2="p4w:New York", f3="p4w:21", f4="p4w:2011/12/12", f5="p4w:$106,450")
    db.ttablesXdynamic0.insert(f0="p4w:Doris Wilder", f1="p4w:Sales Assistant", f2="p4w:Sidney", f3="p4w:23", f4="p4w:2010/09/20", f5="p4w:$85,600")
    db.ttablesXdynamic0.insert(f0="p4w:Angelica Ramos", f1="p4w:Chief Executive Officer (CEO)", f2="p4w:London", f3="p4w:47", f4="p4w:2009/10/09", f5="p4w:$1,200,000")
    db.ttablesXdynamic0.insert(f0="p4w:Gavin Joyce", f1="p4w:Developer", f2="p4w:Edinburgh", f3="p4w:42", f4="p4w:2010/12/22", f5="p4w:$92,575")
    db.ttablesXdynamic0.insert(f0="p4w:Jennifer Chang", f1="p4w:Regional Director", f2="p4w:Singapore", f3="p4w:28", f4="p4w:2010/11/14", f5="p4w:$357,650")
    db.ttablesXdynamic0.insert(f0="p4w:Brenden Wagner", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:28", f4="p4w:2011/06/07", f5="p4w:$206,850")
    db.ttablesXdynamic0.insert(f0="p4w:Fiona Green", f1="p4w:Chief Operating Officer (COO)", f2="p4w:San Francisco", f3="p4w:48", f4="p4w:2010/03/11", f5="p4w:$850,000")
    db.ttablesXdynamic0.insert(f0="p4w:Shou Itou", f1="p4w:Regional Marketing", f2="p4w:Tokyo", f3="p4w:20", f4="p4w:2011/08/14", f5="p4w:$163,000")
    db.ttablesXdynamic0.insert(f0="p4w:Michelle House", f1="p4w:Integration Specialist", f2="p4w:Sidney", f3="p4w:37", f4="p4w:2011/06/02", f5="p4w:$95,400")
    db.ttablesXdynamic0.insert(f0="p4w:Suki Burks", f1="p4w:Developer", f2="p4w:London", f3="p4w:53", f4="p4w:2009/10/22", f5="p4w:$114,500")
    db.ttablesXdynamic0.insert(f0="p4w:Prescott Bartlett", f1="p4w:Technical Author", f2="p4w:London", f3="p4w:27", f4="p4w:2011/05/07", f5="p4w:$145,000")
    db.ttablesXdynamic0.insert(f0="p4w:Gavin Cortez", f1="p4w:Team Leader", f2="p4w:San Francisco", f3="p4w:22", f4="p4w:2008/10/26", f5="p4w:$235,500")
    db.ttablesXdynamic0.insert(f0="p4w:Martena Mccray", f1="p4w:Post-Sales support", f2="p4w:Edinburgh", f3="p4w:46", f4="p4w:2011/03/09", f5="p4w:$324,050")
    db.ttablesXdynamic0.insert(f0="p4w:Unity Butler", f1="p4w:Marketing Designer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/12/09", f5="p4w:$85,675")
    db.ttablesXdynamic0.insert(f0="p4w:Howard Hatfield", f1="p4w:Office Manager", f2="p4w:San Francisco", f3="p4w:51", f4="p4w:2008/12/16", f5="p4w:$164,500")
    db.ttablesXdynamic0.insert(f0="p4w:Hope Fuentes", f1="p4w:Secretary", f2="p4w:San Francisco", f3="p4w:41", f4="p4w:2010/02/12", f5="p4w:$109,850")
    db.ttablesXdynamic0.insert(f0="p4w:Vivian Harrell", f1="p4w:Financial Controller", f2="p4w:San Francisco", f3="p4w:62", f4="p4w:2009/02/14", f5="p4w:$452,500")
    db.ttablesXdynamic0.insert(f0="p4w:Timothy Mooney", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:37", f4="p4w:2008/12/11", f5="p4w:$136,200")
    db.ttablesXdynamic0.insert(f0="p4w:Jackson Bradshaw", f1="p4w:Director", f2="p4w:New York", f3="p4w:65", f4="p4w:2008/09/26", f5="p4w:$645,750")
    db.ttablesXdynamic0.insert(f0="p4w:Olivia Liang", f1="p4w:Support Engineer", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2011/02/03", f5="p4w:$234,500")
    db.ttablesXdynamic0.insert(f0="p4w:Bruno Nash", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:38", f4="p4w:2011/05/03", f5="p4w:$163,500")
    db.ttablesXdynamic0.insert(f0="p4w:Sakura Yamamoto", f1="p4w:Support Engineer", f2="p4w:Tokyo", f3="p4w:37", f4="p4w:2009/08/19", f5="p4w:$139,575")
    db.ttablesXdynamic0.insert(f0="p4w:Thor Walton", f1="p4w:Developer", f2="p4w:New York", f3="p4w:61", f4="p4w:2013/08/11", f5="p4w:$98,540")
    db.ttablesXdynamic0.insert(f0="p4w:Finn Camacho", f1="p4w:Support Engineer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/07/07", f5="p4w:$87,500")
    db.ttablesXdynamic0.insert(f0="p4w:Serge Baldwin", f1="p4w:Data Coordinator", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2012/04/09", f5="p4w:$138,575")
    db.ttablesXdynamic0.insert(f0="p4w:Zenaida Frank", f1="p4w:Software Engineer", f2="p4w:New York", f3="p4w:63", f4="p4w:2010/01/04", f5="p4w:$125,250")
    db.ttablesXdynamic0.insert(f0="p4w:Zorita Serrano", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:56", f4="p4w:2012/06/01", f5="p4w:$115,000")
    db.ttablesXdynamic0.insert(f0="p4w:Jennifer Acosta", f1="p4w:Junior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:43", f4="p4w:2013/02/01", f5="p4w:$75,650")
    db.ttablesXdynamic0.insert(f0="p4w:Cara Stevens", f1="p4w:Sales Assistant", f2="p4w:New York", f3="p4w:46", f4="p4w:2011/12/06", f5="p4w:$145,600")
    db.ttablesXdynamic0.insert(f0="p4w:Hermione Butler", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:47", f4="p4w:2011/03/21", f5="p4w:$356,250")
    db.ttablesXdynamic0.insert(f0="p4w:Lael Greer", f1="p4w:Systems Administrator", f2="p4w:London", f3="p4w:21", f4="p4w:2009/02/27", f5="p4w:$103,500")
    db.ttablesXdynamic0.insert(f0="p4w:Jonas Alexander", f1="p4w:Developer", f2="p4w:San Francisco", f3="p4w:30", f4="p4w:2010/07/14", f5="p4w:$86,500")
    db.ttablesXdynamic0.insert(f0="p4w:Shad Decker", f1="p4w:Regional Director", f2="p4w:Edinburgh", f3="p4w:51", f4="p4w:2008/11/13", f5="p4w:$183,000")
    db.ttablesXdynamic0.insert(f0="p4w:Michael Bruce", f1="p4w:Javascript Developer", f2="p4w:Singapore", f3="p4w:29", f4="p4w:2011/06/27", f5="p4w:$183,000")
    db.ttablesXdynamic0.insert(f0="p4w:Donna Snider", f1="p4w:Customer Support", f2="p4w:New York", f3="p4w:27", f4="p4w:2011/01/25", f5="p4w:$112,000")
    db.commit()

if not db(db.ttablesXdynamic1).count():
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Name", f3="p4w:Position", f4="p4w:Office", f5="p4w:Age", f6="p4w:Start date", f7="p4w:Salary")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Tiger Nixon", f3="p4w:System Architect", f4="p4w:Edinburgh", f5="p4w:61", f6="p4w:2011/04/25", f7="p4w:$320,800")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Garrett Winters", f3="p4w:Accountant", f4="p4w:Tokyo", f5="p4w:63", f6="p4w:2011/07/25", f7="p4w:$170,750")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Ashton Cox", f3="p4w:Junior Technical Author", f4="p4w:San Francisco", f5="p4w:66", f6="p4w:2009/01/12", f7="p4w:$86,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Cedric Kelly", f3="p4w:Senior Javascript Developer", f4="p4w:Edinburgh", f5="p4w:22", f6="p4w:2012/03/29", f7="p4w:$433,060")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Airi Satou", f3="p4w:Accountant", f4="p4w:Tokyo", f5="p4w:33", f6="p4w:2008/11/28", f7="p4w:$162,700")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Brielle Williamson", f3="p4w:Integration Specialist", f4="p4w:New York", f5="p4w:61", f6="p4w:2012/12/02", f7="p4w:$372,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Herrod Chandler", f3="p4w:Sales Assistant", f4="p4w:San Francisco", f5="p4w:59", f6="p4w:2012/08/06", f7="p4w:$137,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Rhona Davidson", f3="p4w:Integration Specialist", f4="p4w:Tokyo", f5="p4w:55", f6="p4w:2010/10/14", f7="p4w:$327,900")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Colleen Hurst", f3="p4w:Javascript Developer", f4="p4w:San Francisco", f5="p4w:39", f6="p4w:2009/09/15", f7="p4w:$205,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Sonya Frost", f3="p4w:Software Engineer", f4="p4w:Edinburgh", f5="p4w:23", f6="p4w:2008/12/13", f7="p4w:$103,600")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Jena Gaines", f3="p4w:Office Manager", f4="p4w:London", f5="p4w:30", f6="p4w:2008/12/19", f7="p4w:$90,560")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Quinn Flynn", f3="p4w:Support Lead", f4="p4w:Edinburgh", f5="p4w:22", f6="p4w:2013/03/03", f7="p4w:$342,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Charde Marshall", f3="p4w:Regional Director", f4="p4w:San Francisco", f5="p4w:36", f6="p4w:2008/10/16", f7="p4w:$470,600")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Haley Kennedy", f3="p4w:Senior Marketing Designer", f4="p4w:London", f5="p4w:43", f6="p4w:2012/12/18", f7="p4w:$313,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Tatyana Fitzpatrick", f3="p4w:Regional Director", f4="p4w:London", f5="p4w:19", f6="p4w:2010/03/17", f7="p4w:$385,750")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Michael Silva", f3="p4w:Marketing Designer", f4="p4w:London", f5="p4w:66", f6="p4w:2012/11/27", f7="p4w:$198,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Paul Byrd", f3="p4w:Chief Financial Officer (CFO)", f4="p4w:New York", f5="p4w:64", f6="p4w:2010/06/09", f7="p4w:$725,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Gloria Little", f3="p4w:Systems Administrator", f4="p4w:New York", f5="p4w:59", f6="p4w:2009/04/10", f7="p4w:$237,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Bradley Greer", f3="p4w:Software Engineer", f4="p4w:London", f5="p4w:41", f6="p4w:2012/10/13", f7="p4w:$132,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Dai Rios", f3="p4w:Personnel Lead", f4="p4w:Edinburgh", f5="p4w:35", f6="p4w:2012/09/26", f7="p4w:$217,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Jenette Caldwell", f3="p4w:Development Lead", f4="p4w:New York", f5="p4w:30", f6="p4w:2011/09/03", f7="p4w:$345,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Yuri Berry", f3="p4w:Chief Marketing Officer (CMO)", f4="p4w:New York", f5="p4w:40", f6="p4w:2009/06/25", f7="p4w:$675,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Caesar Vance", f3="p4w:Pre-Sales Support", f4="p4w:New York", f5="p4w:21", f6="p4w:2011/12/12", f7="p4w:$106,450")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Doris Wilder", f3="p4w:Sales Assistant", f4="p4w:Sidney", f5="p4w:23", f6="p4w:2010/09/20", f7="p4w:$85,600")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Angelica Ramos", f3="p4w:Chief Executive Officer (CEO)", f4="p4w:London", f5="p4w:47", f6="p4w:2009/10/09", f7="p4w:$1,200,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Gavin Joyce", f3="p4w:Developer", f4="p4w:Edinburgh", f5="p4w:42", f6="p4w:2010/12/22", f7="p4w:$92,575")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Jennifer Chang", f3="p4w:Regional Director", f4="p4w:Singapore", f5="p4w:28", f6="p4w:2010/11/14", f7="p4w:$357,650")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Brenden Wagner", f3="p4w:Software Engineer", f4="p4w:San Francisco", f5="p4w:28", f6="p4w:2011/06/07", f7="p4w:$206,850")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Fiona Green", f3="p4w:Chief Operating Officer (COO)", f4="p4w:San Francisco", f5="p4w:48", f6="p4w:2010/03/11", f7="p4w:$850,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Shou Itou", f3="p4w:Regional Marketing", f4="p4w:Tokyo", f5="p4w:20", f6="p4w:2011/08/14", f7="p4w:$163,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Michelle House", f3="p4w:Integration Specialist", f4="p4w:Sidney", f5="p4w:37", f6="p4w:2011/06/02", f7="p4w:$95,400")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Suki Burks", f3="p4w:Developer", f4="p4w:London", f5="p4w:53", f6="p4w:2009/10/22", f7="p4w:$114,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Prescott Bartlett", f3="p4w:Technical Author", f4="p4w:London", f5="p4w:27", f6="p4w:2011/05/07", f7="p4w:$145,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Gavin Cortez", f3="p4w:Team Leader", f4="p4w:San Francisco", f5="p4w:22", f6="p4w:2008/10/26", f7="p4w:$235,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Martena Mccray", f3="p4w:Post-Sales support", f4="p4w:Edinburgh", f5="p4w:46", f6="p4w:2011/03/09", f7="p4w:$324,050")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Unity Butler", f3="p4w:Marketing Designer", f4="p4w:San Francisco", f5="p4w:47", f6="p4w:2009/12/09", f7="p4w:$85,675")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Howard Hatfield", f3="p4w:Office Manager", f4="p4w:San Francisco", f5="p4w:51", f6="p4w:2008/12/16", f7="p4w:$164,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Hope Fuentes", f3="p4w:Secretary", f4="p4w:San Francisco", f5="p4w:41", f6="p4w:2010/02/12", f7="p4w:$109,850")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Vivian Harrell", f3="p4w:Financial Controller", f4="p4w:San Francisco", f5="p4w:62", f6="p4w:2009/02/14", f7="p4w:$452,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Timothy Mooney", f3="p4w:Office Manager", f4="p4w:London", f5="p4w:37", f6="p4w:2008/12/11", f7="p4w:$136,200")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Jackson Bradshaw", f3="p4w:Director", f4="p4w:New York", f5="p4w:65", f6="p4w:2008/09/26", f7="p4w:$645,750")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Olivia Liang", f3="p4w:Support Engineer", f4="p4w:Singapore", f5="p4w:64", f6="p4w:2011/02/03", f7="p4w:$234,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Bruno Nash", f3="p4w:Software Engineer", f4="p4w:London", f5="p4w:38", f6="p4w:2011/05/03", f7="p4w:$163,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Sakura Yamamoto", f3="p4w:Support Engineer", f4="p4w:Tokyo", f5="p4w:37", f6="p4w:2009/08/19", f7="p4w:$139,575")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Thor Walton", f3="p4w:Developer", f4="p4w:New York", f5="p4w:61", f6="p4w:2013/08/11", f7="p4w:$98,540")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Finn Camacho", f3="p4w:Support Engineer", f4="p4w:San Francisco", f5="p4w:47", f6="p4w:2009/07/07", f7="p4w:$87,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Serge Baldwin", f3="p4w:Data Coordinator", f4="p4w:Singapore", f5="p4w:64", f6="p4w:2012/04/09", f7="p4w:$138,575")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Zenaida Frank", f3="p4w:Software Engineer", f4="p4w:New York", f5="p4w:63", f6="p4w:2010/01/04", f7="p4w:$125,250")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Zorita Serrano", f3="p4w:Software Engineer", f4="p4w:San Francisco", f5="p4w:56", f6="p4w:2012/06/01", f7="p4w:$115,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Jennifer Acosta", f3="p4w:Junior Javascript Developer", f4="p4w:Edinburgh", f5="p4w:43", f6="p4w:2013/02/01", f7="p4w:$75,650")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Cara Stevens", f3="p4w:Sales Assistant", f4="p4w:New York", f5="p4w:46", f6="p4w:2011/12/06", f7="p4w:$145,600")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Hermione Butler", f3="p4w:Regional Director", f4="p4w:London", f5="p4w:47", f6="p4w:2011/03/21", f7="p4w:$356,250")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Lael Greer", f3="p4w:Systems Administrator", f4="p4w:London", f5="p4w:21", f6="p4w:2009/02/27", f7="p4w:$103,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Jonas Alexander", f3="p4w:Developer", f4="p4w:San Francisco", f5="p4w:30", f6="p4w:2010/07/14", f7="p4w:$86,500")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Shad Decker", f3="p4w:Regional Director", f4="p4w:Edinburgh", f5="p4w:51", f6="p4w:2008/11/13", f7="p4w:$183,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Michael Bruce", f3="p4w:Javascript Developer", f4="p4w:Singapore", f5="p4w:29", f6="p4w:2011/06/27", f7="p4w:$183,000")
    db.ttablesXdynamic1.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Donna Snider", f3="p4w:Customer Support", f4="p4w:New York", f5="p4w:27", f6="p4w:2011/01/25", f7="p4w:$112,000")
    db.commit()

if not db(db.ttablesXdynamic2).count():
    db.ttablesXdynamic2.insert(f0="p4w:Name", f1="p4w:Position", f2="p4w:Office", f3="p4w:Age", f4="p4w:Start date", f5="p4w:Salary")
    db.ttablesXdynamic2.insert(f0="p4w:Tiger Nixon", f1="p4w:System Architect", f2="p4w:Edinburgh", f3="p4w:61", f4="p4w:2011/04/25", f5="p4w:$320,800")
    db.ttablesXdynamic2.insert(f0="p4w:Garrett Winters", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:63", f4="p4w:2011/07/25", f5="p4w:$170,750")
    db.ttablesXdynamic2.insert(f0="p4w:Ashton Cox", f1="p4w:Junior Technical Author", f2="p4w:San Francisco", f3="p4w:66", f4="p4w:2009/01/12", f5="p4w:$86,000")
    db.ttablesXdynamic2.insert(f0="p4w:Cedric Kelly", f1="p4w:Senior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2012/03/29", f5="p4w:$433,060")
    db.ttablesXdynamic2.insert(f0="p4w:Airi Satou", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:33", f4="p4w:2008/11/28", f5="p4w:$162,700")
    db.ttablesXdynamic2.insert(f0="p4w:Brielle Williamson", f1="p4w:Integration Specialist", f2="p4w:New York", f3="p4w:61", f4="p4w:2012/12/02", f5="p4w:$372,000")
    db.ttablesXdynamic2.insert(f0="p4w:Herrod Chandler", f1="p4w:Sales Assistant", f2="p4w:San Francisco", f3="p4w:59", f4="p4w:2012/08/06", f5="p4w:$137,500")
    db.ttablesXdynamic2.insert(f0="p4w:Rhona Davidson", f1="p4w:Integration Specialist", f2="p4w:Tokyo", f3="p4w:55", f4="p4w:2010/10/14", f5="p4w:$327,900")
    db.ttablesXdynamic2.insert(f0="p4w:Colleen Hurst", f1="p4w:Javascript Developer", f2="p4w:San Francisco", f3="p4w:39", f4="p4w:2009/09/15", f5="p4w:$205,500")
    db.ttablesXdynamic2.insert(f0="p4w:Sonya Frost", f1="p4w:Software Engineer", f2="p4w:Edinburgh", f3="p4w:23", f4="p4w:2008/12/13", f5="p4w:$103,600")
    db.ttablesXdynamic2.insert(f0="p4w:Jena Gaines", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:30", f4="p4w:2008/12/19", f5="p4w:$90,560")
    db.ttablesXdynamic2.insert(f0="p4w:Quinn Flynn", f1="p4w:Support Lead", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2013/03/03", f5="p4w:$342,000")
    db.ttablesXdynamic2.insert(f0="p4w:Charde Marshall", f1="p4w:Regional Director", f2="p4w:San Francisco", f3="p4w:36", f4="p4w:2008/10/16", f5="p4w:$470,600")
    db.ttablesXdynamic2.insert(f0="p4w:Haley Kennedy", f1="p4w:Senior Marketing Designer", f2="p4w:London", f3="p4w:43", f4="p4w:2012/12/18", f5="p4w:$313,500")
    db.ttablesXdynamic2.insert(f0="p4w:Tatyana Fitzpatrick", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:19", f4="p4w:2010/03/17", f5="p4w:$385,750")
    db.ttablesXdynamic2.insert(f0="p4w:Michael Silva", f1="p4w:Marketing Designer", f2="p4w:London", f3="p4w:66", f4="p4w:2012/11/27", f5="p4w:$198,500")
    db.ttablesXdynamic2.insert(f0="p4w:Paul Byrd", f1="p4w:Chief Financial Officer (CFO)", f2="p4w:New York", f3="p4w:64", f4="p4w:2010/06/09", f5="p4w:$725,000")
    db.ttablesXdynamic2.insert(f0="p4w:Gloria Little", f1="p4w:Systems Administrator", f2="p4w:New York", f3="p4w:59", f4="p4w:2009/04/10", f5="p4w:$237,500")
    db.ttablesXdynamic2.insert(f0="p4w:Bradley Greer", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:41", f4="p4w:2012/10/13", f5="p4w:$132,000")
    db.ttablesXdynamic2.insert(f0="p4w:Dai Rios", f1="p4w:Personnel Lead", f2="p4w:Edinburgh", f3="p4w:35", f4="p4w:2012/09/26", f5="p4w:$217,500")
    db.ttablesXdynamic2.insert(f0="p4w:Jenette Caldwell", f1="p4w:Development Lead", f2="p4w:New York", f3="p4w:30", f4="p4w:2011/09/03", f5="p4w:$345,000")
    db.ttablesXdynamic2.insert(f0="p4w:Yuri Berry", f1="p4w:Chief Marketing Officer (CMO)", f2="p4w:New York", f3="p4w:40", f4="p4w:2009/06/25", f5="p4w:$675,000")
    db.ttablesXdynamic2.insert(f0="p4w:Caesar Vance", f1="p4w:Pre-Sales Support", f2="p4w:New York", f3="p4w:21", f4="p4w:2011/12/12", f5="p4w:$106,450")
    db.ttablesXdynamic2.insert(f0="p4w:Doris Wilder", f1="p4w:Sales Assistant", f2="p4w:Sidney", f3="p4w:23", f4="p4w:2010/09/20", f5="p4w:$85,600")
    db.ttablesXdynamic2.insert(f0="p4w:Angelica Ramos", f1="p4w:Chief Executive Officer (CEO)", f2="p4w:London", f3="p4w:47", f4="p4w:2009/10/09", f5="p4w:$1,200,000")
    db.ttablesXdynamic2.insert(f0="p4w:Gavin Joyce", f1="p4w:Developer", f2="p4w:Edinburgh", f3="p4w:42", f4="p4w:2010/12/22", f5="p4w:$92,575")
    db.ttablesXdynamic2.insert(f0="p4w:Jennifer Chang", f1="p4w:Regional Director", f2="p4w:Singapore", f3="p4w:28", f4="p4w:2010/11/14", f5="p4w:$357,650")
    db.ttablesXdynamic2.insert(f0="p4w:Brenden Wagner", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:28", f4="p4w:2011/06/07", f5="p4w:$206,850")
    db.ttablesXdynamic2.insert(f0="p4w:Fiona Green", f1="p4w:Chief Operating Officer (COO)", f2="p4w:San Francisco", f3="p4w:48", f4="p4w:2010/03/11", f5="p4w:$850,000")
    db.ttablesXdynamic2.insert(f0="p4w:Shou Itou", f1="p4w:Regional Marketing", f2="p4w:Tokyo", f3="p4w:20", f4="p4w:2011/08/14", f5="p4w:$163,000")
    db.ttablesXdynamic2.insert(f0="p4w:Michelle House", f1="p4w:Integration Specialist", f2="p4w:Sidney", f3="p4w:37", f4="p4w:2011/06/02", f5="p4w:$95,400")
    db.ttablesXdynamic2.insert(f0="p4w:Suki Burks", f1="p4w:Developer", f2="p4w:London", f3="p4w:53", f4="p4w:2009/10/22", f5="p4w:$114,500")
    db.ttablesXdynamic2.insert(f0="p4w:Prescott Bartlett", f1="p4w:Technical Author", f2="p4w:London", f3="p4w:27", f4="p4w:2011/05/07", f5="p4w:$145,000")
    db.ttablesXdynamic2.insert(f0="p4w:Gavin Cortez", f1="p4w:Team Leader", f2="p4w:San Francisco", f3="p4w:22", f4="p4w:2008/10/26", f5="p4w:$235,500")
    db.ttablesXdynamic2.insert(f0="p4w:Martena Mccray", f1="p4w:Post-Sales support", f2="p4w:Edinburgh", f3="p4w:46", f4="p4w:2011/03/09", f5="p4w:$324,050")
    db.ttablesXdynamic2.insert(f0="p4w:Unity Butler", f1="p4w:Marketing Designer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/12/09", f5="p4w:$85,675")
    db.ttablesXdynamic2.insert(f0="p4w:Howard Hatfield", f1="p4w:Office Manager", f2="p4w:San Francisco", f3="p4w:51", f4="p4w:2008/12/16", f5="p4w:$164,500")
    db.ttablesXdynamic2.insert(f0="p4w:Hope Fuentes", f1="p4w:Secretary", f2="p4w:San Francisco", f3="p4w:41", f4="p4w:2010/02/12", f5="p4w:$109,850")
    db.ttablesXdynamic2.insert(f0="p4w:Vivian Harrell", f1="p4w:Financial Controller", f2="p4w:San Francisco", f3="p4w:62", f4="p4w:2009/02/14", f5="p4w:$452,500")
    db.ttablesXdynamic2.insert(f0="p4w:Timothy Mooney", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:37", f4="p4w:2008/12/11", f5="p4w:$136,200")
    db.ttablesXdynamic2.insert(f0="p4w:Jackson Bradshaw", f1="p4w:Director", f2="p4w:New York", f3="p4w:65", f4="p4w:2008/09/26", f5="p4w:$645,750")
    db.ttablesXdynamic2.insert(f0="p4w:Olivia Liang", f1="p4w:Support Engineer", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2011/02/03", f5="p4w:$234,500")
    db.ttablesXdynamic2.insert(f0="p4w:Bruno Nash", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:38", f4="p4w:2011/05/03", f5="p4w:$163,500")
    db.ttablesXdynamic2.insert(f0="p4w:Sakura Yamamoto", f1="p4w:Support Engineer", f2="p4w:Tokyo", f3="p4w:37", f4="p4w:2009/08/19", f5="p4w:$139,575")
    db.ttablesXdynamic2.insert(f0="p4w:Thor Walton", f1="p4w:Developer", f2="p4w:New York", f3="p4w:61", f4="p4w:2013/08/11", f5="p4w:$98,540")
    db.ttablesXdynamic2.insert(f0="p4w:Finn Camacho", f1="p4w:Support Engineer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/07/07", f5="p4w:$87,500")
    db.ttablesXdynamic2.insert(f0="p4w:Serge Baldwin", f1="p4w:Data Coordinator", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2012/04/09", f5="p4w:$138,575")
    db.ttablesXdynamic2.insert(f0="p4w:Zenaida Frank", f1="p4w:Software Engineer", f2="p4w:New York", f3="p4w:63", f4="p4w:2010/01/04", f5="p4w:$125,250")
    db.ttablesXdynamic2.insert(f0="p4w:Zorita Serrano", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:56", f4="p4w:2012/06/01", f5="p4w:$115,000")
    db.ttablesXdynamic2.insert(f0="p4w:Jennifer Acosta", f1="p4w:Junior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:43", f4="p4w:2013/02/01", f5="p4w:$75,650")
    db.ttablesXdynamic2.insert(f0="p4w:Cara Stevens", f1="p4w:Sales Assistant", f2="p4w:New York", f3="p4w:46", f4="p4w:2011/12/06", f5="p4w:$145,600")
    db.ttablesXdynamic2.insert(f0="p4w:Hermione Butler", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:47", f4="p4w:2011/03/21", f5="p4w:$356,250")
    db.ttablesXdynamic2.insert(f0="p4w:Lael Greer", f1="p4w:Systems Administrator", f2="p4w:London", f3="p4w:21", f4="p4w:2009/02/27", f5="p4w:$103,500")
    db.ttablesXdynamic2.insert(f0="p4w:Jonas Alexander", f1="p4w:Developer", f2="p4w:San Francisco", f3="p4w:30", f4="p4w:2010/07/14", f5="p4w:$86,500")
    db.ttablesXdynamic2.insert(f0="p4w:Shad Decker", f1="p4w:Regional Director", f2="p4w:Edinburgh", f3="p4w:51", f4="p4w:2008/11/13", f5="p4w:$183,000")
    db.ttablesXdynamic2.insert(f0="p4w:Michael Bruce", f1="p4w:Javascript Developer", f2="p4w:Singapore", f3="p4w:29", f4="p4w:2011/06/27", f5="p4w:$183,000")
    db.ttablesXdynamic2.insert(f0="p4w:Donna Snider", f1="p4w:Customer Support", f2="p4w:New York", f3="p4w:27", f4="p4w:2011/01/25", f5="p4w:$112,000")
    db.commit()

if not db(db.ttablesXdynamic3).count():
    db.ttablesXdynamic3.insert(f0="p4w:Name", f1="p4w:Position", f2="p4w:Office", f3="p4w:Age", f4="p4w:Start date", f5="p4w:Salary")
    db.ttablesXdynamic3.insert(f0="p4w:Tiger Nixon", f1="p4w:System Architect", f2="p4w:Edinburgh", f3="p4w:61", f4="p4w:2011/04/25", f5="p4w:$320,800")
    db.ttablesXdynamic3.insert(f0="p4w:Garrett Winters", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:63", f4="p4w:2011/07/25", f5="p4w:$170,750")
    db.ttablesXdynamic3.insert(f0="p4w:Ashton Cox", f1="p4w:Junior Technical Author", f2="p4w:San Francisco", f3="p4w:66", f4="p4w:2009/01/12", f5="p4w:$86,000")
    db.ttablesXdynamic3.insert(f0="p4w:Cedric Kelly", f1="p4w:Senior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2012/03/29", f5="p4w:$433,060")
    db.ttablesXdynamic3.insert(f0="p4w:Airi Satou", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:33", f4="p4w:2008/11/28", f5="p4w:$162,700")
    db.ttablesXdynamic3.insert(f0="p4w:Brielle Williamson", f1="p4w:Integration Specialist", f2="p4w:New York", f3="p4w:61", f4="p4w:2012/12/02", f5="p4w:$372,000")
    db.ttablesXdynamic3.insert(f0="p4w:Herrod Chandler", f1="p4w:Sales Assistant", f2="p4w:San Francisco", f3="p4w:59", f4="p4w:2012/08/06", f5="p4w:$137,500")
    db.ttablesXdynamic3.insert(f0="p4w:Rhona Davidson", f1="p4w:Integration Specialist", f2="p4w:Tokyo", f3="p4w:55", f4="p4w:2010/10/14", f5="p4w:$327,900")
    db.ttablesXdynamic3.insert(f0="p4w:Colleen Hurst", f1="p4w:Javascript Developer", f2="p4w:San Francisco", f3="p4w:39", f4="p4w:2009/09/15", f5="p4w:$205,500")
    db.ttablesXdynamic3.insert(f0="p4w:Sonya Frost", f1="p4w:Software Engineer", f2="p4w:Edinburgh", f3="p4w:23", f4="p4w:2008/12/13", f5="p4w:$103,600")
    db.ttablesXdynamic3.insert(f0="p4w:Jena Gaines", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:30", f4="p4w:2008/12/19", f5="p4w:$90,560")
    db.ttablesXdynamic3.insert(f0="p4w:Quinn Flynn", f1="p4w:Support Lead", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2013/03/03", f5="p4w:$342,000")
    db.ttablesXdynamic3.insert(f0="p4w:Charde Marshall", f1="p4w:Regional Director", f2="p4w:San Francisco", f3="p4w:36", f4="p4w:2008/10/16", f5="p4w:$470,600")
    db.ttablesXdynamic3.insert(f0="p4w:Haley Kennedy", f1="p4w:Senior Marketing Designer", f2="p4w:London", f3="p4w:43", f4="p4w:2012/12/18", f5="p4w:$313,500")
    db.ttablesXdynamic3.insert(f0="p4w:Tatyana Fitzpatrick", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:19", f4="p4w:2010/03/17", f5="p4w:$385,750")
    db.ttablesXdynamic3.insert(f0="p4w:Michael Silva", f1="p4w:Marketing Designer", f2="p4w:London", f3="p4w:66", f4="p4w:2012/11/27", f5="p4w:$198,500")
    db.ttablesXdynamic3.insert(f0="p4w:Paul Byrd", f1="p4w:Chief Financial Officer (CFO)", f2="p4w:New York", f3="p4w:64", f4="p4w:2010/06/09", f5="p4w:$725,000")
    db.ttablesXdynamic3.insert(f0="p4w:Gloria Little", f1="p4w:Systems Administrator", f2="p4w:New York", f3="p4w:59", f4="p4w:2009/04/10", f5="p4w:$237,500")
    db.ttablesXdynamic3.insert(f0="p4w:Bradley Greer", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:41", f4="p4w:2012/10/13", f5="p4w:$132,000")
    db.ttablesXdynamic3.insert(f0="p4w:Dai Rios", f1="p4w:Personnel Lead", f2="p4w:Edinburgh", f3="p4w:35", f4="p4w:2012/09/26", f5="p4w:$217,500")
    db.ttablesXdynamic3.insert(f0="p4w:Jenette Caldwell", f1="p4w:Development Lead", f2="p4w:New York", f3="p4w:30", f4="p4w:2011/09/03", f5="p4w:$345,000")
    db.ttablesXdynamic3.insert(f0="p4w:Yuri Berry", f1="p4w:Chief Marketing Officer (CMO)", f2="p4w:New York", f3="p4w:40", f4="p4w:2009/06/25", f5="p4w:$675,000")
    db.ttablesXdynamic3.insert(f0="p4w:Caesar Vance", f1="p4w:Pre-Sales Support", f2="p4w:New York", f3="p4w:21", f4="p4w:2011/12/12", f5="p4w:$106,450")
    db.ttablesXdynamic3.insert(f0="p4w:Doris Wilder", f1="p4w:Sales Assistant", f2="p4w:Sidney", f3="p4w:23", f4="p4w:2010/09/20", f5="p4w:$85,600")
    db.ttablesXdynamic3.insert(f0="p4w:Angelica Ramos", f1="p4w:Chief Executive Officer (CEO)", f2="p4w:London", f3="p4w:47", f4="p4w:2009/10/09", f5="p4w:$1,200,000")
    db.ttablesXdynamic3.insert(f0="p4w:Gavin Joyce", f1="p4w:Developer", f2="p4w:Edinburgh", f3="p4w:42", f4="p4w:2010/12/22", f5="p4w:$92,575")
    db.ttablesXdynamic3.insert(f0="p4w:Jennifer Chang", f1="p4w:Regional Director", f2="p4w:Singapore", f3="p4w:28", f4="p4w:2010/11/14", f5="p4w:$357,650")
    db.ttablesXdynamic3.insert(f0="p4w:Brenden Wagner", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:28", f4="p4w:2011/06/07", f5="p4w:$206,850")
    db.ttablesXdynamic3.insert(f0="p4w:Fiona Green", f1="p4w:Chief Operating Officer (COO)", f2="p4w:San Francisco", f3="p4w:48", f4="p4w:2010/03/11", f5="p4w:$850,000")
    db.ttablesXdynamic3.insert(f0="p4w:Shou Itou", f1="p4w:Regional Marketing", f2="p4w:Tokyo", f3="p4w:20", f4="p4w:2011/08/14", f5="p4w:$163,000")
    db.ttablesXdynamic3.insert(f0="p4w:Michelle House", f1="p4w:Integration Specialist", f2="p4w:Sidney", f3="p4w:37", f4="p4w:2011/06/02", f5="p4w:$95,400")
    db.ttablesXdynamic3.insert(f0="p4w:Suki Burks", f1="p4w:Developer", f2="p4w:London", f3="p4w:53", f4="p4w:2009/10/22", f5="p4w:$114,500")
    db.ttablesXdynamic3.insert(f0="p4w:Prescott Bartlett", f1="p4w:Technical Author", f2="p4w:London", f3="p4w:27", f4="p4w:2011/05/07", f5="p4w:$145,000")
    db.ttablesXdynamic3.insert(f0="p4w:Gavin Cortez", f1="p4w:Team Leader", f2="p4w:San Francisco", f3="p4w:22", f4="p4w:2008/10/26", f5="p4w:$235,500")
    db.ttablesXdynamic3.insert(f0="p4w:Martena Mccray", f1="p4w:Post-Sales support", f2="p4w:Edinburgh", f3="p4w:46", f4="p4w:2011/03/09", f5="p4w:$324,050")
    db.ttablesXdynamic3.insert(f0="p4w:Unity Butler", f1="p4w:Marketing Designer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/12/09", f5="p4w:$85,675")
    db.ttablesXdynamic3.insert(f0="p4w:Howard Hatfield", f1="p4w:Office Manager", f2="p4w:San Francisco", f3="p4w:51", f4="p4w:2008/12/16", f5="p4w:$164,500")
    db.ttablesXdynamic3.insert(f0="p4w:Hope Fuentes", f1="p4w:Secretary", f2="p4w:San Francisco", f3="p4w:41", f4="p4w:2010/02/12", f5="p4w:$109,850")
    db.ttablesXdynamic3.insert(f0="p4w:Vivian Harrell", f1="p4w:Financial Controller", f2="p4w:San Francisco", f3="p4w:62", f4="p4w:2009/02/14", f5="p4w:$452,500")
    db.ttablesXdynamic3.insert(f0="p4w:Timothy Mooney", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:37", f4="p4w:2008/12/11", f5="p4w:$136,200")
    db.ttablesXdynamic3.insert(f0="p4w:Jackson Bradshaw", f1="p4w:Director", f2="p4w:New York", f3="p4w:65", f4="p4w:2008/09/26", f5="p4w:$645,750")
    db.ttablesXdynamic3.insert(f0="p4w:Olivia Liang", f1="p4w:Support Engineer", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2011/02/03", f5="p4w:$234,500")
    db.ttablesXdynamic3.insert(f0="p4w:Bruno Nash", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:38", f4="p4w:2011/05/03", f5="p4w:$163,500")
    db.ttablesXdynamic3.insert(f0="p4w:Sakura Yamamoto", f1="p4w:Support Engineer", f2="p4w:Tokyo", f3="p4w:37", f4="p4w:2009/08/19", f5="p4w:$139,575")
    db.ttablesXdynamic3.insert(f0="p4w:Thor Walton", f1="p4w:Developer", f2="p4w:New York", f3="p4w:61", f4="p4w:2013/08/11", f5="p4w:$98,540")
    db.ttablesXdynamic3.insert(f0="p4w:Finn Camacho", f1="p4w:Support Engineer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/07/07", f5="p4w:$87,500")
    db.ttablesXdynamic3.insert(f0="p4w:Serge Baldwin", f1="p4w:Data Coordinator", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2012/04/09", f5="p4w:$138,575")
    db.ttablesXdynamic3.insert(f0="p4w:Zenaida Frank", f1="p4w:Software Engineer", f2="p4w:New York", f3="p4w:63", f4="p4w:2010/01/04", f5="p4w:$125,250")
    db.ttablesXdynamic3.insert(f0="p4w:Zorita Serrano", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:56", f4="p4w:2012/06/01", f5="p4w:$115,000")
    db.ttablesXdynamic3.insert(f0="p4w:Jennifer Acosta", f1="p4w:Junior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:43", f4="p4w:2013/02/01", f5="p4w:$75,650")
    db.ttablesXdynamic3.insert(f0="p4w:Cara Stevens", f1="p4w:Sales Assistant", f2="p4w:New York", f3="p4w:46", f4="p4w:2011/12/06", f5="p4w:$145,600")
    db.ttablesXdynamic3.insert(f0="p4w:Hermione Butler", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:47", f4="p4w:2011/03/21", f5="p4w:$356,250")
    db.ttablesXdynamic3.insert(f0="p4w:Lael Greer", f1="p4w:Systems Administrator", f2="p4w:London", f3="p4w:21", f4="p4w:2009/02/27", f5="p4w:$103,500")
    db.ttablesXdynamic3.insert(f0="p4w:Jonas Alexander", f1="p4w:Developer", f2="p4w:San Francisco", f3="p4w:30", f4="p4w:2010/07/14", f5="p4w:$86,500")
    db.ttablesXdynamic3.insert(f0="p4w:Shad Decker", f1="p4w:Regional Director", f2="p4w:Edinburgh", f3="p4w:51", f4="p4w:2008/11/13", f5="p4w:$183,000")
    db.ttablesXdynamic3.insert(f0="p4w:Michael Bruce", f1="p4w:Javascript Developer", f2="p4w:Singapore", f3="p4w:29", f4="p4w:2011/06/27", f5="p4w:$183,000")
    db.ttablesXdynamic3.insert(f0="p4w:Donna Snider", f1="p4w:Customer Support", f2="p4w:New York", f3="p4w:27", f4="p4w:2011/01/25", f5="p4w:$112,000")
    db.commit()

if not db(db.ttablesXdynamic4).count():
    db.ttablesXdynamic4.insert(f0="p4w:Name", f1="p4w:Position", f2="p4w:Office", f3="p4w:Age", f4="p4w:Start date", f5="p4w:Salary")
    db.ttablesXdynamic4.insert(f0="p4w:Tiger Nixon", f1="p4w:System Architect", f2="p4w:Edinburgh", f3="p4w:61", f4="p4w:2011/04/25", f5="p4w:$320,800")
    db.ttablesXdynamic4.insert(f0="p4w:Garrett Winters", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:63", f4="p4w:2011/07/25", f5="p4w:$170,750")
    db.ttablesXdynamic4.insert(f0="p4w:Ashton Cox", f1="p4w:Junior Technical Author", f2="p4w:San Francisco", f3="p4w:66", f4="p4w:2009/01/12", f5="p4w:$86,000")
    db.ttablesXdynamic4.insert(f0="p4w:Cedric Kelly", f1="p4w:Senior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2012/03/29", f5="p4w:$433,060")
    db.ttablesXdynamic4.insert(f0="p4w:Airi Satou", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:33", f4="p4w:2008/11/28", f5="p4w:$162,700")
    db.ttablesXdynamic4.insert(f0="p4w:Brielle Williamson", f1="p4w:Integration Specialist", f2="p4w:New York", f3="p4w:61", f4="p4w:2012/12/02", f5="p4w:$372,000")
    db.ttablesXdynamic4.insert(f0="p4w:Herrod Chandler", f1="p4w:Sales Assistant", f2="p4w:San Francisco", f3="p4w:59", f4="p4w:2012/08/06", f5="p4w:$137,500")
    db.ttablesXdynamic4.insert(f0="p4w:Rhona Davidson", f1="p4w:Integration Specialist", f2="p4w:Tokyo", f3="p4w:55", f4="p4w:2010/10/14", f5="p4w:$327,900")
    db.ttablesXdynamic4.insert(f0="p4w:Colleen Hurst", f1="p4w:Javascript Developer", f2="p4w:San Francisco", f3="p4w:39", f4="p4w:2009/09/15", f5="p4w:$205,500")
    db.ttablesXdynamic4.insert(f0="p4w:Sonya Frost", f1="p4w:Software Engineer", f2="p4w:Edinburgh", f3="p4w:23", f4="p4w:2008/12/13", f5="p4w:$103,600")
    db.ttablesXdynamic4.insert(f0="p4w:Jena Gaines", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:30", f4="p4w:2008/12/19", f5="p4w:$90,560")
    db.ttablesXdynamic4.insert(f0="p4w:Quinn Flynn", f1="p4w:Support Lead", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2013/03/03", f5="p4w:$342,000")
    db.ttablesXdynamic4.insert(f0="p4w:Charde Marshall", f1="p4w:Regional Director", f2="p4w:San Francisco", f3="p4w:36", f4="p4w:2008/10/16", f5="p4w:$470,600")
    db.ttablesXdynamic4.insert(f0="p4w:Haley Kennedy", f1="p4w:Senior Marketing Designer", f2="p4w:London", f3="p4w:43", f4="p4w:2012/12/18", f5="p4w:$313,500")
    db.ttablesXdynamic4.insert(f0="p4w:Tatyana Fitzpatrick", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:19", f4="p4w:2010/03/17", f5="p4w:$385,750")
    db.ttablesXdynamic4.insert(f0="p4w:Michael Silva", f1="p4w:Marketing Designer", f2="p4w:London", f3="p4w:66", f4="p4w:2012/11/27", f5="p4w:$198,500")
    db.ttablesXdynamic4.insert(f0="p4w:Paul Byrd", f1="p4w:Chief Financial Officer (CFO)", f2="p4w:New York", f3="p4w:64", f4="p4w:2010/06/09", f5="p4w:$725,000")
    db.ttablesXdynamic4.insert(f0="p4w:Gloria Little", f1="p4w:Systems Administrator", f2="p4w:New York", f3="p4w:59", f4="p4w:2009/04/10", f5="p4w:$237,500")
    db.ttablesXdynamic4.insert(f0="p4w:Bradley Greer", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:41", f4="p4w:2012/10/13", f5="p4w:$132,000")
    db.ttablesXdynamic4.insert(f0="p4w:Dai Rios", f1="p4w:Personnel Lead", f2="p4w:Edinburgh", f3="p4w:35", f4="p4w:2012/09/26", f5="p4w:$217,500")
    db.ttablesXdynamic4.insert(f0="p4w:Jenette Caldwell", f1="p4w:Development Lead", f2="p4w:New York", f3="p4w:30", f4="p4w:2011/09/03", f5="p4w:$345,000")
    db.ttablesXdynamic4.insert(f0="p4w:Yuri Berry", f1="p4w:Chief Marketing Officer (CMO)", f2="p4w:New York", f3="p4w:40", f4="p4w:2009/06/25", f5="p4w:$675,000")
    db.ttablesXdynamic4.insert(f0="p4w:Caesar Vance", f1="p4w:Pre-Sales Support", f2="p4w:New York", f3="p4w:21", f4="p4w:2011/12/12", f5="p4w:$106,450")
    db.ttablesXdynamic4.insert(f0="p4w:Doris Wilder", f1="p4w:Sales Assistant", f2="p4w:Sidney", f3="p4w:23", f4="p4w:2010/09/20", f5="p4w:$85,600")
    db.ttablesXdynamic4.insert(f0="p4w:Angelica Ramos", f1="p4w:Chief Executive Officer (CEO)", f2="p4w:London", f3="p4w:47", f4="p4w:2009/10/09", f5="p4w:$1,200,000")
    db.ttablesXdynamic4.insert(f0="p4w:Gavin Joyce", f1="p4w:Developer", f2="p4w:Edinburgh", f3="p4w:42", f4="p4w:2010/12/22", f5="p4w:$92,575")
    db.ttablesXdynamic4.insert(f0="p4w:Jennifer Chang", f1="p4w:Regional Director", f2="p4w:Singapore", f3="p4w:28", f4="p4w:2010/11/14", f5="p4w:$357,650")
    db.ttablesXdynamic4.insert(f0="p4w:Brenden Wagner", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:28", f4="p4w:2011/06/07", f5="p4w:$206,850")
    db.ttablesXdynamic4.insert(f0="p4w:Fiona Green", f1="p4w:Chief Operating Officer (COO)", f2="p4w:San Francisco", f3="p4w:48", f4="p4w:2010/03/11", f5="p4w:$850,000")
    db.ttablesXdynamic4.insert(f0="p4w:Shou Itou", f1="p4w:Regional Marketing", f2="p4w:Tokyo", f3="p4w:20", f4="p4w:2011/08/14", f5="p4w:$163,000")
    db.ttablesXdynamic4.insert(f0="p4w:Michelle House", f1="p4w:Integration Specialist", f2="p4w:Sidney", f3="p4w:37", f4="p4w:2011/06/02", f5="p4w:$95,400")
    db.ttablesXdynamic4.insert(f0="p4w:Suki Burks", f1="p4w:Developer", f2="p4w:London", f3="p4w:53", f4="p4w:2009/10/22", f5="p4w:$114,500")
    db.ttablesXdynamic4.insert(f0="p4w:Prescott Bartlett", f1="p4w:Technical Author", f2="p4w:London", f3="p4w:27", f4="p4w:2011/05/07", f5="p4w:$145,000")
    db.ttablesXdynamic4.insert(f0="p4w:Gavin Cortez", f1="p4w:Team Leader", f2="p4w:San Francisco", f3="p4w:22", f4="p4w:2008/10/26", f5="p4w:$235,500")
    db.ttablesXdynamic4.insert(f0="p4w:Martena Mccray", f1="p4w:Post-Sales support", f2="p4w:Edinburgh", f3="p4w:46", f4="p4w:2011/03/09", f5="p4w:$324,050")
    db.ttablesXdynamic4.insert(f0="p4w:Unity Butler", f1="p4w:Marketing Designer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/12/09", f5="p4w:$85,675")
    db.ttablesXdynamic4.insert(f0="p4w:Howard Hatfield", f1="p4w:Office Manager", f2="p4w:San Francisco", f3="p4w:51", f4="p4w:2008/12/16", f5="p4w:$164,500")
    db.ttablesXdynamic4.insert(f0="p4w:Hope Fuentes", f1="p4w:Secretary", f2="p4w:San Francisco", f3="p4w:41", f4="p4w:2010/02/12", f5="p4w:$109,850")
    db.ttablesXdynamic4.insert(f0="p4w:Vivian Harrell", f1="p4w:Financial Controller", f2="p4w:San Francisco", f3="p4w:62", f4="p4w:2009/02/14", f5="p4w:$452,500")
    db.ttablesXdynamic4.insert(f0="p4w:Timothy Mooney", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:37", f4="p4w:2008/12/11", f5="p4w:$136,200")
    db.ttablesXdynamic4.insert(f0="p4w:Jackson Bradshaw", f1="p4w:Director", f2="p4w:New York", f3="p4w:65", f4="p4w:2008/09/26", f5="p4w:$645,750")
    db.ttablesXdynamic4.insert(f0="p4w:Olivia Liang", f1="p4w:Support Engineer", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2011/02/03", f5="p4w:$234,500")
    db.ttablesXdynamic4.insert(f0="p4w:Bruno Nash", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:38", f4="p4w:2011/05/03", f5="p4w:$163,500")
    db.ttablesXdynamic4.insert(f0="p4w:Sakura Yamamoto", f1="p4w:Support Engineer", f2="p4w:Tokyo", f3="p4w:37", f4="p4w:2009/08/19", f5="p4w:$139,575")
    db.ttablesXdynamic4.insert(f0="p4w:Thor Walton", f1="p4w:Developer", f2="p4w:New York", f3="p4w:61", f4="p4w:2013/08/11", f5="p4w:$98,540")
    db.ttablesXdynamic4.insert(f0="p4w:Finn Camacho", f1="p4w:Support Engineer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/07/07", f5="p4w:$87,500")
    db.ttablesXdynamic4.insert(f0="p4w:Serge Baldwin", f1="p4w:Data Coordinator", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2012/04/09", f5="p4w:$138,575")
    db.ttablesXdynamic4.insert(f0="p4w:Zenaida Frank", f1="p4w:Software Engineer", f2="p4w:New York", f3="p4w:63", f4="p4w:2010/01/04", f5="p4w:$125,250")
    db.ttablesXdynamic4.insert(f0="p4w:Zorita Serrano", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:56", f4="p4w:2012/06/01", f5="p4w:$115,000")
    db.ttablesXdynamic4.insert(f0="p4w:Jennifer Acosta", f1="p4w:Junior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:43", f4="p4w:2013/02/01", f5="p4w:$75,650")
    db.ttablesXdynamic4.insert(f0="p4w:Cara Stevens", f1="p4w:Sales Assistant", f2="p4w:New York", f3="p4w:46", f4="p4w:2011/12/06", f5="p4w:$145,600")
    db.ttablesXdynamic4.insert(f0="p4w:Hermione Butler", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:47", f4="p4w:2011/03/21", f5="p4w:$356,250")
    db.ttablesXdynamic4.insert(f0="p4w:Lael Greer", f1="p4w:Systems Administrator", f2="p4w:London", f3="p4w:21", f4="p4w:2009/02/27", f5="p4w:$103,500")
    db.ttablesXdynamic4.insert(f0="p4w:Jonas Alexander", f1="p4w:Developer", f2="p4w:San Francisco", f3="p4w:30", f4="p4w:2010/07/14", f5="p4w:$86,500")
    db.ttablesXdynamic4.insert(f0="p4w:Shad Decker", f1="p4w:Regional Director", f2="p4w:Edinburgh", f3="p4w:51", f4="p4w:2008/11/13", f5="p4w:$183,000")
    db.ttablesXdynamic4.insert(f0="p4w:Michael Bruce", f1="p4w:Javascript Developer", f2="p4w:Singapore", f3="p4w:29", f4="p4w:2011/06/27", f5="p4w:$183,000")
    db.ttablesXdynamic4.insert(f0="p4w:Donna Snider", f1="p4w:Customer Support", f2="p4w:New York", f3="p4w:27", f4="p4w:2011/01/25", f5="p4w:$112,000")
    db.commit()

if not db(db.ttablesXdynamic5).count():
    db.ttablesXdynamic5.insert(f0="p4w:First name", f1="p4w:Last name", f2="p4w:Position", f3="p4w:Office", f4="p4w:Age", f5="p4w:Start date", f6="p4w:Salary", f7="p4w:Extn.", f8="p4w:E-mail")
    db.ttablesXdynamic5.insert(f0="p4w:Tiger", f1="p4w:Nixon", f2="p4w:System Architect", f3="p4w:Edinburgh", f4="p4w:61", f5="p4w:2011/04/25", f6="p4w:$320,800", f7="p4w:5421", f8="p4w:t.nixon@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Garrett", f1="p4w:Winters", f2="p4w:Accountant", f3="p4w:Tokyo", f4="p4w:63", f5="p4w:2011/07/25", f6="p4w:$170,750", f7="p4w:8422", f8="p4w:g.winters@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Ashton", f1="p4w:Cox", f2="p4w:Junior Technical Author", f3="p4w:San Francisco", f4="p4w:66", f5="p4w:2009/01/12", f6="p4w:$86,000", f7="p4w:1562", f8="p4w:a.cox@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Cedric", f1="p4w:Kelly", f2="p4w:Senior Javascript Developer", f3="p4w:Edinburgh", f4="p4w:22", f5="p4w:2012/03/29", f6="p4w:$433,060", f7="p4w:6224", f8="p4w:c.kelly@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Airi", f1="p4w:Satou", f2="p4w:Accountant", f3="p4w:Tokyo", f4="p4w:33", f5="p4w:2008/11/28", f6="p4w:$162,700", f7="p4w:5407", f8="p4w:a.satou@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Brielle", f1="p4w:Williamson", f2="p4w:Integration Specialist", f3="p4w:New York", f4="p4w:61", f5="p4w:2012/12/02", f6="p4w:$372,000", f7="p4w:4804", f8="p4w:b.williamson@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Herrod", f1="p4w:Chandler", f2="p4w:Sales Assistant", f3="p4w:San Francisco", f4="p4w:59", f5="p4w:2012/08/06", f6="p4w:$137,500", f7="p4w:9608", f8="p4w:h.chandler@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Rhona", f1="p4w:Davidson", f2="p4w:Integration Specialist", f3="p4w:Tokyo", f4="p4w:55", f5="p4w:2010/10/14", f6="p4w:$327,900", f7="p4w:6200", f8="p4w:r.davidson@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Colleen", f1="p4w:Hurst", f2="p4w:Javascript Developer", f3="p4w:San Francisco", f4="p4w:39", f5="p4w:2009/09/15", f6="p4w:$205,500", f7="p4w:2360", f8="p4w:c.hurst@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Sonya", f1="p4w:Frost", f2="p4w:Software Engineer", f3="p4w:Edinburgh", f4="p4w:23", f5="p4w:2008/12/13", f6="p4w:$103,600", f7="p4w:1667", f8="p4w:s.frost@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Jena", f1="p4w:Gaines", f2="p4w:Office Manager", f3="p4w:London", f4="p4w:30", f5="p4w:2008/12/19", f6="p4w:$90,560", f7="p4w:3814", f8="p4w:j.gaines@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Quinn", f1="p4w:Flynn", f2="p4w:Support Lead", f3="p4w:Edinburgh", f4="p4w:22", f5="p4w:2013/03/03", f6="p4w:$342,000", f7="p4w:9497", f8="p4w:q.flynn@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Charde", f1="p4w:Marshall", f2="p4w:Regional Director", f3="p4w:San Francisco", f4="p4w:36", f5="p4w:2008/10/16", f6="p4w:$470,600", f7="p4w:6741", f8="p4w:c.marshall@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Haley", f1="p4w:Kennedy", f2="p4w:Senior Marketing Designer", f3="p4w:London", f4="p4w:43", f5="p4w:2012/12/18", f6="p4w:$313,500", f7="p4w:3597", f8="p4w:h.kennedy@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Tatyana", f1="p4w:Fitzpatrick", f2="p4w:Regional Director", f3="p4w:London", f4="p4w:19", f5="p4w:2010/03/17", f6="p4w:$385,750", f7="p4w:1965", f8="p4w:t.fitzpatrick@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Michael", f1="p4w:Silva", f2="p4w:Marketing Designer", f3="p4w:London", f4="p4w:66", f5="p4w:2012/11/27", f6="p4w:$198,500", f7="p4w:1581", f8="p4w:m.silva@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Paul", f1="p4w:Byrd", f2="p4w:Chief Financial Officer (CFO)", f3="p4w:New York", f4="p4w:64", f5="p4w:2010/06/09", f6="p4w:$725,000", f7="p4w:3059", f8="p4w:p.byrd@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Gloria", f1="p4w:Little", f2="p4w:Systems Administrator", f3="p4w:New York", f4="p4w:59", f5="p4w:2009/04/10", f6="p4w:$237,500", f7="p4w:1721", f8="p4w:g.little@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Bradley", f1="p4w:Greer", f2="p4w:Software Engineer", f3="p4w:London", f4="p4w:41", f5="p4w:2012/10/13", f6="p4w:$132,000", f7="p4w:2558", f8="p4w:b.greer@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Dai", f1="p4w:Rios", f2="p4w:Personnel Lead", f3="p4w:Edinburgh", f4="p4w:35", f5="p4w:2012/09/26", f6="p4w:$217,500", f7="p4w:2290", f8="p4w:d.rios@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Jenette", f1="p4w:Caldwell", f2="p4w:Development Lead", f3="p4w:New York", f4="p4w:30", f5="p4w:2011/09/03", f6="p4w:$345,000", f7="p4w:1937", f8="p4w:j.caldwell@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Yuri", f1="p4w:Berry", f2="p4w:Chief Marketing Officer (CMO)", f3="p4w:New York", f4="p4w:40", f5="p4w:2009/06/25", f6="p4w:$675,000", f7="p4w:6154", f8="p4w:y.berry@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Caesar", f1="p4w:Vance", f2="p4w:Pre-Sales Support", f3="p4w:New York", f4="p4w:21", f5="p4w:2011/12/12", f6="p4w:$106,450", f7="p4w:8330", f8="p4w:c.vance@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Doris", f1="p4w:Wilder", f2="p4w:Sales Assistant", f3="p4w:Sidney", f4="p4w:23", f5="p4w:2010/09/20", f6="p4w:$85,600", f7="p4w:3023", f8="p4w:d.wilder@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Angelica", f1="p4w:Ramos", f2="p4w:Chief Executive Officer (CEO)", f3="p4w:London", f4="p4w:47", f5="p4w:2009/10/09", f6="p4w:$1,200,000", f7="p4w:5797", f8="p4w:a.ramos@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Gavin", f1="p4w:Joyce", f2="p4w:Developer", f3="p4w:Edinburgh", f4="p4w:42", f5="p4w:2010/12/22", f6="p4w:$92,575", f7="p4w:8822", f8="p4w:g.joyce@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Jennifer", f1="p4w:Chang", f2="p4w:Regional Director", f3="p4w:Singapore", f4="p4w:28", f5="p4w:2010/11/14", f6="p4w:$357,650", f7="p4w:9239", f8="p4w:j.chang@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Brenden", f1="p4w:Wagner", f2="p4w:Software Engineer", f3="p4w:San Francisco", f4="p4w:28", f5="p4w:2011/06/07", f6="p4w:$206,850", f7="p4w:1314", f8="p4w:b.wagner@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Fiona", f1="p4w:Green", f2="p4w:Chief Operating Officer (COO)", f3="p4w:San Francisco", f4="p4w:48", f5="p4w:2010/03/11", f6="p4w:$850,000", f7="p4w:2947", f8="p4w:f.green@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Shou", f1="p4w:Itou", f2="p4w:Regional Marketing", f3="p4w:Tokyo", f4="p4w:20", f5="p4w:2011/08/14", f6="p4w:$163,000", f7="p4w:8899", f8="p4w:s.itou@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Michelle", f1="p4w:House", f2="p4w:Integration Specialist", f3="p4w:Sidney", f4="p4w:37", f5="p4w:2011/06/02", f6="p4w:$95,400", f7="p4w:2769", f8="p4w:m.house@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Suki", f1="p4w:Burks", f2="p4w:Developer", f3="p4w:London", f4="p4w:53", f5="p4w:2009/10/22", f6="p4w:$114,500", f7="p4w:6832", f8="p4w:s.burks@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Prescott", f1="p4w:Bartlett", f2="p4w:Technical Author", f3="p4w:London", f4="p4w:27", f5="p4w:2011/05/07", f6="p4w:$145,000", f7="p4w:3606", f8="p4w:p.bartlett@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Gavin", f1="p4w:Cortez", f2="p4w:Team Leader", f3="p4w:San Francisco", f4="p4w:22", f5="p4w:2008/10/26", f6="p4w:$235,500", f7="p4w:2860", f8="p4w:g.cortez@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Martena", f1="p4w:Mccray", f2="p4w:Post-Sales support", f3="p4w:Edinburgh", f4="p4w:46", f5="p4w:2011/03/09", f6="p4w:$324,050", f7="p4w:8240", f8="p4w:m.mccray@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Unity", f1="p4w:Butler", f2="p4w:Marketing Designer", f3="p4w:San Francisco", f4="p4w:47", f5="p4w:2009/12/09", f6="p4w:$85,675", f7="p4w:5384", f8="p4w:u.butler@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Howard", f1="p4w:Hatfield", f2="p4w:Office Manager", f3="p4w:San Francisco", f4="p4w:51", f5="p4w:2008/12/16", f6="p4w:$164,500", f7="p4w:7031", f8="p4w:h.hatfield@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Hope", f1="p4w:Fuentes", f2="p4w:Secretary", f3="p4w:San Francisco", f4="p4w:41", f5="p4w:2010/02/12", f6="p4w:$109,850", f7="p4w:6318", f8="p4w:h.fuentes@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Vivian", f1="p4w:Harrell", f2="p4w:Financial Controller", f3="p4w:San Francisco", f4="p4w:62", f5="p4w:2009/02/14", f6="p4w:$452,500", f7="p4w:9422", f8="p4w:v.harrell@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Timothy", f1="p4w:Mooney", f2="p4w:Office Manager", f3="p4w:London", f4="p4w:37", f5="p4w:2008/12/11", f6="p4w:$136,200", f7="p4w:7580", f8="p4w:t.mooney@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Jackson", f1="p4w:Bradshaw", f2="p4w:Director", f3="p4w:New York", f4="p4w:65", f5="p4w:2008/09/26", f6="p4w:$645,750", f7="p4w:1042", f8="p4w:j.bradshaw@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Olivia", f1="p4w:Liang", f2="p4w:Support Engineer", f3="p4w:Singapore", f4="p4w:64", f5="p4w:2011/02/03", f6="p4w:$234,500", f7="p4w:2120", f8="p4w:o.liang@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Bruno", f1="p4w:Nash", f2="p4w:Software Engineer", f3="p4w:London", f4="p4w:38", f5="p4w:2011/05/03", f6="p4w:$163,500", f7="p4w:6222", f8="p4w:b.nash@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Sakura", f1="p4w:Yamamoto", f2="p4w:Support Engineer", f3="p4w:Tokyo", f4="p4w:37", f5="p4w:2009/08/19", f6="p4w:$139,575", f7="p4w:9383", f8="p4w:s.yamamoto@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Thor", f1="p4w:Walton", f2="p4w:Developer", f3="p4w:New York", f4="p4w:61", f5="p4w:2013/08/11", f6="p4w:$98,540", f7="p4w:8327", f8="p4w:t.walton@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Finn", f1="p4w:Camacho", f2="p4w:Support Engineer", f3="p4w:San Francisco", f4="p4w:47", f5="p4w:2009/07/07", f6="p4w:$87,500", f7="p4w:2927", f8="p4w:f.camacho@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Serge", f1="p4w:Baldwin", f2="p4w:Data Coordinator", f3="p4w:Singapore", f4="p4w:64", f5="p4w:2012/04/09", f6="p4w:$138,575", f7="p4w:8352", f8="p4w:s.baldwin@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Zenaida", f1="p4w:Frank", f2="p4w:Software Engineer", f3="p4w:New York", f4="p4w:63", f5="p4w:2010/01/04", f6="p4w:$125,250", f7="p4w:7439", f8="p4w:z.frank@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Zorita", f1="p4w:Serrano", f2="p4w:Software Engineer", f3="p4w:San Francisco", f4="p4w:56", f5="p4w:2012/06/01", f6="p4w:$115,000", f7="p4w:4389", f8="p4w:z.serrano@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Jennifer", f1="p4w:Acosta", f2="p4w:Junior Javascript Developer", f3="p4w:Edinburgh", f4="p4w:43", f5="p4w:2013/02/01", f6="p4w:$75,650", f7="p4w:3431", f8="p4w:j.acosta@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Cara", f1="p4w:Stevens", f2="p4w:Sales Assistant", f3="p4w:New York", f4="p4w:46", f5="p4w:2011/12/06", f6="p4w:$145,600", f7="p4w:3990", f8="p4w:c.stevens@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Hermione", f1="p4w:Butler", f2="p4w:Regional Director", f3="p4w:London", f4="p4w:47", f5="p4w:2011/03/21", f6="p4w:$356,250", f7="p4w:1016", f8="p4w:h.butler@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Lael", f1="p4w:Greer", f2="p4w:Systems Administrator", f3="p4w:London", f4="p4w:21", f5="p4w:2009/02/27", f6="p4w:$103,500", f7="p4w:6733", f8="p4w:l.greer@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Jonas", f1="p4w:Alexander", f2="p4w:Developer", f3="p4w:San Francisco", f4="p4w:30", f5="p4w:2010/07/14", f6="p4w:$86,500", f7="p4w:8196", f8="p4w:j.alexander@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Shad", f1="p4w:Decker", f2="p4w:Regional Director", f3="p4w:Edinburgh", f4="p4w:51", f5="p4w:2008/11/13", f6="p4w:$183,000", f7="p4w:6373", f8="p4w:s.decker@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Michael", f1="p4w:Bruce", f2="p4w:Javascript Developer", f3="p4w:Singapore", f4="p4w:29", f5="p4w:2011/06/27", f6="p4w:$183,000", f7="p4w:5384", f8="p4w:m.bruce@datatables.net")
    db.ttablesXdynamic5.insert(f0="p4w:Donna", f1="p4w:Snider", f2="p4w:Customer Support", f3="p4w:New York", f4="p4w:27", f5="p4w:2011/01/25", f6="p4w:$112,000", f7="p4w:4226", f8="p4w:d.snider@datatables.net")
    db.commit()

if not db(db.totherXcharts0).count():
    db.totherXcharts0.insert(f0="p4w:len0", f1="p4w:len0")
    db.totherXcharts0.insert(f0="p4w:len0", f1="p4w:Line Graph")
    db.totherXcharts0.insert(f0="p4w:len0", f1="p4w:Line Area Graph")
    db.totherXcharts0.insert(f0="p4w:len0", f1="p4w:Bar Graph")
    db.totherXcharts0.insert(f0="p4w:len0", f1="p4w:Pie Chart")
    db.totherXcharts0.insert(f0="p4w:len0", f1="p4w:Discrete chart")
    db.commit()

if not db(db.tprojects0).count():
    db.tprojects0.insert(f0="p4w:#", f1="p4w:Project Name", f2="p4w:Team Members", f3="p4w:Project Progress", f4="p4w:Status", f5="p4w:#Edit")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:Pesamakini Backend UICreated 01.01.2015", f2="p4w:len0", f3="p4w:57% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:Pesamakini Backend UICreated 01.01.2015", f2="p4w:len0", f3="p4w:47% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:Pesamakini Backend UICreated 01.01.2015", f2="p4w:len0", f3="p4w:77% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:Pesamakini Backend UICreated 01.01.2015", f2="p4w:len0", f3="p4w:60% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:Pesamakini Backend UICreated 01.01.2015", f2="p4w:len0", f3="p4w:12% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:Pesamakini Backend UICreated 01.01.2015", f2="p4w:len0", f3="p4w:35% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:Pesamakini Backend UICreated 01.01.2015", f2="p4w:len0", f3="p4w:87% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:Pesamakini Backend UICreated 01.01.2015", f2="p4w:len0", f3="p4w:77% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:Pesamakini Backend UICreated 01.01.2015", f2="p4w:len0", f3="p4w:77% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.commit()

if not db(db.tprofile0).count():
    db.tprofile0.insert(f0="p4w:#", f1="p4w:Project Name", f2="p4w:Client Company", f3="p4w:Hours Spent", f4="p4w:Contribution")
    db.tprofile0.insert(f0="p4w:1", f1="p4w:New Company Takeover Review", f2="p4w:Deveint Inc", f3="p4w:18", f4="p4w:len0")
    db.tprofile0.insert(f0="p4w:2", f1="p4w:New Partner Contracts Consultanci", f2="p4w:Deveint Inc", f3="p4w:13", f4="p4w:len0")
    db.tprofile0.insert(f0="p4w:3", f1="p4w:Partners and Inverstors report", f2="p4w:Deveint Inc", f3="p4w:30", f4="p4w:len0")
    db.tprofile0.insert(f0="p4w:4", f1="p4w:New Company Takeover Review", f2="p4w:Deveint Inc", f3="p4w:28", f4="p4w:len0")
    db.commit()
