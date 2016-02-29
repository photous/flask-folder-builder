# Flask folders builder
### A simple yet powerful function to create the folders you need !
# Get Started
Add the following to your `~/.bashrc`
```
function mkapp { mkdir "$1" "$1/static" "$1/templates" "$1/static/css" "$1/static/js" "$1/static/img"; }
```
Now, if you want to create the directories:
```
.
├── app
│   ├── static
│   │   ├── css
│   │   ├── img
│   │   └── js
│   ├── templates

```
Just run the following command:
```
$ mkapp app
```

# The Python Way:
If you don't want to use bash, You can do the same in pure Python, Just clone this repo, and execute the mkapp.py followed by your application's name:
```
python mkapp.py Myapp
```
