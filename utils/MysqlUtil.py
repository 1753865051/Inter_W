import pymysql
from utils.LogUtil import my_log

class Mysql:
    def __init__(self,host,user,password,database,charset="utf8",port=3306):
        self.log=my_log()
        self.conn=pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
            )
        self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    def fetchone(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def fetchall(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def exec(self,sql):
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.log.error("mysq错误",e)
            return False
        return True
    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not  None:
            self.cursor.close()

if __name__ == '__main__':
    mysql=Mysql("211.103.136.242","test","test123456","meiduo",charset="utf8",port=7090)
    print(mysql.fetchall("select username,password from tb_users"))


# conn=pymysql.connect(
#     host="211.103.136.242",
#     user="test",
#     password="test123456",
#     database="meiduo",
#     charset="utf8",
#     port=7090
# )
# cursor=conn.cursor()
# sql="select username,password from tb_users"
# cursor.execute(sql)
# print(cursor.fetchone())
# cursor.close()
# conn.close()