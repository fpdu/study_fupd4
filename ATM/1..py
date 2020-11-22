import pymysql
def data_1():
    db = pymysql.connect('localhost', 'root', 'adu0253', 'tlxy',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        cursor = db.cursor()
        # sql = 'insert into ATM(name,userid,phone,card_id,pwd) value("111","111","111",111,"111")'
        sql = 'insert into ATM(name,userid,phone,card_id,pwd) value("111","111","111",111,"111")'
        cursor.execute(sql)
        db.commit()
        # data = cursor.fetchall()
        # print(data)
    except Exception as e:
        print(f'出错了:{e}')
    finally:
        db.close()

    # print(data)

data_1()