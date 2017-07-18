#encoding:utf-8
#name:mod_db.py
import redis
from engine.logger import getLogger
from components.database.configure import getConfigInfo


class redis_db(object):
    def __init__(self):
        serv = getConfigInfo('Redis')
        self._host = serv['host']
        self._port = serv['port']
        self.__logger = getLogger('Redis')
        self._conn = self.connect()

    def connect(self):
        conn = False
        try:
            conn=redis.StrictRedis(host=self._host,port=self._port)
        except Exception,data:
            self._logger.error("connect database failed, %s" % data)
            conn = False
        return conn

    def writekey(self,key,value):
        flag = False
        if(self._conn):
            try:
                self._conn.set(key,value)
                flag = True
            except Exception, data:
                flag = False
                self._logger.warn("write database exception, %s" % data)

    def readkey(self,key):
        if(self._conn):
            try:
                value=self._conn.get(key)
            except Exception,data:
                self._logger.warn("read database exception, %s" % data)
        return value

    def deletekey(self,key):
        if(self._conn):
            try:
                value=self._conn.delete(key)
            except Exception,data:
                self._logger.warn("delete database exception, %s" % data)
        return value

if __name__ == "__main__":
    redis_db = redis_db()
    redis_db.writekey('key1','aaa')
    print redis_db.readkey('key1')
    print redis_db.deletekey('key1')
    print redis_db.readkey('key1')
