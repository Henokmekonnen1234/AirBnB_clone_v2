#!/usr/bin/env bash
#this variable holds ngnix default file path
nginx_conf="/etc/nginx/sites-available/default"
#this will make the folder /data/web_static/releases/test
mkdir -p /data/web_static/releases/test
#this will create index file and add test case in it
echo "<html>\n<head>\n</head>\n<body>\nHolberton School</body>\n
	    </html>\nubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html\n<html>\n
	      <head>\n</head>\n<body>\nHolberton School\n</body>\n
	      </html>" |  sudo tee /data/web_static/releases/test/index.html
#this create smbolic link
ln -s /data/web_static/releases/test/ /data/web_static/current
#this line of code will copy the file
sudo sed -i "/server_name/a \\n\t location /hbnb_static {\\n\talias /data/web_static/current;}" "${nginx_conf}"
