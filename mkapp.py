import os
import sys


def mkapp(app_name):
    dirs = ['{}', '{}/static', '{}/static/sass', '{}/static/js', '{}/static/img', '{}/templates']

    py_files = ['routes.py', 'models.py']
    static_files = ['{s}/sass/style.scss', '{s}/js/main.js', '{s}/img/.gitkeep']
    templates_files = ['{t}/index.html', '{t}/base.html']
    for d in dirs:
        os.mkdir(d.format(app_name))
    for sf in static_files:
        static_file = app_name + '/' + sf.format(s='static')
        open(static_file, 'w').close()
    for f in py_files:
        py_file = app_name + '/' + f 
        open(py_file, 'w').close()

    for tf in templates_files:
        templates_file = app_name + '/' + tf.format(t='templates')
        open(templates_file, 'w').close()
    os.system('cd {}; git init; git add .; git status;'.format(app_name))

if __name__ == '__main__':
    app = sys.argv[1]
    mkapp(app)
