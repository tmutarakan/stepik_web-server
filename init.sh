sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo ln -sf /home/box/web/hello.py /etc/gunicorn.d/hello.py
#sudo ln -sf /home/box/web/task.py /etc/gunicorn.d/task.py
#sudo /etc/init.d/gunicorn restart
#gunicorn --bind='0.0.0.0:8080' hello:wsgi_application
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE djbase;"
mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'pass123';"
mysql -uroot -e "GRANT ALL ON djbase.* TO 'django'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
cd ~/web/ask
python3 manage.py makemigrations qa
python3 manage.py migrate
#gunicorn --bind='0.0.0.0:8000' ask.wsgi