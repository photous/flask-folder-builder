# Flask folders builder
### A simple yet powerful function to create the folders you need !
# Get Started
Add the following to your `~/.bashrc`
```
function mkapp { mkdir -p "$1"/{static/{js,img,sass},templates};
    cd $1
    s=static
    touch routes.py models.py $s/js/main.js $s/img/.gitkeep $s/sass/style.scss templates/index.html templates/base.html;
    git init; git add .; git status; 
 }
```
Now, if you want to create the directories and files:
```
.
├── app
│   ├── routes.py
│   ├── models.py
│   ├── static
│   │   ├── sass
│   │   |   ├── style.scss
│   │   ├── img
│   │   ├── js
│   │   |   ├── main.js
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
```
Just run the following command:
```
$ mkapp app
```

the command will also initialize a git repository and add all the files to it, then you'll see that you are now in the app folder with the full `git status`

# The Python Way:
If you don't want to use bash, You can do the same in pure Python, Just clone this repo, and execute the mkapp.py followed by your application's name:
```
python mkapp.py Myapp
```
