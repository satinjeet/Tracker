import json
import MySQLdb;

class DBAccess:
    cur = None
    db = None

    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",user="root",passwd="",db="def")
        self.cur = self.db.cursor();

    def save(self, data):
        sql = "INSERT INTO temp(id , content) values (%s , %s)"
        self.cur.execute(sql , (data['key'] , str(data['data']),))

    def update(self, data):
        sql = "UPDATE temp SET content = %s where id = %s"
        self.cur.execute(sql , (str(data['data']) , data['key'],))

    def execs(self, data):
        sql = "SELECT content from temp where id = %s"
        self.cur.execute(sql , (data['key'],))
        dic = self.cur.fetchone()
        if (dic == None):
            self.save(data)
        else:
            self.update(data)
        
        sql = "SELECT content from temp where id = %s"
        self.cur.execute(sql , (data['key'],))
        dic = self.cur.fetchone()
        dic = eval(dic[0])        
        import operator
        b = sorted(dic.iteritems(), key=operator.itemgetter(1))
        self.db.commit()
        return b[-1][0]

