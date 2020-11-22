class Person():
    name = '名字'
    age = '年龄'
    sex = '性别'

    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.sex = s

    def say(self):
        print('聊聊人生,谈谈理想...')

    def sing(self):
        print('高歌一曲.....')

    # def __getattribute__(self, item):
    #     try:
    #         res = object.__getattribute__(self,item)
    #         return res[0]+'*'+res[-1]
    #     except:
    #         return False

    def __getattr__(self, item):
        print(item)
        print(1)
        return False

    def __setattr__(self, key, value):
        print(self,key,value)
        print(2)
        object.__setattr__(self,key,value)

    def __delattr__(self, item):
        print(item)
        print(3)
        object.__delattr__(self,item)


zs = Person('张三丰','88','男')
print(zs.name)
print(zs.abc)
zs.abc = 'aabbcc'
print(zs.abc)

del zs.abc
print(zs.abc)