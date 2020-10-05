from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate


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
    'dfindex1',
    Field('f0','string'),
    )

db.define_table(
    'dfindex30',
    Field('f0','string'),
    )

db.define_table(
    'dfindex20',
    Field('f0','string'),
    )

db.define_table(
    'dfindex21',
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
    Field('f0','string'),
    )

db.define_table(
    'dfwidgets7',
    Field('f0','string'),
    )

db.define_table(
    'dfwidgets8',
    Field('f0','string'),
    )

db.define_table(
    'dfwidgets9',
    Field('f0','string'),
    )

db.define_table(
    'dfwidgets10',
    Field('f0','string'),
    )

db.define_table(
    'dftopXnav0',
    Field('f0','string'),
    )

db.define_table(
    'dftopXnavXsidebar0',
    Field('f0','string'),
    )

db.define_table(
    'dfboxed0',
    Field('f0','string'),
    )

db.define_table(
    'dffixedXsidebar0',
    Field('f0','string'),
    )

db.define_table(
    'dffixedXsidebarXcustom0',
    Field('f0','string'),
    )

db.define_table(
    'dffixedXtopnav0',
    Field('f0','string'),
    )

db.define_table(
    'dffixedXfooter0',
    Field('f0','string'),
    )

db.define_table(
    'dfcollapsedXsidebar0',
    Field('f0','string'),
    )

db.define_table(
    'dfchartjs0',
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
    'dfmodals0',
    Field('f0','string'),
    )

db.define_table(
    'dfnavbar0',
    Field('f0','string'),
    )

db.define_table(
    'dfnavbar1',
    Field('f0','string'),
    )

db.define_table(
    'dfnavbar2',
    Field('f0','string'),
    )

db.define_table(
    'dfnavbar3',
    Field('f0','string'),
    )

db.define_table(
    'dfnavbar4',
    Field('f0','string'),
    )

db.define_table(
    'dfnavbar5',
    Field('f0','string'),
    )

db.define_table(
    'dfnavbar6',
    Field('f0','string'),
    )

db.define_table(
    'dftimeline0',
    Field('f0','string'),
    )

db.define_table(
    'dfribbons0',
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
    'dfvalidation0',
    Field('f0','string'),
    )

db.define_table(
    'dfvalidation1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','boolean'),
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
    'dfjsgrid0',
    Field('f0','string'),
    )

db.define_table(
    'dfcalendar0',
    Field('f0','string'),
    )

db.define_table(
    'dfgallery0',
    Field('f0','string'),
    )

db.define_table(
    'dfmailbox0',
    Field('f0','string'),
    )

db.define_table(
    'dfcompose0',
    Field('f0','string'),
    )

db.define_table(
    'dfreadXmail0',
    Field('f0','string'),
    )

db.define_table(
    'dfinvoice0',
    Field('f0','string'),
    )

db.define_table(
    'dfprofile0',
    Field('f0','string'),
    )

db.define_table(
    'dfprofile1',
    Field('f0','string'),
    )

db.define_table(
    'dfprofile2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','text'),
    )

db.define_table(
    'dfeXcommerce0',
    Field('f0','string'),
    )

db.define_table(
    'dfprojects0',
    Field('f0','string'),
    )

db.define_table(
    'dfprojectXadd0',
    Field('f0','string'),
    )

db.define_table(
    'dfprojectXedit0',
    Field('f0','string'),
    )

db.define_table(
    'dfprojectXdetail0',
    Field('f0','string'),
    )

db.define_table(
    'dfcontacts0',
    Field('f0','string'),
    )

db.define_table(
    'dffaq0',
    Field('f0','string'),
    )

db.define_table(
    'dfcontactXus0',
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
    Field('f4','boolean'),
    )

db.define_table(
    'dfforgotXpassword0',
    Field('f0','string'),
    )

db.define_table(
    'dfrecoverXpassword0',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dfloginXv20',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','boolean'),
    )

db.define_table(
    'dfregisterXv20',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','boolean'),
    )

db.define_table(
    'dfforgotXpasswordXv20',
    Field('f0','string'),
    )

db.define_table(
    'dfrecoverXpasswordXv20',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'dflockscreen0',
    Field('f0','string'),
    )

db.define_table(
    'dflegacyXuserXmenu0',
    Field('f0','string'),
    )

db.define_table(
    'dflanguageXmenu0',
    Field('f0','string'),
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
    'dfpace0',
    Field('f0','string'),
    )

db.define_table(
    'dfblank0',
    Field('f0','string'),
    )

db.define_table(
    'dfstarter0',
    Field('f0','string'),
    )

db.define_table(
    'dfenhanced0',
    Field('f0','string'),
    )

db.define_table(
    'dfenhanced1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'dfenhancedXresults0',
    Field('f0','string'),
    )

db.define_table(
    'dfenhancedXresults1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tindex30',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tindex20',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tbuttons0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'tbuttons1',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'tbuttons2',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'tbuttons3',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    )

db.define_table(
    'tbuttons4',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
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

db.define_table(
    'tinvoice1',
    Field('f0','string'),
    Field('f1','string'),
    )

db.define_table(
    'tprojects0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    Field('f5','string'),
    )

db.define_table(
    'tprojectXedit0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

db.define_table(
    'tinvoiceXprint0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    Field('f3','string'),
    Field('f4','string'),
    )

db.define_table(
    'tinvoiceXprint1',
    Field('f0','string'),
    Field('f1','string'),
    )

if not db(db.tindex30).count():
    db.tindex30.insert(f0="p4w:Product", f1="p4w:Price", f2="p4w:Sales", f3="p4w:More")
    db.tindex30.insert(f0="p4w:Some Product", f1="p4w:$13 USD", f2="p4w:12% 12,000 Sold", f3="p4w:len0")
    db.tindex30.insert(f0="p4w:Another Product", f1="p4w:$29 USD", f2="p4w:0.5% 123,234 Sold", f3="p4w:len0")
    db.tindex30.insert(f0="p4w:Amazing Product", f1="p4w:$1,230 USD", f2="p4w:3% 198 Sold", f3="p4w:len0")
    db.tindex30.insert(f0="p4w:Perfect Item NEW", f1="p4w:$199 USD", f2="p4w:63% 87 Sold", f3="p4w:len0")
    db.commit()

if not db(db.tindex20).count():
    db.tindex20.insert(f0="p4w:Order ID", f1="p4w:Item", f2="p4w:Status", f3="p4w:Popularity")
    db.tindex20.insert(f0="p4w:OR9842", f1="p4w:Call of Duty IV", f2="p4w:Shipped", f3="p4w:90,80,90,-70,61,-83,63")
    db.tindex20.insert(f0="p4w:OR1848", f1="p4w:Samsung Smart TV", f2="p4w:Pending", f3="p4w:90,80,-90,70,61,-83,68")
    db.tindex20.insert(f0="p4w:OR7429", f1="p4w:iPhone 6 Plus", f2="p4w:Delivered", f3="p4w:90,-80,90,70,-61,83,63")
    db.tindex20.insert(f0="p4w:OR7429", f1="p4w:Samsung Smart TV", f2="p4w:Processing", f3="p4w:90,80,-90,70,-61,83,63")
    db.tindex20.insert(f0="p4w:OR1848", f1="p4w:Samsung Smart TV", f2="p4w:Pending", f3="p4w:90,80,-90,70,61,-83,68")
    db.tindex20.insert(f0="p4w:OR7429", f1="p4w:iPhone 6 Plus", f2="p4w:Delivered", f3="p4w:90,-80,90,70,-61,83,63")
    db.tindex20.insert(f0="p4w:OR9842", f1="p4w:Call of Duty IV", f2="p4w:Shipped", f3="p4w:90,80,90,-70,61,-83,63")
    db.commit()

if not db(db.tbuttons0).count():
    db.tbuttons0.insert(f0="p4w:Normal", f1="p4w:Large .btn-lg", f2="p4w:Small .btn-sm", f3="p4w:Extra Small .btn-xs", f4="p4w:Flat .btn-flat", f5="p4w:Disabled .disabled")
    db.tbuttons0.insert(f0="p4w:Default", f1="p4w:Default", f2="p4w:Default", f3="p4w:Default", f4="p4w:Default", f5="p4w:Default")
    db.tbuttons0.insert(f0="p4w:Primary", f1="p4w:Primary", f2="p4w:Primary", f3="p4w:Primary", f4="p4w:Primary", f5="p4w:Primary")
    db.tbuttons0.insert(f0="p4w:Secondary", f1="p4w:Secondary", f2="p4w:Secondary", f3="p4w:Secondary", f4="p4w:Secondary", f5="p4w:Secondary")
    db.tbuttons0.insert(f0="p4w:Success", f1="p4w:Success", f2="p4w:Success", f3="p4w:Success", f4="p4w:Success", f5="p4w:Success")
    db.tbuttons0.insert(f0="p4w:Info", f1="p4w:Info", f2="p4w:Info", f3="p4w:Info", f4="p4w:Info", f5="p4w:Info")
    db.tbuttons0.insert(f0="p4w:Danger", f1="p4w:Danger", f2="p4w:Danger", f3="p4w:Danger", f4="p4w:Danger", f5="p4w:Danger")
    db.tbuttons0.insert(f0="p4w:Warning", f1="p4w:Warning", f2="p4w:Warning", f3="p4w:Warning", f4="p4w:Warning", f5="p4w:Warning")
    db.commit()

if not db(db.tbuttons1).count():
    db.tbuttons1.insert(f0="p4w:Normal", f1="p4w:Large .btn-lg", f2="p4w:Small .btn-sm", f3="p4w:Extra Small .btn-xs", f4="p4w:Flat .btn-flat", f5="p4w:Disabled .disabled")
    db.tbuttons1.insert(f0="p4w:Primary", f1="p4w:Primary", f2="p4w:Primary", f3="p4w:Primary", f4="p4w:Primary", f5="p4w:Primary")
    db.tbuttons1.insert(f0="p4w:Secondary", f1="p4w:Secondary", f2="p4w:Secondary", f3="p4w:Secondary", f4="p4w:Secondary", f5="p4w:Secondary")
    db.tbuttons1.insert(f0="p4w:Success", f1="p4w:Success", f2="p4w:Success", f3="p4w:Success", f4="p4w:Success", f5="p4w:Success")
    db.tbuttons1.insert(f0="p4w:Info", f1="p4w:Info", f2="p4w:Info", f3="p4w:Info", f4="p4w:Info", f5="p4w:Info")
    db.tbuttons1.insert(f0="p4w:Danger", f1="p4w:Danger", f2="p4w:Danger", f3="p4w:Danger", f4="p4w:Danger", f5="p4w:Danger")
    db.tbuttons1.insert(f0="p4w:Warning", f1="p4w:Warning", f2="p4w:Warning", f3="p4w:Warning", f4="p4w:Warning", f5="p4w:Warning")
    db.commit()

if not db(db.tbuttons2).count():
    db.tbuttons2.insert(f0="p4w:Normal", f1="p4w:Large .btn-lg", f2="p4w:Small .btn-sm", f3="p4w:Extra Small .btn-xs", f4="p4w:Flat .btn-flat", f5="p4w:Disabled .disabled")
    db.tbuttons2.insert(f0="p4w:Primary", f1="p4w:Primary", f2="p4w:Primary", f3="p4w:Primary", f4="p4w:Primary", f5="p4w:Primary")
    db.tbuttons2.insert(f0="p4w:Secondary", f1="p4w:Secondary", f2="p4w:Secondary", f3="p4w:Secondary", f4="p4w:Secondary", f5="p4w:Secondary")
    db.tbuttons2.insert(f0="p4w:Success", f1="p4w:Success", f2="p4w:Success", f3="p4w:Success", f4="p4w:Success", f5="p4w:Success")
    db.tbuttons2.insert(f0="p4w:Info", f1="p4w:Info", f2="p4w:Info", f3="p4w:Info", f4="p4w:Info", f5="p4w:Info")
    db.tbuttons2.insert(f0="p4w:Danger", f1="p4w:Danger", f2="p4w:Danger", f3="p4w:Danger", f4="p4w:Danger", f5="p4w:Danger")
    db.tbuttons2.insert(f0="p4w:Warning", f1="p4w:Warning", f2="p4w:Warning", f3="p4w:Warning", f4="p4w:Warning", f5="p4w:Warning")
    db.commit()

if not db(db.tbuttons3).count():
    db.tbuttons3.insert(f0="p4w:Button", f1="p4w:Icons", f2="p4w:Flat", f3="p4w:Dropdown")
    db.tbuttons3.insert(f0="p4w:LeftMiddleRight", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
    db.tbuttons3.insert(f0="p4w:LeftMiddleRight", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
    db.tbuttons3.insert(f0="p4w:LeftMiddleRight", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
    db.tbuttons3.insert(f0="p4w:LeftMiddleRight", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
    db.tbuttons3.insert(f0="p4w:LeftMiddleRight", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
    db.commit()

if not db(db.tbuttons4).count():
    db.tbuttons4.insert(f0="p4w:Button", f1="p4w:Icons", f2="p4w:Flat", f3="p4w:Dropdown")
    db.tbuttons4.insert(f0="p4w:TopMiddleBottom", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
    db.tbuttons4.insert(f0="p4w:TopMiddleBottom", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
    db.tbuttons4.insert(f0="p4w:TopMiddleBottom", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
    db.tbuttons4.insert(f0="p4w:TopMiddleBottom", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
    db.tbuttons4.insert(f0="p4w:TopMiddleBottom", f1="p4w:len0", f2="p4w:len0", f3="p4w:12Dropdown linkDropdown link")
    db.commit()

if not db(db.tdata0).count():
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
    db.commit()

if not db(db.tdata1).count():
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
    db.commit()

if not db(db.tmailbox0).count():
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:5 mins ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:28 mins ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:11 hours ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:15 hours ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:Yesterday")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:2 days ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:2 days ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:2 days ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:2 days ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:2 days ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:4 days ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:12 days ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:12 days ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:14 days ago")
    db.tmailbox0.insert(f0="p4w:len0", f1="p4w:len0", f2="p4w:Alexander Pierce", f3="p4w:AdminLTE 3.0 Issue - Trying to find a solution to this problem...", f4="p4w:len0", f5="p4w:15 days ago")
    db.commit()

if not db(db.tinvoice0).count():
    db.tinvoice0.insert(f0="p4w:Qty", f1="p4w:Product", f2="p4w:Serial #", f3="p4w:Description", f4="p4w:Subtotal")
    db.tinvoice0.insert(f0="p4w:1", f1="p4w:Call of Duty", f2="p4w:455-981-221", f3="p4w:El snort testosterone trophy driving gloves handsome", f4="p4w:$64.50")
    db.tinvoice0.insert(f0="p4w:1", f1="p4w:Need for Speed IV", f2="p4w:247-925-726", f3="p4w:Wes Anderson umami biodiesel", f4="p4w:$50.00")
    db.tinvoice0.insert(f0="p4w:1", f1="p4w:Monsters DVD", f2="p4w:735-845-642", f3="p4w:Terry Richardson helvetica tousled street art master", f4="p4w:$10.70")
    db.tinvoice0.insert(f0="p4w:1", f1="p4w:Grown Ups Blue Ray", f2="p4w:422-568-642", f3="p4w:Tousled lomo letterpress", f4="p4w:$25.99")
    db.commit()

if not db(db.tinvoice1).count():
    db.tinvoice1.insert(f0="p4w:Subtotal:", f1="p4w:$250.30")
    db.tinvoice1.insert(f0="p4w:Tax (9.3%)", f1="p4w:$10.34")
    db.tinvoice1.insert(f0="p4w:Shipping:", f1="p4w:$5.80")
    db.tinvoice1.insert(f0="p4w:Total:", f1="p4w:$265.24")
    db.commit()

if not db(db.tprojects0).count():
    db.tprojects0.insert(f0="p4w:#", f1="p4w:Project Name", f2="p4w:Team Members", f3="p4w:Project Progress", f4="p4w:Status", f5="p4w:len0")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:AdminLTE v3 Created 01.01.2019", f2="p4w:len0", f3="p4w:57% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:AdminLTE v3 Created 01.01.2019", f2="p4w:len0", f3="p4w:47% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:AdminLTE v3 Created 01.01.2019", f2="p4w:len0", f3="p4w:77% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:AdminLTE v3 Created 01.01.2019", f2="p4w:len0", f3="p4w:60% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:AdminLTE v3 Created 01.01.2019", f2="p4w:len0", f3="p4w:12% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:AdminLTE v3 Created 01.01.2019", f2="p4w:len0", f3="p4w:35% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:AdminLTE v3 Created 01.01.2019", f2="p4w:len0", f3="p4w:87% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:AdminLTE v3 Created 01.01.2019", f2="p4w:len0", f3="p4w:77% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.tprojects0.insert(f0="p4w:#", f1="p4w:AdminLTE v3 Created 01.01.2019", f2="p4w:len0", f3="p4w:77% Complete", f4="p4w:Success", f5="p4w:View Edit Delete")
    db.commit()

if not db(db.tprojectXedit0).count():
    db.tprojectXedit0.insert(f0="p4w:File Name", f1="p4w:File Size", f2="p4w:len0")
    db.tprojectXedit0.insert(f0="p4w:Functional-requirements.docx", f1="p4w:49.8005 kb", f2="p4w:len0")
    db.tprojectXedit0.insert(f0="p4w:UAT.pdf", f1="p4w:28.4883 kb", f2="p4w:len0")
    db.tprojectXedit0.insert(f0="p4w:Email-from-flatbal.mln", f1="p4w:57.9003 kb", f2="p4w:len0")
    db.tprojectXedit0.insert(f0="p4w:Logo.png", f1="p4w:50.5190 kb", f2="p4w:len0")
    db.tprojectXedit0.insert(f0="p4w:Contract-10_12_2014.docx", f1="p4w:44.9715 kb", f2="p4w:len0")
    db.commit()

if not db(db.tinvoiceXprint0).count():
    db.tinvoiceXprint0.insert(f0="p4w:Qty", f1="p4w:Product", f2="p4w:Serial #", f3="p4w:Description", f4="p4w:Subtotal")
    db.tinvoiceXprint0.insert(f0="p4w:1", f1="p4w:Call of Duty", f2="p4w:455-981-221", f3="p4w:El snort testosterone trophy driving gloves handsome", f4="p4w:$64.50")
    db.tinvoiceXprint0.insert(f0="p4w:1", f1="p4w:Need for Speed IV", f2="p4w:247-925-726", f3="p4w:Wes Anderson umami biodiesel", f4="p4w:$50.00")
    db.tinvoiceXprint0.insert(f0="p4w:1", f1="p4w:Monsters DVD", f2="p4w:735-845-642", f3="p4w:Terry Richardson helvetica tousled street art master", f4="p4w:$10.70")
    db.tinvoiceXprint0.insert(f0="p4w:1", f1="p4w:Grown Ups Blue Ray", f2="p4w:422-568-642", f3="p4w:Tousled lomo letterpress", f4="p4w:$25.99")
    db.commit()

if not db(db.tinvoiceXprint1).count():
    db.tinvoiceXprint1.insert(f0="p4w:Subtotal:", f1="p4w:$250.30")
    db.tinvoiceXprint1.insert(f0="p4w:Tax (9.3%)", f1="p4w:$10.34")
    db.tinvoiceXprint1.insert(f0="p4w:Shipping:", f1="p4w:$5.80")
    db.tinvoiceXprint1.insert(f0="p4w:Total:", f1="p4w:$265.24")
    db.commit()
