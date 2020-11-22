import time
class Views():

    def __init__(self):
        self.__showindex()
        print('系统正在加载,请稍后....')
        time.sleep(1)
        self.showfunc()

    def __showindex(self):
        varstr = '''
***************************************
*                                     *
*                                     *
*           Welcome To Bank           *
*                                     *
*                                     *
***************************************
        '''
        print(varstr)

    def showfunc(self):
        varstr = '''
***************************************
*        (1)注册      (2)查询          *
*        (3)存款      (4)取款          *
*        (5)转账      (6)改密          *
*        (7)锁卡      (8)解卡          *
*        (9)补卡      (0)退出          *
***************************************
        '''
        print(varstr)

if __name__ == '__main__':
    Views()