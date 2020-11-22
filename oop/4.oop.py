import time
class WriteLog():
    fileurl = './'
    filename = '2019-09-19'

    def __init__(self,):
        print('初始化方法触发类.完成文件打开')
        self.fileobj = open(self.fileurl+self.filename,'a',encoding='utf-8')

    def log(self,s):
        print(f'把日志:{s}写入到文件中')

    def __del__(self):
        print("析构方法出发了,关闭打开的文件")
        self.fileobj.close()

# l = WriteLog()
# l.log('今天天气还不错哦......')

# del l
# WriteLog()

class Cart():
    brand = ''

    def __init__(self,b):
        self.brand = b
        print(f'初始化很爱被触动:创建{self.brand}汽车')
    def __del__(self):
        print(f'析构方法触发:{self.brand}汽车已经被销毁了')


bm = Cart('宝马')
bc = Cart('奔驰')
fll = Cart('法拉利')