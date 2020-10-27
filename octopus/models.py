from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 27.10.2020 14:00:18
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
    db.commit()


db.define_table(
    'dfindex0',
    Field('f0','string'),
    )

db.define_table(
    'dfindex1',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXsearchXresults0',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXsearchXresults1',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXuserXprofile0',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXuserXprofile1',
    Field('f0','text'),
    )

db.define_table(
    'dfpagesXuserXprofile2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','text'),
    )

db.define_table(
    'dfpagesXsignin0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','boolean'),
    )

db.define_table(
    'dfmailboxXfolder0',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXsignup0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','boolean'),
    )

db.define_table(
    'dfpagesXrecoverXpassword0',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXlockXscreen0',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXsessionXtimeout0',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXcalendar0',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXtimeline0',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXmediaXgallery0',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXinvoice0',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXblank0',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesX4040',
    Field('f0','string'),
    )

db.define_table(
    'dfpagesXlogXviewer0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXtypography0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXicons0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXtabs0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXpanels0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXwidgets0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXportlets0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXbuttons0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXalerts0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXnotifications0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXmodals0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXmodals1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','text'),
    )

db.define_table(
    'dfuiXelementsXlightbox0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXlightbox1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','text'),
    )

db.define_table(
    'dfuiXelementsXprogressbars0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXsliders0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXcarousels0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXaccordions0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXnestable0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXtreeXview0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXgridXsystem0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXcharts0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXanimations0',
    Field('f0','string'),
    )

db.define_table(
    'dfuiXelementsXextra0',
    Field('f0','string'),
    )

db.define_table(
    'dfformsXbasic0',
    Field('f0','string'),
    )

db.define_table(
    'dfformsXbasic1',
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
    Field('f10','string'),
    Field('f11','string'),
    Field('f12','string'),
    Field('f13','string'),
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
    )

db.define_table(
    'dfformsXbasic2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'dfformsXbasic3',
    Field('f0','boolean'),
    Field('f1','boolean'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','boolean'),
    Field('f5','boolean'),
    Field('f6','boolean'),
    Field('f7','string'),
    Field('f8','string'),
    )

db.define_table(
    'dfformsXbasic4',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    Field('f7','string'),
    Field('f8','boolean'),
    Field('f9','string'),
    Field('f10','string'),
    Field('f11','string'),
    Field('f12','string'),
    Field('f13','string'),
    Field('f14','string'),
    Field('f15','string'),
    )

db.define_table(
    'dfformsXbasic5',
    Field('f0','boolean'),
    Field('f1','boolean'),
    Field('f2','boolean'),
    Field('f3','boolean'),
    Field('f4','boolean'),
    Field('f5','boolean'),
    Field('f6','boolean'),
    )

db.define_table(
    'dfformsXbasic6',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    )

db.define_table(
    'dfformsXbasic7',
    Field('f0','text'),
    )

db.define_table(
    'dfformsXadvanced0',
    Field('f0','string'),
    )

db.define_table(
    'dfformsXadvanced1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'dfformsXadvanced2',
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
    'dfformsXadvanced3',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfformsXadvanced4',
    Field('f0','boolean'),
    Field('f1','boolean'),
    Field('f2','boolean'),
    Field('f3','boolean'),
    Field('f4','boolean'),
    Field('f5','boolean'),
    Field('f6','boolean'),
    Field('f7','boolean'),
    Field('f8','boolean'),
    Field('f9','boolean'),
    Field('f10','boolean'),
    Field('f11','boolean'),
    Field('f12','boolean'),
    Field('f13','boolean'),
    Field('f14','boolean'),
    Field('f15','boolean'),
    Field('f16','boolean'),
    Field('f17','boolean'),
    )

db.define_table(
    'dfformsXadvanced5',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfformsXadvanced6',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'dfformsXadvanced7',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'dfformsXadvanced8',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'dfformsXadvanced9',
    Field('f0','string'),
    Field('f1','text'),
    )

db.define_table(
    'dfformsXadvanced10',
    )

db.define_table(
    'dfformsXadvanced11',
    )

db.define_table(
    'dfformsXadvanced12',
    Field('f0','text'),
    )

db.define_table(
    'dfformsXvalidation0',
    Field('f0','string'),
    )

db.define_table(
    'dfformsXvalidation1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','text'),
    )

db.define_table(
    'dfformsXvalidation2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','boolean'),
    Field('f4','boolean'),
    Field('f5','boolean'),
    )

db.define_table(
    'dfformsXvalidation3',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','text'),
    )

db.define_table(
    'dfformsXvalidation4',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfformsXlayouts0',
    Field('f0','string'),
    )

db.define_table(
    'dfformsXlayouts1',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfformsXlayouts2',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfformsXlayouts3',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','text'),
    )

db.define_table(
    'dfformsXlayouts4',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','boolean'),
    )

db.define_table(
    'dfformsXwizard0',
    Field('f0','string'),
    )

db.define_table(
    'dfformsXwizard1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','boolean'),
    )

db.define_table(
    'dfformsXwizard2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','boolean'),
    )

db.define_table(
    'dfformsXwizard3',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    Field('f7','string'),
    Field('f8','boolean'),
    )

db.define_table(
    'dfformsXwizard4',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    Field('f7','string'),
    Field('f8','boolean'),
    )

db.define_table(
    'dfformsXwizard5',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    Field('f6','string'),
    Field('f7','string'),
    Field('f8','boolean'),
    )

db.define_table(
    'dfformsXcodeXeditor0',
    Field('f0','string'),
    )

db.define_table(
    'dfformsXcodeXeditor1',
    Field('f0','text'),
    )

db.define_table(
    'dftablesXbasic0',
    Field('f0','string'),
    )

db.define_table(
    'dftablesXadvanced0',
    Field('f0','string'),
    )

db.define_table(
    'dftablesXresponsive0',
    Field('f0','string'),
    )

db.define_table(
    'dftablesXeditable0',
    Field('f0','string'),
    )

db.define_table(
    'dftablesXajax0',
    Field('f0','string'),
    )

db.define_table(
    'dftablesXpricing0',
    Field('f0','string'),
    )

db.define_table(
    'dfmapsXgoogleXmaps0',
    Field('f0','string'),
    )

db.define_table(
    'dfmapsXgoogleXmapsXbuilder0',
    Field('f0','string'),
    )

db.define_table(
    'dfmapsXgoogleXmapsXbuilder1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','text'),
    )

db.define_table(
    'dfmapsXvector0',
    Field('f0','string'),
    )

db.define_table(
    'dflayoutsXdefault0',
    Field('f0','string'),
    )

db.define_table(
    'dflayoutsXboxed0',
    Field('f0','string'),
    )

db.define_table(
    'dflayoutsXmenuXcollapsed0',
    Field('f0','string'),
    )

db.define_table(
    'dflayoutsXscroll0',
    Field('f0','string'),
    )

db.define_table(
    'dfmailboxXemail0',
    Field('f0','string'),
    )

db.define_table(
    'dfmailboxXcompose0',
    Field('f0','string'),
    )

db.define_table(
    'dfmailboxXcompose1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tindex0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tpagesXinvoice0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'tpagesXinvoice1',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'tpagesXlogXviewer0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tpagesXlogXviewer1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tpagesXlogXviewer2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'ttablesXbasic0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'ttablesXbasic1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'ttablesXbasic2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'ttablesXbasic3',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'ttablesXbasic4',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'ttablesXbasic5',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'ttablesXbasic6',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'ttablesXbasic7',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'ttablesXbasic8',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'ttablesXbasic9',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'ttablesXadvanced0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'ttablesXadvanced1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'ttablesXadvanced2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'ttablesXresponsive0',
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
    'ttablesXresponsive1',
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
    'ttablesXresponsive2',
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
    'ttablesXeditable0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'ttablesXajax0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tpagesXinvoiceXprint0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'tpagesXinvoiceXprint1',
    Field('f0','string'),
    Field('f1','string'),
    )

if not db(db.tindex0).count():
    db.tindex0.insert(f0="p4w:#", f1="p4w:Project", f2="p4w:Status", f3="p4w:Progress")
    db.tindex0.insert(f0="p4w:1", f1="p4w:JSOFT - Responsive HTML5 Template", f2="p4w:Success", f3="p4w:100%")
    db.tindex0.insert(f0="p4w:2", f1="p4w:JSOFT - Responsive Drupal 7 Theme", f2="p4w:Success", f3="p4w:100%")
    db.tindex0.insert(f0="p4w:3", f1="p4w:Tucson - Responsive HTML5 Template", f2="p4w:Warning", f3="p4w:60%")
    db.tindex0.insert(f0="p4w:4", f1="p4w:Tucson - Responsive Business WordPress Theme", f2="p4w:Success", f3="p4w:90%")
    db.tindex0.insert(f0="p4w:5", f1="p4w:JSOFT - Responsive Admin HTML5 Template", f2="p4w:Warning", f3="p4w:45%")
    db.tindex0.insert(f0="p4w:6", f1="p4w:JSOFT - Responsive HTML5 Template", f2="p4w:Danger", f3="p4w:40%")
    db.tindex0.insert(f0="p4w:7", f1="p4w:JSOFT - Responsive Drupal 7 Theme", f2="p4w:Success", f3="p4w:95%")
    db.commit()

if not db(db.tpagesXinvoice0).count():
    db.tpagesXinvoice0.insert(f0="p4w:#", f1="p4w:Item", f2="p4w:Description", f3="p4w:Price", f4="p4w:Quantity", f5="p4w:Total")
    db.tpagesXinvoice0.insert(f0="p4w:123456", f1="p4w:Porto HTML5 Template", f2="p4w:Multipourpouse Website Template", f3="p4w:$14.00", f4="p4w:2", f5="p4w:$28.00")
    db.tpagesXinvoice0.insert(f0="p4w:654321", f1="p4w:Tucson HTML5 Template", f2="p4w:Awesome Website Template", f3="p4w:$17.00", f4="p4w:1", f5="p4w:$17.00")
    db.commit()

if not db(db.tpagesXinvoice1).count():
    db.tpagesXinvoice1.insert(f0="p4w:Subtotal", f1="p4w:$73.00")
    db.tpagesXinvoice1.insert(f0="p4w:Shipping", f1="p4w:$0.00")
    db.tpagesXinvoice1.insert(f0="p4w:Grand Total", f1="p4w:$73.00")
    db.commit()

if not db(db.tpagesXlogXviewer0).count():
    db.tpagesXlogXviewer0.insert(f0="p4w:Type", f1="p4w:Date", f2="p4w:Message")
    db.tpagesXlogXviewer0.insert(f0="p4w:Debug", f1="p4w:13/04/2014 18:25:59", f2="p4w:my.host - oh snap! another exception")
    db.tpagesXlogXviewer0.insert(f0="p4w:Info", f1="p4w:13/04/2014 21:50:17", f2="p4w:GET / HTTP/1.1 200 1225")
    db.tpagesXlogXviewer0.insert(f0="p4w:Warning", f1="p4w:13/04/2014 17:44:21", f2="p4w:DocumentRoot [/var/www/porto-admin/] does not exist")
    db.tpagesXlogXviewer0.insert(f0="p4w:Error", f1="p4w:13/04/2014 21:55:18", f2="p4w:File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer0.insert(f0="p4w:Fatal", f1="p4w:13/04/2014 22:13:39", f2="p4w:not a tree object")
    db.commit()

if not db(db.tpagesXlogXviewer1).count():
    db.tpagesXlogXviewer1.insert(f0="p4w:Type", f1="p4w:Date", f2="p4w:Message")
    db.tpagesXlogXviewer1.insert(f0="p4w:Error", f1="p4w:13/04/2014 21:55:30", f2="p4w:File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="p4w:Error", f1="p4w:13/04/2014 21:55:29", f2="p4w:File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="p4w:Error", f1="p4w:13/04/2014 21:55:28", f2="p4w:File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="p4w:Error", f1="p4w:13/04/2014 21:55:27", f2="p4w:File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="p4w:Error", f1="p4w:13/04/2014 21:55:26", f2="p4w:File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="p4w:Error", f1="p4w:13/04/2014 21:55:25", f2="p4w:File does not exist: /var/www/porto-admin/favicon.ico")
    db.tpagesXlogXviewer1.insert(f0="p4w:Fatal", f1="p4w:12/04/2014 22:13:39", f2="p4w:not a tree object")
    db.commit()

if not db(db.tpagesXlogXviewer2).count():
    db.tpagesXlogXviewer2.insert(f0="p4w:Type", f1="p4w:Date", f2="p4w:Message")
    db.tpagesXlogXviewer2.insert(f0="p4w:Info", f1="p4w:12/04/2014 21:50:54", f2="p4w:GET / HTTP/1.1 200 1225")
    db.tpagesXlogXviewer2.insert(f0="p4w:Info", f1="p4w:12/04/2014 21:50:53", f2="p4w:GET /assets/vendor/bootstrap/css/bootstrap.css HTTP/1.1 200 110495")
    db.tpagesXlogXviewer2.insert(f0="p4w:Info", f1="p4w:12/04/2014 21:50:52", f2="p4w:GET /assets/stylesheets/theme.css HTTP/1.1 200 1273")
    db.tpagesXlogXviewer2.insert(f0="p4w:Info", f1="p4w:12/04/2014 21:50:51", f2="p4w:GET /assets/stylesheets/skin.css HTTP/1.1 200 230")
    db.tpagesXlogXviewer2.insert(f0="p4w:Info", f1="p4w:12/04/2014 21:50:50", f2="p4w:GET /assets/vendor/jquery/jquery.js HTTP/1.1 200 244962")
    db.commit()

if not db(db.ttablesXbasic0).count():
    db.ttablesXbasic0.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.ttablesXbasic0.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttablesXbasic0.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttablesXbasic0.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.commit()

if not db(db.ttablesXbasic1).count():
    db.ttablesXbasic1.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.ttablesXbasic1.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttablesXbasic1.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttablesXbasic1.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.commit()

if not db(db.ttablesXbasic2).count():
    db.ttablesXbasic2.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.ttablesXbasic2.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttablesXbasic2.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttablesXbasic2.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.commit()

if not db(db.ttablesXbasic3).count():
    db.ttablesXbasic3.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.ttablesXbasic3.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttablesXbasic3.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttablesXbasic3.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.commit()

if not db(db.ttablesXbasic4).count():
    db.ttablesXbasic4.insert(f0="p4w:#", f1="p4w:Class", f2="p4w:Text")
    db.ttablesXbasic4.insert(f0="p4w:1", f1="p4w:active", f2="p4w:Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="p4w:2", f1="p4w:primary", f2="p4w:Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="p4w:3", f1="p4w:success", f2="p4w:Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="p4w:4", f1="p4w:warning", f2="p4w:Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="p4w:5", f1="p4w:danger", f2="p4w:Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="p4w:6", f1="p4w:info", f2="p4w:Lorem ipsum dolor sit amet")
    db.ttablesXbasic4.insert(f0="p4w:7", f1="p4w:dark", f2="p4w:Lorem ipsum dolor sit amet")
    db.commit()

if not db(db.ttablesXbasic5).count():
    db.ttablesXbasic5.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username")
    db.ttablesXbasic5.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttablesXbasic5.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttablesXbasic5.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.ttablesXbasic5.insert(f0="p4w:4", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttablesXbasic5.insert(f0="p4w:5", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.ttablesXbasic5.insert(f0="p4w:6", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter")
    db.ttablesXbasic5.insert(f0="p4w:7", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo")
    db.ttablesXbasic5.insert(f0="p4w:8", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat")
    db.commit()

if not db(db.ttablesXbasic6).count():
    db.ttablesXbasic6.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username", f4="p4w:Actions")
    db.ttablesXbasic6.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo", f4="p4w:len0")
    db.ttablesXbasic6.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat", f4="p4w:len0")
    db.ttablesXbasic6.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter", f4="p4w:len0")
    db.commit()

if not db(db.ttablesXbasic7).count():
    db.ttablesXbasic7.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username", f4="p4w:Actions")
    db.ttablesXbasic7.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo", f4="p4w:len0")
    db.ttablesXbasic7.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat", f4="p4w:len0")
    db.ttablesXbasic7.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter", f4="p4w:len0")
    db.commit()

if not db(db.ttablesXbasic8).count():
    db.ttablesXbasic8.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username", f4="p4w:Actions")
    db.ttablesXbasic8.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo", f4="p4w:len0")
    db.ttablesXbasic8.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat", f4="p4w:len0")
    db.ttablesXbasic8.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter", f4="p4w:len0")
    db.commit()

if not db(db.ttablesXbasic9).count():
    db.ttablesXbasic9.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username", f4="p4w:Actions")
    db.ttablesXbasic9.insert(f0="p4w:1", f1="p4w:Mark", f2="p4w:Otto", f3="p4w:@mdo", f4="p4w:len0")
    db.ttablesXbasic9.insert(f0="p4w:2", f1="p4w:Jacob", f2="p4w:Thornton", f3="p4w:@fat", f4="p4w:len0")
    db.ttablesXbasic9.insert(f0="p4w:3", f1="p4w:Larry", f2="p4w:the Bird", f3="p4w:@twitter", f4="p4w:len0")
    db.commit()

if not db(db.ttablesXadvanced0).count():
    db.ttablesXadvanced0.insert(f0="p4w:Rendering engine", f1="p4w:Browser", f2="p4w:Platform(s)", f3="p4w:Engine version", f4="p4w:CSS grade")
    db.ttablesXadvanced0.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 4.0", f2="p4w:Win 95+", f3="p4w:4", f4="p4w:X")
    db.ttablesXadvanced0.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 5.0", f2="p4w:Win 95+", f3="p4w:5", f4="p4w:C")
    db.ttablesXadvanced0.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 5.5", f2="p4w:Win 95+", f3="p4w:5.5", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 6", f2="p4w:Win 98+", f3="p4w:6", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 7", f2="p4w:Win XP SP2+", f3="p4w:7", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Trident", f1="p4w:AOL browser (AOL desktop)", f2="p4w:Win XP", f3="p4w:6", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.5", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Firefox 2.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Firefox 3.0", f2="p4w:Win 2k+ / OSX.3+", f3="p4w:1.9", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Camino 1.0", f2="p4w:OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Camino 1.5", f2="p4w:OSX.3+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Netscape 7.2", f2="p4w:Win 95+ / Mac OS 8.6-9.2", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Netscape Browser 8", f2="p4w:Win 98SE+", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Netscape Navigator 9", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.1", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.1", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.2", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.2", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.3", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.3", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.4", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.4", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.5", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.5", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.6", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.6", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.7", f2="p4w:Win 98+ / OSX.1+", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.8", f2="p4w:Win 98+ / OSX.1+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Seamonkey 1.1", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Gecko", f1="p4w:Epiphany 2.20", f2="p4w:Gnome", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Webkit", f1="p4w:Safari 1.2", f2="p4w:OSX.3", f3="p4w:125.5", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Webkit", f1="p4w:Safari 1.3", f2="p4w:OSX.3", f3="p4w:312.8", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Webkit", f1="p4w:Safari 2.0", f2="p4w:OSX.4+", f3="p4w:419.3", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Webkit", f1="p4w:Safari 3.0", f2="p4w:OSX.4+", f3="p4w:522.1", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Webkit", f1="p4w:OmniWeb 5.5", f2="p4w:OSX.4+", f3="p4w:420", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Webkit", f1="p4w:iPod Touch / iPhone", f2="p4w:iPod", f3="p4w:420.1", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Webkit", f1="p4w:S60", f2="p4w:S60", f3="p4w:413", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Presto", f1="p4w:Opera 7.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Presto", f1="p4w:Opera 7.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Presto", f1="p4w:Opera 8.0", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Presto", f1="p4w:Opera 8.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Presto", f1="p4w:Opera 9.0", f2="p4w:Win 95+ / OSX.3+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Presto", f1="p4w:Opera 9.2", f2="p4w:Win 88+ / OSX.3+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Presto", f1="p4w:Opera 9.5", f2="p4w:Win 88+ / OSX.3+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Presto", f1="p4w:Opera for Wii", f2="p4w:Wii", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Presto", f1="p4w:Nokia N800", f2="p4w:N800", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Presto", f1="p4w:Nintendo DS browser", f2="p4w:Nintendo DS", f3="p4w:8.5", f4="p4w:C/A1")
    db.ttablesXadvanced0.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.1", f2="p4w:KDE 3.1", f3="p4w:3.1", f4="p4w:C")
    db.ttablesXadvanced0.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.3", f2="p4w:KDE 3.3", f3="p4w:3.3", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.5", f2="p4w:KDE 3.5", f3="p4w:3.5", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 4.5", f2="p4w:Mac OS 8-9", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced0.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.1", f2="p4w:Mac OS 7.6-9", f3="p4w:1", f4="p4w:C")
    db.ttablesXadvanced0.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.2", f2="p4w:Mac OS 8-X", f3="p4w:1", f4="p4w:C")
    db.ttablesXadvanced0.insert(f0="p4w:Misc", f1="p4w:NetFront 3.1", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:C")
    db.ttablesXadvanced0.insert(f0="p4w:Misc", f1="p4w:NetFront 3.4", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced0.insert(f0="p4w:Misc", f1="p4w:Dillo 0.8", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced0.insert(f0="p4w:Misc", f1="p4w:Links", f2="p4w:Text only", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced0.insert(f0="p4w:Misc", f1="p4w:Lynx", f2="p4w:Text only", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced0.insert(f0="p4w:Misc", f1="p4w:IE Mobile", f2="p4w:Windows Mobile 6", f3="p4w:-", f4="p4w:C")
    db.ttablesXadvanced0.insert(f0="p4w:Misc", f1="p4w:PSP browser", f2="p4w:PSP", f3="p4w:-", f4="p4w:C")
    db.ttablesXadvanced0.insert(f0="p4w:Other browsers", f1="p4w:All others", f2="p4w:-", f3="p4w:-", f4="p4w:U")
    db.commit()

if not db(db.ttablesXadvanced1).count():
    db.ttablesXadvanced1.insert(f0="p4w:Rendering engine", f1="p4w:Browser", f2="p4w:Platform(s)", f3="p4w:Engine version", f4="p4w:CSS grade")
    db.ttablesXadvanced1.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 4.0", f2="p4w:Win 95+", f3="p4w:4", f4="p4w:X")
    db.ttablesXadvanced1.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 5.0", f2="p4w:Win 95+", f3="p4w:5", f4="p4w:C")
    db.ttablesXadvanced1.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 5.5", f2="p4w:Win 95+", f3="p4w:5.5", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 6", f2="p4w:Win 98+", f3="p4w:6", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 7", f2="p4w:Win XP SP2+", f3="p4w:7", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Trident", f1="p4w:AOL browser (AOL desktop)", f2="p4w:Win XP", f3="p4w:6", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.5", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Firefox 2.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Firefox 3.0", f2="p4w:Win 2k+ / OSX.3+", f3="p4w:1.9", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Camino 1.0", f2="p4w:OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Camino 1.5", f2="p4w:OSX.3+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Netscape 7.2", f2="p4w:Win 95+ / Mac OS 8.6-9.2", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Netscape Browser 8", f2="p4w:Win 98SE+", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Netscape Navigator 9", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.1", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.1", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.2", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.2", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.3", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.3", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.4", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.4", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.5", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.5", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.6", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.6", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.7", f2="p4w:Win 98+ / OSX.1+", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.8", f2="p4w:Win 98+ / OSX.1+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Seamonkey 1.1", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Gecko", f1="p4w:Epiphany 2.20", f2="p4w:Gnome", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Webkit", f1="p4w:Safari 1.2", f2="p4w:OSX.3", f3="p4w:125.5", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Webkit", f1="p4w:Safari 1.3", f2="p4w:OSX.3", f3="p4w:312.8", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Webkit", f1="p4w:Safari 2.0", f2="p4w:OSX.4+", f3="p4w:419.3", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Webkit", f1="p4w:Safari 3.0", f2="p4w:OSX.4+", f3="p4w:522.1", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Webkit", f1="p4w:OmniWeb 5.5", f2="p4w:OSX.4+", f3="p4w:420", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Webkit", f1="p4w:iPod Touch / iPhone", f2="p4w:iPod", f3="p4w:420.1", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Webkit", f1="p4w:S60", f2="p4w:S60", f3="p4w:413", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Presto", f1="p4w:Opera 7.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Presto", f1="p4w:Opera 7.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Presto", f1="p4w:Opera 8.0", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Presto", f1="p4w:Opera 8.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Presto", f1="p4w:Opera 9.0", f2="p4w:Win 95+ / OSX.3+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Presto", f1="p4w:Opera 9.2", f2="p4w:Win 88+ / OSX.3+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Presto", f1="p4w:Opera 9.5", f2="p4w:Win 88+ / OSX.3+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Presto", f1="p4w:Opera for Wii", f2="p4w:Wii", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Presto", f1="p4w:Nokia N800", f2="p4w:N800", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Presto", f1="p4w:Nintendo DS browser", f2="p4w:Nintendo DS", f3="p4w:8.5", f4="p4w:C/A1")
    db.ttablesXadvanced1.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.1", f2="p4w:KDE 3.1", f3="p4w:3.1", f4="p4w:C")
    db.ttablesXadvanced1.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.3", f2="p4w:KDE 3.3", f3="p4w:3.3", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.5", f2="p4w:KDE 3.5", f3="p4w:3.5", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 4.5", f2="p4w:Mac OS 8-9", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced1.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.1", f2="p4w:Mac OS 7.6-9", f3="p4w:1", f4="p4w:C")
    db.ttablesXadvanced1.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.2", f2="p4w:Mac OS 8-X", f3="p4w:1", f4="p4w:C")
    db.ttablesXadvanced1.insert(f0="p4w:Misc", f1="p4w:NetFront 3.1", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:C")
    db.ttablesXadvanced1.insert(f0="p4w:Misc", f1="p4w:NetFront 3.4", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced1.insert(f0="p4w:Misc", f1="p4w:Dillo 0.8", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced1.insert(f0="p4w:Misc", f1="p4w:Links", f2="p4w:Text only", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced1.insert(f0="p4w:Misc", f1="p4w:Lynx", f2="p4w:Text only", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced1.insert(f0="p4w:Misc", f1="p4w:IE Mobile", f2="p4w:Windows Mobile 6", f3="p4w:-", f4="p4w:C")
    db.ttablesXadvanced1.insert(f0="p4w:Misc", f1="p4w:PSP browser", f2="p4w:PSP", f3="p4w:-", f4="p4w:C")
    db.ttablesXadvanced1.insert(f0="p4w:Other browsers", f1="p4w:All others", f2="p4w:-", f3="p4w:-", f4="p4w:U")
    db.commit()

if not db(db.ttablesXadvanced2).count():
    db.ttablesXadvanced2.insert(f0="p4w:Rendering engine", f1="p4w:Browser", f2="p4w:Platform(s)", f3="p4w:Engine version", f4="p4w:CSS grade")
    db.ttablesXadvanced2.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 4.0", f2="p4w:Win 95+", f3="p4w:4", f4="p4w:X")
    db.ttablesXadvanced2.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 5.0", f2="p4w:Win 95+", f3="p4w:5", f4="p4w:C")
    db.ttablesXadvanced2.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 5.5", f2="p4w:Win 95+", f3="p4w:5.5", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 6", f2="p4w:Win 98+", f3="p4w:6", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 7", f2="p4w:Win XP SP2+", f3="p4w:7", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Trident", f1="p4w:AOL browser (AOL desktop)", f2="p4w:Win XP", f3="p4w:6", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.5", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Firefox 2.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Firefox 3.0", f2="p4w:Win 2k+ / OSX.3+", f3="p4w:1.9", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Camino 1.0", f2="p4w:OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Camino 1.5", f2="p4w:OSX.3+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Netscape 7.2", f2="p4w:Win 95+ / Mac OS 8.6-9.2", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Netscape Browser 8", f2="p4w:Win 98SE+", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Netscape Navigator 9", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.1", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.1", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.2", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.2", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.3", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.3", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.4", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.4", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.5", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.5", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.6", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.6", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.7", f2="p4w:Win 98+ / OSX.1+", f3="p4w:1.7", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.8", f2="p4w:Win 98+ / OSX.1+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Seamonkey 1.1", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Gecko", f1="p4w:Epiphany 2.20", f2="p4w:Gnome", f3="p4w:1.8", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Webkit", f1="p4w:Safari 1.2", f2="p4w:OSX.3", f3="p4w:125.5", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Webkit", f1="p4w:Safari 1.3", f2="p4w:OSX.3", f3="p4w:312.8", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Webkit", f1="p4w:Safari 2.0", f2="p4w:OSX.4+", f3="p4w:419.3", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Webkit", f1="p4w:Safari 3.0", f2="p4w:OSX.4+", f3="p4w:522.1", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Webkit", f1="p4w:OmniWeb 5.5", f2="p4w:OSX.4+", f3="p4w:420", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Webkit", f1="p4w:iPod Touch / iPhone", f2="p4w:iPod", f3="p4w:420.1", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Webkit", f1="p4w:S60", f2="p4w:S60", f3="p4w:413", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Presto", f1="p4w:Opera 7.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Presto", f1="p4w:Opera 7.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Presto", f1="p4w:Opera 8.0", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Presto", f1="p4w:Opera 8.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Presto", f1="p4w:Opera 9.0", f2="p4w:Win 95+ / OSX.3+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Presto", f1="p4w:Opera 9.2", f2="p4w:Win 88+ / OSX.3+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Presto", f1="p4w:Opera 9.5", f2="p4w:Win 88+ / OSX.3+", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Presto", f1="p4w:Opera for Wii", f2="p4w:Wii", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Presto", f1="p4w:Nokia N800", f2="p4w:N800", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Presto", f1="p4w:Nintendo DS browser", f2="p4w:Nintendo DS", f3="p4w:8.5", f4="p4w:C/A1")
    db.ttablesXadvanced2.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.1", f2="p4w:KDE 3.1", f3="p4w:3.1", f4="p4w:C")
    db.ttablesXadvanced2.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.3", f2="p4w:KDE 3.3", f3="p4w:3.3", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.5", f2="p4w:KDE 3.5", f3="p4w:3.5", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 4.5", f2="p4w:Mac OS 8-9", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced2.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.1", f2="p4w:Mac OS 7.6-9", f3="p4w:1", f4="p4w:C")
    db.ttablesXadvanced2.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.2", f2="p4w:Mac OS 8-X", f3="p4w:1", f4="p4w:C")
    db.ttablesXadvanced2.insert(f0="p4w:Misc", f1="p4w:NetFront 3.1", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:C")
    db.ttablesXadvanced2.insert(f0="p4w:Misc", f1="p4w:NetFront 3.4", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:A")
    db.ttablesXadvanced2.insert(f0="p4w:Misc", f1="p4w:Dillo 0.8", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced2.insert(f0="p4w:Misc", f1="p4w:Links", f2="p4w:Text only", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced2.insert(f0="p4w:Misc", f1="p4w:Lynx", f2="p4w:Text only", f3="p4w:-", f4="p4w:X")
    db.ttablesXadvanced2.insert(f0="p4w:Misc", f1="p4w:IE Mobile", f2="p4w:Windows Mobile 6", f3="p4w:-", f4="p4w:C")
    db.ttablesXadvanced2.insert(f0="p4w:Misc", f1="p4w:PSP browser", f2="p4w:PSP", f3="p4w:-", f4="p4w:C")
    db.ttablesXadvanced2.insert(f0="p4w:Other browsers", f1="p4w:All others", f2="p4w:-", f3="p4w:-", f4="p4w:U")
    db.commit()

if not db(db.ttablesXresponsive0).count():
    db.ttablesXresponsive0.insert(f0="p4w:Code", f1="p4w:Company", f2="p4w:Price", f3="p4w:Change", f4="p4w:Change %", f5="p4w:Open", f6="p4w:High", f7="p4w:Low", f8="p4w:Volume")
    db.ttablesXresponsive0.insert(f0="p4w:AAC", f1="p4w:AUSTRALIAN AGRICULTURAL COMPANY LIMITED.", f2="p4w:$1.38", f3="p4w:-0.01", f4="p4w:-0.36%", f5="p4w:$1.39", f6="p4w:$1.39", f7="p4w:$1.38", f8="p4w:9,395")
    db.ttablesXresponsive0.insert(f0="p4w:AAD", f1="p4w:ARDENT LEISURE GROUP", f2="p4w:$1.15", f3="p4w:+0.02", f4="p4w:1.32%", f5="p4w:$1.14", f6="p4w:$1.15", f7="p4w:$1.13", f8="p4w:56,431")
    db.ttablesXresponsive0.insert(f0="p4w:AAX", f1="p4w:AUSENCO LIMITED", f2="p4w:$4.00", f3="p4w:-0.04", f4="p4w:-0.99%", f5="p4w:$4.01", f6="p4w:$4.05", f7="p4w:$4.00", f8="p4w:90,641")
    db.ttablesXresponsive0.insert(f0="p4w:ABC", f1="p4w:ADELAIDE BRIGHTON LIMITED", f2="p4w:$3.00", f3="p4w:+0.06", f4="p4w:2.04%", f5="p4w:$2.98", f6="p4w:$3.00", f7="p4w:$2.96", f8="p4w:862,518")
    db.ttablesXresponsive0.insert(f0="p4w:ABP", f1="p4w:ABACUS PROPERTY GROUP", f2="p4w:$1.91", f3="p4w:0.00", f4="p4w:0.00%", f5="p4w:$1.92", f6="p4w:$1.93", f7="p4w:$1.90", f8="p4w:595,701")
    db.ttablesXresponsive0.insert(f0="p4w:ABY", f1="p4w:ADITYA BIRLA MINERALS LIMITED", f2="p4w:$0.77", f3="p4w:+0.02", f4="p4w:2.00%", f5="p4w:$0.76", f6="p4w:$0.77", f7="p4w:$0.76", f8="p4w:54,567")
    db.ttablesXresponsive0.insert(f0="p4w:ACR", f1="p4w:ACRUX LIMITED", f2="p4w:$3.71", f3="p4w:+0.01", f4="p4w:0.14%", f5="p4w:$3.70", f6="p4w:$3.72", f7="p4w:$3.68", f8="p4w:191,373")
    db.ttablesXresponsive0.insert(f0="p4w:ADU", f1="p4w:ADAMUS RESOURCES LIMITED", f2="p4w:$0.72", f3="p4w:0.00", f4="p4w:0.00%", f5="p4w:$0.73", f6="p4w:$0.74", f7="p4w:$0.72", f8="p4w:8,602,291")
    db.ttablesXresponsive0.insert(f0="p4w:AGG", f1="p4w:ANGLOGOLD ASHANTI LIMITED", f2="p4w:$7.81", f3="p4w:-0.22", f4="p4w:-2.74%", f5="p4w:$7.82", f6="p4w:$7.82", f7="p4w:$7.81", f8="p4w:148")
    db.ttablesXresponsive0.insert(f0="p4w:AGK", f1="p4w:AGL ENERGY LIMITED", f2="p4w:$13.82", f3="p4w:+0.02", f4="p4w:0.14%", f5="p4w:$13.83", f6="p4w:$13.83", f7="p4w:$13.67", f8="p4w:846,403")
    db.ttablesXresponsive0.insert(f0="p4w:AGO", f1="p4w:ATLAS IRON LIMITED", f2="p4w:$3.17", f3="p4w:-0.02", f4="p4w:-0.47%", f5="p4w:$3.11", f6="p4w:$3.22", f7="p4w:$3.10", f8="p4w:5,416,303")
    db.commit()

if not db(db.ttablesXresponsive1).count():
    db.ttablesXresponsive1.insert(f0="p4w:Code", f1="p4w:Company", f2="p4w:Price", f3="p4w:Change", f4="p4w:Change %", f5="p4w:Open", f6="p4w:High", f7="p4w:Low", f8="p4w:Volume")
    db.ttablesXresponsive1.insert(f0="p4w:AAC", f1="p4w:AUSTRALIAN AGRICULTURAL COMPANY LIMITED.", f2="p4w:$1.38", f3="p4w:-0.01", f4="p4w:-0.36%", f5="p4w:$1.39", f6="p4w:$1.39", f7="p4w:$1.38", f8="p4w:9,395")
    db.ttablesXresponsive1.insert(f0="p4w:AAD", f1="p4w:ARDENT LEISURE GROUP", f2="p4w:$1.15", f3="p4w:+0.02", f4="p4w:1.32%", f5="p4w:$1.14", f6="p4w:$1.15", f7="p4w:$1.13", f8="p4w:56,431")
    db.ttablesXresponsive1.insert(f0="p4w:AAX", f1="p4w:AUSENCO LIMITED", f2="p4w:$4.00", f3="p4w:-0.04", f4="p4w:-0.99%", f5="p4w:$4.01", f6="p4w:$4.05", f7="p4w:$4.00", f8="p4w:90,641")
    db.ttablesXresponsive1.insert(f0="p4w:ABC", f1="p4w:ADELAIDE BRIGHTON LIMITED", f2="p4w:$3.00", f3="p4w:+0.06", f4="p4w:2.04%", f5="p4w:$2.98", f6="p4w:$3.00", f7="p4w:$2.96", f8="p4w:862,518")
    db.ttablesXresponsive1.insert(f0="p4w:ABP", f1="p4w:ABACUS PROPERTY GROUP", f2="p4w:$1.91", f3="p4w:0.00", f4="p4w:0.00%", f5="p4w:$1.92", f6="p4w:$1.93", f7="p4w:$1.90", f8="p4w:595,701")
    db.ttablesXresponsive1.insert(f0="p4w:ABY", f1="p4w:ADITYA BIRLA MINERALS LIMITED", f2="p4w:$0.77", f3="p4w:+0.02", f4="p4w:2.00%", f5="p4w:$0.76", f6="p4w:$0.77", f7="p4w:$0.76", f8="p4w:54,567")
    db.ttablesXresponsive1.insert(f0="p4w:ACR", f1="p4w:ACRUX LIMITED", f2="p4w:$3.71", f3="p4w:+0.01", f4="p4w:0.14%", f5="p4w:$3.70", f6="p4w:$3.72", f7="p4w:$3.68", f8="p4w:191,373")
    db.ttablesXresponsive1.insert(f0="p4w:ADU", f1="p4w:ADAMUS RESOURCES LIMITED", f2="p4w:$0.72", f3="p4w:0.00", f4="p4w:0.00%", f5="p4w:$0.73", f6="p4w:$0.74", f7="p4w:$0.72", f8="p4w:8,602,291")
    db.ttablesXresponsive1.insert(f0="p4w:AGG", f1="p4w:ANGLOGOLD ASHANTI LIMITED", f2="p4w:$7.81", f3="p4w:-0.22", f4="p4w:-2.74%", f5="p4w:$7.82", f6="p4w:$7.82", f7="p4w:$7.81", f8="p4w:148")
    db.ttablesXresponsive1.insert(f0="p4w:AGK", f1="p4w:AGL ENERGY LIMITED", f2="p4w:$13.82", f3="p4w:+0.02", f4="p4w:0.14%", f5="p4w:$13.83", f6="p4w:$13.83", f7="p4w:$13.67", f8="p4w:846,403")
    db.ttablesXresponsive1.insert(f0="p4w:AGO", f1="p4w:ATLAS IRON LIMITED", f2="p4w:$3.17", f3="p4w:-0.02", f4="p4w:-0.47%", f5="p4w:$3.11", f6="p4w:$3.22", f7="p4w:$3.10", f8="p4w:5,416,303")
    db.commit()

if not db(db.ttablesXresponsive2).count():
    db.ttablesXresponsive2.insert(f0="p4w:Code", f1="p4w:Company", f2="p4w:Price", f3="p4w:Change", f4="p4w:Change %", f5="p4w:Open", f6="p4w:High", f7="p4w:Low", f8="p4w:Volume")
    db.ttablesXresponsive2.insert(f0="p4w:AAC", f1="p4w:AUSTRALIAN AGRICULTURAL COMPANY LIMITED.", f2="p4w:$1.38", f3="p4w:-0.01", f4="p4w:-0.36%", f5="p4w:$1.39", f6="p4w:$1.39", f7="p4w:$1.38", f8="p4w:9,395")
    db.ttablesXresponsive2.insert(f0="p4w:AAD", f1="p4w:ARDENT LEISURE GROUP", f2="p4w:$1.15", f3="p4w:+0.02", f4="p4w:1.32%", f5="p4w:$1.14", f6="p4w:$1.15", f7="p4w:$1.13", f8="p4w:56,431")
    db.ttablesXresponsive2.insert(f0="p4w:AAX", f1="p4w:AUSENCO LIMITED", f2="p4w:$4.00", f3="p4w:-0.04", f4="p4w:-0.99%", f5="p4w:$4.01", f6="p4w:$4.05", f7="p4w:$4.00", f8="p4w:90,641")
    db.ttablesXresponsive2.insert(f0="p4w:ABC", f1="p4w:ADELAIDE BRIGHTON LIMITED", f2="p4w:$3.00", f3="p4w:+0.06", f4="p4w:2.04%", f5="p4w:$2.98", f6="p4w:$3.00", f7="p4w:$2.96", f8="p4w:862,518")
    db.ttablesXresponsive2.insert(f0="p4w:ABP", f1="p4w:ABACUS PROPERTY GROUP", f2="p4w:$1.91", f3="p4w:0.00", f4="p4w:0.00%", f5="p4w:$1.92", f6="p4w:$1.93", f7="p4w:$1.90", f8="p4w:595,701")
    db.ttablesXresponsive2.insert(f0="p4w:ABY", f1="p4w:ADITYA BIRLA MINERALS LIMITED", f2="p4w:$0.77", f3="p4w:+0.02", f4="p4w:2.00%", f5="p4w:$0.76", f6="p4w:$0.77", f7="p4w:$0.76", f8="p4w:54,567")
    db.ttablesXresponsive2.insert(f0="p4w:ACR", f1="p4w:ACRUX LIMITED", f2="p4w:$3.71", f3="p4w:+0.01", f4="p4w:0.14%", f5="p4w:$3.70", f6="p4w:$3.72", f7="p4w:$3.68", f8="p4w:191,373")
    db.ttablesXresponsive2.insert(f0="p4w:ADU", f1="p4w:ADAMUS RESOURCES LIMITED", f2="p4w:$0.72", f3="p4w:0.00", f4="p4w:0.00%", f5="p4w:$0.73", f6="p4w:$0.74", f7="p4w:$0.72", f8="p4w:8,602,291")
    db.ttablesXresponsive2.insert(f0="p4w:AGG", f1="p4w:ANGLOGOLD ASHANTI LIMITED", f2="p4w:$7.81", f3="p4w:-0.22", f4="p4w:-2.74%", f5="p4w:$7.82", f6="p4w:$7.82", f7="p4w:$7.81", f8="p4w:148")
    db.ttablesXresponsive2.insert(f0="p4w:AGK", f1="p4w:AGL ENERGY LIMITED", f2="p4w:$13.82", f3="p4w:+0.02", f4="p4w:0.14%", f5="p4w:$13.83", f6="p4w:$13.83", f7="p4w:$13.67", f8="p4w:846,403")
    db.ttablesXresponsive2.insert(f0="p4w:AGO", f1="p4w:ATLAS IRON LIMITED", f2="p4w:$3.17", f3="p4w:-0.02", f4="p4w:-0.47%", f5="p4w:$3.11", f6="p4w:$3.22", f7="p4w:$3.10", f8="p4w:5,416,303")
    db.commit()

if not db(db.ttablesXeditable0).count():
    db.ttablesXeditable0.insert(f0="p4w:Rendering engine", f1="p4w:Browser", f2="p4w:Platform(s)", f3="p4w:Actions")
    db.ttablesXeditable0.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 4.0", f2="p4w:Win 95+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 5.0", f2="p4w:Win 95+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 5.5", f2="p4w:Win 95+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Trident", f1="p4w:InternetExplorer 6", f2="p4w:Win 98+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 7", f2="p4w:Win XP SP2+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Trident", f1="p4w:AOL browser (AOL desktop)", f2="p4w:Win XP", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.5", f2="p4w:Win 98+ / OSX.2+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Firefox 2.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Firefox 3.0", f2="p4w:Win 2k+ / OSX.3+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Camino 1.0", f2="p4w:OSX.2+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Camino 1.5", f2="p4w:OSX.3+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Netscape 7.2", f2="p4w:Win 95+ / Mac OS 8.6-9.2", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Netscape Browser 8", f2="p4w:Win 98SE+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Netscape Navigator 9", f2="p4w:Win 98+ / OSX.2+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.1", f2="p4w:Win 95+ / OSX.1+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.2", f2="p4w:Win 95+ / OSX.1+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.3", f2="p4w:Win 95+ / OSX.1+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.4", f2="p4w:Win 95+ / OSX.1+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.5", f2="p4w:Win 95+ / OSX.1+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.6", f2="p4w:Win 95+ / OSX.1+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.7", f2="p4w:Win 98+ / OSX.1+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.8", f2="p4w:Win 98+ / OSX.1+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Seamonkey 1.1", f2="p4w:Win 98+ / OSX.2+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Gecko", f1="p4w:Epiphany 2.20", f2="p4w:Gnome", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Webkit", f1="p4w:Safari 1.2", f2="p4w:OSX.3", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Webkit", f1="p4w:Safari 1.3", f2="p4w:OSX.3", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Webkit", f1="p4w:Safari 2.0", f2="p4w:OSX.4+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Webkit", f1="p4w:Safari 3.0", f2="p4w:OSX.4+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Webkit", f1="p4w:OmniWeb 5.5", f2="p4w:OSX.4+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Webkit", f1="p4w:iPod Touch / iPhone", f2="p4w:iPod", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Webkit", f1="p4w:S60", f2="p4w:S60", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Presto", f1="p4w:Opera 7.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Presto", f1="p4w:Opera 7.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Presto", f1="p4w:Opera 8.0", f2="p4w:Win 95+ / OSX.2+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Presto", f1="p4w:Opera 8.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Presto", f1="p4w:Opera 9.0", f2="p4w:Win 95+ / OSX.3+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Presto", f1="p4w:Opera 9.2", f2="p4w:Win 88+ / OSX.3+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Presto", f1="p4w:Opera 9.5", f2="p4w:Win 88+ / OSX.3+", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Presto", f1="p4w:Opera for Wii", f2="p4w:Wii", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Presto", f1="p4w:Nokia N800", f2="p4w:N800", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Presto", f1="p4w:Nintendo DS browser", f2="p4w:Nintendo DS", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.1", f2="p4w:KDE 3.1", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.3", f2="p4w:KDE 3.3", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.5", f2="p4w:KDE 3.5", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 4.5", f2="p4w:Mac OS 8-9", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.1", f2="p4w:Mac OS 7.6-9", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.2", f2="p4w:Mac OS 8-X", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Misc", f1="p4w:NetFront 3.1", f2="p4w:Embedded devices", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Misc", f1="p4w:NetFront 3.4", f2="p4w:Embedded devices", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Misc", f1="p4w:Dillo 0.8", f2="p4w:Embedded devices", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Misc", f1="p4w:Links", f2="p4w:Text only", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Misc", f1="p4w:Lynx", f2="p4w:Text only", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Misc", f1="p4w:IE Mobile", f2="p4w:Windows Mobile 6", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Misc", f1="p4w:PSP browser", f2="p4w:PSP", f3="p4w:len0")
    db.ttablesXeditable0.insert(f0="p4w:Other browsers", f1="p4w:All others", f2="p4w:-", f3="p4w:len0")
    db.commit()

if not db(db.ttablesXajax0).count():
    db.ttablesXajax0.insert(f0="p4w:Rendering engine", f1="p4w:Browser", f2="p4w:Platform(s)", f3="p4w:Engine version", f4="p4w:CSS grade")
    db.commit()

if not db(db.tpagesXinvoiceXprint0).count():
    db.tpagesXinvoiceXprint0.insert(f0="p4w:#", f1="p4w:Item", f2="p4w:Description", f3="p4w:Price", f4="p4w:Quantity", f5="p4w:Total")
    db.tpagesXinvoiceXprint0.insert(f0="p4w:123456", f1="p4w:Porto HTML5 Template", f2="p4w:Multipourpouse Website Template", f3="p4w:$14.00", f4="p4w:2", f5="p4w:$28.00")
    db.tpagesXinvoiceXprint0.insert(f0="p4w:654321", f1="p4w:Tucson HTML5 Template", f2="p4w:Awesome Website Template", f3="p4w:$17.00", f4="p4w:1", f5="p4w:$17.00")
    db.commit()

if not db(db.tpagesXinvoiceXprint1).count():
    db.tpagesXinvoiceXprint1.insert(f0="p4w:Subtotal", f1="p4w:$73.00")
    db.tpagesXinvoiceXprint1.insert(f0="p4w:Shipping", f1="p4w:$0.00")
    db.tpagesXinvoiceXprint1.insert(f0="p4w:Grand Total", f1="p4w:$73.00")
    db.commit()
