userlist = []
pwdlist = []
blacklist = []
def readallusers():
    with open('user.txt', 'a+', encoding='utf-8') as fp:
        fp.seek(0)
        res = fp.readlines()
        for i in res:
            r = i.strip()
            arr = r.split(':')
            userlist.append(arr[0])
            pwdlist.append(arr[1])
    with open('black.txt', 'a+', encoding='utf-8') as fp:
        fp.seek(0)
        res = fp.readlines()
        for i in res:
            blacklist.append(i.strip())
def register():
    site = True
    while site:
        username = input("欢迎注册,清输入用户名:")
        if username in userlist:
            print('用户名已存在,请更换用户名')
        else:
            while True:
                pwd = input('请输入密码:')
                if len(pwd) >= 3:
                    repwd = input('请输入确认密码')
                    if pwd == repwd:
                        with open('user.txt', 'a+', encoding='utf-8') as fp:
                            fp.write(f'{username}:{pwd}\n')
                        print(f'注册成功:用户名:{username}')
                        site = False
                        break
                    else:
                        print('两次输入的密码不一致,清重新输入')
                else:
                    print('密码格式不正确,请重新输入')

def login():
    islogin = True
    errornum = 3
    while islogin:
        username = input('欢迎登录,请输入你的用户名:')
        if username in userlist:
            if username in blacklist:
                print('当前用户属于锁定状态,不可登录,请忏悔去吧,,')
            else:
                while True:
                    pwd = input("请输入您的密码:")
                    inx = userlist.index(username)
                    if pwd == pwdlist[inx]:
                        print('登录成功')
                        islogin = False
                        break
                    else:
                        errornum -= 1
                        if errornum == 0:
                            print('曾经有那么几次机会摆在你面前,你没有珍惜,,')
                            with open('black.txt', "a+", encoding="utf-8") as fp:
                                fp.write(username+'\n')
                            islogin = False
                            break
                        else:
                            print(f'密码输入错误,请重新输入密码,你有{errornum}机会')



        else:
            print("用户名错误,请重新输入")

if __name__ == '__main__':
    readallusers()
    while True:
        vars = '''
        ****************************************
        **   登录(1)  注册(2)  退出(任意内容)    **
        ****************************************
        '''
        print(vars)
        num = input('请输入对应的序号,体验功能:')
        if num == '1':
            login()
        elif num == '2':
            register()
        else:
            print('欢迎下次体验,,,,')
            break