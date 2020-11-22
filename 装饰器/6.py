def kovj(var):
    def outer(func):
        def inner1():
            print('妹子给了你微信')
            func()
        def inner2():
            print('妹子给介绍了个大妈')
            func()
        if var == 1:
            return inner1
        else:
            return inner2
    return outer

@kovj(2)
def love():
    print('谈谈人生')

love()