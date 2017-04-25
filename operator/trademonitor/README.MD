What do I need?
=============

trademonitor version 0.1 runs on,

- Python (2.7, 3.4, 3.5)
- PyPy (5.4, 5.5)

and below 
* MongDB: https://www.mongodb.com/download-center#community
* Djongo: https://www.djangoproject.com/download/
* Redis: https://redis.io/
* Celery: 
* Flower: 
* django-celery: 

Get Started
=============
Pre-condition:
-------------
MongoDB: <br/>
* potatodb<br/>
* Collection: account_info, strategy_info, tasks_info, trade_detail <br/>

Startup:
-------------
export PYTHONPATH=\<pyalgo path\>/pyalgotrade-cn/ <br/>
python manage.py celery worker --loglevel=info <br/>
python manage.py celery flower <br/>
python manage.py runserver 0.0.0.0:8888 --noreload <br/>

Trademonitor is...
=============
- **Simple**

    This is a exsample that how to use 'Trademonitor'
    
- **Highly Available**

    Introduce what is the mechanism to support the Highly Available

- **Fast**

    Introduce the speed...(asynchronous)

- **Flexible**
    
    Modular???

Getting Help
=============
QQ:???????

Contributing
=============
Development of `trademonitor` happens at GitHub: https://github.com/????/trademonitor

You're highly encouraged to participate in the development
of `trademonitor`. If you don't like GitHub (for some reason) you're welcome
to send regular patches.

License
=======
This software is licensed under the `New BSD License`. See the ``LICENSE``
file in the top distribution directory for the full license text.