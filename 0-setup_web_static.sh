#!/usr/bin/env bash
#Sets up web servers for the deployment of web_static
apt-get update
apt-get -y install nginx
FILE=/etc/nginx/sites-available/default
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "Holberton School" | tee /data/web_static/releases/test/index.html
ln -sf  /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sudo sed -i '41i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $FILE
service nginx restart
