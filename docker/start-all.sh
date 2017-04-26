#/bin/bash
redis-server /etc/redis/redis.conf &
mongod --bind_ip 0.0.0.0 -f /etc/mongod.conf &

jupyter notebook --allow-root --generate-config
#password='123456'
echo "c.NotebookApp.password = u'sha1:99fe94ebc806:03a62bee4303e6db8ec0c9d03569365f46e0cc67'" >> /root/.jupyter/jupyter_notebook_config.py
jupyter notebook --allow-root --port=8888 --ip=0.0.0.0  --notebook-dir=/notebook &

python manage.py celery worker --loglevel=info &
python manage.py celery flower &
python manage.py runserver 0.0.0.0:8080 --noreload