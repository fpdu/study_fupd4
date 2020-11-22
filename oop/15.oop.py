class PersonName():
    __name = 'abc'

    def __get__(self, instance, owner):
        # print(self,instance,owner)
        print(1)
        return self.__name

    def __set__(self, instance, value):
        # print(self,instance,value)
        print(2)
        self.__name = value

    def __delete__(self, instance):
        # print(self,instance)
        print(3)
        print('不允许删除')

class Person():
    name = PersonName()

zs = Person()
print(zs.name)
zs.name = '张三'
print(zs.name)

del zs.name
print(zs.name)