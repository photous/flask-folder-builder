# Put this in your ~/.bashrc file.
# Create a new app by running: `mkapp my_app`
function mkapp { mkdir -p "$1"/{static/{js,img,sass},templates};
    cd $1
    s=static
    touch routes.py models.py $s/js/main.js $s/img/.gitkeep $s/sass/style.scss templates/index.html templates/base.html;
    git init; git add .; git status; 
 }
