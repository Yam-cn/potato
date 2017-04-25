from pymongo import MongoClient

class MongoDBHelper(object):
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client['potatodb']
        
    def getTaskCollection(self):
        return self.db.tasks_info

def add_task(task_id, task):
    mongoDBHelper = MongoDBHelper()
    task_table = mongoDBHelper.getTaskCollection()
    task_dic = {'strategy_id':task_id, 'task': task}
    task_table.update({'strategy_id':task_id}, task_dic, True )

def remove_task(task_id):
    mongoDBHelper = MongoDBHelper()
    task_table = mongoDBHelper.getTaskCollection()
    task_table.remove( {'strategy_id': task_id})
    
def find_task(task_id):
    mongoDBHelper = MongoDBHelper()
    task_table = mongoDBHelper.getTaskCollection()
    return task_table.find_one( { "strategy_id": task_id} )["task"]
    
if __name__ == '__main__':
    add_task("1234567", 111)
    add_task("1234566", 112)
    add_task("1234565", 113)
    print find_task("1234565")
    remove_task("1234565")
