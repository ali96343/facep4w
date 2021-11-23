


import os
from py4web import action, request, abort, redirect, URL, Field, HTTP
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A
from py4web.core import Template, Reloader


from .common import db, session, T, cache, authenticated, unauthenticated, auth
from .settings import APP_NAME

import ombott



## exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)

#
# generated by unbun https://github.com/ali96343/unbundler
#
# 10:13:50 12.10.2021 MSK
# src: https://github.com/flatlogic/angular-material-admin 
#



@action('index', method=["GET", "POST"] )
@action('index.html', method=["GET", "POST"] )
@action('static/tte/index', method=["GET", "POST"] )
@action('static/tte/index.html', method=["GET", "POST"] )
@action.uses( db, session, T, Template('index.html', delimiters='[%[ ]]',) )
#
def index(param=None):
   ctrl_info= "ctrl: index, view: index.html"
   if not param is None:
       print (param)
   return locals()




#Glb= {'debug': True, 'my_app_name': APP_NAME, 'tte_path': '/static/tte'}
Glb= {'debug': True, 'my_app_name': "flat", 'tte_path': '/static/tte'}

# @ombott.error(404, '/web<_:path()>')
# @ombott.error(404, '/web/<params:path>')
@ombott.error(404, f"/{APP_NAME}")
def url_not_found(route, params):
    # print ( str(dict(route=route, params=params))  )

    ombott.response.status = 303
    ombott.response.headers["Location"] = f"/{APP_NAME}"
    #ombott.response.headers['Location'] = route #f'/{APP_NAME}'



from pydal.restapi import RestAPI, Policy

policy = Policy()

policy.set('*', 'GET', authorize=True, allowed_patterns=['*'])
policy.set('*', 'PUT', authorize=True)
policy.set('*', 'POST', authorize=True)
policy.set('*', 'DELETE', authorize=True)

@action('api/<tablename>/', method=["GET", "POST", "PUT", "DELETE"])
@action('api/<tablename>/<rec_id>', method=["GET", "POST", "PUT", "DELETE"])
def api(tablename, rec_id=None):
    return RestAPI(db, policy)(request.method,
                               tablename,
                               rec_id,
                               request.GET,
                               request.POST
                               )
#
# curl -X  GET   http://localhost:8000/flat/api/test_table/
# curl -X  GET   http://localhost:8000/flat/api/test_table/9
# curl -X DELETE  http://localhost:8000/flat/api/test_table/2
# curl -X POST -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/flat/api/test_table/
# curl -X PUT -d 'f0=1111111&f1=2222222222&f2=33333333333' http://localhost:8000/flat/api/test_table/19
# curl -X POST -d f0=1111111   -d f1=2222222222 -d f2=8888888888  http://localhost:8000/flat/api/test_table/
#
#  pip install httpie
#  http         localhost:8000/flat/api/test_table/
#  http -f POST localhost:8000/flat/api/test_table/ f0=111111 f1=2222222 f2=333333
#  http -f DELETE localhost:8000/flat/api/test_table/2
#  http -f PUT localhost:8000/flat/api/test_table/2 f0=111111 f1=2222222 f2=333333
