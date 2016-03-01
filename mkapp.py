#function mkapp { mkdir "$1" "$1/static" "$1/templates" "$1/static/css" "$1/static/js" "$1/static/img"; }
import os
import sys


def mkapp(app_name):
    dirs = ['{}', '{}/static', '{}/static/css', '{}/static/js', '{}/static/img', '{}/templates']
    for d in dirs:
        os.mkdir(d.format(app_name))


if __name__ == '__main__':
    app = sys.argv[1]
    mkapp(app)
