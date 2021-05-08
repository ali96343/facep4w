import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 06.05.2021 16:14:35 UTC+3, src: https://github.com/puikinsh/CoolAdmin


#import pydal
#from py4web import *
#from apps.myapp.models import db

if not db(db.auth_user).count():
    u1 = {
        "username": "anil",
        "email": "anil@nil.com",
        "password": str(CRYPT()("xyz12345")[0]),
        "first_name": "Anil_first",
        "last_name": "Anil_Last",
    }

    u2 = {
        "username": "bnil",
        "email": "bnil@nil.com",
        "password": str(CRYPT()("xyz12345")[0]),
        "first_name": "Bnil_first",
        "last_name": "Bnil_Last",
    }

    u3 = {
        "username": "cnil",
        "email": "cnil@nil.com",
        "password": str(CRYPT()("xyz12345")[0]),
        "first_name": "Cnil_first",
        "last_name": "Cnil_Last",
    }

    for e in [u1, u2, u3]: db.auth_user.insert(**db.auth_user._filter_fields(e) )
    db.commit()

    #groups = Tags(db.auth_user)

    groups.add(1, 'manager')
    groups.add(2, ['dancer', 'teacher'])
    groups.add(3, 'dancer')
    db.commit()

db.define_table(
    'test_table',
    Field( 'f0', 'string', label='l0'),
    Field( 'f1', 'string', label='l1'),
    Field( 'f2', 'string', label='l2'),
    )
db.commit()

if not db(db.test_table).count():
    populate(db.test_table, n=50)
    db.commit()

db.define_table( 'uploaded_files',
    Field('orig_file_name', requires=IS_NOT_EMPTY(),  ),
    Field("remark",'text',),
    Field('uniq_file_name', requires=IS_NOT_EMPTY(),  ),
    Field('time', 'datetime', editable=False, default = datetime.datetime.now(), requires = IS_DATETIME( )),
    )

db.commit()
#
db.define_table( 'app_images',
    Field('f0', requires=IS_NOT_EMPTY(),  ),
    )
    
if not db(db.app_images).count():
    db.app_images.insert(f0='images/icon/logo.png', )
    db.app_images.insert(f0='images/icon/avatar-06.jpg', )
    db.app_images.insert(f0='images/icon/avatar-04.jpg', )
    db.app_images.insert(f0='images/icon/avatar-05.jpg', )
    db.app_images.insert(f0='images/icon/avatar-01.jpg', )
    db.app_images.insert(f0='images/icon/avatar-02.jpg', )
    db.app_images.insert(f0='images/icon/avatar-03.jpg', )
    db.app_images.insert(f0='images/bg-title-01.jpg', )
    db.app_images.insert(f0='images/bg-title-02.jpg', )
    db.app_images.insert(f0='images/icon/logo-white.png', )
    db.app_images.insert(f0='images/icon/avatar-big-01.jpg', )
    db.app_images.insert(f0='images/icon/logo-blue.png', )

db.commit()

db.define_table( 'app_css_js',
    Field('f0', requires=IS_NOT_EMPTY(),  ),
    )

db.define_table( 'app_js_script',
    Field('f0', requires=IS_NOT_EMPTY(),  ),
    Field('in_html', ),
    )

db.define_table( 'app_html_text',
    Field('f0', requires=IS_NOT_EMPTY(), ),
    Field('key',requires=IS_NOT_EMPTY(), ),
    Field('in_html', ),
    )

db.commit()

db.define_table(
    'dfindex0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex20',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex30',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex40',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfindex41',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfchart0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftable0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform6',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','string', length=1024, ),
    Field('f9','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform7',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform8',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform9',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform10',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform11',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','string', length=1024, ),
    Field('f9','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform12',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','string', length=1024, ),
    Field('f9','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform13',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform14',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfform15',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcalendar0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmap0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfloginA0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfregisterA0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','boolean',  ),
    )
db.commit()

db.define_table(
    'dfforgetXpass0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbutton0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfbadge0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftab0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcard0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfalert0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfprogressXbar0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfmodal0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfswitch0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfgrid0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dffontawesome0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dftypo0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinbox0',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinbox1',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfinbox2',
    Field('f0','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex20',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex21',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex22',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex40',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttable1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttable2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttable3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttable4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    )
db.commit()

db.define_table(
    'ttable5',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tswitch0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="2018-09-29 05:57", f1="100398", f2="iPhone X 64Gb Grey", f3="$999.00", f4="1", f5="$999.00")
    db.tindex0.insert(f0="2018-09-28 01:22", f1="100397", f2="Samsung S8 Black", f3="$756.00", f4="1", f5="$756.00")
    db.tindex0.insert(f0="2018-09-27 02:12", f1="100396", f2="Game Console Controller", f3="$22.00", f4="2", f5="$44.00")
    db.tindex0.insert(f0="2018-09-26 23:06", f1="100395", f2="iPhone X 256Gb Black", f3="$1199.00", f4="1", f5="$1199.00")
    db.tindex0.insert(f0="2018-09-25 19:03", f1="100393", f2="USB 3.0 Cable", f3="$10.00", f4="3", f5="$30.00")
    db.tindex0.insert(f0="2018-09-29 05:57", f1="100392", f2="Smartwatch 4.0 LTE Wifi", f3="$199.00", f4="6", f5="$1494.00")
    db.tindex0.insert(f0="2018-09-24 19:10", f1="100391", f2="Camera C430W 4k", f3="$699.00", f4="1", f5="$699.00")
    db.tindex0.insert(f0="2018-09-22 00:43", f1="100393", f2="USB 3.0 Cable", f3="$10.00", f4="3", f5="$30.00")
    db.commit()

if not db(db.tindex1).count():
    db.tindex1.insert(f0="Australia", f1="$70,261.65")
    db.tindex1.insert(f0="United Kingdom", f1="$46,399.22")
    db.tindex1.insert(f0="Turkey", f1="$35,364.90")
    db.tindex1.insert(f0="Germany", f1="$20,366.96")
    db.tindex1.insert(f0="France", f1="$10,366.96")
    db.tindex1.insert(f0="Australia", f1="$5,366.96")
    db.tindex1.insert(f0="Italy", f1="$1639.32")
    db.commit()

if not db(db.tindex20).count():
    db.tindex20.insert(f0="<label class=\"au-checkbox\"><input type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="<div class=\"table-data__info\"><h6>lori lynch</h6><span><a href=\"#\">johndoe@gmail.com</a></span></div>", f2="<span class=\"role admin\">admin</span>", f3="<div class=\"rs-select2--trans rs-select2--sm\"><select class=\"js-select2\" name=\"property\"><option selected=\"selected\">Full Control</option><option value=\"\">Post</option><option value=\"\">Watch</option></select><div class=\"dropDownSelect2\"></div></div>", f4="<span class=\"more\"><i class=\"zmdi zmdi-more\"></i></span>")
    db.tindex20.insert(f0="<label class=\"au-checkbox\"><input checked=\"checked\" type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="<div class=\"table-data__info\"><h6>lori lynch</h6><span><a href=\"#\">johndoe@gmail.com</a></span></div>", f2="<span class=\"role user\">user</span>", f3="<div class=\"rs-select2--trans rs-select2--sm\"><select class=\"js-select2\" name=\"property\"><option value=\"\">Full Control</option><option selected=\"selected\" value=\"\">Post</option><option value=\"\">Watch</option></select><div class=\"dropDownSelect2\"></div></div>", f4="<span class=\"more\"><i class=\"zmdi zmdi-more\"></i></span>")
    db.tindex20.insert(f0="<label class=\"au-checkbox\"><input type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="<div class=\"table-data__info\"><h6>lori lynch</h6><span><a href=\"#\">johndoe@gmail.com</a></span></div>", f2="<span class=\"role user\">user</span>", f3="<div class=\"rs-select2--trans rs-select2--sm\"><select class=\"js-select2\" name=\"property\"><option value=\"\">Full Control</option><option selected=\"selected\" value=\"\">Post</option><option value=\"\">Watch</option></select><div class=\"dropDownSelect2\"></div></div>", f4="<span class=\"more\"><i class=\"zmdi zmdi-more\"></i></span>")
    db.tindex20.insert(f0="<label class=\"au-checkbox\"><input type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="<div class=\"table-data__info\"><h6>lori lynch</h6><span><a href=\"#\">johndoe@gmail.com</a></span></div>", f2="<span class=\"role member\">member</span>", f3="<div class=\"rs-select2--trans rs-select2--sm\"><select class=\"js-select2\" name=\"property\"><option selected=\"selected\">Full Control</option><option value=\"\">Post</option><option value=\"\">Watch</option></select><div class=\"dropDownSelect2\"></div></div>", f4="<span class=\"more\"><i class=\"zmdi zmdi-more\"></i></span>")
    db.commit()

if not db(db.tindex21).count():
    db.tindex21.insert(f0="Australia", f1="$70,261.65")
    db.tindex21.insert(f0="United Kingdom", f1="$46,399.22")
    db.commit()

if not db(db.tindex22).count():
    db.tindex22.insert(f0="France", f1="$10,366.96")
    db.tindex22.insert(f0="Russian", f1="$5,366.96")
    db.commit()

if not db(db.tindex40).count():
    db.tindex40.insert(f0="2018-09-29 05:57", f1="Mobile", f2="iPhone X 64Gb Grey", f3="Processed", f4="$999.00")
    db.tindex40.insert(f0="2018-09-28 01:22", f1="Mobile", f2="Samsung S8 Black", f3="Processed", f4="$756.00")
    db.tindex40.insert(f0="2018-09-27 02:12", f1="Game", f2="Game Console Controller", f3="Denied", f4="$22.00")
    db.tindex40.insert(f0="2018-09-26 23:06", f1="Mobile", f2="iPhone X 256Gb Black", f3="Denied", f4="$1199.00")
    db.tindex40.insert(f0="2018-09-25 19:03", f1="Accessories", f2="USB 3.0 Cable", f3="Processed", f4="$10.00")
    db.tindex40.insert(f0="2018-09-29 05:57", f1="Accesories", f2="Smartwatch 4.0 LTE Wifi", f3="Denied", f4="$199.00")
    db.tindex40.insert(f0="2018-09-24 19:10", f1="Camera", f2="Camera C430W 4k", f3="Processed", f4="$699.00")
    db.tindex40.insert(f0="2018-09-22 00:43", f1="Computer", f2="Macbook Pro Retina 2017", f3="Processed", f4="$10.00")
    db.commit()

if not db(db.ttable0).count():
    db.ttable0.insert(f0="2018-09-29 05:57", f1="100398", f2="iPhone X 64Gb Grey", f3="$999.00", f4="1", f5="$999.00")
    db.ttable0.insert(f0="2018-09-28 01:22", f1="100397", f2="Samsung S8 Black", f3="$756.00", f4="1", f5="$756.00")
    db.ttable0.insert(f0="2018-09-27 02:12", f1="100396", f2="Game Console Controller", f3="$22.00", f4="2", f5="$44.00")
    db.ttable0.insert(f0="2018-09-26 23:06", f1="100395", f2="iPhone X 256Gb Black", f3="$1199.00", f4="1", f5="$1199.00")
    db.ttable0.insert(f0="2018-09-25 19:03", f1="100393", f2="USB 3.0 Cable", f3="$10.00", f4="3", f5="$30.00")
    db.ttable0.insert(f0="2018-09-29 05:57", f1="100392", f2="Smartwatch 4.0 LTE Wifi", f3="$199.00", f4="6", f5="$1494.00")
    db.ttable0.insert(f0="2018-09-24 19:10", f1="100391", f2="Camera C430W 4k", f3="$699.00", f4="1", f5="$699.00")
    db.ttable0.insert(f0="2018-09-22 00:43", f1="100393", f2="USB 3.0 Cable", f3="$10.00", f4="3", f5="$30.00")
    db.commit()

if not db(db.ttable1).count():
    db.ttable1.insert(f0="Australia", f1="$70,261.65")
    db.ttable1.insert(f0="United Kingdom", f1="$46,399.22")
    db.ttable1.insert(f0="Turkey", f1="$35,364.90")
    db.ttable1.insert(f0="Germany", f1="$20,366.96")
    db.ttable1.insert(f0="France", f1="$10,366.96")
    db.ttable1.insert(f0="Australia", f1="$5,366.96")
    db.ttable1.insert(f0="Italy", f1="$1639.32")
    db.commit()

if not db(db.ttable2).count():
    db.ttable2.insert(f0="<label class=\"au-checkbox\"><input type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="<div class=\"table-data__info\"><h6> lori lynch </h6><span><a href=\"#\"> johndoe@gmail.com </a></span></div>", f2="<span class=\"role admin\"> admin </span>", f3="<div class=\"rs-select2--trans rs-select2--sm\"><select class=\"js-select2\" name=\"property\"><option selected=\"selected\"> Full Control </option><option value=\"\"> Post </option><option value=\"\"> Watch </option></select><div class=\"dropDownSelect2\"></div></div>", f4="<span class=\"more\"><i class=\"zmdi zmdi-more\"></i></span>")
    db.ttable2.insert(f0="<label class=\"au-checkbox\"><input checked=\"checked\" type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="<div class=\"table-data__info\"><h6> lori lynch </h6><span><a href=\"#\"> johndoe@gmail.com </a></span></div>", f2="<span class=\"role user\"> user </span>", f3="<div class=\"rs-select2--trans rs-select2--sm\"><select class=\"js-select2\" name=\"property\"><option value=\"\"> Full Control </option><option selected=\"selected\" value=\"\"> Post </option><option value=\"\"> Watch </option></select><div class=\"dropDownSelect2\"></div></div>", f4="<span class=\"more\"><i class=\"zmdi zmdi-more\"></i></span>")
    db.ttable2.insert(f0="<label class=\"au-checkbox\"><input type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="<div class=\"table-data__info\"><h6> lori lynch </h6><span><a href=\"#\"> johndoe@gmail.com </a></span></div>", f2="<span class=\"role user\"> user </span>", f3="<div class=\"rs-select2--trans rs-select2--sm\"><select class=\"js-select2\" name=\"property\"><option value=\"\"> Full Control </option><option selected=\"selected\" value=\"\"> Post </option><option value=\"\"> Watch </option></select><div class=\"dropDownSelect2\"></div></div>", f4="<span class=\"more\"><i class=\"zmdi zmdi-more\"></i></span>")
    db.ttable2.insert(f0="<label class=\"au-checkbox\"><input type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="<div class=\"table-data__info\"><h6> lori lynch </h6><span><a href=\"#\"> johndoe@gmail.com </a></span></div>", f2="<span class=\"role member\"> member </span>", f3="<div class=\"rs-select2--trans rs-select2--sm\"><select class=\"js-select2\" name=\"property\"><option selected=\"selected\"> Full Control </option><option value=\"\"> Post </option><option value=\"\"> Watch </option></select><div class=\"dropDownSelect2\"></div></div>", f4="<span class=\"more\"><i class=\"zmdi zmdi-more\"></i></span>")
    db.commit()

if not db(db.ttable3).count():
    db.ttable3.insert(f0="2. United Kingdom", f1="$46,399.22")
    db.ttable3.insert(f0="3. Turkey", f1="$35,364.90")
    db.ttable3.insert(f0="4. Germany", f1="$20,366.96")
    db.ttable3.insert(f0="5. France", f1="$10,366.96")
    db.ttable3.insert(f0="3. Turkey", f1="$35,364.90")
    db.ttable3.insert(f0="4. Germany", f1="$20,366.96")
    db.ttable3.insert(f0="5. France", f1="$10,366.96")
    db.ttable3.insert(f0="3. Turkey", f1="$35,364.90")
    db.ttable3.insert(f0="4. Germany", f1="$20,366.96")
    db.ttable3.insert(f0="5. France", f1="$10,366.96")
    db.ttable3.insert(f0="4. Germany", f1="$20,366.96")
    db.commit()

if not db(db.ttable4).count():
    db.ttable4.insert(f0="<label class=\"au-checkbox\"><input type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="Lori Lynch", f2="<span class=\"block-email\"> lori@example.com </span>", f3="Samsung S8 Black", f4="2018-09-27 02:12", f5="<span class=\"status--process\"> Processed </span>", f6="$679.00", f7="<div class=\"table-data-feature\"><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Send\"><i class=\"zmdi zmdi-mail-send\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Edit\"><i class=\"zmdi zmdi-edit\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Delete\"><i class=\"zmdi zmdi-delete\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"More\"><i class=\"zmdi zmdi-more\"></i></button></div>")
    db.ttable4.insert()
    db.ttable4.insert(f0="<label class=\"au-checkbox\"><input type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="Lori Lynch", f2="<span class=\"block-email\"> john@example.com </span>", f3="iPhone X 64Gb Grey", f4="2018-09-29 05:57", f5="<span class=\"status--process\"> Processed </span>", f6="$999.00", f7="<div class=\"table-data-feature\"><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Send\"><i class=\"zmdi zmdi-mail-send\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Edit\"><i class=\"zmdi zmdi-edit\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Delete\"><i class=\"zmdi zmdi-delete\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"More\"><i class=\"zmdi zmdi-more\"></i></button></div>")
    db.ttable4.insert()
    db.ttable4.insert(f0="<label class=\"au-checkbox\"><input type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="Lori Lynch", f2="<span class=\"block-email\"> lyn@example.com </span>", f3="iPhone X 256Gb Black", f4="2018-09-25 19:03", f5="<span class=\"status--denied\"> Denied </span>", f6="$1199.00", f7="<div class=\"table-data-feature\"><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Send\"><i class=\"zmdi zmdi-mail-send\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Edit\"><i class=\"zmdi zmdi-edit\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Delete\"><i class=\"zmdi zmdi-delete\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"More\"><i class=\"zmdi zmdi-more\"></i></button></div>")
    db.ttable4.insert()
    db.ttable4.insert(f0="<label class=\"au-checkbox\"><input type=\"checkbox\"/><span class=\"au-checkmark\"></span></label>", f1="Lori Lynch", f2="<span class=\"block-email\"> doe@example.com </span>", f3="Camera C430W 4k", f4="2018-09-24 19:10", f5="<span class=\"status--process\"> Processed </span>", f6="$699.00", f7="<div class=\"table-data-feature\"><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Send\"><i class=\"zmdi zmdi-mail-send\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Edit\"><i class=\"zmdi zmdi-edit\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"Delete\"><i class=\"zmdi zmdi-delete\"></i></button><button class=\"item\" data-placement=\"top\" data-toggle=\"tooltip\" title=\"More\"><i class=\"zmdi zmdi-more\"></i></button></div>")
    db.commit()

if not db(db.ttable5).count():
    db.ttable5.insert(f0="2018-09-29 05:57", f1="Mobile", f2="iPhone X 64Gb Grey", f3="Processed", f4="$999.00")
    db.ttable5.insert(f0="2018-09-28 01:22", f1="Mobile", f2="Samsung S8 Black", f3="Processed", f4="$756.00")
    db.ttable5.insert(f0="2018-09-27 02:12", f1="Game", f2="Game Console Controller", f3="Denied", f4="$22.00")
    db.ttable5.insert(f0="2018-09-26 23:06", f1="Mobile", f2="iPhone X 256Gb Black", f3="Denied", f4="$1199.00")
    db.ttable5.insert(f0="2018-09-25 19:03", f1="Accessories", f2="USB 3.0 Cable", f3="Processed", f4="$10.00")
    db.ttable5.insert(f0="2018-09-29 05:57", f1="Accesories", f2="Smartwatch 4.0 LTE Wifi", f3="Denied", f4="$199.00")
    db.ttable5.insert(f0="2018-09-24 19:10", f1="Camera", f2="Camera C430W 4k", f3="Processed", f4="$699.00")
    db.ttable5.insert(f0="2018-09-22 00:43", f1="Computer", f2="Macbook Pro Retina 2017", f3="Processed", f4="$10.00")
    db.commit()

if not db(db.tswitch0).count():
    db.tswitch0.insert(f0="Default", f1="basix-switch", f2="==0")
    db.tswitch0.insert(f0="Small", f1="basix-switch", f2="<code>size=\"sm\"</code>")
    db.tswitch0.insert(f0="Extra small", f1="basix-switch", f2="<code>size=\"xs\"</code>")
    db.commit()
