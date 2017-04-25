# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.decorators import task

#@shared_task
@task()
def runAlgo(algo_file, para):
    a = open('/usr/lib/python2.7/site-packages/pyalgotrade-cn/stratlib/%s'%(algo_file,))
    lines = a.read()
    
    global para_list
    para_list = para
    print algo_file, para_list
    exec(lines, globals())
    print 'task end'
def add(x, y):
    return x + y
