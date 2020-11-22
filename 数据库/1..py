import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='adu0253',
                     db='tlxy',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
try:
    cursor = db.cursor()


    sql = 'insert into users(name,age,sex,classid) values("张三丰",99,"男","lamp111")'

    cursor.execute(sql)

    data = cursor.fetchall()
finally:
    db.close()
    # print(data)

