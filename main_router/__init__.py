from py4web import action

import ombott


@action("/favicon.ico") 
def favi():
    return "it is my favicon"

@action("/robot.txt")
def robo():
    return "it is my robot"

#@ombott.error(404, "/")
#@ombott.error(404, '/<_:path()>')
#@ombott.error(404, '/<params:path>')

#def url_not_found(route, params):
#    print ( str(dict(route=route, params=params))  )
#    ombott.response.status = 303
#    ombott.response.headers['Location'] = 'https://google.com' 

