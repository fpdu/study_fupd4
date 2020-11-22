n2 = 3
if isinstance(n2,int):
    res = 10 + n2
    print(res)


try:
    with open('./user.txt','r') as fp:
        res = fp.read()
    print(res)

except:
    print('文件不存在')

print('让程序继续执行....')