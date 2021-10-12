import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 12.10.2021 15:16:27 UTC+3, src: https://github.com/davidgrzyb/tailwind-admin-template

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
    'dfforms0',
    Field('f0','string', length=1024, default='fNo' ),
    Field('f1','string', length=1024, default='fNo' ),
    Field('f2','text', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'dfforms1',
    Field('f0','string', length=1024, default='fNo' ),
    Field('f1','string', length=1024, default='fNo' ),
    Field('f2','string', length=1024, default='fNo' ),
    Field('f3','string', length=1024, default='fNo' ),
    Field('f4','string', length=1024, default='fNo' ),
    Field('f5','string', length=1024, default='fNo' ),
    Field('f6','string', length=1024, default='fNo' ),
    )
db.commit()

db.define_table(
    'tindex0',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    Field('f2','string', length=1024, default='tNo' ),
    Field('f3','string', length=1024, default='tNo' ),
    )
db.commit()

db.define_table(
    'ttables0',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    Field('f2','string', length=1024, default='tNo' ),
    Field('f3','string', length=1024, default='tNo' ),
    )
db.commit()

db.define_table(
    'ttables1',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    Field('f2','string', length=1024, default='tNo' ),
    Field('f3','string', length=1024, default='tNo' ),
    )
db.commit()

db.define_table(
    'ttables2',
    Field('f0','string', length=1024, default='tNo' ),
    Field('f1','string', length=1024, default='tNo' ),
    Field('f2','string', length=1024, default='tNo' ),
    Field('f3','string', length=1024, default='tNo' ),
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="Lian", f1="Smith", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.tindex0.insert(f0="Emma", f1="Johnson", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.tindex0.insert(f0="Oliver", f1="Williams", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.tindex0.insert(f0="Isabella", f1="Brown", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.tindex0.insert(f0="Lian", f1="Smith", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.tindex0.insert(f0="Emma", f1="Johnson", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.tindex0.insert(f0="Oliver", f1="Williams", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.tindex0.insert(f0="Isabella", f1="Brown", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.commit()

if not db(db.ttables0).count():
    db.ttables0.insert(f0="Lian", f1="Smith", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.ttables0.insert(f0="Emma", f1="Johnson", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.ttables0.insert(f0="Oliver", f1="Williams", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.ttables0.insert(f0="Isabella", f1="Brown", f2="<a class=\"hover:text-blue-500\" href=\"tel:622322662\">622322662</a>", f3="<a class=\"hover:text-blue-500\" href=\"mailto:jonsmith@mail.com\">jonsmith@mail.com</a>")
    db.commit()

if not db(db.ttables1).count():
    db.ttables1.insert(f0="Lian", f1="Smith", f2="622322662", f3="jonsmith@mail.com")
    db.ttables1.insert(f0="Lian", f1="Smith", f2="622322662", f3="jonsmith@mail.com")
    db.ttables1.insert(f0="Lian", f1="Smith", f2="622322662", f3="jonsmith@mail.com")
    db.ttables1.insert(f0="Lian", f1="Smith", f2="622322662", f3="jonsmith@mail.com")
    db.commit()

if not db(db.ttables2).count():
    db.ttables2.insert(f0="<div class=\"flex items-center\"><div class=\"flex-shrink-0 w-10 h-10\"><img alt=\"\" class=\"w-full h-full rounded-full\" src=\"https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=2.2&amp;w=160&amp;h=160&amp;q=80\"/></div><div class=\"ml-3\"><p class=\"text-gray-900 whitespace-no-wrap\"> Vera Carpenter </p></div></div>", f1="<p class=\"text-gray-900 whitespace-no-wrap\">Admin</p>", f2="<p class=\"text-gray-900 whitespace-no-wrap\"> Jan 21, 2020 </p>", f3="<span class=\"relative inline-block px-3 py-1 font-semibold text-green-900 leading-tight\"><span aria-hidden=\"\" class=\"absolute inset-0 bg-green-200 opacity-50 rounded-full\"></span><span class=\"relative\">Activo</span></span>")
    db.ttables2.insert(f0="<div class=\"flex items-center\"><div class=\"flex-shrink-0 w-10 h-10\"><img alt=\"\" class=\"w-full h-full rounded-full\" src=\"https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=2.2&amp;w=160&amp;h=160&amp;q=80\"/></div><div class=\"ml-3\"><p class=\"text-gray-900 whitespace-no-wrap\"> Blake Bowman </p></div></div>", f1="<p class=\"text-gray-900 whitespace-no-wrap\">Editor</p>", f2="<p class=\"text-gray-900 whitespace-no-wrap\"> Jan 01, 2020 </p>", f3="<span class=\"relative inline-block px-3 py-1 font-semibold text-green-900 leading-tight\"><span aria-hidden=\"\" class=\"absolute inset-0 bg-green-200 opacity-50 rounded-full\"></span><span class=\"relative\">Activo</span></span>")
    db.ttables2.insert(f0="<div class=\"flex items-center\"><div class=\"flex-shrink-0 w-10 h-10\"><img alt=\"\" class=\"w-full h-full rounded-full\" src=\"https://images.unsplash.com/photo-1540845511934-7721dd7adec3?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=2.2&amp;w=160&amp;h=160&amp;q=80\"/></div><div class=\"ml-3\"><p class=\"text-gray-900 whitespace-no-wrap\"> Dana Moore </p></div></div>", f1="<p class=\"text-gray-900 whitespace-no-wrap\">Editor</p>", f2="<p class=\"text-gray-900 whitespace-no-wrap\"> Jan 10, 2020 </p>", f3="<span class=\"relative inline-block px-3 py-1 font-semibold text-orange-900 leading-tight\"><span aria-hidden=\"\" class=\"absolute inset-0 bg-orange-200 opacity-50 rounded-full\"></span><span class=\"relative\">Suspended</span></span>")
    db.ttables2.insert(f0="<div class=\"flex items-center\"><div class=\"flex-shrink-0 w-10 h-10\"><img alt=\"\" class=\"w-full h-full rounded-full\" src=\"https://images.unsplash.com/photo-1522609925277-66fea332c575?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=2.2&amp;h=160&amp;w=160&amp;q=80\"/></div><div class=\"ml-3\"><p class=\"text-gray-900 whitespace-no-wrap\"> Alonzo Cox </p></div></div>", f1="<p class=\"text-gray-900 whitespace-no-wrap\">Admin</p>", f2="<p class=\"text-gray-900 whitespace-no-wrap\">Jan 18, 2020</p>", f3="<span class=\"relative inline-block px-3 py-1 font-semibold text-red-900 leading-tight\"><span aria-hidden=\"\" class=\"absolute inset-0 bg-red-200 opacity-50 rounded-full\"></span><span class=\"relative\">Inactive</span></span>")
    db.commit()
