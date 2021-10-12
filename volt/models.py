import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 12.10.2021 08:12:54 UTC+3, src: https://github.com/themesberg/volt-bootstrap-5-dashboard


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
    db.app_images.insert(f0='assets/img/favicon/apple-touch-icon.png', )
    db.app_images.insert(f0='assets/img/favicon/favicon-32x32.png', )
    db.app_images.insert(f0='assets/img/favicon/favicon-16x16.png', )
    db.app_images.insert(f0='assets/img/favicon/safari-pinned-tab.svg', )
    db.app_images.insert(f0='assets/img/brand/light.svg', )
    db.app_images.insert(f0='assets/img/themesberg.svg', )
    db.app_images.insert(f0='assets/img/mockup-presentation.png', )
    db.app_images.insert(f0='assets/img/illustrations/bs5-illustrations.svg', )
    db.app_images.insert(f0='assets/img/mockup-kanban-presentation.png', )
    db.app_images.insert(f0='assets/img/mockup-map-presentation.png', )
    db.app_images.insert(f0='assets/img/mockup-calendar-presentation.png', )
    db.app_images.insert(f0='assets/img/pages/overview.jpg', )
    db.app_images.insert(f0='assets/img/pages/transactions.jpg', )
    db.app_images.insert(f0='assets/img/pages/settings.jpg', )
    db.app_images.insert(f0='assets/img/pages/sign-in.jpg', )
    db.app_images.insert(f0='assets/img/pages/sign-up.jpg', )
    db.app_images.insert(f0='assets/img/pages/lock.jpg', )
    db.app_images.insert(f0='assets/img/pages/forgot-password.jpg', )
    db.app_images.insert(f0='assets/img/pages/reset-password.jpg', )
    db.app_images.insert(f0='assets/img/pages/404.jpg', )
    db.app_images.insert(f0='assets/img/pages/500.jpg', )
    db.app_images.insert(f0='assets/img/technologies/bootstrap-5-logo.svg', )
    db.app_images.insert(f0='assets/img/technologies/react-logo.svg', )
    db.app_images.insert(f0='assets/img/themesberg-logo-alt.svg', )
    db.app_images.insert(f0='assets/img/brand/dark.svg', )
    db.app_images.insert(f0='assets/img/team/profile-picture-3.jpg', )
    db.app_images.insert(f0='assets/img/team/profile-picture-1.jpg', )
    db.app_images.insert(f0='assets/img/team/profile-picture-2.jpg', )
    db.app_images.insert(f0='assets/img/team/profile-picture-4.jpg', )
    db.app_images.insert(f0='assets/img/team/profile-picture-5.jpg', )
    db.app_images.insert(f0='assets/img/illustrations/signin.svg', )
    db.app_images.insert(f0='assets/img/profile-cover.jpg', )
    db.app_images.insert(f0='assets/img/illustrations/404.svg', )
    db.app_images.insert(f0='assets/img/illustrations/500.svg', )
    db.app_images.insert(f0='assets/img/flags/united-states-of-america.svg', )
    db.app_images.insert(f0='assets/img/flags/canada.svg', )
    db.app_images.insert(f0='assets/img/flags/united-kingdom.svg', )
    db.app_images.insert(f0='assets/img/flags/france.svg', )
    db.app_images.insert(f0='assets/img/flags/japan.svg', )
    db.app_images.insert(f0='assets/img/flags/germany.svg', )

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
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfdashboard0',
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfsignXin0',
    Field('f0','string', length=1024, default='fNo' ),
    Field('f1','string', length=1024, default='fNo' ),
    Field('f2','boolean', False ),
    )
db.commit()

db.define_table(
    'dfsignXup0',
    Field('f0','string', length=1024, default='fNo' ),
    Field('f1','string', length=1024, default='fNo' ),
    Field('f2','string', length=1024, default='fNo' ),
    Field('f3','boolean', False ),
    )
db.commit()

db.define_table(
    'dflock0',
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dftransactions0',
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfsettings0',
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfsettings1',
    Field('f0','string', length=1024, default='fNo' ),
    Field('f1','string', length=1024, default='fNo' ),
    Field('f2','string', length=1024, default='fNo' ),
    Field('f3','string', length=1024, default='fNo' ),
    Field('f4','string', length=1024, default='fNo' ),
    Field('f5','string', length=1024, default='fNo' ),
    Field('f6','string', length=1024, default='fNo' ),
    Field('f7','string', length=1024, default='fNo' ),
    Field('f8','string', length=1024, default='fNo' ),
    Field('f9','string', length=1024, default='fNo' ),
    Field('f10','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfforgotXpassword0',
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfresetXpassword0',
    Field('f0','string', length=1024, default='fNo' ),
    Field('f1','string', length=1024, default='fNo' ),
    Field('f2','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfbootstrapXtables0',
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfbuttons0',
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfnotifications0',
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfforms0',
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfmodals0',
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfmodals1',
    Field('f0','string', length=1024, default='fNo' ),
    Field('f1','string', length=1024, default='fNo' ),
    Field('f2','boolean', False ),
    )
db.commit()

db.define_table(
    'dfmodals2',
    Field('f0','string', length=1024, default='fNo' ),
    Field('f1','string', length=1024, default='fNo' ),
    Field('f2','string', length=1024, default='fNo' ),
    Field('f3','boolean', False ),
    )
db.commit()

db.define_table(
    'dftypography0',
    Field('f0','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'tdashboard0',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    Field('f2','string', length=1024, default='tNo' ),
    Field('f3','string', length=1024, default='tNo' ),
    )
db.commit()

db.define_table(
    'tupgradeXtoXpro0',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    Field('f2','string', length=1024, default='tNo' ),
    )
db.commit()

db.define_table(
    'ttransactions0',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    Field('f2','string', length=1024, default='tNo' ),
    Field('f3','string', length=1024, default='tNo' ),
    Field('f4','string', length=1024, default='tNo' ),
    Field('f5','string', length=1024, default='tNo' ),
    Field('f6','string', length=1024, default='tNo' ),
    )
db.commit()

db.define_table(
    'tbootstrapXtables0',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    Field('f2','string', length=1024, default='tNo' ),
    Field('f3','string', length=1024, default='tNo' ),
    Field('f4','string', length=1024, default='tNo' ),
    Field('f5','string', length=1024, default='tNo' ),
    Field('f6','string', length=1024, default='tNo' ),
    )
db.commit()

db.define_table(
    'tbootstrapXtables1',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    Field('f2','string', length=1024, default='tNo' ),
    Field('f3','string', length=1024, default='tNo' ),
    Field('f4','string', length=1024, default='tNo' ),
    Field('f5','string', length=1024, default='tNo' ),
    Field('f6','string', length=1024, default='tNo' ),
    )
db.commit()

if not db(db.tdashboard0).count():
    db.tdashboard0.insert(f0="/demo/admin/index.html", f1="3,225", f2="$20", f3="<div class=\"d-flex\"><svg class=\"icon icon-xs text-danger me-2\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z\" fill-rule=\"evenodd\"></path></svg> 42,55% </div>")
    db.tdashboard0.insert(f0="/demo/admin/forms.html", f1="2,987", f2="0", f3="<div class=\"d-flex\"><svg class=\"icon icon-xs text-success me-2\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l2.293-2.293a1 1 0 011.414 0z\" fill-rule=\"evenodd\"></path></svg> 43,24% </div>")
    db.tdashboard0.insert(f0="/demo/admin/util.html", f1="2,844", f2="294", f3="<div class=\"d-flex\"><svg class=\"icon icon-xs text-success me-2\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l2.293-2.293a1 1 0 011.414 0z\" fill-rule=\"evenodd\"></path></svg> 32,35% </div>")
    db.tdashboard0.insert(f0="/demo/admin/validation.html", f1="2,050", f2="$147", f3="<div class=\"d-flex\"><svg class=\"icon icon-xs text-danger me-2\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z\" fill-rule=\"evenodd\"></path></svg> 50,87% </div>")
    db.tdashboard0.insert(f0="/demo/admin/modals.html", f1="1,483", f2="$19", f3="<div class=\"d-flex\"><svg class=\"icon icon-xs text-success me-2\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l2.293-2.293a1 1 0 011.414 0z\" fill-rule=\"evenodd\"></path></svg> 26,12% </div>")
    db.commit()

if not db(db.tupgradeXtoXpro0).count():
    db.tupgradeXtoXpro0.insert(f0="Elements", f1="100 BS5 components", f2="800+ BS5 components")
    db.tupgradeXtoXpro0.insert(f0="Plugins", f1="3 plugins", f2="10 plugins")
    db.tupgradeXtoXpro0.insert(f0="Examples Pages", f1="11 pages", f2="21 pages")
    db.tupgradeXtoXpro0.insert(f0="Advanced charts", f1="<svg class=\"icon icon-xs text-danger\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z\" fill-rule=\"evenodd\"></path></svg>", f2="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>")
    db.tupgradeXtoXpro0.insert(f0="Toggleable sidebar (icons only)", f1="<svg class=\"icon icon-xs text-danger\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z\" fill-rule=\"evenodd\"></path></svg>", f2="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>")
    db.tupgradeXtoXpro0.insert(f0="Kanban Drag & Drop Board", f1="<svg class=\"icon icon-xs text-danger\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z\" fill-rule=\"evenodd\"></path></svg>", f2="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>")
    db.tupgradeXtoXpro0.insert(f0="Kanban Board", f1="<svg class=\"icon icon-xs text-danger\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z\" fill-rule=\"evenodd\"></path></svg>", f2="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>")
    db.tupgradeXtoXpro0.insert(f0="Full Calendar", f1="<svg class=\"icon icon-xs text-danger\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z\" fill-rule=\"evenodd\"></path></svg>", f2="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>")
    db.tupgradeXtoXpro0.insert(f0="MapBox", f1="<svg class=\"icon icon-xs text-danger\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z\" fill-rule=\"evenodd\"></path></svg>", f2="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>")
    db.tupgradeXtoXpro0.insert(f0="SASS Files", f1="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>", f2="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>")
    db.tupgradeXtoXpro0.insert(f0="Documentation", f1="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>", f2="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>")
    db.tupgradeXtoXpro0.insert(f0="6 Months Premium Support", f1="<svg class=\"icon icon-xs text-danger\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z\" fill-rule=\"evenodd\"></path></svg>", f2="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>")
    db.tupgradeXtoXpro0.insert(f0="Free updates", f1="<svg class=\"icon icon-xs text-danger\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z\" fill-rule=\"evenodd\"></path></svg>", f2="<svg class=\"icon icon-xs text-success\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" fill-rule=\"evenodd\"></path></svg>")
    db.tupgradeXtoXpro0.insert(f0="==0", f1="<a class=\"btn btn-gray-800 d-inline-flex align-items-center\" href=\"https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard\" target=\"_blank\"><svg class=\"icon icon-xs me-2\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M2 9.5A3.5 3.5 0 005.5 13H9v2.586l-1.293-1.293a1 1 0 00-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 15.586V13h2.5a4.5 4.5 0 10-.616-8.958 4.002 4.002 0 10-7.753 1.977A3.5 3.5 0 002 9.5zm9 3.5H9V8a1 1 0 012 0v5z\" fill-rule=\"evenodd\"></path></svg> Download </a>", f2="<a class=\"btn btn-secondary d-inline-flex align-items-center justify-content-center\" href=\"https://demo.themesberg.com/volt-pro/pages/dashboard/dashboard.html\" target=\"_blank\"> Live Demo PRO <svg class=\"icon icon-xs ms-2\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M11 3a1 1 0 100 2h2.586l-6.293 6.293a1 1 0 101.414 1.414L15 6.414V9a1 1 0 102 0V4a1 1 0 00-1-1h-5z\"></path><path d=\"M5 5a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2v-3a1 1 0 10-2 0v3H5V7h3a1 1 0 000-2H5z\"></path></svg></a> <a class=\"btn btn-outline-gray-800 d-inline-flex align-items-center ms-3\" href=\"https://themesberg.com/product/admin-dashboard/volt-premium-bootstrap-5-dashboard\" target=\"_blank\"><svg class=\"icon icon-xs me-2\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3...")
    db.commit()

if not db(db.ttransactions0).count():
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456478 </a>", f1="<span class=\"fw-normal\"> Platinum Subscription Plan </span>", f2="<span class=\"fw-normal\"> 1 May 2020 </span>", f3="<span class=\"fw-normal\"> 1 Jun 2020 </span>", f4="<span class=\"fw-bold\"> $799,00 </span>", f5="<span class=\"fw-bold text-warning\"> Due </span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"visually-hidden\"> Toggle Dropdown </span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span> View Details </a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span> Edit </a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span> Remove </a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456423 </a>", f1="<span class=\"fw-normal\"> Platinum Subscription Plan </span>", f2="<span class=\"fw-normal\"> 1 Apr 2020 </span>", f3="<span class=\"fw-normal\"> 1 May 2020 </span>", f4="<span class=\"fw-bold\"> $799,00 </span>", f5="<span class=\"fw-bold text-success\"> Paid </span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"visually-hidden\"> Toggle Dropdown </span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span> View Details </a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span> Edit </a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span> Remove </a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456420 </a>", f1="<span class=\"fw-normal\"> Platinum Subscription Plan </span>", f2="<span class=\"fw-normal\"> 1 Mar 2020 </span>", f3="<span class=\"fw-normal\"> 1 Apr 2020 </span>", f4="<span class=\"fw-bold\"> $799,00 </span>", f5="<span class=\"fw-bold text-success\"> Paid </span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"visually-hidden\"> Toggle Dropdown </span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span> View Details </a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span> Edit </a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span> Remove </a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456421 </a>", f1="<span class=\"fw-normal\"> Platinum Subscription Plan </span>", f2="<span class=\"fw-normal\"> 1 Feb 2020 </span>", f3="<span class=\"fw-normal\"> 1 Mar 2020 </span>", f4="<span class=\"fw-bold\"> $799,00 </span>", f5="<span class=\"fw-bold text-success\"> Paid </span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"visually-hidden\"> Toggle Dropdown </span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span> View Details </a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span> Edit </a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span> Remove </a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456420 </a>", f1="<span class=\"fw-normal\"> Platinum Subscription Plan </span>", f2="<span class=\"fw-normal\"> 1 Jan 2020 </span>", f3="<span class=\"fw-normal\"> 1 Feb 2020 </span>", f4="<span class=\"fw-bold\"> $799,00 </span>", f5="<span class=\"fw-bold text-success\"> Paid </span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"visually-hidden\"> Toggle Dropdown </span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span> View Details </a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span> Edit </a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span> Remove </a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456479 </a>", f1="<span class=\"fw-normal\"> Platinum Subscription Plan </span>", f2="<span class=\"fw-normal\"> 1 Dec 2019 </span>", f3="<span class=\"fw-normal\"> 1 Jan 2020 </span>", f4="<span class=\"fw-bold\"> $799,00 </span>", f5="<span class=\"fw-bold text-success\"> Paid </span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"visually-hidden\"> Toggle Dropdown </span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span> View Details </a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span> Edit </a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span> Remove </a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456478 </a>", f1="<span class=\"fw-normal\"> Platinum Subscription Plan </span>", f2="<span class=\"fw-normal\"> 1 Nov 2019 </span>", f3="<span class=\"fw-normal\"> 1 Dec 2019 </span>", f4="<span class=\"fw-bold\"> $799,00 </span>", f5="<span class=\"fw-bold text-success\"> Paid </span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"visually-hidden\"> Toggle Dropdown </span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span> View Details </a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span> Edit </a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span> Remove </a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 453673 </a>", f1="<span class=\"fw-normal\"> Gold Subscription Plan </span>", f2="<span class=\"fw-normal\"> 1 Oct 2019 </span>", f3="<span class=\"fw-normal\"> 1 Nov 2019 </span>", f4="<span class=\"fw-bold\"> $533,42 </span>", f5="<span class=\"fw-bold text-danger\"> Cancelled </span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"visually-hidden\"> Toggle Dropdown </span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span> View Details </a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span> Edit </a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span> Remove </a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456468 </a>", f1="<span class=\"fw-normal\"> Gold Subscription Plan </span>", f2="<span class=\"fw-normal\"> 1 Sep 2019 </span>", f3="<span class=\"fw-normal\"> 1 Oct 2019 </span>", f4="<span class=\"fw-bold\"> $533,42 </span>", f5="<span class=\"fw-bold text-success\"> Paid </span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"visually-hidden\"> Toggle Dropdown </span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span> View Details </a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span> Edit </a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span> Remove </a></div></div>")
    db.ttransactions0.insert(f0="<a class=\"fw-bold\" href=\"#\"> 456478 </a>", f1="<span class=\"fw-normal\"> Flexible Subscription Plan </span>", f2="<span class=\"fw-normal\"> 1 Aug 2019 </span>", f3="<span class=\"fw-normal\"> 1 Sep 2019 </span>", f4="<span class=\"fw-bold\"> $233,42 </span>", f5="<span class=\"fw-bold text-success\"> Paid </span>", f6="<div class=\"btn-group\"><button aria-expanded=\"false\" aria-haspopup=\"true\" class=\"btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0\" data-bs-toggle=\"dropdown\"><span class=\"icon icon-sm\"><span class=\"fas fa-ellipsis-h icon-dark\"></span></span><span class=\"visually-hidden\"> Toggle Dropdown </span></button><div class=\"dropdown-menu py-0\"><a class=\"dropdown-item rounded-top\" href=\"#\"><span class=\"fas fa-eye me-2\"></span> View Details </a><a class=\"dropdown-item\" href=\"#\"><span class=\"fas fa-edit me-2\"></span> Edit </a><a class=\"dropdown-item text-danger rounded-bottom\" href=\"#\"><span class=\"fas fa-trash-alt me-2\"></span> Remove </a></div></div>")
    db.commit()

if not db(db.tbootstrapXtables0).count():
    db.tbootstrapXtables0.insert(f0="<a class=\"text-primary fw-bold\" href=\"#\"> 1 </a>", f1="<svg class=\"icon icon-xxs text-gray-500 me-2\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zM4.332 8.027a6.012 6.012 0 011.912-2.706C6.512 5.73 6.974 6 7.5 6A1.5 1.5 0 019 7.5V8a2 2 0 004 0 2 2 0 011.523-1.943A5.977 5.977 0 0116 10c0 .34-.028.675-.083 1H15a2 2 0 00-2 2v2.197A5.973 5.973 0 0110 16v-2a2 2 0 00-2-2 2 2 0 01-2-2 2 2 0 00-1.668-1.973z\" fill-rule=\"evenodd\"></path></svg>", f2="Direct", f3="-", f4="--", f5="<div class=\"row d-flex align-items-center\"><div class=\"col-12 col-xl-2 px-0\"><div class=\"small fw-bold\"> 51% </div></div><div class=\"col-12 col-xl-10 px-0 px-xl-1\"><div class=\"progress progress-lg mb-0\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"51\" class=\"progress-bar bg-dark\" role=\"progressbar\" style=\"width: 51%;\"></div></div></div></div>", f6="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 2.45% </span></div>")
    db.tbootstrapXtables0.insert(f0="<a class=\"text-primary fw-bold\" href=\"#\"> 2 </a>", f1="<svg aria-hidden=\"true\" class=\"icon icon-xxs text-gray-500 me-2\" data-icon=\"google\" data-prefix=\"fab\" focusable=\"false\" role=\"img\" viewbox=\"0 0 488 512\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M488 261.8C488 403.3 391.1 504 248 504 110.8 504 0 393.2 0 256S110.8 8 248 8c66.8 0 123 24.5 166.3 64.9l-67.5 64.9C258.5 52.6 94.3 116.6 94.3 256c0 86.5 69.1 156.6 153.7 156.6 98.2 0 135-70.4 140.8-106.9H248v-85.3h236.1c2.3 12.7 3.9 24.9 3.9 41.4z\" fill=\"currentColor\"></path></svg>", f2="Search / Organic", f3="-", f4="--", f5="<div class=\"row d-flex align-items-center\"><div class=\"col-12 col-xl-2 px-0\"><div class=\"small fw-bold\"> 18% </div></div><div class=\"col-12 col-xl-10 px-0 px-xl-1\"><div class=\"progress progress-lg mb-0\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"18\" class=\"progress-bar bg-dark\" role=\"progressbar\" style=\"width: 18%;\"></div></div></div></div>", f6="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 17.78% </span></div>")
    db.tbootstrapXtables0.insert(f0="<a class=\"text-primary fw-bold\" href=\"#\"> 3 </a>", f1="<svg aria-hidden=\"true\" class=\"icon icon-xxs text-gray-500 me-2\" data-icon=\"youtube\" data-prefix=\"fab\" focusable=\"false\" role=\"img\" viewbox=\"0 0 576 512\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z\" fill=\"currentColor\"></path></svg>", f2="Social", f3="<a class=\"small fw-bold\" href=\"#\"> Arts and Entertainment </a>", f4="#2", f5="<div class=\"row d-flex align-items-center\"><div class=\"col-12 col-xl-2 px-0\"><div class=\"small fw-bold\"> 18% </div></div><div class=\"col-12 col-xl-10 px-0 px-xl-1\"><div class=\"progress progress-lg mb-0\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"18\" class=\"progress-bar bg-dark\" role=\"progressbar\" style=\"width: 18%;\"></div></div></div></div>", f6="-")
    db.tbootstrapXtables0.insert(f0="<a class=\"text-primary fw-bold\" href=\"#\"> 4 </a>", f1="<svg aria-hidden=\"true\" class=\"icon icon-xxs text-gray-500 me-2\" data-icon=\"yahoo\" data-prefix=\"fab\" focusable=\"false\" role=\"img\" viewbox=\"0 0 512 512\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M223.69,141.06,167,284.23,111,141.06H14.93L120.76,390.19,82.19,480h94.17L317.27,141.06Zm105.4,135.79a58.22,58.22,0,1,0,58.22,58.22A58.22,58.22,0,0,0,329.09,276.85ZM394.65,32l-93,223.47H406.44L499.07,32Z\" fill=\"currentColor\"></path></svg>", f2="Referral", f3="<a class=\"small fw-bold\" href=\"#\"> News and Media </a>", f4="#11", f5="<div class=\"row d-flex align-items-center\"><div class=\"col-12 col-xl-2 px-0\"><div class=\"small fw-bold\"> 8% </div></div><div class=\"col-12 col-xl-10 px-0 px-xl-1\"><div class=\"progress progress-lg mb-0\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"8\" class=\"progress-bar bg-dark\" role=\"progressbar\" style=\"width: 8%;\"></div></div></div></div>", f6="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 9.45% </span></div>")
    db.tbootstrapXtables0.insert(f0="<a class=\"text-primary fw-bold\" href=\"#\"> 5 </a>", f1="<svg aria-hidden=\"true\" class=\"icon icon-xxs text-gray-500 me-2\" data-icon=\"twitter\" data-prefix=\"fab\" focusable=\"false\" role=\"img\" viewbox=\"0 0 512 512\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z\" fill=\"currentColor\"></pat...", f2="Social", f3="<a class=\"small fw-bold\" href=\"#\"> Social Networks </a>", f4="#4", f5="<div class=\"row d-flex align-items-center\"><div class=\"col-12 col-xl-2 px-0\"><div class=\"small fw-bold\"> 4% </div></div><div class=\"col-12 col-xl-10 px-0 px-xl-1\"><div class=\"progress progress-lg mb-0\"><div aria-valuemax=\"100\" aria-valuemin=\"0\" aria-valuenow=\"4\" class=\"progress-bar bg-dark\" role=\"progressbar\" style=\"width: 4%;\"></div></div></div></div>", f6="-")
    db.commit()

if not db(db.tbootstrapXtables1).count():
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\"> United States </span></div></a>", f1="106", f2="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 5 </span></div>", f3="3", f4="=", f5="32", f6="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 3 </span></div>")
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\"> Canada </span></div></a>", f1="76", f2="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 17 </span></div>", f3="4", f4="=", f5="30", f6="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 3 </span></div>")
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\"> United Kingdom </span></div></a>", f1="147", f2="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 10 </span></div>", f3="5", f4="=", f5="34", f6="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 7 </span></div>")
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\"> France </span></div></a>", f1="112", f2="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 3 </span></div>", f3="5", f4="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 1 </span></div>", f5="34", f6="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 2 </span></div>")
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\"> Japan </span></div></a>", f1="115", f2="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 12 </span></div>", f3="6", f4="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 1 </span></div>", f5="37", f6="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 5 </span></div>")
    db.tbootstrapXtables1.insert(f0="<a class=\"d-flex align-items-center\" href=\"#\"><img alt=\"Image placeholder\" class=\"me-2 image image-small rounded-circle\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==\"/><div><span class=\"h6\"> Germany </span></div></a>", f1="220", f2="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 56 </span></div>", f3="7", f4="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 3 </span></div>", f5="30", f6="<div class=\"d-flex align-items-center\"><svg class=\"icon icon-xs me-1\" fill=\"currentColor\" viewbox=\"0 0 20 20\" xmlns=\"http://www.w3.org/2000/svg\"><path clip-rule=\"evenodd\" d=\"M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z\" fill-rule=\"evenodd\"></path></svg><span class=\"fw-bold\"> 2 </span></div>")
    db.commit()
