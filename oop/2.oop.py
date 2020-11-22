class Person():

    name = '名字'
    age = '年龄'
    sex = '性别'

    def sing(self):
        print('会唱......')

    def dance(self):
        print('会跳......')

    def rap(self):
        print(f'我是{self.name}我会rap')

    def func(self):
        print(self)
        print(self.name)
        self.name = '张三三'
        self.sjwz = '80 80 80'
        print(self.sjwz)
        self.rap()

    def func2(self):
        print('我是一个没有self爱的方法doge')

zs = Person()
# zs.func()
zs.name = '张三'
print(zs.name)
zs.func()
zs.rap()
# zs.func2()
# Person.func2()