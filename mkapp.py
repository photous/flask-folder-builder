#function mkapp { mkdir "$1" "$1/static" "$1/templates" "$1/static/css" "$1/static/js" "$1/static/img"; }
import os
import sys


def mkapp(app_name):
    dirs = [app_name,
            '{}/static'.format(app_name),
            '{}/static/css'.format(app_name),
            '{}/static/js'.format(app_name) ,
            '{}/static/img'.format(app_name),
            '{}/templates'.format(app_name)]
    for d in dirs:
        os.mkdir(d)
app = sys.argv[1]
mkapp(app)
