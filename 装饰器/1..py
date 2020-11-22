def outer(f):
    def inner():
        print('我是外函数中的内函数1')
        f()
        print('我是外函数中的内函数2')
    return inner

# def old():
#     print('我是一个普通的函数')
#
# old()
# old = outer(old)
# old()

@outer
def old():
    print('我是一个普通的函数')
old()