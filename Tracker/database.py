import json
import MySQLdb
import operator
from db_base import DbBase

class DBAccess(DbBase):
    cur = None
    db = None

    def __init__(self):
        self.db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.database)
        self.cur = self.db.cursor();

    def save(self, data):
        sql = "INSERT INTO " + self.table + "(id , content) values (%s , %s)"
        self.cur.execute(sql , (data['key'] , str(data['data']),))

    def update(self, data):
        sql = "UPDATE " + self.table + " SET content = %s where id = %s"
        self.cur.execute(sql , (str(data['data']) , data['key'],))

    def get(self, data):
        sql = "SELECT content from " + self.table + " where id = %s"
        self.cur.execute(sql , (data['key'],))
        return self.cur.fetchone()

    def execs(self, data):
        dic = self.get(data)
        if (dic == None):
            self.save(data)
        else:
            self.update(data)
        
        dic = self.get(data)
        dic = eval(dic[0])        
        b = sorted(dic.iteritems(), key=operator.itemgetter(1))
        self.db.commit()
        return b[-1][0]

