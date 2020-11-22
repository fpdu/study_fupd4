class Demo():
    pass

class A():
    pass

class B(A):
    pass
class C(A):
    c = 'abc'

class D(B,C):
    name = 'a'
    __age = 20

    def say(self):
        pass

d = D()
# res = issubclass(D,B)
# res = isinstance(d,A)
res = hasattr(d,'name')

res = getattr(D,'say')

res = setattr(d,'name','ooo')

delattr(D,'name')
print(d.name)
print(res)

print(dir(d))