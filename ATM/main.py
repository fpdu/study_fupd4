from packages.viewsclass import Views
from packages.controllerclass import Controller

class Main():

    def __init__(self):
        view = Views()
        obj = Controller()
        while True:
            num = input('请输入您要选择的操作:')
            code = ['1','2','3','4','5','6','7','8','9','0']
            if num not in code:
                print('您输入的内容有误,请重新输入。')
                view.showfunc()
                # 跳过本次循环
                continue
            if num == '1':
                obj.register()
            if num == '2':
                pass
            if num == '3':
                pass
            if num == '4':
                pass
            if num == '5':
                pass
            if num == '6':
                pass
            if num == '7':
                pass
            if num == '8':
                pass
            if num == '9':
                pass
            if num == '0':
                pass



if __name__ == '__main__':
    Main()