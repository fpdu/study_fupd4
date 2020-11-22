class Demo():
    def func1(self):
        print(self)
        print('this is object function func1')
    @classmethod
    def func2(cls):
        print(cls)
        print('this is object function func2')

    def func3():
        print('this is object function func3')

    @staticmethod
    def func4():
        print('this is object function func4')

obj = Demo()
# obj.func1()
# Demo.func1()
# Demo.func1('a')
# Demo.func2()
# obj.func2()

# Demo.func3()
# obj.func3()

Demo.func4()
obj.func4()