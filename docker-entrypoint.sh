#!/bin/bash

export TERM=xterm

if [ ! -d 'logs' ]; then

    mkdir -p logs
    mkdir -p logs/nginx
    mkdir -p logs/app

fi

cd backend

python3 migrate.py db upgrade

cd  $HOME

if [ "$ENVIRONMENT" = "DEV" ] ; then

    sudo cp $HOME/docker/nginx-dev.conf /etc/nginx/nginx.conf
    screen -dmS BACKEND bash -c 'flask run'

else

    sudo cp $HOME/docker/nginx-uwsgi.conf /etc/nginx/nginx.conf
    screen -dmS BACKEND bash -c 'uwsgi uwsgi.ini'

fi

cd frontend

npm install

screen -dmS FRONTEND bash -c 'npm start'

cd $HOME

sudo nginx

tail -f logs/nginx/access.log -f logs/nginx/error.log
