#!/bin/bash

export TERM=xterm

if [ ! -d 'logs' ]; then

    mkdir -p logs
    mkdir -p logs/nginx
    mkdir -p logs/app

fi

python3 migrate.py db upgrade

if [ "$ENVIRONMENT" = "DEV" ] ; then

    sudo cp $HOME/docker/nginx-dev.conf /etc/nginx/nginx.conf
    screen -dmS APP bash -c 'flask run'

else

    sudo cp $HOME/docker/nginx-uwsgi.conf /etc/nginx/nginx.conf
    screen -dmS APP bash -c 'uwsgi uwsgi.ini'

fi

sudo nginx

cd frontend

npm install
npm start

cd ../

tail -f logs/nginx/access.log -f logs/nginx/error.log
