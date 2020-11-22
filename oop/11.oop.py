class Person():
    def __new__(cls, *args, **kwargs):
        print('构造方法触发了')

        return object.__new__(cls)

    def __init__(self,name,age,sex):
        print('初始化方法出发了')
        self.name = name
        self.age = age
        self.sex = sex

    def __call__(self, *args, **kwargs):
        print('你把对象当成了函数调用了')

    def __del__(self):
        print('触发了析构方法')

zs = Person('张三丰','108','男')
# print(zs)
