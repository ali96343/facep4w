from .common import db, Field
from pydal.validators import *

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
    'dfindex0',
    Field('f0','string'),
    )

db.define_table(
    'dfindex1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','text'),
    )

db.define_table(
    'dfwidgets0',
    Field('f0','string'),
    )

db.define_table(
    'dfmorris0',
    Field('f0','string'),
    )

db.define_table(
    'dfflot0',
    Field('f0','string'),
    )

db.define_table(
    'dfinline0',
    Field('f0','string'),
    )

db.define_table(
    'dfgeneral0',
    Field('f0','string'),
    )

db.define_table(
    'dficons0',
    Field('f0','string'),
    )

db.define_table(
    'dfbuttons0',
    Field('f0','string'),
    )

db.define_table(
    'dfsliders0',
    Field('f0','string'),
    )

db.define_table(
    'dftimeline0',
    Field('f0','string'),
    )

db.define_table(
    'dfadvanced0',
    Field('f0','string'),
    )

db.define_table(
    'dfeditors0',
    Field('f0','string'),
    )

db.define_table(
    'dfeditors1',
    Field('f0','text'),
    )

db.define_table(
    'dfeditors2',
    Field('f0','text'),
    )

db.define_table(
    'dfsimple0',
    Field('f0','string'),
    )

db.define_table(
    'dfdata0',
    Field('f0','string'),
    )

db.define_table(
    'dfcalendar0',
    Field('f0','string'),
    )

db.define_table(
    'dfmailbox0',
    Field('f0','string'),
    )

db.define_table(
    'dfmailbox1',
    Field('f0','string'),
    )

db.define_table(
    'dfmailbox2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','text'),
    )

db.define_table(
    'dfinvoice0',
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
    )

db.define_table(
    'dfX4040',
    Field('f0','string'),
    )

db.define_table(
    'dfX4041',
    Field('f0','string'),
    )

db.define_table(
    'dfX5000',
    Field('f0','string'),
    )

db.define_table(
    'dfX5001',
    Field('f0','string'),
    )

db.define_table(
    'dfblank0',
    Field('f0','string'),
    )

db.define_table(
    'tbuttons0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tbuttons1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tbuttons2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tsimple0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tsimple1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tsimple2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tsimple3',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tsimple4',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tdata0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tdata1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tmailbox0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
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

db.tbuttons0.insert(f0="p4w:Normal", f1="p4w:Large .btn-lg", f2="p4w:Mini .btn-sm", f3="p4w:Flat .btn-flat", f4="p4w:Disabled .disabled")
db.tbuttons0.insert(f0="p4w:Default", f1="p4w:Default", f2="p4w:Default", f3="p4w:Default", f4="p4w:Default")
db.tbuttons0.insert(f0="p4w:Primary", f1="p4w:Primary", f2="p4w:Primary", f3="p4w:Primary", f4="p4w:Primary")
db.tbuttons0.insert(f0="p4w:Success", f1="p4w:Success", f2="p4w:Success", f3="p4w:Success", f4="p4w:Success")
db.tbuttons0.insert(f0="p4w:Info", f1="p4w:Info", f2="p4w:Info", f3="p4w:Info", f4="p4w:Info")
db.tbuttons0.insert(f0="p4w:Danger", f1="p4w:Danger", f2="p4w:Danger", f3="p4w:Danger", f4="p4w:Danger")
db.tbuttons0.insert(f0="p4w:Warning", f1="p4w:Warning", f2="p4w:Warning", f3="p4w:Warning", f4="p4w:Warning")
db.tbuttons1.insert(f0="p4w:Button", f1="p4w:Icons", f2="p4w:Flat", f3="p4w:Dropdown")
db.tbuttons1.insert(f0="p4w:LeftMiddleRight", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
db.tbuttons1.insert(f0="p4w:LeftMiddleRight", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
db.tbuttons1.insert(f0="p4w:LeftMiddleRight", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
db.tbuttons1.insert(f0="p4w:LeftMiddleRight", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
db.tbuttons1.insert(f0="p4w:LeftMiddleRight", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
db.tbuttons2.insert(f0="p4w:Button", f1="p4w:Icons", f2="p4w:Flat", f3="p4w:Dropdown")
db.tbuttons2.insert(f0="p4w:TopMiddleBottom", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
db.tbuttons2.insert(f0="p4w:TopMiddleBottom", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
db.tbuttons2.insert(f0="p4w:TopMiddleBottom", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
db.tbuttons2.insert(f0="p4w:TopMiddleBottom", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
db.tbuttons2.insert(f0="p4w:TopMiddleBottom", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
db.tsimple0.insert(f0="p4w:#", f1="p4w:Task", f2="p4w:Progress", f3="p4w:Label")
db.tsimple0.insert(f0="p4w:1.", f1="p4w:Update software", f2="p4w:len0", f3="p4w:55%")
db.tsimple0.insert(f0="p4w:2.", f1="p4w:Clean database", f2="p4w:len0", f3="p4w:70%")
db.tsimple0.insert(f0="p4w:3.", f1="p4w:Cron job running", f2="p4w:len0", f3="p4w:30%")
db.tsimple0.insert(f0="p4w:4.", f1="p4w:Fix and squish bugs", f2="p4w:len0", f3="p4w:90%")
db.tsimple1.insert(f0="p4w:#", f1="p4w:Task", f2="p4w:Progress", f3="p4w:Label")
db.tsimple1.insert(f0="p4w:1.", f1="p4w:Update software", f2="p4w:len0", f3="p4w:55%")
db.tsimple1.insert(f0="p4w:2.", f1="p4w:Clean database", f2="p4w:len0", f3="p4w:70%")
db.tsimple1.insert(f0="p4w:3.", f1="p4w:Cron job running", f2="p4w:len0", f3="p4w:30%")
db.tsimple1.insert(f0="p4w:4.", f1="p4w:Fix and squish bugs", f2="p4w:len0", f3="p4w:90%")
db.tsimple2.insert(f0="p4w:#", f1="p4w:Task", f2="p4w:Progress", f3="p4w:Label")
db.tsimple2.insert(f0="p4w:1.", f1="p4w:Update software", f2="p4w:len0", f3="p4w:55%")
db.tsimple2.insert(f0="p4w:2.", f1="p4w:Clean database", f2="p4w:len0", f3="p4w:70%")
db.tsimple2.insert(f0="p4w:3.", f1="p4w:Cron job running", f2="p4w:len0", f3="p4w:30%")
db.tsimple2.insert(f0="p4w:4.", f1="p4w:Fix and squish bugs", f2="p4w:len0", f3="p4w:90%")
db.tsimple3.insert(f0="p4w:#", f1="p4w:Task", f2="p4w:Progress", f3="p4w:Label")
db.tsimple3.insert(f0="p4w:1.", f1="p4w:Update software", f2="p4w:len0", f3="p4w:55%")
db.tsimple3.insert(f0="p4w:2.", f1="p4w:Clean database", f2="p4w:len0", f3="p4w:70%")
db.tsimple3.insert(f0="p4w:3.", f1="p4w:Cron job running", f2="p4w:len0", f3="p4w:30%")
db.tsimple3.insert(f0="p4w:4.", f1="p4w:Fix and squish bugs", f2="p4w:len0", f3="p4w:90%")
db.tsimple4.insert(f0="p4w:ID", f1="p4w:User", f2="p4w:Date", f3="p4w:Status", f4="p4w:Reason")
db.tsimple4.insert(f0="p4w:183", f1="p4w:John Doe", f2="p4w:11-7-2014", f3="p4w:Approved", f4="p4w:Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.")
db.tsimple4.insert(f0="p4w:219", f1="p4w:Jane Doe", f2="p4w:11-7-2014", f3="p4w:Pending", f4="p4w:Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.")
db.tsimple4.insert(f0="p4w:657", f1="p4w:Bob Doe", f2="p4w:11-7-2014", f3="p4w:Approved", f4="p4w:Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.")
db.tsimple4.insert(f0="p4w:175", f1="p4w:Mike Doe", f2="p4w:11-7-2014", f3="p4w:Denied", f4="p4w:Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.")
db.tdata0.insert(f0="p4w:Rendering engine", f1="p4w:Browser", f2="p4w:Platform(s)", f3="p4w:Engine version", f4="p4w:CSS grade")
db.tdata0.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 4.0", f2="p4w:Win 95+", f3="p4w:4", f4="p4w:X")
db.tdata0.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 5.0", f2="p4w:Win 95+", f3="p4w:5", f4="p4w:C")
db.tdata0.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 5.5", f2="p4w:Win 95+", f3="p4w:5.5", f4="p4w:A")
db.tdata0.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 6", f2="p4w:Win 98+", f3="p4w:6", f4="p4w:A")
db.tdata0.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 7", f2="p4w:Win XP SP2+", f3="p4w:7", f4="p4w:A")
db.tdata0.insert(f0="p4w:Trident", f1="p4w:AOL browser (AOL desktop)", f2="p4w:Win XP", f3="p4w:6", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.7", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.5", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Firefox 2.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Firefox 3.0", f2="p4w:Win 2k+ / OSX.3+", f3="p4w:1.9", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Camino 1.0", f2="p4w:OSX.2+", f3="p4w:1.8", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Camino 1.5", f2="p4w:OSX.3+", f3="p4w:1.8", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Netscape 7.2", f2="p4w:Win 95+ / Mac OS 8.6-9.2", f3="p4w:1.7", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Netscape Browser 8", f2="p4w:Win 98SE+", f3="p4w:1.7", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Netscape Navigator 9", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.1", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.1", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.2", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.2", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.3", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.3", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.4", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.4", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.5", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.5", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.6", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.6", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.7", f2="p4w:Win 98+ / OSX.1+", f3="p4w:1.7", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.8", f2="p4w:Win 98+ / OSX.1+", f3="p4w:1.8", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Seamonkey 1.1", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
db.tdata0.insert(f0="p4w:Gecko", f1="p4w:Epiphany 2.20", f2="p4w:Gnome", f3="p4w:1.8", f4="p4w:A")
db.tdata0.insert(f0="p4w:Webkit", f1="p4w:Safari 1.2", f2="p4w:OSX.3", f3="p4w:125.5", f4="p4w:A")
db.tdata0.insert(f0="p4w:Webkit", f1="p4w:Safari 1.3", f2="p4w:OSX.3", f3="p4w:312.8", f4="p4w:A")
db.tdata0.insert(f0="p4w:Webkit", f1="p4w:Safari 2.0", f2="p4w:OSX.4+", f3="p4w:419.3", f4="p4w:A")
db.tdata0.insert(f0="p4w:Webkit", f1="p4w:Safari 3.0", f2="p4w:OSX.4+", f3="p4w:522.1", f4="p4w:A")
db.tdata0.insert(f0="p4w:Webkit", f1="p4w:OmniWeb 5.5", f2="p4w:OSX.4+", f3="p4w:420", f4="p4w:A")
db.tdata0.insert(f0="p4w:Webkit", f1="p4w:iPod Touch / iPhone", f2="p4w:iPod", f3="p4w:420.1", f4="p4w:A")
db.tdata0.insert(f0="p4w:Webkit", f1="p4w:S60", f2="p4w:S60", f3="p4w:413", f4="p4w:A")
db.tdata0.insert(f0="p4w:Presto", f1="p4w:Opera 7.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:-", f4="p4w:A")
db.tdata0.insert(f0="p4w:Presto", f1="p4w:Opera 7.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
db.tdata0.insert(f0="p4w:Presto", f1="p4w:Opera 8.0", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
db.tdata0.insert(f0="p4w:Presto", f1="p4w:Opera 8.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
db.tdata0.insert(f0="p4w:Presto", f1="p4w:Opera 9.0", f2="p4w:Win 95+ / OSX.3+", f3="p4w:-", f4="p4w:A")
db.tdata0.insert(f0="p4w:Presto", f1="p4w:Opera 9.2", f2="p4w:Win 88+ / OSX.3+", f3="p4w:-", f4="p4w:A")
db.tdata0.insert(f0="p4w:Presto", f1="p4w:Opera 9.5", f2="p4w:Win 88+ / OSX.3+", f3="p4w:-", f4="p4w:A")
db.tdata0.insert(f0="p4w:Presto", f1="p4w:Opera for Wii", f2="p4w:Wii", f3="p4w:-", f4="p4w:A")
db.tdata0.insert(f0="p4w:Presto", f1="p4w:Nokia N800", f2="p4w:N800", f3="p4w:-", f4="p4w:A")
db.tdata0.insert(f0="p4w:Presto", f1="p4w:Nintendo DS browser", f2="p4w:Nintendo DS", f3="p4w:8.5", f4="p4w:C/A1")
db.tdata0.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.1", f2="p4w:KDE 3.1", f3="p4w:3.1", f4="p4w:C")
db.tdata0.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.3", f2="p4w:KDE 3.3", f3="p4w:3.3", f4="p4w:A")
db.tdata0.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.5", f2="p4w:KDE 3.5", f3="p4w:3.5", f4="p4w:A")
db.tdata0.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 4.5", f2="p4w:Mac OS 8-9", f3="p4w:-", f4="p4w:X")
db.tdata0.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.1", f2="p4w:Mac OS 7.6-9", f3="p4w:1", f4="p4w:C")
db.tdata0.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.2", f2="p4w:Mac OS 8-X", f3="p4w:1", f4="p4w:C")
db.tdata0.insert(f0="p4w:Misc", f1="p4w:NetFront 3.1", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:C")
db.tdata0.insert(f0="p4w:Misc", f1="p4w:NetFront 3.4", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:A")
db.tdata0.insert(f0="p4w:Misc", f1="p4w:Dillo 0.8", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:X")
db.tdata0.insert(f0="p4w:Misc", f1="p4w:Links", f2="p4w:Text only", f3="p4w:-", f4="p4w:X")
db.tdata0.insert(f0="p4w:Misc", f1="p4w:Lynx", f2="p4w:Text only", f3="p4w:-", f4="p4w:X")
db.tdata0.insert(f0="p4w:Misc", f1="p4w:IE Mobile", f2="p4w:Windows Mobile 6", f3="p4w:-", f4="p4w:C")
db.tdata0.insert(f0="p4w:Misc", f1="p4w:PSP browser", f2="p4w:PSP", f3="p4w:-", f4="p4w:C")
db.tdata0.insert(f0="p4w:Other browsers", f1="p4w:All others", f2="p4w:-", f3="p4w:-", f4="p4w:U")
db.tdata0.insert(f0="p4w:Rendering engine", f1="p4w:Browser", f2="p4w:Platform(s)", f3="p4w:Engine version", f4="p4w:CSS grade")
db.tdata1.insert(f0="p4w:Rendering engine", f1="p4w:Browser", f2="p4w:Platform(s)", f3="p4w:Engine version", f4="p4w:CSS grade")
db.tdata1.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 4.0", f2="p4w:Win 95+", f3="p4w:4", f4="p4w:X")
db.tdata1.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 5.0", f2="p4w:Win 95+", f3="p4w:5", f4="p4w:C")
db.tdata1.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 5.5", f2="p4w:Win 95+", f3="p4w:5.5", f4="p4w:A")
db.tdata1.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 6", f2="p4w:Win 98+", f3="p4w:6", f4="p4w:A")
db.tdata1.insert(f0="p4w:Trident", f1="p4w:Internet Explorer 7", f2="p4w:Win XP SP2+", f3="p4w:7", f4="p4w:A")
db.tdata1.insert(f0="p4w:Trident", f1="p4w:AOL browser (AOL desktop)", f2="p4w:Win XP", f3="p4w:6", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.7", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Firefox 1.5", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Firefox 2.0", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Firefox 3.0", f2="p4w:Win 2k+ / OSX.3+", f3="p4w:1.9", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Camino 1.0", f2="p4w:OSX.2+", f3="p4w:1.8", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Camino 1.5", f2="p4w:OSX.3+", f3="p4w:1.8", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Netscape 7.2", f2="p4w:Win 95+ / Mac OS 8.6-9.2", f3="p4w:1.7", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Netscape Browser 8", f2="p4w:Win 98SE+", f3="p4w:1.7", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Netscape Navigator 9", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.1", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.1", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.2", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.2", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.3", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.3", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.4", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.4", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.5", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.5", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.6", f2="p4w:Win 95+ / OSX.1+", f3="p4w:1.6", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.7", f2="p4w:Win 98+ / OSX.1+", f3="p4w:1.7", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Mozilla 1.8", f2="p4w:Win 98+ / OSX.1+", f3="p4w:1.8", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Seamonkey 1.1", f2="p4w:Win 98+ / OSX.2+", f3="p4w:1.8", f4="p4w:A")
db.tdata1.insert(f0="p4w:Gecko", f1="p4w:Epiphany 2.20", f2="p4w:Gnome", f3="p4w:1.8", f4="p4w:A")
db.tdata1.insert(f0="p4w:Webkit", f1="p4w:Safari 1.2", f2="p4w:OSX.3", f3="p4w:125.5", f4="p4w:A")
db.tdata1.insert(f0="p4w:Webkit", f1="p4w:Safari 1.3", f2="p4w:OSX.3", f3="p4w:312.8", f4="p4w:A")
db.tdata1.insert(f0="p4w:Webkit", f1="p4w:Safari 2.0", f2="p4w:OSX.4+", f3="p4w:419.3", f4="p4w:A")
db.tdata1.insert(f0="p4w:Webkit", f1="p4w:Safari 3.0", f2="p4w:OSX.4+", f3="p4w:522.1", f4="p4w:A")
db.tdata1.insert(f0="p4w:Webkit", f1="p4w:OmniWeb 5.5", f2="p4w:OSX.4+", f3="p4w:420", f4="p4w:A")
db.tdata1.insert(f0="p4w:Webkit", f1="p4w:iPod Touch / iPhone", f2="p4w:iPod", f3="p4w:420.1", f4="p4w:A")
db.tdata1.insert(f0="p4w:Webkit", f1="p4w:S60", f2="p4w:S60", f3="p4w:413", f4="p4w:A")
db.tdata1.insert(f0="p4w:Presto", f1="p4w:Opera 7.0", f2="p4w:Win 95+ / OSX.1+", f3="p4w:-", f4="p4w:A")
db.tdata1.insert(f0="p4w:Presto", f1="p4w:Opera 7.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
db.tdata1.insert(f0="p4w:Presto", f1="p4w:Opera 8.0", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
db.tdata1.insert(f0="p4w:Presto", f1="p4w:Opera 8.5", f2="p4w:Win 95+ / OSX.2+", f3="p4w:-", f4="p4w:A")
db.tdata1.insert(f0="p4w:Presto", f1="p4w:Opera 9.0", f2="p4w:Win 95+ / OSX.3+", f3="p4w:-", f4="p4w:A")
db.tdata1.insert(f0="p4w:Presto", f1="p4w:Opera 9.2", f2="p4w:Win 88+ / OSX.3+", f3="p4w:-", f4="p4w:A")
db.tdata1.insert(f0="p4w:Presto", f1="p4w:Opera 9.5", f2="p4w:Win 88+ / OSX.3+", f3="p4w:-", f4="p4w:A")
db.tdata1.insert(f0="p4w:Presto", f1="p4w:Opera for Wii", f2="p4w:Wii", f3="p4w:-", f4="p4w:A")
db.tdata1.insert(f0="p4w:Presto", f1="p4w:Nokia N800", f2="p4w:N800", f3="p4w:-", f4="p4w:A")
db.tdata1.insert(f0="p4w:Presto", f1="p4w:Nintendo DS browser", f2="p4w:Nintendo DS", f3="p4w:8.5", f4="p4w:C/A1")
db.tdata1.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.1", f2="p4w:KDE 3.1", f3="p4w:3.1", f4="p4w:C")
db.tdata1.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.3", f2="p4w:KDE 3.3", f3="p4w:3.3", f4="p4w:A")
db.tdata1.insert(f0="p4w:KHTML", f1="p4w:Konqureror 3.5", f2="p4w:KDE 3.5", f3="p4w:3.5", f4="p4w:A")
db.tdata1.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 4.5", f2="p4w:Mac OS 8-9", f3="p4w:-", f4="p4w:X")
db.tdata1.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.1", f2="p4w:Mac OS 7.6-9", f3="p4w:1", f4="p4w:C")
db.tdata1.insert(f0="p4w:Tasman", f1="p4w:Internet Explorer 5.2", f2="p4w:Mac OS 8-X", f3="p4w:1", f4="p4w:C")
db.tdata1.insert(f0="p4w:Misc", f1="p4w:NetFront 3.1", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:C")
db.tdata1.insert(f0="p4w:Misc", f1="p4w:NetFront 3.4", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:A")
db.tdata1.insert(f0="p4w:Misc", f1="p4w:Dillo 0.8", f2="p4w:Embedded devices", f3="p4w:-", f4="p4w:X")
db.tdata1.insert(f0="p4w:Misc", f1="p4w:Links", f2="p4w:Text only", f3="p4w:-", f4="p4w:X")
db.tdata1.insert(f0="p4w:Misc", f1="p4w:Lynx", f2="p4w:Text only", f3="p4w:-", f4="p4w:X")
db.tdata1.insert(f0="p4w:Misc", f1="p4w:IE Mobile", f2="p4w:Windows Mobile 6", f3="p4w:-", f4="p4w:C")
db.tdata1.insert(f0="p4w:Misc", f1="p4w:PSP browser", f2="p4w:PSP", f3="p4w:-", f4="p4w:C")
db.tdata1.insert(f0="p4w:Other browsers", f1="p4w:All others", f2="p4w:-", f3="p4w:-", f4="p4w:U")
db.tdata1.insert(f0="p4w:Rendering engine", f1="p4w:Browser", f2="p4w:Platform(s)", f3="p4w:Engine version", f4="p4w:CSS grade")
db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:John Doe", f3="p4w:Urgent! Please read", f4="p4w:12:30 PM")
db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:John Doe", f3="p4w:Urgent! Please read", f4="p4w:12:30 PM")
db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:John Doe", f3="p4w:Urgent! Please read", f4="p4w:12:30 PM")
db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:John Doe", f3="p4w:Urgent! Please read", f4="p4w:12:30 PM")
db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:John Doe", f3="p4w:Urgent! Please read", f4="p4w:12:30 PM")
db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:John Doe", f3="p4w:Urgent! Please read", f4="p4w:12:30 PM")
db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:John Doe", f3="p4w:Urgent! Please read", f4="p4w:12:30 PM")
db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:John Doe", f3="p4w:Urgent! Please read", f4="p4w:12:30 PM")
db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:John Doe", f3="p4w:Urgent! Please read", f4="p4w:12:30 PM")
db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:John Doe", f3="p4w:Urgent! Please read", f4="p4w:12:30 PM")
db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:John Doe", f3="p4w:Urgent! Please read", f4="p4w:12:30 PM")
db.tinvoice0.insert(f0="p4w:Qty", f1="p4w:Product", f2="p4w:Serial #", f3="p4w:Description", f4="p4w:Subtotal")
db.tinvoice0.insert(f0="p4w:1", f1="p4w:Call of Duty", f2="p4w:455-981-221", f3="p4w:El snort testosterone trophy driving gloves handsome", f4="p4w:$64.50")
db.tinvoice0.insert(f0="p4w:1", f1="p4w:Need for Speed IV", f2="p4w:247-925-726", f3="p4w:Wes Anderson umami biodiesel", f4="p4w:$50.00")
db.tinvoice0.insert(f0="p4w:1", f1="p4w:Monsters DVD", f2="p4w:735-845-642", f3="p4w:Terry Richardson helvetica tousled street art master", f4="p4w:$10.70")
db.tinvoice0.insert(f0="p4w:1", f1="p4w:Grown Ups Blue Ray", f2="p4w:422-568-642", f3="p4w:Tousled lomo letterpress", f4="p4w:$25.99")
db.tinvoice1.insert(f0="p4w:Subtotal:", f1="p4w:$250.30")
db.tinvoice1.insert(f0="p4w:Tax (9.3%)", f1="p4w:$10.34")
db.tinvoice1.insert(f0="p4w:Shipping:", f1="p4w:$5.80")
db.tinvoice1.insert(f0="p4w:Total:", f1="p4w:$265.24")