import MySQLdb, os;
from Tracker import DbBase

class DBSetup(DbBase):

    def __init__(self):
        print "creating database"
        command = "mysql -u%s -p%s -e \"create database %s\"" % (self.user, self.passwd, self.database)
        os.system(command)

        print "creating table"
        db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.database)
        cur = db.cursor();
        cur.execute("CREATE TABLE IF NOT EXISTS %s(id varchar(200) , content varchar(200))" % self.table)

        print "complete"

DBSetup()
