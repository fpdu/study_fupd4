def outer(func):
    def inner():
        print('找到妹子,成功拿到微信....3')
        func()
        print('约妹子,看一场午夜电影....4')
    return inner
# @outer
# def love():
#     print('跟妹子畅谈人生和理想....')
# love()

# love = outer(love)
# love()

def kovj(f):
    def kzinner():
        print('扩展1')
        f()
        print('扩展2')
    return kzinner
@kovj
@outer
def love():
    print('跟妹子畅谈人生和理想....5')

love()