from celery.result import AsyncResult
from components.database.mongo import *

def get_mongodb_inst():
    return mongo_db(collection = "tasks_info")

def add_task(strategy_id, task_id):
    db = get_mongodb_inst()
    task_dic = {'strategy_id':strategy_id, 'task_id': task_id}
    db.update({'strategy_id':strategy_id}, task_dic, upsert=True)

def remove_task(strategy_id):
    db = get_mongodb_inst()
    db.delete( {'strategy_id': strategy_id})

def find_task(strategy_id):
    db = get_mongodb_inst()
    return db.read( { 'strategy_id': strategy_id} )['task_id']

def find_strategy(task_id):
    db = get_mongodb_inst()
    return db.read( { 'task_id': task_id} )['strategy_id']

def get_task_status(strategy_id):
    return AsyncResult(find_task(strategy_id)).status

def stop_task(task_id):
    return AsyncResult(find_task(task_id)).revoke(terminate=True)

if __name__ == '__main__':
    add_task("1234567", 111)
    add_task("1234566", 112)
    add_task("1234565", 113)
    print find_task("1234565")
    remove_task("1234565")
