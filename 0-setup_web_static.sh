#!/usr/bin/env bash
sudo apt update
sudo apt install -y nginx
sudo ufw allow 80
sudp ufw reload 
#this variable holds ngnix default file path
nginx_conf="/etc/nginx/sites-available/default"
#this will make the folder /data/web_static/releases/test
mkdir -p /data/web_static/releases/test
#this will create index file and add test case in it
echo "<html><head></head><body>Holberton School</body></html>" |  sudo tee /data/web_static/releases/test/index.html
#this create smbolic link
ln -s /data/web_static/releases/test/ /data/web_static/current
#this line of code will copy the file
sudo sed -i "/server_name/a \\n\t location /hbnb_static {\\n\talias /data/web_static/current;}" "${nginx_conf}"
#restarting nginx
sudo service nginx restart
