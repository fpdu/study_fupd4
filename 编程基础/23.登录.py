userlist = []
pwdlist = []
blacklist = []

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

def login():
    islogin = True
    errornum = 3

    while islogin:
        username = input('欢迎登录,请输入你的用户名:')
        if username in userlist:
            if username not in userlist:
                print('当前的用户属于锁定状态,不可登录,忏悔去吧...')
            else:
                while True:
                    pwd = input('请输入你的密码')
                    inx = userlist.index(username)
                    if pwd == pwdlist[inx]:
                        print('登录成功')
                        islogin = False
                        break
                    else:
                        errornum -= 1
                        if errornum == 0:
                            print('曾经有那么几次机会摆在你面前,但是你没有珍惜,,')
                            with open('balck.txt', 'a+', encoding='utf-8') as fp:
                                fp.write(username+'\n')
                            islogin = False
                            break
        else:
            print('输入的用户名不存在')
login()








