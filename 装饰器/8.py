class Outer():
    def newinner(func):
        Outer.func = func
        return Outer.inner

    def inner():
        print('拿到妹子微信')
        Outer.func()
        print('看一场电影')

@Outer.newinner
def love():
    print('和妹子谈谈人生喝喝茶....')
love()
