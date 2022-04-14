import os, sys
from py4web import action, request, response
from py4web.core import Reloader
import ombott
from datetime import datetime

# https://github.com/jwulf/letsencrypt-nginx-sidecar
# https://martinheinz.dev/blog/34
# https://realpython.com/python-with-statement/


this_dir = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(this_dir, "static")
log404 = os.path.join('/tmp', "404.log")
#log404 = os.path.join(this_dir, "404.log")


def str2file(str_data, file_name, mode="a"):
    with open(file_name, mode) as f:
        f.write(str_data)
    return file_name


@action("/favicon.ico")
def favicon_ico():
    # return ombott.static_file( 'favicon.ico', static_path, )
    response.headers["Content-Type"] = "text/plain"
    response.headers["Content-disposition"] = 'inline; filename="favicon.ico"'
    return ""


@action("/robot.txt")
def robot_txt():
    # return ombott.static_file( 'robot.txt', static_path, )
    response.headers["Content-Type"] = "text/plain"
    response.headers["Content-disposition"] = 'inline; filename="robot.txt"'
    return ""


# socketio driver works before ombott router
@action("/socket.io", overwrite=True)
def socketio_txt():
    return ""


@action("/page_404")
def page_404():
    return ombott.static_file("page_404.html", static_path,)



p4w_apps = None

class Router:

    sys_apps = tuple(
        "_ . README git index static favicon.ico robot.txt examples page_404 socket.io".split()
    )
    FMT = "%d.%m.%Y %H:%M:%S"

    # my_pep: Z === self

    def __init__(Z, route, params):
        Z.route = route
        Z.params = params
        global p4w_apps
        if p4w_apps is None:
             
            #r_lst = {e["rule"].split('/', 2)[1] for e in Reloader.ROUTES}
            r_lst = {e  for e in Reloader.ROUTES}
            p4w_apps = [e for e in r_lst if (e and not e.startswith(Z.sys_apps))]
            str2file( '404-error-start: ' + datetime.now().strftime(Z.FMT) + '\n',log404, mode='w' ) 

        err_str = "404:" + str(dict(route=route, params=params))
        print(err_str)
        str2file(err_str + "\n", log404)
            
        Z.who = {k: v for k, v in request.headers.items()}
        Z.who["user_ip"] = request.environ.get(
            "HTTP_X_FORWARDED_FOR"
        ) or request.environ.get("REMOTE_ADDR")

        Z.who["app"] = "unk"
        Z.who["date"] = datetime.now().strftime(Z.FMT)
        Z.who["route"] = Z.route
        Z.who["params"] = Z.params
        Z.who["method"] = request.environ.get("REQUEST_METHOD")
        Z.who["agent"] = request.environ.get("HTTP_USER_AGENT")

    def is_allow(Z, app_name):
        global p4w_apps
        if app_name and app_name in p4w_apps:
            Z.who["app"] = app_name
            return True
        return False

    @property
    def location(Z,):
        try:
            p = Z.params[0].split('/', 1)
            if Z.is_allow(p[0]):
                return f"/{p[0]}"
        except Exception as ex:
            print(ex)
        return "/page_404"


# @ombott.error(404, "/")
# @ombott.error(404, '/<_:path()>')
@ombott.error(404, "/<params:path>")
def url_not_found(route, params):

    ombott.response.status = 303
    ombott.response.headers["Server"] = "404-logged"
    ombott.response.headers["Location"] = Router(route, params).location
