
import os
from py4web import action, request, abort, redirect, URL, Field, HTTP
from yatl.helpers import A
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A
from py4web.core import Template, Reloader

from .common import db, session, T, cache, authenticated, unauthenticated, auth
import bottle

## exposes services necessary to access the db.thing via ajax
publisher = Publisher(db, policy=ALLOW_ALL_POLICY)

#
# AI-biorex, 00:16:40 03.10.2020
# src: https://github.com/akveo/ngx-admin 
#



@action('index', method=["GET", "POST"] )
@action.uses(Template('index.html', delimiters='[%[ ]]',), db, session, T, )
#
def index(param=None):
   ctrl_info= "ctrl: index, view: index.html"
   if not param is None:
       print (param)
   return locals()



Glb= {'debug': True , 'my_app_name' : "ngx", 'pp': '/static/tte' }

@bottle.error(404)
def error404(error):
    def find_app( maybe_app_root):
        for e in Reloader.ROUTES:
            if e['rule'] == maybe_app_root:
                Glb['debug'] and print('     found rule: ', e['rule'] )
                return True
        return False

    my_app = Glb['my_app_name']
    location = f'/{my_app}'
    lx = bottle.request.path.split('/', 2)
    if len(lx) >= 2 and find_app( f'/{lx[1]}'):
        location = f'/{lx[1]}'
        file_prefix = location + Glb['pp']
        location_2x = location + location + '/'
        file_prefix_2x = file_prefix + file_prefix + '/'

        if bottle.request.path.startswith( file_prefix_2x ):
            if len( bottle.request.path ) > len ( file_prefix_2x ):
                location = bottle.request.path.replace( file_prefix, '', 1 )
                Glb['debug'] and print ('     removed: ', file_prefix )

        elif bottle.request.path.startswith( location_2x ):
            if len( bottle.request.path ) > len ( location_2x ):
                location = bottle.request.path.replace( location , '', 1 )
                Glb['debug'] and print ('     removed: ', f'/{lx[1]}')

    if Glb['debug'] == True:
        print (f'404  app=/{my_app}, err_path={bottle.request.path}')
        print  ('     info=', error )
        print (f'     goto_new_path={location}')
        print  ('')

    bottle.response.status = 303
    bottle.response.set_header("Location", location)



from pydal.restapi import RestAPI, Policy

policy = Policy()

policy.set('*', 'GET', authorize=True, allowed_patterns=['*'])
policy.set('*', 'PUT', authorize=True)
policy.set('*', 'POST', authorize=True)
policy.set('*', 'DELETE', authorize=True)

@action('api/<tablename>/')
@action('api/<tablename>/<rec_id>')
def api(tablename, rec_id=None):
    return RestAPI(db, policy)(request.method,
                               tablename,
                               rec_id,
                               request.GET,
                               request.POST
                               )
# /superheroes/rest/api/superhero?name.eq=Superman

