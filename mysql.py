# encoding: utf-8
import  pymysql
from datetime import datetime
from itertools import chain
todayDate = datetime.now().strftime("%Y%m%d")

print(todayDate)


# 打开数据库连接

db = pymysql.connect(host='',
                     user='',
                     port= ,
                     password='',
                     database='')

# 使用 cursor() 方法创建一个游标对象
cursor = db.cursor()


# print("Database version : %s " % data)#

sql2 = "select * from  table_name where createtime like '%s%%' "  %todayDate
print(sql2)
try :
    # 执行SQL语句
    result = cursor.execute(sql2)
    # 提交到数据库执行
    # db.commit()
    result = cursor.fetchall()

except pymysql.Error as e:
    print(e.args)
    #回滚
    db.rollback()
#数据库关闭连接
db.close()
resultList = list(chain.from_iterable(result))
print(resultList)

