class Cart():
    color = '白色'
    brand = '奥迪'
    pailiang = '2.4'

    def laho(self):
        print('小汽车能拉货')

    def dbfg(self):
        print('小汽车能兜风')

    def bamz(self):
        print('小汽车能把妹')

# a = Cart()
# b = Cart()

# print(a)
# print(b)
#
# res = a.color
# print(res)
# a.color = '黑色'
# print(a.color)
# print(b.color)
#
# a.name = 'a6'
# print(a.name)
# # print(b.name)
# del a.color
# del a.name
# # del a.brand
# print(a.color)
# # print(a.name)

# def func():
#     print('这是一个新的方法')
#
# a.laho = func
# a.laho()
#
# a.func2 = func
# a.func2()
#
# del a.laho
# del a.func2
#
# a.laho()
# a.func2()

a = Cart()
print(Cart.brand)
Cart.brand = '宝马'
print(Cart.brand)

b = Cart()
print(a.brand)
print(b.brand)

Cart.name = 'A6'
print(Cart.name)
c = Cart()
print(c.name)
print(a.name)

print("*"*15)

del Cart.brand
print(a.brand)

