class USB():
    def start(self):
        pass

class Mouse(USB):
    def start(self):
        print('鼠标启动成功')

class KyeBord(USB):
    def start(self):
        print('键盘插入成功')

class Udisk(USB):
    def start(self):
        print('U盘插入成功')

m = Mouse()
k = KyeBord()
u = Udisk()

m.start()
k.start()
u.start()