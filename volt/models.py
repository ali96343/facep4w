from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 21.10.2020 16:01:29
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
    'dfindex0',
    Field('f0','string'),
    )

db.define_table(
    'dfdashboard0',
    Field('f0','string'),
    )

db.define_table(
    'dfsignXin0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','boolean'),
    )

db.define_table(
    'dfsignXup0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','boolean'),
    )

db.define_table(
    'dflock0',
    Field('f0','string'),
    )

db.define_table(
    'dftransactions0',
    Field('f0','string'),
    )

db.define_table(
    'dfsettings0',
    Field('f0','string'),
    )

db.define_table(
    'dfsettings1',
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
    )

db.define_table(
    'dfforgotXpassword0',
    Field('f0','string'),
    )

db.define_table(
    'dfresetXpassword0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'dfbootstrapXtables0',
    Field('f0','string'),
    )

db.define_table(
    'dfbuttons0',
    Field('f0','string'),
    )

db.define_table(
    'dfnotifications0',
    Field('f0','string'),
    )

db.define_table(
    'dfforms0',
    Field('f0','string'),
    )

db.define_table(
    'dfmodals0',
    Field('f0','string'),
    )

db.define_table(
    'dfmodals1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','boolean'),
    )

db.define_table(
    'dfmodals2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','boolean'),
    )

db.define_table(
    'dftypography0',
    Field('f0','string'),
    )

db.define_table(
    'tdashboard0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'ttransactions0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    )

db.define_table(
    'tbootstrapXtables0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    )

db.define_table(
    'tbootstrapXtables1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    )

if not db(db.tdashboard0).count():
    db.tdashboard0.insert(f0="p4w:Page name", f1="p4w:Page Views", f2="p4w:Page Value", f3="p4w:Bounce rate")
    db.tdashboard0.insert(f0="p4w:/demo/admin/index.html", f1="p4w:3,225", f2="p4w:$20", f3="p4w:42,55%")
    db.tdashboard0.insert(f0="p4w:/demo/admin/forms.html", f1="p4w:2,987", f2="p4w:0", f3="p4w:43,52%")
    db.tdashboard0.insert(f0="p4w:/demo/admin/util.html", f1="p4w:2,844", f2="p4w:294", f3="p4w:32,35%")
    db.tdashboard0.insert(f0="p4w:/demo/admin/validation.html", f1="p4w:2,050", f2="p4w:$147", f3="p4w:50,87%")
    db.tdashboard0.insert(f0="p4w:/demo/admin/modals.html", f1="p4w:1,483", f2="p4w:$19", f3="p4w:32,24%")
    db.commit()

if not db(db.ttransactions0).count():
    db.ttransactions0.insert(f0="p4w:#", f1="p4w:Bill For", f2="p4w:Issue Date", f3="p4w:Due Date", f4="p4w:Total", f5="p4w:Status", f6="p4w:Action")
    db.ttransactions0.insert(f0="p4w:456478", f1="p4w:Platinum Subscription Plan", f2="p4w:1 May 2020", f3="p4w:1 Jun 2020", f4="p4w:$799,00", f5="p4w:Due", f6="p4w:Toggle Dropdown View Details Edit Remove")
    db.ttransactions0.insert(f0="p4w:456423", f1="p4w:Platinum Subscription Plan", f2="p4w:1 Apr 2020", f3="p4w:1 May 2020", f4="p4w:$799,00", f5="p4w:Paid", f6="p4w:Toggle Dropdown View Details Edit Remove")
    db.ttransactions0.insert(f0="p4w:456420", f1="p4w:Platinum Subscription Plan", f2="p4w:1 Mar 2020", f3="p4w:1 Apr 2020", f4="p4w:$799,00", f5="p4w:Paid", f6="p4w:Toggle Dropdown View Details Edit Remove")
    db.ttransactions0.insert(f0="p4w:456421", f1="p4w:Platinum Subscription Plan", f2="p4w:1 Feb 2020", f3="p4w:1 Mar 2020", f4="p4w:$799,00", f5="p4w:Paid", f6="p4w:Toggle Dropdown View Details Edit Remove")
    db.ttransactions0.insert(f0="p4w:456420", f1="p4w:Platinum Subscription Plan", f2="p4w:1 Jan 2020", f3="p4w:1 Feb 2020", f4="p4w:$799,00", f5="p4w:Paid", f6="p4w:Toggle Dropdown View Details Edit Remove")
    db.ttransactions0.insert(f0="p4w:456479", f1="p4w:Platinum Subscription Plan", f2="p4w:1 Dec 2019", f3="p4w:1 Jan 2020", f4="p4w:$799,00", f5="p4w:Paid", f6="p4w:Toggle Dropdown View Details Edit Remove")
    db.ttransactions0.insert(f0="p4w:456478", f1="p4w:Platinum Subscription Plan", f2="p4w:1 Nov 2019", f3="p4w:1 Dec 2019", f4="p4w:$799,00", f5="p4w:Paid", f6="p4w:Toggle Dropdown View Details Edit Remove")
    db.ttransactions0.insert(f0="p4w:453673", f1="p4w:Gold Subscription Plan", f2="p4w:1 Oct 2019", f3="p4w:1 Nov 2019", f4="p4w:$533,42", f5="p4w:Canceled", f6="p4w:Toggle Dropdown View Details Edit Remove")
    db.ttransactions0.insert(f0="p4w:456468", f1="p4w:Gold Subscription Plan", f2="p4w:1 Sep 2019", f3="p4w:1 Oct 2019", f4="p4w:$533,42", f5="p4w:Paid", f6="p4w:Toggle Dropdown View Details Edit Remove")
    db.ttransactions0.insert(f0="p4w:456478", f1="p4w:Flexible Subscription Plan", f2="p4w:1 Aug 2019", f3="p4w:1 Sep 2019", f4="p4w:$233,42", f5="p4w:Paid", f6="p4w:Toggle Dropdown View Details Edit Remove")
    db.commit()

if not db(db.tbootstrapXtables0).count():
    db.tbootstrapXtables0.insert(f0="p4w:#", f1="p4w:Traffic Source", f2="p4w:Source Type", f3="p4w:Category", f4="p4w:Global Rank", f5="p4w:Traffic Share", f6="p4w:Change")
    db.tbootstrapXtables0.insert(f0="p4w:1", f1="p4w:Direct", f2="p4w:Direct", f3="p4w:-", f4="p4w:--", f5="p4w:51%", f6="p4w:2.45%")
    db.tbootstrapXtables0.insert(f0="p4w:2", f1="p4w:Google Search", f2="p4w:Search / Organic", f3="p4w:-", f4="p4w:--", f5="p4w:18%", f6="p4w:17.67%")
    db.tbootstrapXtables0.insert(f0="p4w:3", f1="p4w:youtube.com", f2="p4w:Social", f3="p4w:Arts and Entertainment", f4="p4w:#2", f5="p4w:18%", f6="p4w:-")
    db.tbootstrapXtables0.insert(f0="p4w:4", f1="p4w:yahoo.com", f2="p4w:Referral", f3="p4w:News and Media", f4="p4w:#11", f5="p4w:8%", f6="p4w:9.30%")
    db.tbootstrapXtables0.insert(f0="p4w:5", f1="p4w:twitter.com", f2="p4w:Social", f3="p4w:Social Networks", f4="p4w:#4", f5="p4w:4%", f6="p4w:-")
    db.commit()

if not db(db.tbootstrapXtables1).count():
    db.tbootstrapXtables1.insert(f0="p4w:Country", f1="p4w:All", f2="p4w:All Change", f3="p4w:Travel & Local", f4="p4w:Travel & Local Change", f5="p4w:Widgets", f6="p4w:Widgets Change")
    db.tbootstrapXtables1.insert(f0="p4w:United States", f1="p4w:106", f2="p4w:5", f3="p4w:3", f4="p4w:=", f5="p4w:32", f6="p4w:3")
    db.tbootstrapXtables1.insert(f0="p4w:Canada", f1="p4w:76", f2="p4w:17", f3="p4w:4", f4="p4w:=", f5="p4w:30", f6="p4w:3")
    db.tbootstrapXtables1.insert(f0="p4w:United Kingdom", f1="p4w:147", f2="p4w:10", f3="p4w:5", f4="p4w:=", f5="p4w:34", f6="p4w:7")
    db.tbootstrapXtables1.insert(f0="p4w:France", f1="p4w:112", f2="p4w:3", f3="p4w:5", f4="p4w:1", f5="p4w:34", f6="p4w:2")
    db.tbootstrapXtables1.insert(f0="p4w:Japan", f1="p4w:115", f2="p4w:12", f3="p4w:6", f4="p4w:1", f5="p4w:37", f6="p4w:5")
    db.tbootstrapXtables1.insert(f0="p4w:Germany", f1="p4w:220", f2="p4w:56", f3="p4w:7", f4="p4w:3", f5="p4w:30", f6="p4w:2")
    db.commit()
