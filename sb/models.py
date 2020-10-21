from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 21.10.2020 14:13:52
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
    'dflogin0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','boolean'),
    )

db.define_table(
    'dfregister0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'dfforgotXpassword0',
    Field('f0','string'),
    )

db.define_table(
    'dfX4040',
    Field('f0','string'),
    )

db.define_table(
    'dfblank0',
    Field('f0','string'),
    )

db.define_table(
    'dfcharts0',
    Field('f0','string'),
    )

db.define_table(
    'dftables0',
    Field('f0','string'),
    )

db.define_table(
    'tindex0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'ttables0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

if not db(db.tindex0).count():
    db.tindex0.insert(f0="p4w:Name", f1="p4w:Position", f2="p4w:Office", f3="p4w:Age", f4="p4w:Start date", f5="p4w:Salary")
    db.tindex0.insert(f0="p4w:Name", f1="p4w:Position", f2="p4w:Office", f3="p4w:Age", f4="p4w:Start date", f5="p4w:Salary")
    db.tindex0.insert(f0="p4w:Tiger Nixon", f1="p4w:System Architect", f2="p4w:Edinburgh", f3="p4w:61", f4="p4w:2011/04/25", f5="p4w:$320,800")
    db.tindex0.insert(f0="p4w:Garrett Winters", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:63", f4="p4w:2011/07/25", f5="p4w:$170,750")
    db.tindex0.insert(f0="p4w:Ashton Cox", f1="p4w:Junior Technical Author", f2="p4w:San Francisco", f3="p4w:66", f4="p4w:2009/01/12", f5="p4w:$86,000")
    db.tindex0.insert(f0="p4w:Cedric Kelly", f1="p4w:Senior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2012/03/29", f5="p4w:$433,060")
    db.tindex0.insert(f0="p4w:Airi Satou", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:33", f4="p4w:2008/11/28", f5="p4w:$162,700")
    db.tindex0.insert(f0="p4w:Brielle Williamson", f1="p4w:Integration Specialist", f2="p4w:New York", f3="p4w:61", f4="p4w:2012/12/02", f5="p4w:$372,000")
    db.tindex0.insert(f0="p4w:Herrod Chandler", f1="p4w:Sales Assistant", f2="p4w:San Francisco", f3="p4w:59", f4="p4w:2012/08/06", f5="p4w:$137,500")
    db.tindex0.insert(f0="p4w:Rhona Davidson", f1="p4w:Integration Specialist", f2="p4w:Tokyo", f3="p4w:55", f4="p4w:2010/10/14", f5="p4w:$327,900")
    db.tindex0.insert(f0="p4w:Colleen Hurst", f1="p4w:Javascript Developer", f2="p4w:San Francisco", f3="p4w:39", f4="p4w:2009/09/15", f5="p4w:$205,500")
    db.tindex0.insert(f0="p4w:Sonya Frost", f1="p4w:Software Engineer", f2="p4w:Edinburgh", f3="p4w:23", f4="p4w:2008/12/13", f5="p4w:$103,600")
    db.tindex0.insert(f0="p4w:Jena Gaines", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:30", f4="p4w:2008/12/19", f5="p4w:$90,560")
    db.tindex0.insert(f0="p4w:Quinn Flynn", f1="p4w:Support Lead", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2013/03/03", f5="p4w:$342,000")
    db.tindex0.insert(f0="p4w:Charde Marshall", f1="p4w:Regional Director", f2="p4w:San Francisco", f3="p4w:36", f4="p4w:2008/10/16", f5="p4w:$470,600")
    db.tindex0.insert(f0="p4w:Haley Kennedy", f1="p4w:Senior Marketing Designer", f2="p4w:London", f3="p4w:43", f4="p4w:2012/12/18", f5="p4w:$313,500")
    db.tindex0.insert(f0="p4w:Tatyana Fitzpatrick", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:19", f4="p4w:2010/03/17", f5="p4w:$385,750")
    db.tindex0.insert(f0="p4w:Michael Silva", f1="p4w:Marketing Designer", f2="p4w:London", f3="p4w:66", f4="p4w:2012/11/27", f5="p4w:$198,500")
    db.tindex0.insert(f0="p4w:Paul Byrd", f1="p4w:Chief Financial Officer (CFO)", f2="p4w:New York", f3="p4w:64", f4="p4w:2010/06/09", f5="p4w:$725,000")
    db.tindex0.insert(f0="p4w:Gloria Little", f1="p4w:Systems Administrator", f2="p4w:New York", f3="p4w:59", f4="p4w:2009/04/10", f5="p4w:$237,500")
    db.tindex0.insert(f0="p4w:Bradley Greer", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:41", f4="p4w:2012/10/13", f5="p4w:$132,000")
    db.tindex0.insert(f0="p4w:Dai Rios", f1="p4w:Personnel Lead", f2="p4w:Edinburgh", f3="p4w:35", f4="p4w:2012/09/26", f5="p4w:$217,500")
    db.tindex0.insert(f0="p4w:Jenette Caldwell", f1="p4w:Development Lead", f2="p4w:New York", f3="p4w:30", f4="p4w:2011/09/03", f5="p4w:$345,000")
    db.tindex0.insert(f0="p4w:Yuri Berry", f1="p4w:Chief Marketing Officer (CMO)", f2="p4w:New York", f3="p4w:40", f4="p4w:2009/06/25", f5="p4w:$675,000")
    db.tindex0.insert(f0="p4w:Caesar Vance", f1="p4w:Pre-Sales Support", f2="p4w:New York", f3="p4w:21", f4="p4w:2011/12/12", f5="p4w:$106,450")
    db.tindex0.insert(f0="p4w:Doris Wilder", f1="p4w:Sales Assistant", f2="p4w:Sidney", f3="p4w:23", f4="p4w:2010/09/20", f5="p4w:$85,600")
    db.tindex0.insert(f0="p4w:Angelica Ramos", f1="p4w:Chief Executive Officer (CEO)", f2="p4w:London", f3="p4w:47", f4="p4w:2009/10/09", f5="p4w:$1,200,000")
    db.tindex0.insert(f0="p4w:Gavin Joyce", f1="p4w:Developer", f2="p4w:Edinburgh", f3="p4w:42", f4="p4w:2010/12/22", f5="p4w:$92,575")
    db.tindex0.insert(f0="p4w:Jennifer Chang", f1="p4w:Regional Director", f2="p4w:Singapore", f3="p4w:28", f4="p4w:2010/11/14", f5="p4w:$357,650")
    db.tindex0.insert(f0="p4w:Brenden Wagner", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:28", f4="p4w:2011/06/07", f5="p4w:$206,850")
    db.tindex0.insert(f0="p4w:Fiona Green", f1="p4w:Chief Operating Officer (COO)", f2="p4w:San Francisco", f3="p4w:48", f4="p4w:2010/03/11", f5="p4w:$850,000")
    db.tindex0.insert(f0="p4w:Shou Itou", f1="p4w:Regional Marketing", f2="p4w:Tokyo", f3="p4w:20", f4="p4w:2011/08/14", f5="p4w:$163,000")
    db.tindex0.insert(f0="p4w:Michelle House", f1="p4w:Integration Specialist", f2="p4w:Sidney", f3="p4w:37", f4="p4w:2011/06/02", f5="p4w:$95,400")
    db.tindex0.insert(f0="p4w:Suki Burks", f1="p4w:Developer", f2="p4w:London", f3="p4w:53", f4="p4w:2009/10/22", f5="p4w:$114,500")
    db.tindex0.insert(f0="p4w:Prescott Bartlett", f1="p4w:Technical Author", f2="p4w:London", f3="p4w:27", f4="p4w:2011/05/07", f5="p4w:$145,000")
    db.tindex0.insert(f0="p4w:Gavin Cortez", f1="p4w:Team Leader", f2="p4w:San Francisco", f3="p4w:22", f4="p4w:2008/10/26", f5="p4w:$235,500")
    db.tindex0.insert(f0="p4w:Martena Mccray", f1="p4w:Post-Sales support", f2="p4w:Edinburgh", f3="p4w:46", f4="p4w:2011/03/09", f5="p4w:$324,050")
    db.tindex0.insert(f0="p4w:Unity Butler", f1="p4w:Marketing Designer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/12/09", f5="p4w:$85,675")
    db.tindex0.insert(f0="p4w:Howard Hatfield", f1="p4w:Office Manager", f2="p4w:San Francisco", f3="p4w:51", f4="p4w:2008/12/16", f5="p4w:$164,500")
    db.tindex0.insert(f0="p4w:Hope Fuentes", f1="p4w:Secretary", f2="p4w:San Francisco", f3="p4w:41", f4="p4w:2010/02/12", f5="p4w:$109,850")
    db.tindex0.insert(f0="p4w:Vivian Harrell", f1="p4w:Financial Controller", f2="p4w:San Francisco", f3="p4w:62", f4="p4w:2009/02/14", f5="p4w:$452,500")
    db.tindex0.insert(f0="p4w:Timothy Mooney", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:37", f4="p4w:2008/12/11", f5="p4w:$136,200")
    db.tindex0.insert(f0="p4w:Jackson Bradshaw", f1="p4w:Director", f2="p4w:New York", f3="p4w:65", f4="p4w:2008/09/26", f5="p4w:$645,750")
    db.tindex0.insert(f0="p4w:Olivia Liang", f1="p4w:Support Engineer", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2011/02/03", f5="p4w:$234,500")
    db.tindex0.insert(f0="p4w:Bruno Nash", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:38", f4="p4w:2011/05/03", f5="p4w:$163,500")
    db.tindex0.insert(f0="p4w:Sakura Yamamoto", f1="p4w:Support Engineer", f2="p4w:Tokyo", f3="p4w:37", f4="p4w:2009/08/19", f5="p4w:$139,575")
    db.tindex0.insert(f0="p4w:Thor Walton", f1="p4w:Developer", f2="p4w:New York", f3="p4w:61", f4="p4w:2013/08/11", f5="p4w:$98,540")
    db.tindex0.insert(f0="p4w:Finn Camacho", f1="p4w:Support Engineer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/07/07", f5="p4w:$87,500")
    db.tindex0.insert(f0="p4w:Serge Baldwin", f1="p4w:Data Coordinator", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2012/04/09", f5="p4w:$138,575")
    db.tindex0.insert(f0="p4w:Zenaida Frank", f1="p4w:Software Engineer", f2="p4w:New York", f3="p4w:63", f4="p4w:2010/01/04", f5="p4w:$125,250")
    db.tindex0.insert(f0="p4w:Zorita Serrano", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:56", f4="p4w:2012/06/01", f5="p4w:$115,000")
    db.tindex0.insert(f0="p4w:Jennifer Acosta", f1="p4w:Junior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:43", f4="p4w:2013/02/01", f5="p4w:$75,650")
    db.tindex0.insert(f0="p4w:Cara Stevens", f1="p4w:Sales Assistant", f2="p4w:New York", f3="p4w:46", f4="p4w:2011/12/06", f5="p4w:$145,600")
    db.tindex0.insert(f0="p4w:Hermione Butler", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:47", f4="p4w:2011/03/21", f5="p4w:$356,250")
    db.tindex0.insert(f0="p4w:Lael Greer", f1="p4w:Systems Administrator", f2="p4w:London", f3="p4w:21", f4="p4w:2009/02/27", f5="p4w:$103,500")
    db.tindex0.insert(f0="p4w:Jonas Alexander", f1="p4w:Developer", f2="p4w:San Francisco", f3="p4w:30", f4="p4w:2010/07/14", f5="p4w:$86,500")
    db.tindex0.insert(f0="p4w:Shad Decker", f1="p4w:Regional Director", f2="p4w:Edinburgh", f3="p4w:51", f4="p4w:2008/11/13", f5="p4w:$183,000")
    db.tindex0.insert(f0="p4w:Michael Bruce", f1="p4w:Javascript Developer", f2="p4w:Singapore", f3="p4w:29", f4="p4w:2011/06/27", f5="p4w:$183,000")
    db.tindex0.insert(f0="p4w:Donna Snider", f1="p4w:Customer Support", f2="p4w:New York", f3="p4w:27", f4="p4w:2011/01/25", f5="p4w:$112,000")
    db.commit()

if not db(db.ttables0).count():
    db.ttables0.insert(f0="p4w:Name", f1="p4w:Position", f2="p4w:Office", f3="p4w:Age", f4="p4w:Start date", f5="p4w:Salary")
    db.ttables0.insert(f0="p4w:Name", f1="p4w:Position", f2="p4w:Office", f3="p4w:Age", f4="p4w:Start date", f5="p4w:Salary")
    db.ttables0.insert(f0="p4w:Tiger Nixon", f1="p4w:System Architect", f2="p4w:Edinburgh", f3="p4w:61", f4="p4w:2011/04/25", f5="p4w:$320,800")
    db.ttables0.insert(f0="p4w:Garrett Winters", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:63", f4="p4w:2011/07/25", f5="p4w:$170,750")
    db.ttables0.insert(f0="p4w:Ashton Cox", f1="p4w:Junior Technical Author", f2="p4w:San Francisco", f3="p4w:66", f4="p4w:2009/01/12", f5="p4w:$86,000")
    db.ttables0.insert(f0="p4w:Cedric Kelly", f1="p4w:Senior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2012/03/29", f5="p4w:$433,060")
    db.ttables0.insert(f0="p4w:Airi Satou", f1="p4w:Accountant", f2="p4w:Tokyo", f3="p4w:33", f4="p4w:2008/11/28", f5="p4w:$162,700")
    db.ttables0.insert(f0="p4w:Brielle Williamson", f1="p4w:Integration Specialist", f2="p4w:New York", f3="p4w:61", f4="p4w:2012/12/02", f5="p4w:$372,000")
    db.ttables0.insert(f0="p4w:Herrod Chandler", f1="p4w:Sales Assistant", f2="p4w:San Francisco", f3="p4w:59", f4="p4w:2012/08/06", f5="p4w:$137,500")
    db.ttables0.insert(f0="p4w:Rhona Davidson", f1="p4w:Integration Specialist", f2="p4w:Tokyo", f3="p4w:55", f4="p4w:2010/10/14", f5="p4w:$327,900")
    db.ttables0.insert(f0="p4w:Colleen Hurst", f1="p4w:Javascript Developer", f2="p4w:San Francisco", f3="p4w:39", f4="p4w:2009/09/15", f5="p4w:$205,500")
    db.ttables0.insert(f0="p4w:Sonya Frost", f1="p4w:Software Engineer", f2="p4w:Edinburgh", f3="p4w:23", f4="p4w:2008/12/13", f5="p4w:$103,600")
    db.ttables0.insert(f0="p4w:Jena Gaines", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:30", f4="p4w:2008/12/19", f5="p4w:$90,560")
    db.ttables0.insert(f0="p4w:Quinn Flynn", f1="p4w:Support Lead", f2="p4w:Edinburgh", f3="p4w:22", f4="p4w:2013/03/03", f5="p4w:$342,000")
    db.ttables0.insert(f0="p4w:Charde Marshall", f1="p4w:Regional Director", f2="p4w:San Francisco", f3="p4w:36", f4="p4w:2008/10/16", f5="p4w:$470,600")
    db.ttables0.insert(f0="p4w:Haley Kennedy", f1="p4w:Senior Marketing Designer", f2="p4w:London", f3="p4w:43", f4="p4w:2012/12/18", f5="p4w:$313,500")
    db.ttables0.insert(f0="p4w:Tatyana Fitzpatrick", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:19", f4="p4w:2010/03/17", f5="p4w:$385,750")
    db.ttables0.insert(f0="p4w:Michael Silva", f1="p4w:Marketing Designer", f2="p4w:London", f3="p4w:66", f4="p4w:2012/11/27", f5="p4w:$198,500")
    db.ttables0.insert(f0="p4w:Paul Byrd", f1="p4w:Chief Financial Officer (CFO)", f2="p4w:New York", f3="p4w:64", f4="p4w:2010/06/09", f5="p4w:$725,000")
    db.ttables0.insert(f0="p4w:Gloria Little", f1="p4w:Systems Administrator", f2="p4w:New York", f3="p4w:59", f4="p4w:2009/04/10", f5="p4w:$237,500")
    db.ttables0.insert(f0="p4w:Bradley Greer", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:41", f4="p4w:2012/10/13", f5="p4w:$132,000")
    db.ttables0.insert(f0="p4w:Dai Rios", f1="p4w:Personnel Lead", f2="p4w:Edinburgh", f3="p4w:35", f4="p4w:2012/09/26", f5="p4w:$217,500")
    db.ttables0.insert(f0="p4w:Jenette Caldwell", f1="p4w:Development Lead", f2="p4w:New York", f3="p4w:30", f4="p4w:2011/09/03", f5="p4w:$345,000")
    db.ttables0.insert(f0="p4w:Yuri Berry", f1="p4w:Chief Marketing Officer (CMO)", f2="p4w:New York", f3="p4w:40", f4="p4w:2009/06/25", f5="p4w:$675,000")
    db.ttables0.insert(f0="p4w:Caesar Vance", f1="p4w:Pre-Sales Support", f2="p4w:New York", f3="p4w:21", f4="p4w:2011/12/12", f5="p4w:$106,450")
    db.ttables0.insert(f0="p4w:Doris Wilder", f1="p4w:Sales Assistant", f2="p4w:Sidney", f3="p4w:23", f4="p4w:2010/09/20", f5="p4w:$85,600")
    db.ttables0.insert(f0="p4w:Angelica Ramos", f1="p4w:Chief Executive Officer (CEO)", f2="p4w:London", f3="p4w:47", f4="p4w:2009/10/09", f5="p4w:$1,200,000")
    db.ttables0.insert(f0="p4w:Gavin Joyce", f1="p4w:Developer", f2="p4w:Edinburgh", f3="p4w:42", f4="p4w:2010/12/22", f5="p4w:$92,575")
    db.ttables0.insert(f0="p4w:Jennifer Chang", f1="p4w:Regional Director", f2="p4w:Singapore", f3="p4w:28", f4="p4w:2010/11/14", f5="p4w:$357,650")
    db.ttables0.insert(f0="p4w:Brenden Wagner", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:28", f4="p4w:2011/06/07", f5="p4w:$206,850")
    db.ttables0.insert(f0="p4w:Fiona Green", f1="p4w:Chief Operating Officer (COO)", f2="p4w:San Francisco", f3="p4w:48", f4="p4w:2010/03/11", f5="p4w:$850,000")
    db.ttables0.insert(f0="p4w:Shou Itou", f1="p4w:Regional Marketing", f2="p4w:Tokyo", f3="p4w:20", f4="p4w:2011/08/14", f5="p4w:$163,000")
    db.ttables0.insert(f0="p4w:Michelle House", f1="p4w:Integration Specialist", f2="p4w:Sidney", f3="p4w:37", f4="p4w:2011/06/02", f5="p4w:$95,400")
    db.ttables0.insert(f0="p4w:Suki Burks", f1="p4w:Developer", f2="p4w:London", f3="p4w:53", f4="p4w:2009/10/22", f5="p4w:$114,500")
    db.ttables0.insert(f0="p4w:Prescott Bartlett", f1="p4w:Technical Author", f2="p4w:London", f3="p4w:27", f4="p4w:2011/05/07", f5="p4w:$145,000")
    db.ttables0.insert(f0="p4w:Gavin Cortez", f1="p4w:Team Leader", f2="p4w:San Francisco", f3="p4w:22", f4="p4w:2008/10/26", f5="p4w:$235,500")
    db.ttables0.insert(f0="p4w:Martena Mccray", f1="p4w:Post-Sales support", f2="p4w:Edinburgh", f3="p4w:46", f4="p4w:2011/03/09", f5="p4w:$324,050")
    db.ttables0.insert(f0="p4w:Unity Butler", f1="p4w:Marketing Designer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/12/09", f5="p4w:$85,675")
    db.ttables0.insert(f0="p4w:Howard Hatfield", f1="p4w:Office Manager", f2="p4w:San Francisco", f3="p4w:51", f4="p4w:2008/12/16", f5="p4w:$164,500")
    db.ttables0.insert(f0="p4w:Hope Fuentes", f1="p4w:Secretary", f2="p4w:San Francisco", f3="p4w:41", f4="p4w:2010/02/12", f5="p4w:$109,850")
    db.ttables0.insert(f0="p4w:Vivian Harrell", f1="p4w:Financial Controller", f2="p4w:San Francisco", f3="p4w:62", f4="p4w:2009/02/14", f5="p4w:$452,500")
    db.ttables0.insert(f0="p4w:Timothy Mooney", f1="p4w:Office Manager", f2="p4w:London", f3="p4w:37", f4="p4w:2008/12/11", f5="p4w:$136,200")
    db.ttables0.insert(f0="p4w:Jackson Bradshaw", f1="p4w:Director", f2="p4w:New York", f3="p4w:65", f4="p4w:2008/09/26", f5="p4w:$645,750")
    db.ttables0.insert(f0="p4w:Olivia Liang", f1="p4w:Support Engineer", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2011/02/03", f5="p4w:$234,500")
    db.ttables0.insert(f0="p4w:Bruno Nash", f1="p4w:Software Engineer", f2="p4w:London", f3="p4w:38", f4="p4w:2011/05/03", f5="p4w:$163,500")
    db.ttables0.insert(f0="p4w:Sakura Yamamoto", f1="p4w:Support Engineer", f2="p4w:Tokyo", f3="p4w:37", f4="p4w:2009/08/19", f5="p4w:$139,575")
    db.ttables0.insert(f0="p4w:Thor Walton", f1="p4w:Developer", f2="p4w:New York", f3="p4w:61", f4="p4w:2013/08/11", f5="p4w:$98,540")
    db.ttables0.insert(f0="p4w:Finn Camacho", f1="p4w:Support Engineer", f2="p4w:San Francisco", f3="p4w:47", f4="p4w:2009/07/07", f5="p4w:$87,500")
    db.ttables0.insert(f0="p4w:Serge Baldwin", f1="p4w:Data Coordinator", f2="p4w:Singapore", f3="p4w:64", f4="p4w:2012/04/09", f5="p4w:$138,575")
    db.ttables0.insert(f0="p4w:Zenaida Frank", f1="p4w:Software Engineer", f2="p4w:New York", f3="p4w:63", f4="p4w:2010/01/04", f5="p4w:$125,250")
    db.ttables0.insert(f0="p4w:Zorita Serrano", f1="p4w:Software Engineer", f2="p4w:San Francisco", f3="p4w:56", f4="p4w:2012/06/01", f5="p4w:$115,000")
    db.ttables0.insert(f0="p4w:Jennifer Acosta", f1="p4w:Junior Javascript Developer", f2="p4w:Edinburgh", f3="p4w:43", f4="p4w:2013/02/01", f5="p4w:$75,650")
    db.ttables0.insert(f0="p4w:Cara Stevens", f1="p4w:Sales Assistant", f2="p4w:New York", f3="p4w:46", f4="p4w:2011/12/06", f5="p4w:$145,600")
    db.ttables0.insert(f0="p4w:Hermione Butler", f1="p4w:Regional Director", f2="p4w:London", f3="p4w:47", f4="p4w:2011/03/21", f5="p4w:$356,250")
    db.ttables0.insert(f0="p4w:Lael Greer", f1="p4w:Systems Administrator", f2="p4w:London", f3="p4w:21", f4="p4w:2009/02/27", f5="p4w:$103,500")
    db.ttables0.insert(f0="p4w:Jonas Alexander", f1="p4w:Developer", f2="p4w:San Francisco", f3="p4w:30", f4="p4w:2010/07/14", f5="p4w:$86,500")
    db.ttables0.insert(f0="p4w:Shad Decker", f1="p4w:Regional Director", f2="p4w:Edinburgh", f3="p4w:51", f4="p4w:2008/11/13", f5="p4w:$183,000")
    db.ttables0.insert(f0="p4w:Michael Bruce", f1="p4w:Javascript Developer", f2="p4w:Singapore", f3="p4w:29", f4="p4w:2011/06/27", f5="p4w:$183,000")
    db.ttables0.insert(f0="p4w:Donna Snider", f1="p4w:Customer Support", f2="p4w:New York", f3="p4w:27", f4="p4w:2011/01/25", f5="p4w:$112,000")
    db.commit()
