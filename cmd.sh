#!/bin/bash
# Django commands

# declare a dictionary
declare -A djangoCommands=(
    ["run"]="python manage.py runserver"
    ["m"]="python manage.py migrate"
    ["mms"]="python manage.py makemigrations"
    ["csu"]="python manage.py createsuperuser"
    ["test"]="pytest"
    ["shell"]="python manage.py shell"
    ["dbshell"]="python manage.py dbshell"
    ["help"]="help"
)

if [ -z "$1" ]; then
    echo "No command provided"
    echo "Run 'cmd.sh help' for help"
    exit 1
else
    command=${djangoCommands["$1"]}
fi
command=${djangoCommands["$1"]}

runcmd () {
    echo "Executing: $command"
    eval "$command"
}

runhelp () {
    echo "Usage: cmd.sh [command]"
    echo "Commands:"
    for key in "${!djangoCommands[@]}"; do
        echo "  $key: ${djangoCommands[$key]}"
    done
}
if [ -z "$command" ]; then
    echo "Invalid command"
    echo "Run 'cmd.sh help' for help"
    exit 1
elif [ "$command"  == "help" ]; then
    runhelp "$@"
else
    runcmd "$@"
      
fi
