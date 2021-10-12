import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 12.10.2021 09:05:10 UTC+3, src: https://github.com/adminkit/adminkit

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
    db.app_images.insert(f0='img/icons/icon-48x48.png', )
    db.app_images.insert(f0='img/avatars/avatar-5.jpg', )
    db.app_images.insert(f0='img/avatars/avatar-2.jpg', )
    db.app_images.insert(f0='img/avatars/avatar-4.jpg', )
    db.app_images.insert(f0='img/avatars/avatar-3.jpg', )
    db.app_images.insert(f0='img/avatars/avatar.jpg', )
    db.app_images.insert(f0='img/photos/unsplash-1.jpg', )
    db.app_images.insert(f0='img/photos/unsplash-2.jpg', )

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
    'dfpagesXsignXin0',
    Field('f0','string', length=1024, default='fNo' ),
    Field('f1','string', length=1024, default='fNo' ),
    Field('f2','boolean', False ),
    )
db.commit()

db.define_table(
    'dfpagesXsignXup0',
    Field('f0','string', length=1024, default='fNo' ),
    Field('f1','string', length=1024, default='fNo' ),
    Field('f2','string', length=1024, default='fNo' ),
    Field('f3','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'tindex0',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    )
db.commit()

db.define_table(
    'tindex1',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    Field('f2','string', length=1024, default='tNo' ),
    Field('f3','string', length=1024, default='tNo' ),
    Field('f4','string', length=1024, default='tNo' ),
    )
db.commit()

db.define_table(
    'tupgradeXtoXpro0',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    Field('f2','string', length=1024, default='tNo' ),
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="Firefox", f1="3801")
    db.tindex0.insert(f0="IE", f1="1689")
    db.commit()

if not db(db.tindex1).count():
    db.tindex1.insert(f0="Project Apollo", f1="01/01/2021", f2="31/06/2021", f3="<span class=\"badge bg-success\">Done</span>", f4="Vanessa Tucker")
    db.tindex1.insert(f0="Project Fireball", f1="01/01/2021", f2="31/06/2021", f3="<span class=\"badge bg-danger\">Cancelled</span>", f4="William Harris")
    db.tindex1.insert(f0="Project Hades", f1="01/01/2021", f2="31/06/2021", f3="<span class=\"badge bg-success\">Done</span>", f4="Sharon Lessman")
    db.tindex1.insert(f0="Project Nitro", f1="01/01/2021", f2="31/06/2021", f3="<span class=\"badge bg-warning\">In progress</span>", f4="Vanessa Tucker")
    db.tindex1.insert(f0="Project Phoenix", f1="01/01/2021", f2="31/06/2021", f3="<span class=\"badge bg-success\">Done</span>", f4="William Harris")
    db.tindex1.insert(f0="Project X", f1="01/01/2021", f2="31/06/2021", f3="<span class=\"badge bg-success\">Done</span>", f4="Sharon Lessman")
    db.tindex1.insert(f0="Project Romeo", f1="01/01/2021", f2="31/06/2021", f3="<span class=\"badge bg-success\">Done</span>", f4="Christina Mason")
    db.tindex1.insert(f0="Project Wombat", f1="01/01/2021", f2="31/06/2021", f3="<span class=\"badge bg-warning\">In progress</span>", f4="William Harris")
    db.commit()

if not db(db.tupgradeXtoXpro0).count():
    db.tupgradeXtoXpro0.insert(f0="==0", f1="<a class=\"btn btn-light\" href=\"https://adminkit.io/\" target=\"_blank\">Download</a>", f2="<a class=\"btn btn-primary\" href=\"https://adminkit.io/pricing\" target=\"_blank\">Upgrade to Pro</a>")
    db.tupgradeXtoXpro0.insert(f0="Demo Pages", f1="15", f2="<strong>45+</strong>")
    db.tupgradeXtoXpro0.insert(f0="Plugins", f1="1", f2="<strong>10+</strong>")
    db.tupgradeXtoXpro0.insert(f0="Color Schemes", f1="1", f2="<strong>3</strong>")
    db.tupgradeXtoXpro0.insert(f0="All Bootstrap 5 Components", f1="<span aria-label=\"no\" role=\"img\"></span>", f2="<span aria-label=\"yes\" role=\"img\"></span>")
    db.tupgradeXtoXpro0.insert(f0="Dark Mode", f1="<span aria-label=\"no\" role=\"img\"></span>", f2="<span aria-label=\"yes\" role=\"img\"></span>")
    db.tupgradeXtoXpro0.insert(f0="Compact Sidebar", f1="<span aria-label=\"no\" role=\"img\"></span>", f2="<span aria-label=\"yes\" role=\"img\"></span>")
    db.tupgradeXtoXpro0.insert(f0="Calendar", f1="<span aria-label=\"no\" role=\"img\"></span>", f2="<span aria-label=\"yes\" role=\"img\"></span>")
    db.tupgradeXtoXpro0.insert(f0="Advanced Forms", f1="<span aria-label=\"no\" role=\"img\"></span>", f2="<span aria-label=\"yes\" role=\"img\"></span>")
    db.tupgradeXtoXpro0.insert(f0="Drag and Drop", f1="<span aria-label=\"no\" role=\"img\"></span>", f2="<span aria-label=\"yes\" role=\"img\"></span>")
    db.tupgradeXtoXpro0.insert(f0="Toast Notifications", f1="<span aria-label=\"no\" role=\"img\"></span>", f2="<span aria-label=\"yes\" role=\"img\"></span>")
    db.tupgradeXtoXpro0.insert(f0="WYSIWYG Editors", f1="<span aria-label=\"no\" role=\"img\"></span>", f2="<span aria-label=\"yes\" role=\"img\"></span>")
    db.tupgradeXtoXpro0.insert(f0="Premium Support", f1="<span aria-label=\"no\" role=\"img\"></span>", f2="<span aria-label=\"yes\" role=\"img\"></span>")
    db.tupgradeXtoXpro0.insert(f0="==0", f1="Free", f2="Starting from $59")
    db.tupgradeXtoXpro0.insert(f0="==0", f1="<a class=\"btn btn-light\" href=\"https://adminkit.io/\" target=\"_blank\">Download</a>", f2="<a class=\"btn btn-primary\" href=\"https://adminkit.io/pricing\" target=\"_blank\">Upgrade to Pro</a>")
    db.commit()
