import os, sys
from py4web import action, request, response
from py4web.core import Reloader, PY4WEB_CMD
import ombott
from datetime import datetime

# https://github.com/jwulf/letsencrypt-nginx-sidecar
# https://martinheinz.dev/blog/34
# https://realpython.com/python-with-statement/


this_dir = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(this_dir, "static")
log404 = os.path.join("/tmp", "404.log")
# log404 = os.path.join(this_dir, "404.log")


# from py4web.core import Template, action

# def render_template(data, html):
#    context = dict(output=data)
#    Template(html).on_success(context)
#    return context['output']

# @action('index')
# def index():
#     d = dict(a='hello', b='world')
#     return render_template(d, 'generic.html')


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
    return ombott.static_file(
        "page_404.html",
        static_path,
    )


FMT = "%d.%m.%Y %H:%M:%S"

def apps_list():
    apps_dir = os.environ["PY4WEB_APPS_FOLDER"]
    return sorted ( [ k  for k in Reloader.ROUTES.keys()  
              if ( 
                 not k.startswith( ('.','_')  )   
                 and (os.path.isdir(os.path.join(apps_dir, k)))
              )
            ]
           )


p4w_apps=  apps_list()

class Router:

    # my_pep: Z === self

    def __init__(Z, route, params):
        Z.route = route
        Z.params = params
        err_str = "404:" + str(dict(route=route, params=params))
        print(err_str)
        str2file(err_str + "\n", log404)

        Z.who = {k: v for k, v in request.headers.items()}
        Z.who["user_ip"] = request.environ.get(
            "HTTP_X_FORWARDED_FOR"
        ) or request.environ.get("REMOTE_ADDR")

        Z.who["app"] = "unk"
        Z.who["date"] = datetime.now().strftime(FMT)
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
    def location(
        Z,
    ):
        global p4w_apps
        try:
            if Z.route == "/":
                return p4w_apps[0] if p4w_apps else "/page_404"
            p = Z.params[0].split("/", 1)
            if Z.is_allow(p[0]):
                return f"/{p[0]}"
        except Exception as ex:
            print(ex)
        # return "/page_404"
        return p4w_apps[0] if p4w_apps else "/page_404"


# @ombott.error(404, "/")
# @ombott.error(404, '/<_:path()>')
@ombott.error(404, "/")
@ombott.error(404, "/<params:path>")
def url_not_found(route="/", params=[]):
    print(str(dict(route=route, params=params)))
    ombott.response.status = 303
    # ombott.response.headers["Server"] = "404-logged"
    ombott.response.headers["Location"] = Router(route, params).location
