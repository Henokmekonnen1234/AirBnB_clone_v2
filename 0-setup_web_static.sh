#!/usr/bin/env bash
sudo apt update
sudo apt-get install -y nginx
sudo ufw allow "Nginx HTTP"
sudo ufw reload
#this variable holds ngnix default file path
nginx_conf="/etc/nginx/sites-available/default"
#this will make the folder /data/web_static/releases/test
mkdir -p /data/web_static/releases/test
#this will create index file and add test case in it
echo "<html><head></head><body>Holberton School</body></html>" |  sudo tee /data/web_static/releases/test/index.html
#this create smbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
#change owner
sudo chown -hR ubuntu:ubuntu /data
#this line of code will copy the file
sudo sed -i "/server_name/a \\n\t location /hbnb_static {\\n\talias /data/web_static/current;}" "${nginx_conf}"
#create smbolic link for nginx
sudo ln -sf "${nginx_conf}" /etc/nginx/sites-enabled/default
#restarting nginx
sudo service nginx restart
