
## [py4web](http://py4web.com) apps ported from multistars-github-dashboards

You can easily install them on py4web. First you need to install the requirements with:

   `python3 -m pip install  --upgrade gunicorn gevent `

(it' better on a virtual environment - and unfortunately this make it impossible to use them with the binary installation).

Then goto the py4web folder and:

   `git clone https://github.com/ali96343/facep4w    # this will copy all the apps on the facep4w subfolder`
   
   `./py4web.py run facep4w  -w 4`

By default it will display the bulma app on http://127.0.0.1:8000/ , but there are 14 total apps!

1. http://127.0.0.1:8000/bulma
1. http://127.0.0.1:8000/chen
1. http://127.0.0.1:8000/corona
1. http://127.0.0.1:8000/desk
1. http://127.0.0.1:8000/flat
1. http://127.0.0.1:8000/gentelella
1. http://127.0.0.1:8000/kapella
1. http://127.0.0.1:8000/kit
1. http://127.0.0.1:8000/lte3
1. http://127.0.0.1:8000/ngx
1. http://127.0.0.1:8000/notika
1. http://127.0.0.1:8000/tail
1. http://127.0.0.1:8000/volt
1. http://127.0.0.1:8000/wind


### js, jquery, bootstrap, bulma, tailwind, alpine

( forms and tables with pydal and sqlite )

- https://github.com/themesberg/volt-bootstrap-5-dashboard
- https://github.com/ColorlibHQ/AdminLTE
- https://github.com/BootstrapDash/Kapella-Free-Bootstrap-Admin-Template
- https://github.com/BootstrapDash/corona-free-dark-bootstrap-admin-template
- https://github.com/ColorlibHQ/gentelella
- https://github.com/adminkit/adminkit
- https://github.com/BulmaTemplates/bulma-templates
- https://github.com/dropways/deskapp
- https://github.com/tailwindadmin/admin  
- https://github.com/davidgrzyb/tailwind-admin-template
- https://github.com/puikinsh/notika

### angular, vue

( nodejs apps on py4web )

- https://github.com/akveo/ngx-admin
- https://github.com/flatlogic/angular-material-admin
- https://github.com/PanJiaChen/vue-element-admin.git


### Credits

Many Thanks to Massimo Di Pierro for his help  

- https://github.com/web2py/py4web 

Many Thanks to Luca de Alfaro 

- https://sites.google.com/a/ucsc.edu/luca/classes/cmps-183-hypermedia-and-the-web/cse-183-spring-2020 
- https://learn-py4web.github.io/ 
- https://bitbucket.org/luca_de_alfaro/workspace/projects/PY4WEB 

Also many Thanks to py4web-web2py-forums
 
- https://groups.google.com/forum/#!forum/py4web/
- https://groups.google.com/forum/?fromgroups#!forum/web2py/
