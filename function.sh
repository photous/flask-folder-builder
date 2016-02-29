
function mkapp {  mkdir -p $1/{'static','static/css','static/js','static/img','templates'}; }

# The following also works, but the above is shorter
#function mkapp { mkdir "$1" "$1/static" "$1/templates" "$1/static/css" "$1/static/js" "$1/static/img"; }
