#sudo rm -rf /etc/nginx/sites-enabled/default
#sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo ln -sf /home/box/web/hello.py /etc/gunicorn.d/hello.py
#sudo ln -sf /home/box/web/task.py /etc/gunicorn.d/task.py
#sudo /etc/init.d/gunicorn restart
#gunicorn --bind='0.0.0.0:8080' hello:wsgi_application
sudo /etc/init.d/mysql start
mysql -uroot -e "create database web;"
mysql -uroot -e "create user 'box'@'localhost' identified by '1234';"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
cd ~/web/ask
python3 manage.py makemigrations qa
python3 manage.py migrate