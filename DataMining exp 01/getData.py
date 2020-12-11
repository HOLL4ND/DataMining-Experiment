import pymysql
db = pymysql.connect(host="localhost",user="root",db="studenttest")
print(db)
cur=db.cursor()
cur.execute("select * from test")
resTuple=cur.fetchall()
cur.close()
db.commit()
db.close()
print(resTuple)
print(type(resTuple[0][3]))
print((resTuple[0][3]))


