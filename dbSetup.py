import MySQLdb;

class DBSetup:

    def __init__(self):
        db = MySQLdb.connect(host="localhost",user="root",passwd="",db="def")
        cur = db.cursor();
        cur.execute("CREATE TABLE IF NOT EXISTS temp(id varchar(200) , content varchar(200))")

DBSetup()
