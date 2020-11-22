num = 521
r1 = str(num)
r2 = repr(num)

print(r1,type(r1))
print(r2,type(r2))

class Demo():
    def __str__(self):
        return '123'
    def __repr__(self):
        return '123'

obj = Demo()
r1 = str(obj)
r2 = repr(obj)
print(r1,type(r1))
print(r2,type(r2))
