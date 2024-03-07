#!/usr/bin/env bash
# A bash script that sets up your web servers for the deployment of web_static
# update and install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
# make folders and html file
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "Holberton School" >> /data/web_static/releases/test/index.html
# creating a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "35i\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
