from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 27.10.2020 12:50:51
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
    'dfindex2',
    Field('f0','string'),
    )

db.define_table(
    'dfindex3',
    Field('f0','string'),
    )

db.define_table(
    'dfindex4',
    Field('f0','string'),
    )

db.define_table(
    'dfindex5',
    Field('f0','string'),
    )

db.define_table(
    'dfindex6',
    Field('f0','string'),
    )

db.define_table(
    'dfindex7',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX20',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX21',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX22',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX23',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX24',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX25',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX26',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX27',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX30',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX31',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX32',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX33',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX34',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX35',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX36',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX37',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX40',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX41',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX42',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX43',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX44',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX45',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX46',
    Field('f0','string'),
    )

db.define_table(
    'dfindexX47',
    Field('f0','string'),
    )

db.define_table(
    'dfanalytics0',
    Field('f0','string'),
    )

db.define_table(
    'dfanalytics1',
    Field('f0','string'),
    )

db.define_table(
    'dfwidgets0',
    Field('f0','string'),
    )

db.define_table(
    'dfwidgets1',
    Field('f0','string'),
    )

db.define_table(
    'dfwidgets2',
    Field('f0','string'),
    )

db.define_table(
    'dfwidgets3',
    Field('f0','string'),
    )

db.define_table(
    'dfwidgets4',
    Field('f0','string'),
    )

db.define_table(
    'dfwidgets5',
    Field('f0','string'),
    )

db.define_table(
    'dfwidgets6',
    Field('f0','text'),
    )

db.define_table(
    'dfinbox0',
    Field('f0','string'),
    )

db.define_table(
    'dfinbox1',
    Field('f0','string'),
    )

db.define_table(
    'dfinbox2',
    Field('f0','string'),
    )

db.define_table(
    'dfinbox3',
    Field('f0','boolean'),
    )

db.define_table(
    'dfinbox4',
    Field('f0','boolean'),
    )

db.define_table(
    'dfinbox5',
    Field('f0','boolean'),
    )

db.define_table(
    'dfinbox6',
    Field('f0','boolean'),
    )

db.define_table(
    'dfinbox7',
    Field('f0','boolean'),
    )

db.define_table(
    'dfinbox8',
    Field('f0','boolean'),
    )

db.define_table(
    'dfinbox9',
    Field('f0','boolean'),
    )

db.define_table(
    'dfinbox10',
    Field('f0','boolean'),
    )

db.define_table(
    'dfviewXemail0',
    Field('f0','string'),
    )

db.define_table(
    'dfviewXemail1',
    Field('f0','string'),
    )

db.define_table(
    'dfcomposeXemail0',
    )

db.define_table(
    'dfanimations0',
    Field('f0','string'),
    )

db.define_table(
    'dfanimations1',
    Field('f0','string'),
    )

db.define_table(
    'dfgoogleXmap0',
    Field('f0','string'),
    )

db.define_table(
    'dfgoogleXmap1',
    Field('f0','string'),
    )

db.define_table(
    'dfdataXmap0',
    Field('f0','string'),
    )

db.define_table(
    'dfdataXmap1',
    Field('f0','string'),
    )

db.define_table(
    'dfcodeXeditor0',
    Field('f0','string'),
    )

db.define_table(
    'dfcodeXeditor1',
    Field('f0','string'),
    )

db.define_table(
    'dfimageXcropper0',
    Field('f0','string'),
    )

db.define_table(
    'dfimageXcropper1',
    Field('f0','string'),
    )

db.define_table(
    'dfwizard0',
    Field('f0','string'),
    )

db.define_table(
    'dfwizard1',
    Field('f0','string'),
    )

db.define_table(
    'dfflotXcharts0',
    Field('f0','string'),
    )

db.define_table(
    'dfflotXcharts1',
    Field('f0','string'),
    )

db.define_table(
    'dfbarXcharts0',
    Field('f0','string'),
    )

db.define_table(
    'dfbarXcharts1',
    Field('f0','string'),
    )

db.define_table(
    'dflineXcharts0',
    Field('f0','string'),
    )

db.define_table(
    'dflineXcharts1',
    Field('f0','string'),
    )

db.define_table(
    'dfareaXcharts0',
    Field('f0','string'),
    )

db.define_table(
    'dfareaXcharts1',
    Field('f0','string'),
    )

db.define_table(
    'dfnormalXtable0',
    Field('f0','string'),
    )

db.define_table(
    'dfnormalXtable1',
    Field('f0','string'),
    )

db.define_table(
    'dfdataXtable0',
    Field('f0','string'),
    )

db.define_table(
    'dfdataXtable1',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements0',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements1',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements2',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements3',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements4',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements5',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements6',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements7',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements8',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements9',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements10',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements11',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements12',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements13',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements14',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements15',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements16',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements17',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements18',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements19',
    Field('f0','text'),
    )

db.define_table(
    'dfformXelements20',
    Field('f0','text'),
    )

db.define_table(
    'dfformXelements21',
    Field('f0','text'),
    )

db.define_table(
    'dfformXelements22',
    Field('f0','boolean'),
    )

db.define_table(
    'dfformXelements23',
    Field('f0','boolean'),
    )

db.define_table(
    'dfformXelements24',
    Field('f0','boolean'),
    )

db.define_table(
    'dfformXelements25',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements26',
    Field('f0','string'),
    )

db.define_table(
    'dfformXelements27',
    Field('f0','string'),
    )

db.define_table(
    'dfformXcomponents0',
    )

db.define_table(
    'dfformXexamples0',
    Field('f0','string'),
    )

db.define_table(
    'dfformXexamples1',
    Field('f0','string'),
    )

db.define_table(
    'dfformXexamples2',
    Field('f0','string'),
    )

db.define_table(
    'dfformXexamples3',
    Field('f0','string'),
    )

db.define_table(
    'dfformXexamples4',
    Field('f0','boolean'),
    )

db.define_table(
    'dfformXexamples5',
    Field('f0','string'),
    )

db.define_table(
    'dfformXexamples6',
    Field('f0','string'),
    )

db.define_table(
    'dfformXexamples7',
    Field('f0','boolean'),
    )

db.define_table(
    'dfformXexamples8',
    Field('f0','string'),
    )

db.define_table(
    'dfformXexamples9',
    Field('f0','string'),
    )

db.define_table(
    'dfformXexamples10',
    Field('f0','boolean'),
    )

db.define_table(
    'dfnotification0',
    Field('f0','string'),
    )

db.define_table(
    'dfnotification1',
    Field('f0','string'),
    )

db.define_table(
    'dfalert0',
    Field('f0','string'),
    )

db.define_table(
    'dfalert1',
    Field('f0','string'),
    )

db.define_table(
    'dfmodals0',
    Field('f0','string'),
    )

db.define_table(
    'dfmodals1',
    Field('f0','string'),
    )

db.define_table(
    'dfbuttons0',
    Field('f0','string'),
    )

db.define_table(
    'dfbuttons1',
    Field('f0','string'),
    )

db.define_table(
    'dftabs0',
    Field('f0','string'),
    )

db.define_table(
    'dftabs1',
    Field('f0','string'),
    )

db.define_table(
    'dfaccordion0',
    Field('f0','string'),
    )

db.define_table(
    'dfaccordion1',
    Field('f0','string'),
    )

db.define_table(
    'dfdialog0',
    Field('f0','string'),
    )

db.define_table(
    'dfdialog1',
    Field('f0','string'),
    )

db.define_table(
    'dfpopovers0',
    Field('f0','string'),
    )

db.define_table(
    'dfpopovers1',
    Field('f0','string'),
    )

db.define_table(
    'dftooltips0',
    Field('f0','string'),
    )

db.define_table(
    'dftooltips1',
    Field('f0','string'),
    )

db.define_table(
    'dfdropdown0',
    Field('f0','string'),
    )

db.define_table(
    'dfdropdown1',
    Field('f0','string'),
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
    'dfinvoice0',
    Field('f0','string'),
    )

db.define_table(
    'dfinvoice1',
    Field('f0','string'),
    )

db.define_table(
    'dftypography0',
    Field('f0','string'),
    )

db.define_table(
    'dftypography1',
    Field('f0','string'),
    )

db.define_table(
    'dfcolor0',
    Field('f0','string'),
    )

db.define_table(
    'dfcolor1',
    Field('f0','string'),
    )

db.define_table(
    'dfloginXregister0',
    Field('f0','string'),
    )

db.define_table(
    'dfloginXregister1',
    Field('f0','string'),
    )

db.define_table(
    'dfloginXregister2',
    Field('f0','boolean'),
    )

db.define_table(
    'dfloginXregister3',
    Field('f0','string'),
    )

db.define_table(
    'dfloginXregister4',
    Field('f0','string'),
    )

db.define_table(
    'dfloginXregister5',
    Field('f0','string'),
    )

db.define_table(
    'dfloginXregister6',
    Field('f0','string'),
    )

db.define_table(
    'tindex0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tindexX20',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tindexX30',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tindexX40',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tanalytics0',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'tanalytics1',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'tanalytics2',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'tinbox0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tnormalXtable0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tnormalXtable1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tnormalXtable2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tnormalXtable3',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tnormalXtable4',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tnormalXtable5',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tdataXtable0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'tinvoice0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

if not db(db.tindex0).count():
    db.tindex0.insert(f0="p4w:ID", f1="p4w:Name", f2="p4w:Price")
    db.tindex0.insert(f0="p4w:4555", f1="p4w:Samsung Galaxy Mega", f2="p4w:$921")
    db.tindex0.insert(f0="p4w:4556", f1="p4w:Huawei Ascend P6", f2="p4w:$240")
    db.tindex0.insert(f0="p4w:8778", f1="p4w:HTC One M8", f2="p4w:$400")
    db.tindex0.insert(f0="p4w:5667", f1="p4w:Samsung Galaxy Alpha", f2="p4w:$870")
    db.tindex0.insert(f0="p4w:7886", f1="p4w:LG G3", f2="p4w:$790")
    db.commit()

if not db(db.tindexX20).count():
    db.tindexX20.insert(f0="p4w:ID", f1="p4w:Name", f2="p4w:Price")
    db.tindexX20.insert(f0="p4w:4555", f1="p4w:Samsung Galaxy Mega", f2="p4w:$921")
    db.tindexX20.insert(f0="p4w:4556", f1="p4w:Huawei Ascend P6", f2="p4w:$240")
    db.tindexX20.insert(f0="p4w:8778", f1="p4w:HTC One M8", f2="p4w:$400")
    db.tindexX20.insert(f0="p4w:5667", f1="p4w:Samsung Galaxy Alpha", f2="p4w:$870")
    db.tindexX20.insert(f0="p4w:7886", f1="p4w:LG G3", f2="p4w:$790")
    db.commit()

if not db(db.tindexX30).count():
    db.tindexX30.insert(f0="p4w:ID", f1="p4w:Name", f2="p4w:Price")
    db.tindexX30.insert(f0="p4w:4555", f1="p4w:Samsung Galaxy Mega", f2="p4w:$921")
    db.tindexX30.insert(f0="p4w:4556", f1="p4w:Huawei Ascend P6", f2="p4w:$240")
    db.tindexX30.insert(f0="p4w:8778", f1="p4w:HTC One M8", f2="p4w:$400")
    db.tindexX30.insert(f0="p4w:5667", f1="p4w:Samsung Galaxy Alpha", f2="p4w:$870")
    db.tindexX30.insert(f0="p4w:7886", f1="p4w:LG G3", f2="p4w:$790")
    db.commit()

if not db(db.tindexX40).count():
    db.tindexX40.insert(f0="p4w:ID", f1="p4w:Name", f2="p4w:Price")
    db.tindexX40.insert(f0="p4w:4555", f1="p4w:Samsung Galaxy Mega", f2="p4w:$921")
    db.tindexX40.insert(f0="p4w:4556", f1="p4w:Huawei Ascend P6", f2="p4w:$240")
    db.tindexX40.insert(f0="p4w:8778", f1="p4w:HTC One M8", f2="p4w:$400")
    db.tindexX40.insert(f0="p4w:5667", f1="p4w:Samsung Galaxy Alpha", f2="p4w:$870")
    db.tindexX40.insert(f0="p4w:7886", f1="p4w:LG G3", f2="p4w:$790")
    db.commit()

if not db(db.tanalytics0).count():
    db.tanalytics0.insert(f0="p4w:Search Engine", f1="p4w:Visitors")
    db.tanalytics0.insert(f0="p4w:Google", f1="p4w:3831")
    db.tanalytics0.insert(f0="p4w:Bing", f1="p4w:2123")
    db.tanalytics0.insert(f0="p4w:Baidu", f1="p4w:4375")
    db.tanalytics0.insert(f0="p4w:Yahoo", f1="p4w:4020")
    db.tanalytics0.insert(f0="p4w:DuckDuckGo", f1="p4w:2064")
    db.tanalytics0.insert(f0="p4w:Yandex", f1="p4w:936")
    db.commit()

if not db(db.tanalytics1).count():
    db.tanalytics1.insert(f0="p4w:Website", f1="p4w:Visitors")
    db.tanalytics1.insert(f0="p4w:themeforest.net", f1="p4w:620")
    db.tanalytics1.insert(f0="p4w:codecanyon.net", f1="p4w:432")
    db.tanalytics1.insert(f0="p4w:google.com", f1="p4w:8702")
    db.tanalytics1.insert(f0="p4w:yahoo.com", f1="p4w:683")
    db.tanalytics1.insert(f0="p4w:youtube.com", f1="p4w:253")
    db.tanalytics1.insert(f0="p4w:bing.com", f1="p4w:3018")
    db.commit()

if not db(db.tanalytics2).count():
    db.tanalytics2.insert(f0="p4w:Work Flow", f1="p4w:Counter")
    db.tanalytics2.insert(f0="p4w:External Backlinks", f1="p4w:54,302")
    db.tanalytics2.insert(f0="p4w:Page Speed Score", f1="p4w:87")
    db.tanalytics2.insert(f0="p4w:Citation Flow", f1="p4w:987")
    db.tanalytics2.insert(f0="p4w:Mozrank", f1="p4w:9.43")
    db.tanalytics2.insert(f0="p4w:Domain Authority", f1="p4w:455")
    db.tanalytics2.insert(f0="p4w:Alexa Rank", f1="p4w:342,234")
    db.commit()

if not db(db.tinbox0).count():
    db.tinbox0.insert(f0="p4w:len0", f1="p4w:Jeremy Massey", f2="p4w:Lorem ipsum dolor sit amet, consectetur adipiscing elit.", f3="p4w:len0", f4="p4w:Tue, Nov 25")
    db.tinbox0.insert(f0="p4w:len0", f1="p4w:Marshall Horne", f2="p4w:Praesent nec nisl sed neque ornare maximus at ac enim.", f3="p4w:len0", f4="p4w:Wed, Jan 13")
    db.tinbox0.insert(f0="p4w:len0", f1="p4w:Grant Franco Finance", f2="p4w:Etiam maximus tellus a turpis tempor mollis.", f3="p4w:len0", f4="p4w:Mon, Oct 19")
    db.tinbox0.insert(f0="p4w:len0", f1="p4w:Ferdinand Meadows", f2="p4w:Aenean hendrerit ligula eget augue gravida semper.", f3="p4w:len0", f4="p4w:Sat, Aug 29")
    db.tinbox0.insert(f0="p4w:len0", f1="p4w:Ivor Rios Social", f2="p4w:Sed quis augue in nunc venenatis finibus.", f3="p4w:len0", f4="p4w:Sat, Dec 12")
    db.tinbox0.insert(f0="p4w:len0", f1="p4w:Maxwell Murphy", f2="p4w:Quisque eu tortor quis justo viverra cursus.", f3="p4w:len0", f4="p4w:Sun, May 17")
    db.tinbox0.insert(f0="p4w:len0", f1="p4w:Henry Patterson", f2="p4w:Aliquam nec justo interdum, ornare mi non, elementum lacus.", f3="p4w:len0", f4="p4w:Thu, Aug 06")
    db.tinbox0.insert(f0="p4w:len0", f1="p4w:Maxwell Murphy", f2="p4w:Quisque eu tortor quis justo viverra cursus.", f3="p4w:len0", f4="p4w:Sun, May 17")
    db.commit()

if not db(db.tnormalXtable0).count():
    db.tnormalXtable0.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username", f4="p4w:Nickname")
    db.tnormalXtable0.insert(f0="p4w:1", f1="p4w:Alexandra", f2="p4w:Christopher", f3="p4w:@makinton", f4="p4w:Ducky")
    db.tnormalXtable0.insert(f0="p4w:2", f1="p4w:Madeleine", f2="p4w:Hollaway", f3="p4w:@hollway", f4="p4w:Cheese")
    db.tnormalXtable0.insert(f0="p4w:3", f1="p4w:Sebastian", f2="p4w:Johnston", f3="p4w:@sebastian", f4="p4w:Jaycee")
    db.tnormalXtable0.insert(f0="p4w:4", f1="p4w:Mitchell", f2="p4w:Christin", f3="p4w:@mitchell4u", f4="p4w:AdskiDeAnus")
    db.tnormalXtable0.insert(f0="p4w:5", f1="p4w:Elizabeth", f2="p4w:Belkitt", f3="p4w:@belkitt", f4="p4w:Goat")
    db.tnormalXtable0.insert(f0="p4w:6", f1="p4w:Benjamin", f2="p4w:Parnell", f3="p4w:@wayne234", f4="p4w:Pokie")
    db.tnormalXtable0.insert(f0="p4w:7", f1="p4w:Katherine", f2="p4w:Buckland", f3="p4w:@anitabelle", f4="p4w:Wokie")
    db.tnormalXtable0.insert(f0="p4w:8", f1="p4w:Nicholas", f2="p4w:Walmart", f3="p4w:@mwalmart", f4="p4w:Spike")
    db.commit()

if not db(db.tnormalXtable1).count():
    db.tnormalXtable1.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username", f4="p4w:Nickname")
    db.tnormalXtable1.insert(f0="p4w:1", f1="p4w:Alexandra", f2="p4w:Christopher", f3="p4w:@makinton", f4="p4w:Ducky")
    db.tnormalXtable1.insert(f0="p4w:2", f1="p4w:Madeleine", f2="p4w:Hollaway", f3="p4w:@hollway", f4="p4w:Cheese")
    db.tnormalXtable1.insert(f0="p4w:3", f1="p4w:Sebastian", f2="p4w:Johnston", f3="p4w:@sebastian", f4="p4w:Jaycee")
    db.tnormalXtable1.insert(f0="p4w:4", f1="p4w:Mitchell", f2="p4w:Christin", f3="p4w:@mitchell4u", f4="p4w:AdskiDeAnus")
    db.tnormalXtable1.insert(f0="p4w:5", f1="p4w:Elizabeth", f2="p4w:Belkitt", f3="p4w:@belkitt", f4="p4w:Goat")
    db.tnormalXtable1.insert(f0="p4w:6", f1="p4w:Benjamin", f2="p4w:Parnell", f3="p4w:@wayne234", f4="p4w:Pokie")
    db.tnormalXtable1.insert(f0="p4w:7", f1="p4w:Katherine", f2="p4w:Buckland", f3="p4w:@anitabelle", f4="p4w:Wokie")
    db.tnormalXtable1.insert(f0="p4w:8", f1="p4w:Nicholas", f2="p4w:Walmart", f3="p4w:@mwalmart", f4="p4w:Spike")
    db.commit()

if not db(db.tnormalXtable2).count():
    db.tnormalXtable2.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username", f4="p4w:Nickname")
    db.tnormalXtable2.insert(f0="p4w:1", f1="p4w:Alexandra", f2="p4w:Christopher", f3="p4w:@makinton", f4="p4w:Ducky")
    db.tnormalXtable2.insert(f0="p4w:2", f1="p4w:Madeleine", f2="p4w:Hollaway", f3="p4w:@hollway", f4="p4w:Cheese")
    db.tnormalXtable2.insert(f0="p4w:3", f1="p4w:Sebastian", f2="p4w:Johnston", f3="p4w:@sebastian", f4="p4w:Jaycee")
    db.tnormalXtable2.insert(f0="p4w:4", f1="p4w:Mitchell", f2="p4w:Christin", f3="p4w:@mitchell4u", f4="p4w:AdskiDeAnus")
    db.tnormalXtable2.insert(f0="p4w:5", f1="p4w:Elizabeth", f2="p4w:Belkitt", f3="p4w:@belkitt", f4="p4w:Goat")
    db.tnormalXtable2.insert(f0="p4w:6", f1="p4w:Benjamin", f2="p4w:Parnell", f3="p4w:@wayne234", f4="p4w:Pokie")
    db.tnormalXtable2.insert(f0="p4w:7", f1="p4w:Katherine", f2="p4w:Buckland", f3="p4w:@anitabelle", f4="p4w:Wokie")
    db.tnormalXtable2.insert(f0="p4w:8", f1="p4w:Nicholas", f2="p4w:Walmart", f3="p4w:@mwalmart", f4="p4w:Spike")
    db.commit()

if not db(db.tnormalXtable3).count():
    db.tnormalXtable3.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username", f4="p4w:Nickname")
    db.tnormalXtable3.insert(f0="p4w:1", f1="p4w:Alexandra", f2="p4w:Christopher", f3="p4w:@makinton", f4="p4w:Ducky")
    db.tnormalXtable3.insert(f0="p4w:2", f1="p4w:Madeleine", f2="p4w:Hollaway", f3="p4w:@hollway", f4="p4w:Cheese")
    db.tnormalXtable3.insert(f0="p4w:3", f1="p4w:Sebastian", f2="p4w:Johnston", f3="p4w:@sebastian", f4="p4w:Jaycee")
    db.tnormalXtable3.insert(f0="p4w:4", f1="p4w:Mitchell", f2="p4w:Christin", f3="p4w:@mitchell4u", f4="p4w:AdskiDeAnus")
    db.tnormalXtable3.insert(f0="p4w:5", f1="p4w:Elizabeth", f2="p4w:Belkitt", f3="p4w:@belkitt", f4="p4w:Goat")
    db.tnormalXtable3.insert(f0="p4w:6", f1="p4w:Benjamin", f2="p4w:Parnell", f3="p4w:@wayne234", f4="p4w:Pokie")
    db.tnormalXtable3.insert(f0="p4w:7", f1="p4w:Katherine", f2="p4w:Buckland", f3="p4w:@anitabelle", f4="p4w:Wokie")
    db.tnormalXtable3.insert(f0="p4w:8", f1="p4w:Nicholas", f2="p4w:Walmart", f3="p4w:@mwalmart", f4="p4w:Spike")
    db.commit()

if not db(db.tnormalXtable4).count():
    db.tnormalXtable4.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username", f4="p4w:Nickname")
    db.tnormalXtable4.insert(f0="p4w:1", f1="p4w:Alexandra", f2="p4w:Christopher", f3="p4w:@makinton", f4="p4w:Ducky")
    db.tnormalXtable4.insert(f0="p4w:2", f1="p4w:Madeleine", f2="p4w:Hollaway", f3="p4w:@hollway", f4="p4w:Cheese")
    db.tnormalXtable4.insert(f0="p4w:3", f1="p4w:Sebastian", f2="p4w:Johnston", f3="p4w:@sebastian", f4="p4w:Jaycee")
    db.tnormalXtable4.insert(f0="p4w:4", f1="p4w:Mitchell", f2="p4w:Christin", f3="p4w:@mitchell4u", f4="p4w:AdskiDeAnus")
    db.tnormalXtable4.insert(f0="p4w:5", f1="p4w:Elizabeth", f2="p4w:Belkitt", f3="p4w:@belkitt", f4="p4w:Goat")
    db.tnormalXtable4.insert(f0="p4w:6", f1="p4w:Benjamin", f2="p4w:Parnell", f3="p4w:@wayne234", f4="p4w:Pokie")
    db.tnormalXtable4.insert(f0="p4w:7", f1="p4w:Katherine", f2="p4w:Buckland", f3="p4w:@anitabelle", f4="p4w:Wokie")
    db.tnormalXtable4.insert(f0="p4w:8", f1="p4w:Nicholas", f2="p4w:Walmart", f3="p4w:@mwalmart", f4="p4w:Spike")
    db.commit()

if not db(db.tnormalXtable5).count():
    db.tnormalXtable5.insert(f0="p4w:#", f1="p4w:First Name", f2="p4w:Last Name", f3="p4w:Username", f4="p4w:Nickname")
    db.tnormalXtable5.insert(f0="p4w:1", f1="p4w:Alexandra", f2="p4w:Christopher", f3="p4w:@makinton", f4="p4w:Ducky")
    db.tnormalXtable5.insert(f0="p4w:3", f1="p4w:Sebastian", f2="p4w:Johnston", f3="p4w:@sebastian", f4="p4w:Jaycee")
    db.tnormalXtable5.insert(f0="p4w:4", f1="p4w:Mitchell", f2="p4w:Christin", f3="p4w:@mitchell4u", f4="p4w:AdskiDeAnus")
    db.tnormalXtable5.insert(f0="p4w:2", f1="p4w:Madeleine", f2="p4w:Hollaway", f3="p4w:@hollway", f4="p4w:Cheese")
    db.tnormalXtable5.insert(f0="p4w:5", f1="p4w:Elizabeth", f2="p4w:Belkitt", f3="p4w:@belkitt", f4="p4w:Goat")
    db.commit()

if not db(db.tdataXtable0).count():
    db.tdataXtable0.insert(f0="p4w:Name", f1="p4w:Position", f2="p4w:Office", f3="p4w:Age", f4="p4w:Start date", f5="p4w:Salary")
    db.tdataXtable0.insert(f0="p4w:Tiger Nixon", f1="p4w:System Architect", f2="p4w:Edinburgh", f3="p4w:61", f4="p4w:2011/04/25", f5="p4w:$320,800")
    db.tdataXtable0.insert(f0="p4w:Garrett Winters", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:63", f4="p4w:2011/07/25", f5="p4w:$170,750")
    db.tdataXtable0.insert(f0="p4w:Ashton Cox", f1="p4w:Junior Technical Author", f2="p4w:San Francisco", f3="p4w:66", f4="p4w:2009/01/12", f5="p4w:$86,000")
    db.tdataXtable0.insert(f0="p4w:Cedric Kelly", f1="p4w:Senior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2012/03/29", f5="p4w:$433,060")
    db.tdataXtable0.insert(f0="p4w:Airi Satou", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:33", f4="p4w:2008/11/28", f5="p4w:$162,700")
    db.tdataXtable0.insert(f0="p4w:Brielle Williamson", f1="p4w:Integration Specialist", f2="p4w:New York", f3="p4w:61", f4="p4w:2012/12/02", f5="p4w:$372,000")
    db.tdataXtable0.insert(f0="p4w:Herrod Chandler", f1="p4w:Sales Assistant", f2="p4w:San Francisco", f3="p4w:59", f4="p4w:2012/08/06", f5="p4w:$137,500")
    db.tdataXtable0.insert(f0="p4w:Rhona Davidson", f1="p4w:Integration Specialist", f2="p4w:Tokyo", f3="p4w:55", f4="p4w:2010/10/14", f5="p4w:$327,900")
    db.tdataXtable0.insert(f0="p4w:Colleen Hurst", f1="p4w:Javascript Developer", f2="p4w:San Francisco", f3="p4w:39", f4="p4w:2009/09/15", f5="p4w:$205,500")
    db.tdataXtable0.insert(f0="p4w:Sonya Frost", f1="p4w:Software Engineer", f2="p4w:Edinburgh", f3="p4w:23", f4="p4w:2008/12/13", f5="p4w:$103,600")
    db.tdataXtable0.insert(f0="p4w:Jena Gaines", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:30", f4="p4w:2008/12/19", f5="p4w:$90,560")
    db.tdataXtable0.insert(f0="p4w:Quinn Flynn", f1="p4w:Support Lead", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2013/03/03", f5="p4w:$342,000")
    db.tdataXtable0.insert(f0="p4w:Charde Marshall", f1="p4w:Regional Director", f2="p4w:San Francisco", f3="p4w:36", f4="p4w:2008/10/16", f5="p4w:$470,600")
    db.tdataXtable0.insert(f0="p4w:Haley Kennedy", f1="p4w:Senior Marketing Designer", f2="p4w:London", f3="p4w:43", f4="p4w:2012/12/18", f5="p4w:$313,500")
    db.tdataXtable0.insert(f0="p4w:Tatyana Fitzpatrick", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:19", f4="p4w:2010/03/17", f5="p4w:$385,750")
    db.tdataXtable0.insert(f0="p4w:Michael Silva", f1="p4w:Marketing Designer", f2="p4w:London", f3="p4w:66", f4="p4w:2012/11/27", f5="p4w:$198,500")
    db.tdataXtable0.insert(f0="p4w:Paul Byrd", f1="p4w:Chief Financial Officer (CFO)", f2="p4w:New York", f3="p4w:64", f4="p4w:2010/06/09", f5="p4w:$725,000")
    db.tdataXtable0.insert(f0="p4w:Gloria Little", f1="p4w:Systems Administrator", f2="p4w:New York", f3="p4w:59", f4="p4w:2009/04/10", f5="p4w:$237,500")
    db.tdataXtable0.insert(f0="p4w:Bradley Greer", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:41", f4="p4w:2012/10/13", f5="p4w:$132,000")
    db.tdataXtable0.insert(f0="p4w:Dai Rios", f1="p4w:Personnel Lead", f2="p4w:Edinburgh", f3="p4w:35", f4="p4w:2012/09/26", f5="p4w:$217,500")
    db.tdataXtable0.insert(f0="p4w:Jenette Caldwell", f1="p4w:Development Lead", f2="p4w:New York", f3="p4w:30", f4="p4w:2011/09/03", f5="p4w:$345,000")
    db.tdataXtable0.insert(f0="p4w:Yuri Berry", f1="p4w:Chief Marketing Officer (CMO)", f2="p4w:New York", f3="p4w:40", f4="p4w:2009/06/25", f5="p4w:$675,000")
    db.tdataXtable0.insert(f0="p4w:Caesar Vance", f1="p4w:Pre-Sales Support", f2="p4w:New York", f3="p4w:21", f4="p4w:2011/12/12", f5="p4w:$106,450")
    db.tdataXtable0.insert(f0="p4w:Doris Wilder", f1="p4w:Sales Assistant", f2="p4w:Sidney", f3="p4w:23", f4="p4w:2010/09/20", f5="p4w:$85,600")
    db.tdataXtable0.insert(f0="p4w:Angelica Ramos", f1="p4w:Chief Executive Officer (CEO)", f2="p4w:London", f3="p4w:47", f4="p4w:2009/10/09", f5="p4w:$1,200,000")
    db.tdataXtable0.insert(f0="p4w:Gavin Joyce", f1="p4w:Developer", f2="p4w:Edinburgh", f3="p4w:42", f4="p4w:2010/12/22", f5="p4w:$92,575")
    db.tdataXtable0.insert(f0="p4w:Jennifer Chang", f1="p4w:Regional Director", f2="p4w:Singapore", f3="p4w:28", f4="p4w:2010/11/14", f5="p4w:$357,650")
    db.tdataXtable0.insert(f0="p4w:Brenden Wagner", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:28", f4="p4w:2011/06/07", f5="p4w:$206,850")
    db.tdataXtable0.insert(f0="p4w:Fiona Green", f1="p4w:Chief Operating Officer (COO)", f2="p4w:San Francisco", f3="p4w:48", f4="p4w:2010/03/11", f5="p4w:$850,000")
    db.tdataXtable0.insert(f0="p4w:Shou Itou", f1="p4w:Regional Marketing", f2="p4w:Tokyo", f3="p4w:20", f4="p4w:2011/08/14", f5="p4w:$163,000")
    db.tdataXtable0.insert(f0="p4w:Michelle House", f1="p4w:Integration Specialist", f2="p4w:Sidney", f3="p4w:37", f4="p4w:2011/06/02", f5="p4w:$95,400")
    db.tdataXtable0.insert(f0="p4w:Suki Burks", f1="p4w:Developer", f2="p4w:London", f3="p4w:53", f4="p4w:2009/10/22", f5="p4w:$114,500")
    db.tdataXtable0.insert(f0="p4w:Prescott Bartlett", f1="p4w:Technical Author", f2="p4w:London", f3="p4w:27", f4="p4w:2011/05/07", f5="p4w:$145,000")
    db.tdataXtable0.insert(f0="p4w:Gavin Cortez", f1="p4w:Team Leader", f2="p4w:San Francisco", f3="p4w:22", f4="p4w:2008/10/26", f5="p4w:$235,500")
    db.tdataXtable0.insert(f0="p4w:Martena Mccray", f1="p4w:Post-Sales support", f2="p4w:Edinburgh", f3="p4w:46", f4="p4w:2011/03/09", f5="p4w:$324,050")
    db.tdataXtable0.insert(f0="p4w:Unity Butler", f1="p4w:Marketing Designer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/12/09", f5="p4w:$85,675")
    db.tdataXtable0.insert(f0="p4w:Howard Hatfield", f1="p4w:Office Manager", f2="p4w:San Francisco", f3="p4w:51", f4="p4w:2008/12/16", f5="p4w:$164,500")
    db.tdataXtable0.insert(f0="p4w:Hope Fuentes", f1="p4w:Secretary", f2="p4w:San Francisco", f3="p4w:41", f4="p4w:2010/02/12", f5="p4w:$109,850")
    db.tdataXtable0.insert(f0="p4w:Vivian Harrell", f1="p4w:Financial Controller", f2="p4w:San Francisco", f3="p4w:62", f4="p4w:2009/02/14", f5="p4w:$452,500")
    db.tdataXtable0.insert(f0="p4w:Timothy Mooney", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:37", f4="p4w:2008/12/11", f5="p4w:$136,200")
    db.tdataXtable0.insert(f0="p4w:Jackson Bradshaw", f1="p4w:Director", f2="p4w:New York", f3="p4w:65", f4="p4w:2008/09/26", f5="p4w:$645,750")
    db.tdataXtable0.insert(f0="p4w:Olivia Liang", f1="p4w:Support Engineer", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2011/02/03", f5="p4w:$234,500")
    db.tdataXtable0.insert(f0="p4w:Bruno Nash", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:38", f4="p4w:2011/05/03", f5="p4w:$163,500")
    db.tdataXtable0.insert(f0="p4w:Sakura Yamamoto", f1="p4w:Support Engineer", f2="p4w:Tokyo", f3="p4w:37", f4="p4w:2009/08/19", f5="p4w:$139,575")
    db.tdataXtable0.insert(f0="p4w:Thor Walton", f1="p4w:Developer", f2="p4w:New York", f3="p4w:61", f4="p4w:2013/08/11", f5="p4w:$98,540")
    db.tdataXtable0.insert(f0="p4w:Finn Camacho", f1="p4w:Support Engineer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/07/07", f5="p4w:$87,500")
    db.tdataXtable0.insert(f0="p4w:Serge Baldwin", f1="p4w:Data Coordinator", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2012/04/09", f5="p4w:$138,575")
    db.tdataXtable0.insert(f0="p4w:Zenaida Frank", f1="p4w:Software Engineer", f2="p4w:New York", f3="p4w:63", f4="p4w:2010/01/04", f5="p4w:$125,250")
    db.tdataXtable0.insert(f0="p4w:Zorita Serrano", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:56", f4="p4w:2012/06/01", f5="p4w:$115,000")
    db.tdataXtable0.insert(f0="p4w:Jennifer Acosta", f1="p4w:Junior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:43", f4="p4w:2013/02/01", f5="p4w:$75,650")
    db.tdataXtable0.insert(f0="p4w:Cara Stevens", f1="p4w:Sales Assistant", f2="p4w:New York", f3="p4w:46", f4="p4w:2011/12/06", f5="p4w:$145,600")
    db.tdataXtable0.insert(f0="p4w:Hermione Butler", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:47", f4="p4w:2011/03/21", f5="p4w:$356,250")
    db.tdataXtable0.insert(f0="p4w:Lael Greer", f1="p4w:Systems Administrator", f2="p4w:London", f3="p4w:21", f4="p4w:2009/02/27", f5="p4w:$103,500")
    db.tdataXtable0.insert(f0="p4w:Jonas Alexander", f1="p4w:Developer", f2="p4w:San Francisco", f3="p4w:30", f4="p4w:2010/07/14", f5="p4w:$86,500")
    db.tdataXtable0.insert(f0="p4w:Shad Decker", f1="p4w:Regional Director", f2="p4w:Edinburgh", f3="p4w:51", f4="p4w:2008/11/13", f5="p4w:$183,000")
    db.tdataXtable0.insert(f0="p4w:Michael Bruce", f1="p4w:Javascript Developer", f2="p4w:Singapore", f3="p4w:29", f4="p4w:2011/06/27", f5="p4w:$183,000")
    db.tdataXtable0.insert(f0="p4w:Donna Snider", f1="p4w:Customer Support", f2="p4w:New York", f3="p4w:27", f4="p4w:2011/01/25", f5="p4w:$112,000")
    db.tdataXtable0.insert(f0="p4w:Name", f1="p4w:Position", f2="p4w:Office", f3="p4w:Age", f4="p4w:Start date", f5="p4w:Salary")
    db.commit()

if not db(db.tinvoice0).count():
    db.tinvoice0.insert(f0="p4w:#", f1="p4w:Item Title", f2="p4w:Unit Price", f3="p4w:Quantity", f4="p4w:Total")
    db.tinvoice0.insert(f0="p4w:1", f1="p4w:Crusal Damperal", f2="p4w:$500", f3="p4w:05", f4="p4w:$3000")
    db.tinvoice0.insert(f0="p4w:2", f1="p4w:Indriacal Superral", f2="p4w:$650", f3="p4w:06", f4="p4w:$7000")
    db.tinvoice0.insert(f0="p4w:3", f1="p4w:Vidaska Adrioal", f2="p4w:$400", f3="p4w:03", f4="p4w:$2000")
    db.tinvoice0.insert(f0="p4w:4", f1="p4w:Croustal Desrikal", f2="p4w:$600", f3="p4w:04", f4="p4w:$7000")
    db.commit()
