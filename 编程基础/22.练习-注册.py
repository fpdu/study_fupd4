userlist = []
pwdlist = []
with open('user.txt', 'a+', encoding='utf-8') as fp:
    fp.seek(0)
    res = fp.readlines()
    for i in res:
        r = i.strip()
        arr = r.split(':')
        userlist.append(arr[0])
        pwdlist.append(arr[1])

def register():
    site = True
    while site:
        username = input('欢迎注册,请输入用户名:')
        if username in userlist:
            print('当前用户名已存在,清更换用户名')
        else:
            while True:
                pwd = input('请输入密码:')
                if len(pwd) >= 3:
                    repwd = input('请输入确认密码')
                    if pwd == repwd:
                        with open('user.txt', 'a+', encoding='utf-8') as fp:
                            fp.write(f'{username}:{pwd}\n')
                        print(f'用户注册成功:用户名:{username}')
                        site = False
                        break
                    else:
                        print('两次密码输入不一致,清重新输入')
                else:
                    print('密码格式不对')


register()




