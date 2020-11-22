import time
class MyLog():
    fileurl = './'
    filename = str(time.strftime('%Y-%m-%d'))+ '.log'
    fileobj = None

    def __init__(self):
        self.fileobj = open(self.fileurl + self.filename,'a',encoding='utf-8')

    def log(self,s):
        data = time.strftime('%Y-%m-%d %H:%M:%S')
        msg = data + ' ' + s + '\n'
        self.fileobj.write(msg)

    def __del__(self):
        self.fileobj.close()

w = MyLog()
w.log('今天天气不太好,而且楼下在装修...')
w.log('今天楼上装修能理解,但是说话不算数,很讨厌...')
