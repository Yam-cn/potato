# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.decorators import task

class Task:
    task_id = None

def set_task_id(id):
    Task.task_id = id

def get_task_id():
    return str(Task.task_id)
 
#@shared_task
@task(bind=True)
def runAlgo(self, ticker, account_id, algo_file, para):
    import os
    strategy_path = os.environ.get('STRATEGYPATH')
    print strategy_path
    import sys
    sys.path.append(strategy_path)
    from importlib import import_module
    print algo_file
    module = algo_file.split('.')[0]
    strat = import_module(module)
    set_task_id(self.request.id)
    print get_task_id()
    strat.run_strategy(ticker, account_id, para)
