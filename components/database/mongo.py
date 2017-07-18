#encoding:utf-8
#name:mod_db.py
from pymongo import MongoClient
from components.database.configure import getConfigInfo
from engine.logger import getLogger

class mongo_db(object):
    def __init__(self, collection):
        serv = getConfigInfo('Mongo')
        self.__host = serv['host']
        self.__port = serv['port']
        self.__dbname = serv['dbname']
        self.__logger = getLogger('Mongodb')
        self.__client = self.__connect()
        self.__col = self.__client[self.__dbname][collection]

    def __connect(self):
        conn = False
        try:
            conn = MongoClient(host = self.__host, port = int(self.__port))
        except Exception, e:
            self.__logger.error("connect database failed, %s" % str(e))
            conn = False
        return conn

    def get_col(self):
        return self.__col

    def insert(self, doc):
        flag = False
        if(self.__client):
            try:
            	self.__col.insert_one(doc)
            	flag = True
            except Exception, e:
                self.__logger.warn("insert mongodb exception, %s" % str(e))
        return flag

    def update(self, filter, doc, upsert):
        flag = False
        if(self.__client):
            try:
            	self.__col.update_one(filter, {"$set": doc}, upsert)
            	flag = True
            except Exception, e:
            	self.__logger.warn("update monogodb exception, %s" % str(e))
        return flag

    def read(self, filter):
        result = {}
        if(self.__client):
            try:
            	result = self.__col.find_one(filter)
            except Exception, e:
            	self.__logger.warn("find monogodb exception, %s" % str(e))
        return result

    def delete(self, filter):
        flag = False
        if(self.__client):
            try:
            	self.__col.delete_one(filter)
            	flag = True
            except Exception, e:
            	self.__logger.warn("delete_one monogodb exception, %s" % str(e))
        return flag

if __name__ == "__main__":
    col = mongo_db("test_Mongo_API")
    col.update({'2':'b'}, {'2':'b', 'd':'2'}, upsert=True)
    col.update({'3':'b'}, {'2':'b', 'd':'2'}, upsert=True)
    print col.get_col().update_one({'4':'b'}, {"$set":{'2':'b', 'd':'2'}}, upsert=True)
