import os, sys
from py4web import action, request, response
from py4web.core import Reloader
import ombott

# https://github.com/ali96343/facep4w

this_dir = os.path.dirname( os.path.abspath(__file__) )
file_404 = os.path.join( this_dir, 'static','page_404.html' )

def file2str(file_name, mode='r'):
    code = ""
    try:
        with open(file_name, mode) as f:
            code = f.read()
    except IOError:
        print("File not accessible: ", file_name)
    return code


@action("/favicon.ico", overwrite=True)
def favicon_ico():
    response.headers["Content-Type"] = 'text/plain'
    response.headers["Content-disposition"] = 'inline; filename="favicon.ico"'
    return ''

@action("/robot.txt", overwrite=True)
def robot_txt():
    response.headers["Content-Type"] = 'text/plain'
    response.headers["Content-disposition"] = 'inline; filename="robot.txt"'
    return ''


@action("/socket.io", overwrite=True)
def socketio_txt():
    return ''

@action("/page_404")
def page_404():
    response.headers["Content-Type"] = 'text/html'
    response.headers["Content-disposition"] = 'inline; filename="file_404.html"'
    return file2str( file_404 )


class Router:

    sys_apps = tuple("_ index static favicon.ico robot.txt examples page_404 socket.io".split() )

    def __init__(Z, params):
        Z.params = params
        r_lst = {e["rule"].split(os.sep, 2)[1] for e in Reloader.ROUTES}
        Z.a_lst = [e for e in r_lst if (e and not e.startswith(Z.sys_apps))]
        Z.who = { k:v for k,v in request.headers.items() }
        Z.who['user_ip'] = request.environ.get(
            "HTTP_X_FORWARDED_FOR"
        ) or request.environ.get("REMOTE_ADDR")
        Z.who['method'] = request.environ.get('REQUEST_METHOD')
        #print (Z.who)

    def is_allow(Z, app_name):
        if app_name and app_name in Z.a_lst:
            return True
        return False

    @property
    def location(Z, ):
       l = "/page_404"
       try:
           p = Z.params[0].split(os.sep, 2)
           if Z.is_allow(p[0]):
               l = f"/{p[0]}"
       except Exception as ex:
            print (ex)
       return l


# @ombott.error(404, "/")
# @ombott.error(404, '/<_:path()>')
@ombott.error(404, "/<params:path>")
def url_not_found(route, params):
    print('404: ', str(dict(route=route, params=params)))

    ombott.response.status = 303
    ombott.response.headers["Server"] = 'Xping' 
    ombott.response.headers["Location"] =  Router(params).location


