#!/bin/sh

set -e

# データベースが完全に立ち上がるまで待機する。
python manage.py wait_for_db
# collectstaticにより、すべてのstatic files がSTATIC_ROOTへ集まる。nginxはshared volumeを通して、アクセスできる。
python manage.py collectstatic --noinput
# database migrations を行う。
python manage.py migrate

# Runs uWSGI on port 9000 with 4 workers. The --master flag is used to ensure the daemon runs in the foreground, so the log outputs are sent to the Docker console. The --enable-threads will enable multi-threading in our app, and --module app.wsgi tells uWSGI to use our wsgi module provided in side the app directory (the default one generated by Django)
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi

# uWSGI を使うためのscriptを書く。