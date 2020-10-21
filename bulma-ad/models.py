from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

#
# py4web app, AI-biorex ported 21.10.2020 14:21:48
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
    'tindex0',
    Field('f0','string'),
    )

db.define_table(
    'tindex1',
    Field('f0','string'),
    )

db.define_table(
    'telements0',
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
    )

db.define_table(
    'tdatatables0',
    Field('f0','string'),
    Field('f1','string'),
    Field('f2','string'),
    )

if not db(db.tindex0).count():
    db.tindex0.insert(f0="p4w:Three")
    db.tindex0.insert(f0="p4w:Five")
    db.tindex0.insert(f0="p4w:Seven")
    db.tindex0.insert(f0="p4w:Ten")
    db.tindex0.insert(f0="p4w:Twelve")
    db.commit()

if not db(db.tindex1).count():
    db.tindex1.insert(f0="p4w:Muhammad ibn Abdullh (PBUH)")
    db.tindex1.insert(f0="p4w:Abu Bakar As Shidiq")
    db.tindex1.insert(f0="p4w:Umar Bin Khattab")
    db.tindex1.insert(f0="p4w:Usman Bin Affan")
    db.tindex1.insert(f0="p4w:Said Bin zaid")
    db.commit()

if not db(db.telements0).count():
    db.telements0.insert(f0="p4w:Pos", f1="p4w:Team", f2="p4w:Pld", f3="p4w:W", f4="p4w:D", f5="p4w:L", f6="p4w:GF", f7="p4w:GA", f8="p4w:GD", f9="p4w:Pts", f10="p4w:Qualification or relegation")
    db.telements0.insert(f0="p4w:Pos", f1="p4w:Team", f2="p4w:Pld", f3="p4w:W", f4="p4w:D", f5="p4w:L", f6="p4w:GF", f7="p4w:GA", f8="p4w:GD", f9="p4w:Pts", f10="p4w:Qualification or relegation")
    db.telements0.insert(f0="p4w:1", f1="p4w:Leicester City (C)", f2="p4w:38", f3="p4w:23", f4="p4w:12", f5="p4w:3", f6="p4w:68", f7="p4w:36", f8="p4w:+32", f9="p4w:81", f10="p4w:Qualification for the Champions League group stage")
    db.telements0.insert(f0="p4w:2", f1="p4w:Arsenal", f2="p4w:38", f3="p4w:20", f4="p4w:11", f5="p4w:7", f6="p4w:65", f7="p4w:36", f8="p4w:+29", f9="p4w:71", f10="p4w:Qualification for the Champions League group stage")
    db.telements0.insert(f0="p4w:3", f1="p4w:Tottenham Hotspur", f2="p4w:38", f3="p4w:19", f4="p4w:13", f5="p4w:6", f6="p4w:69", f7="p4w:35", f8="p4w:+34", f9="p4w:70", f10="p4w:Qualification for the Champions League group stage")
    db.telements0.insert(f0="p4w:4", f1="p4w:Manchester City", f2="p4w:38", f3="p4w:19", f4="p4w:9", f5="p4w:10", f6="p4w:71", f7="p4w:41", f8="p4w:+30", f9="p4w:66", f10="p4w:Qualification for the Champions League play-off round")
    db.telements0.insert(f0="p4w:5", f1="p4w:Manchester United", f2="p4w:38", f3="p4w:19", f4="p4w:9", f5="p4w:10", f6="p4w:49", f7="p4w:35", f8="p4w:+14", f9="p4w:66", f10="p4w:Qualification for the Europa League group stage")
    db.telements0.insert(f0="p4w:6", f1="p4w:Southampton", f2="p4w:38", f3="p4w:18", f4="p4w:9", f5="p4w:11", f6="p4w:59", f7="p4w:41", f8="p4w:+18", f9="p4w:63", f10="p4w:Qualification for the Europa League group stage")
    db.telements0.insert(f0="p4w:7", f1="p4w:West Ham United", f2="p4w:38", f3="p4w:16", f4="p4w:14", f5="p4w:8", f6="p4w:65", f7="p4w:51", f8="p4w:+14", f9="p4w:62", f10="p4w:Qualification for the Europa League third qualifying round")
    db.telements0.insert(f0="p4w:8", f1="p4w:Liverpool", f2="p4w:38", f3="p4w:16", f4="p4w:12", f5="p4w:10", f6="p4w:63", f7="p4w:50", f8="p4w:+13", f9="p4w:60", f10="p4w:len0")
    db.telements0.insert(f0="p4w:9", f1="p4w:Stoke City", f2="p4w:38", f3="p4w:14", f4="p4w:9", f5="p4w:15", f6="p4w:41", f7="p4w:55", f8="p4w:14", f9="p4w:51", f10="p4w:len0")
    db.telements0.insert(f0="p4w:10", f1="p4w:Chelsea", f2="p4w:38", f3="p4w:12", f4="p4w:14", f5="p4w:12", f6="p4w:59", f7="p4w:53", f8="p4w:+6", f9="p4w:50", f10="p4w:len0")
    db.telements0.insert(f0="p4w:11", f1="p4w:Everton", f2="p4w:38", f3="p4w:11", f4="p4w:14", f5="p4w:13", f6="p4w:59", f7="p4w:55", f8="p4w:+4", f9="p4w:47", f10="p4w:len0")
    db.telements0.insert(f0="p4w:12", f1="p4w:Swansea City", f2="p4w:38", f3="p4w:12", f4="p4w:11", f5="p4w:15", f6="p4w:42", f7="p4w:52", f8="p4w:10", f9="p4w:47", f10="p4w:len0")
    db.telements0.insert(f0="p4w:13", f1="p4w:Watford", f2="p4w:38", f3="p4w:12", f4="p4w:9", f5="p4w:17", f6="p4w:40", f7="p4w:50", f8="p4w:10", f9="p4w:45", f10="p4w:len0")
    db.telements0.insert(f0="p4w:14", f1="p4w:West Bromwich Albion", f2="p4w:38", f3="p4w:10", f4="p4w:13", f5="p4w:15", f6="p4w:34", f7="p4w:48", f8="p4w:14", f9="p4w:43", f10="p4w:len0")
    db.telements0.insert(f0="p4w:15", f1="p4w:Crystal Palace", f2="p4w:38", f3="p4w:11", f4="p4w:9", f5="p4w:18", f6="p4w:39", f7="p4w:51", f8="p4w:12", f9="p4w:42", f10="p4w:len0")
    db.telements0.insert(f0="p4w:16", f1="p4w:AFC Bournemouth", f2="p4w:38", f3="p4w:11", f4="p4w:9", f5="p4w:18", f6="p4w:45", f7="p4w:67", f8="p4w:22", f9="p4w:42", f10="p4w:len0")
    db.telements0.insert(f0="p4w:17", f1="p4w:Sunderland", f2="p4w:38", f3="p4w:9", f4="p4w:12", f5="p4w:17", f6="p4w:48", f7="p4w:62", f8="p4w:14", f9="p4w:39", f10="p4w:len0")
    db.telements0.insert(f0="p4w:18", f1="p4w:Newcastle United (R)", f2="p4w:38", f3="p4w:9", f4="p4w:10", f5="p4w:19", f6="p4w:44", f7="p4w:65", f8="p4w:21", f9="p4w:37", f10="p4w:Relegation to the Football League Championship")
    db.telements0.insert(f0="p4w:19", f1="p4w:Norwich City (R)", f2="p4w:38", f3="p4w:9", f4="p4w:7", f5="p4w:22", f6="p4w:39", f7="p4w:67", f8="p4w:28", f9="p4w:34", f10="p4w:Relegation to the Football League Championship")
    db.telements0.insert(f0="p4w:20", f1="p4w:Aston Villa (R)", f2="p4w:38", f3="p4w:3", f4="p4w:8", f5="p4w:27", f6="p4w:27", f7="p4w:76", f8="p4w:49", f9="p4w:17", f10="p4w:Relegation to the Football League Championship")
    db.commit()

if not db(db.tdatatables0).count():
    db.tdatatables0.insert(f0="p4w:No", f1="p4w:Name", f2="p4w:Action")
    db.tdatatables0.insert(f0="p4w:1", f1="p4w:Abu Bakar As-Shiddiq", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:2", f1="p4w:Umar bin Khattab", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:3", f1="p4w:Utsman bin Affan", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:4", f1="p4w:Ali bin Abi Thalib", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:5", f1="p4w:Hamzah bin Abdul-Muththalib", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:6", f1="p4w:Mushab bin Umair", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:7", f1="p4w:Zaid bin Haritsah", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:8", f1="p4w:Jafar bin Abu Thalib", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:9", f1="p4w:Husain bin Ali", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:10", f1="p4w:Saad bin Muadz", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:11", f1="p4w:Ammar bin Yasir", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:12", f1="p4w:Abad bin Bisyr", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:13", f1="p4w:Salim Maula Abi Hudzaifah", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:14", f1="p4w:Al-Bara bin Malik", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:15", f1="p4w:Abu Dujanah", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:16", f1="p4w:Amr bin al-Jamuh", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:17", f1="p4w:Abu Ayyub al-Anshari", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:18", f1="p4w:Abu Thalhah", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:19", f1="p4w:Abdullah bin Jahsy", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:20", f1="p4w:Khubaib bin Adi", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:21", f1="p4w:Ikrimah bin Abu Jahal", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:22", f1="p4w:Khadijah Binti Khuwailid", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:23", f1="p4w:Imam Al-Ghazali", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:24", f1="p4w:Sofyan Ats-Tsauri", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:25", f1="p4w:Khalid bin Walid", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:26", f1="p4w:Utbah bin Ghazwan", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:27", f1="p4w:Mushab bin Umair", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:28", f1="p4w:Muadz bin Jabal", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:29", f1="p4w:Zaid bin Haritsah", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:30", f1="p4w:Fatimah binti Muhammad", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:31", f1="p4w:Bilal bin Rabah", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:32", f1="p4w:Abdullah bin Zubeir", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:33", f1="p4w:Zainab Binti Jahsy Bin Riab", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:34", f1="p4w:Abu Ubaidah bin Jarrah", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:35", f1="p4w:Ibnu Qayyim Al-Jauziyyah", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:36", f1="p4w:Ibnu Katsir", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:37", f1="p4w:Ibnu Taimiyyah", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:38", f1="p4w:Ahmed Deedat", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:39", f1="p4w:Yusuf Qardhawi", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:40", f1="p4w:Imam Muslim", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:41", f1="p4w:Hasan Al Banna", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:42", f1="p4w:Tuanku Tambusai", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:43", f1="p4w:Tuanku Imam Bonjol", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:44", f1="p4w:Sunan Gresik", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:45", f1="p4w:Sunan Ampel", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:46", f1="p4w:Sunan Bonang", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:47", f1="p4w:Sunan Drajat", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:48", f1="p4w:Sunan Kudus", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:49", f1="p4w:Sunan Giri", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:50", f1="p4w:Sunan Kalijaga", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:51", f1="p4w:Sunan Muria", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:52", f1="p4w:Sunan Gunung Jati", f2="p4w:len0")
    db.tdatatables0.insert(f0="p4w:53", f1="p4w:Jumadil Qubro", f2="p4w:len0")
    db.commit()
