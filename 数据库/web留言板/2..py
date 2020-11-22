import pymysql
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():

    data = model('select * from lyb')

    return render_template('index.html',data=data)

@app.route('/add')
def add():
    return render_template('add.html')


def model(sql):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='adu0253',
                         db='tlxy',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    try:
        cursor = db.cursor()

        row = cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        if data:
            return data
        else:
            return row
    finally:
        db.close()
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port='8080')