def outer(func):
    def inner(who,name,*args,**kwargs):
        print('约到妹子,聊微信....')
        func(who,name,*args,**kwargs)
        print('天色已晚,怎么办?')
    return inner

@outer
def love(who,name,*args,**kwargs):
    print(f'{who}跟{name}畅谈人生....')
    print('完事去吃了好多美食',args)
    print('看了一场电影',kwargs)

love('三多','思思','火锅','辣条','麻辣烫',mov='唐山大地震')

    