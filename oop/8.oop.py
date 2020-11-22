class A():
    pass

class B(A):
    pass

class C(A):
    pass

class Demo(B,C):
    '''
    此处是说明类文档
    '''
    name = 'a'
    age = 20

    def say(self):
        print('会说会唱会rap...')

obj = Demo()
obj.san = 'aaa'
# res = Demo.__dict__
# res = obj.__dict__
# res = Demo.__doc__
# res = obj.__doc__

# res = Demo.__name__

# res = Demo.__module__
#
# res = Demo.__base__

# res = Demo.__bases__
#
res = Demo.__mro__
print(res)
