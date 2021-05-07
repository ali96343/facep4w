import datetime

from .common import db, Field, Tags, groups
from pydal.validators import *
from py4web.utils.populate import populate

# py4web app, AI-biorex ported 07.05.2021 14:48:48 UTC+3, src: https://github.com/puikinsh/Adminator-admin-dashboard


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
    db.app_images.insert(f0='assets/static/images/logo.png', )
    db.app_images.insert(f0='assets/static/images/404.png', )
    db.app_images.insert(f0='assets/static/images/500.png', )
    db.app_images.insert(f0='assets/static/images/bg.jpg', )

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
    'dfcompose0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfcalendar0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','text', length=1024, ),
    )
db.commit()

db.define_table(
    'dfforms0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfforms1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    Field('f6','string', length=1024, ),
    Field('f7','string', length=1024, ),
    Field('f8','boolean',  ),
    )
db.commit()

db.define_table(
    'dfforms2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','boolean',  ),
    )
db.commit()

db.define_table(
    'dfforms3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfforms4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    )
db.commit()

db.define_table(
    'dfsignin0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','boolean',  ),
    )
db.commit()

db.define_table(
    'dfsignup0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tindex0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable1',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable2',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable3',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tbasicXtable4',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    )
db.commit()

db.define_table(
    'tdatatable0',
    Field('f0','string', length=1024, ),
    Field('f1','string', length=1024, ),
    Field('f2','string', length=1024, ),
    Field('f3','string', length=1024, ),
    Field('f4','string', length=1024, ),
    Field('f5','string', length=1024, ),
    )
db.commit()

if not db(db.tindex0).count():
    db.tindex0.insert(f0="Item #1 Name", f1="<span class=\"badge bgc-red-50 c-red-700 p-10 lh-0 tt-c badge-pill\"> Unavailable </span>", f2="Nov 18", f3="<span class=\"text-success\"> $12 </span>")
    db.tindex0.insert(f0="Item #2 Name", f1="<span class=\"badge bgc-deep-purple-50 c-deep-purple-700 p-10 lh-0 tt-c badge-pill\"> New </span>", f2="Nov 19", f3="<span class=\"text-info\"> $34 </span>")
    db.tindex0.insert(f0="Item #3 Name", f1="<span class=\"badge bgc-pink-50 c-pink-700 p-10 lh-0 tt-c badge-pill\"> New </span>", f2="Nov 20", f3="<span class=\"text-danger\"> -$45 </span>")
    db.tindex0.insert(f0="Item #4 Name", f1="<span class=\"badge bgc-green-50 c-green-700 p-10 lh-0 tt-c badge-pill\"> Unavailable </span>", f2="Nov 21", f3="<span class=\"text-success\"> $65 </span>")
    db.tindex0.insert(f0="Item #5 Name", f1="<span class=\"badge bgc-red-50 c-red-700 p-10 lh-0 tt-c badge-pill\"> Used </span>", f2="Nov 22", f3="<span class=\"text-success\"> $78 </span>")
    db.tindex0.insert(f0="Item #6 Name", f1="<span class=\"badge bgc-orange-50 c-orange-700 p-10 lh-0 tt-c badge-pill\"> Used </span>", f2="Nov 23", f3="<span class=\"text-danger\"> -$88 </span>")
    db.tindex0.insert(f0="Item #7 Name", f1="<span class=\"badge bgc-yellow-50 c-yellow-700 p-10 lh-0 tt-c badge-pill\"> Old </span>", f2="Nov 22", f3="<span class=\"text-success\"> $56 </span>")
    db.commit()

if not db(db.tbasicXtable0).count():
    db.tbasicXtable0.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tbasicXtable0.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tbasicXtable0.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.tbasicXtable1).count():
    db.tbasicXtable1.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tbasicXtable1.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tbasicXtable1.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.tbasicXtable2).count():
    db.tbasicXtable2.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tbasicXtable2.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tbasicXtable2.insert(f0="3", f1="Larry", f2="the Bird", f3="@twitter")
    db.commit()

if not db(db.tbasicXtable3).count():
    db.tbasicXtable3.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tbasicXtable3.insert(f0="2", f1="Mark", f2="Otto", f3="@TwBootstrap")
    db.tbasicXtable3.insert(f0="3", f1="Jacob", f2="Thornton", f3="@fat")
    db.tbasicXtable3.insert(f0="4", f1="Larry the Bird", f2="@twitter")
    db.commit()

if not db(db.tbasicXtable4).count():
    db.tbasicXtable4.insert(f0="1", f1="Mark", f2="Otto", f3="@mdo")
    db.tbasicXtable4.insert(f0="2", f1="Jacob", f2="Thornton", f3="@fat")
    db.tbasicXtable4.insert(f0="3", f1="Larry the Bird", f2="@twitter")
    db.commit()

if not db(db.tdatatable0).count():
    db.tdatatable0.insert(f0="Name", f1="Position", f2="Office", f3="Age", f4="Start date", f5="Salary")
    db.tdatatable0.insert(f0="Tiger Nixon", f1="System Architect", f2="Edinburgh", f3="61", f4="2011/04/25", f5="$320,800")
    db.tdatatable0.insert(f0="Garrett Winters", f1="Accountant", f2="Tokyo", f3="63", f4="2011/07/25", f5="$170,750")
    db.tdatatable0.insert(f0="Ashton Cox", f1="Junior Technical Author", f2="San Francisco", f3="66", f4="2009/01/12", f5="$86,000")
    db.tdatatable0.insert(f0="Cedric Kelly", f1="Senior Javascript Developer", f2="Edinburgh", f3="22", f4="2012/03/29", f5="$433,060")
    db.tdatatable0.insert(f0="Airi Satou", f1="Accountant", f2="Tokyo", f3="33", f4="2008/11/28", f5="$162,700")
    db.tdatatable0.insert(f0="Brielle Williamson", f1="Integration Specialist", f2="New York", f3="61", f4="2012/12/02", f5="$372,000")
    db.tdatatable0.insert(f0="Herrod Chandler", f1="Sales Assistant", f2="San Francisco", f3="59", f4="2012/08/06", f5="$137,500")
    db.tdatatable0.insert(f0="Rhona Davidson", f1="Integration Specialist", f2="Tokyo", f3="55", f4="2010/10/14", f5="$327,900")
    db.tdatatable0.insert(f0="Colleen Hurst", f1="Javascript Developer", f2="San Francisco", f3="39", f4="2009/09/15", f5="$205,500")
    db.tdatatable0.insert(f0="Sonya Frost", f1="Software Engineer", f2="Edinburgh", f3="23", f4="2008/12/13", f5="$103,600")
    db.tdatatable0.insert(f0="Jena Gaines", f1="Office Manager", f2="London", f3="30", f4="2008/12/19", f5="$90,560")
    db.tdatatable0.insert(f0="Quinn Flynn", f1="Support Lead", f2="Edinburgh", f3="22", f4="2013/03/03", f5="$342,000")
    db.tdatatable0.insert(f0="Charde Marshall", f1="Regional Director", f2="San Francisco", f3="36", f4="2008/10/16", f5="$470,600")
    db.tdatatable0.insert(f0="Haley Kennedy", f1="Senior Marketing Designer", f2="London", f3="43", f4="2012/12/18", f5="$313,500")
    db.tdatatable0.insert(f0="Tatyana Fitzpatrick", f1="Regional Director", f2="London", f3="19", f4="2010/03/17", f5="$385,750")
    db.tdatatable0.insert(f0="Michael Silva", f1="Marketing Designer", f2="London", f3="66", f4="2012/11/27", f5="$198,500")
    db.tdatatable0.insert(f0="Paul Byrd", f1="Chief Financial Officer (CFO)", f2="New York", f3="64", f4="2010/06/09", f5="$725,000")
    db.tdatatable0.insert(f0="Gloria Little", f1="Systems Administrator", f2="New York", f3="59", f4="2009/04/10", f5="$237,500")
    db.tdatatable0.insert(f0="Bradley Greer", f1="Software Engineer", f2="London", f3="41", f4="2012/10/13", f5="$132,000")
    db.tdatatable0.insert(f0="Dai Rios", f1="Personnel Lead", f2="Edinburgh", f3="35", f4="2012/09/26", f5="$217,500")
    db.tdatatable0.insert(f0="Jenette Caldwell", f1="Development Lead", f2="New York", f3="30", f4="2011/09/03", f5="$345,000")
    db.tdatatable0.insert(f0="Yuri Berry", f1="Chief Marketing Officer (CMO)", f2="New York", f3="40", f4="2009/06/25", f5="$675,000")
    db.tdatatable0.insert(f0="Caesar Vance", f1="Pre-Sales Support", f2="New York", f3="21", f4="2011/12/12", f5="$106,450")
    db.tdatatable0.insert(f0="Doris Wilder", f1="Sales Assistant", f2="Sidney", f3="23", f4="2010/09/20", f5="$85,600")
    db.tdatatable0.insert(f0="Angelica Ramos", f1="Chief Executive Officer (CEO)", f2="London", f3="47", f4="2009/10/09", f5="$1,200,000")
    db.tdatatable0.insert(f0="Gavin Joyce", f1="Developer", f2="Edinburgh", f3="42", f4="2010/12/22", f5="$92,575")
    db.tdatatable0.insert(f0="Jennifer Chang", f1="Regional Director", f2="Singapore", f3="28", f4="2010/11/14", f5="$357,650")
    db.tdatatable0.insert(f0="Brenden Wagner", f1="Software Engineer", f2="San Francisco", f3="28", f4="2011/06/07", f5="$206,850")
    db.tdatatable0.insert(f0="Fiona Green", f1="Chief Operating Officer (COO)", f2="San Francisco", f3="48", f4="2010/03/11", f5="$850,000")
    db.tdatatable0.insert(f0="Shou Itou", f1="Regional Marketing", f2="Tokyo", f3="20", f4="2011/08/14", f5="$163,000")
    db.tdatatable0.insert(f0="Michelle House", f1="Integration Specialist", f2="Sidney", f3="37", f4="2011/06/02", f5="$95,400")
    db.tdatatable0.insert(f0="Suki Burks", f1="Developer", f2="London", f3="53", f4="2009/10/22", f5="$114,500")
    db.tdatatable0.insert(f0="Prescott Bartlett", f1="Technical Author", f2="London", f3="27", f4="2011/05/07", f5="$145,000")
    db.tdatatable0.insert(f0="Gavin Cortez", f1="Team Leader", f2="San Francisco", f3="22", f4="2008/10/26", f5="$235,500")
    db.tdatatable0.insert(f0="Martena Mccray", f1="Post-Sales support", f2="Edinburgh", f3="46", f4="2011/03/09", f5="$324,050")
    db.tdatatable0.insert(f0="Unity Butler", f1="Marketing Designer", f2="San Francisco", f3="47", f4="2009/12/09", f5="$85,675")
    db.tdatatable0.insert(f0="Howard Hatfield", f1="Office Manager", f2="San Francisco", f3="51", f4="2008/12/16", f5="$164,500")
    db.tdatatable0.insert(f0="Hope Fuentes", f1="Secretary", f2="San Francisco", f3="41", f4="2010/02/12", f5="$109,850")
    db.tdatatable0.insert(f0="Vivian Harrell", f1="Financial Controller", f2="San Francisco", f3="62", f4="2009/02/14", f5="$452,500")
    db.tdatatable0.insert(f0="Timothy Mooney", f1="Office Manager", f2="London", f3="37", f4="2008/12/11", f5="$136,200")
    db.tdatatable0.insert(f0="Jackson Bradshaw", f1="Director", f2="New York", f3="65", f4="2008/09/26", f5="$645,750")
    db.tdatatable0.insert(f0="Olivia Liang", f1="Support Engineer", f2="Singapore", f3="64", f4="2011/02/03", f5="$234,500")
    db.tdatatable0.insert(f0="Bruno Nash", f1="Software Engineer", f2="London", f3="38", f4="2011/05/03", f5="$163,500")
    db.tdatatable0.insert(f0="Sakura Yamamoto", f1="Support Engineer", f2="Tokyo", f3="37", f4="2009/08/19", f5="$139,575")
    db.tdatatable0.insert(f0="Thor Walton", f1="Developer", f2="New York", f3="61", f4="2013/08/11", f5="$98,540")
    db.tdatatable0.insert(f0="Finn Camacho", f1="Support Engineer", f2="San Francisco", f3="47", f4="2009/07/07", f5="$87,500")
    db.tdatatable0.insert(f0="Serge Baldwin", f1="Data Coordinator", f2="Singapore", f3="64", f4="2012/04/09", f5="$138,575")
    db.tdatatable0.insert(f0="Zenaida Frank", f1="Software Engineer", f2="New York", f3="63", f4="2010/01/04", f5="$125,250")
    db.tdatatable0.insert(f0="Zorita Serrano", f1="Software Engineer", f2="San Francisco", f3="56", f4="2012/06/01", f5="$115,000")
    db.tdatatable0.insert(f0="Jennifer Acosta", f1="Junior Javascript Developer", f2="Edinburgh", f3="43", f4="2013/02/01", f5="$75,650")
    db.tdatatable0.insert(f0="Cara Stevens", f1="Sales Assistant", f2="New York", f3="46", f4="2011/12/06", f5="$145,600")
    db.tdatatable0.insert(f0="Hermione Butler", f1="Regional Director", f2="London", f3="47", f4="2011/03/21", f5="$356,250")
    db.tdatatable0.insert(f0="Lael Greer", f1="Systems Administrator", f2="London", f3="21", f4="2009/02/27", f5="$103,500")
    db.tdatatable0.insert(f0="Jonas Alexander", f1="Developer", f2="San Francisco", f3="30", f4="2010/07/14", f5="$86,500")
    db.tdatatable0.insert(f0="Shad Decker", f1="Regional Director", f2="Edinburgh", f3="51", f4="2008/11/13", f5="$183,000")
    db.tdatatable0.insert(f0="Michael Bruce", f1="Javascript Developer", f2="Singapore", f3="29", f4="2011/06/27", f5="$183,000")
    db.tdatatable0.insert(f0="Donna Snider", f1="Customer Support", f2="New York", f3="27", f4="2011/01/25", f5="$112,000")
    db.commit()
