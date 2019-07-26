python3 dl.py {{ filename  }} ./static.zip
# config files:
# nginx
/etc/nginx/sites-enabled/159.100.242.211.conf

# uwsgi
python3 -m pipenv run uwsgi --http-socket :8080 --wsgi-file app.py

# service
/etc/systemd/system/FlaskRTP.service
