def outer(func):
    def inner(var):
        print(f'找到{var}妹子,成功拿到微信....')
        func(var)
        print(f'找到{var}妹子,看一场午夜电影....')
    return inner

@outer
def love(name):
    print(f'跟{name}妹子畅谈人生')

love('思思')
