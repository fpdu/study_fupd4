class MyException():
    pass

def func():
    print('我是个一个模板中的func函数')

love = 'iloveyou'

name = __name__
print(name)

if __name__ == '__main__':
    print('这个位置写的代码只有当前脚本被直接运行是触发')