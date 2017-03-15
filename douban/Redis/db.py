import redis
class DB:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = '6379'

    def initialize(self):
        pool = redis.ConnectionPool(host = self.ip, port = self.port)
        r = redis.Redis(connection_pool=pool)
        return r

    def hset(self,db,name,key,value):
        db.hset(name, key, value)

    def hexist(self, db, name ,key):
        Boolean = db.hexists(name, key)
        return Boolean


