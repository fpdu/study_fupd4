# vart = (1,23,4,5,6,7,7,8)
# # res = vart.count(3)
# res = vart.index(5)
# print(res)
#
#
# res1 = (1,2,3) + ('a','b')
# res2 = (1,23)*4
# print(res1)
# print(res2)
#
# res = 22 in res1
# print(res)

# varlist = [1,2,3,4,5,6,7,8,9]
# # newlist = [i**2 for i in varlist]
# # print(newlist)
# newt = (i**2 for i in varlist)
# print(newt)
# # print(list(newt))
# # print(next(newt))
# # print(next(newt))
# print(list(newt))
# print(tuple(newt))
#
# for i in newt:
#     print(i)


# def hello():
#     print('hello 1')
#     return 1
#     print('hello 2')
#     return
#
# hello()
# hello()

# def hello():
#     print('hello 1')
#     yield 1
#     print('hello 2')
#     yield 2
#     print('hello 3')
#     yield
#
#
# res = hello()
#
# r = next(res)
# print(r)
# r = next(res)
# print(r)
#
# r = list(res)
# print(r)
# for i in res:
#     print(i)

# def fzbo(num):
#     a,b,i = 0,1,0
#     while i < num:
#         print(b,end=',')
#         a,b = b,a+b
#         i += 1
# fzbo(7)
# def fzbo():
#     a,b,i = 0,1,0
#     while True:
#         yield b
#         a,b = b,a+b
#         i += 1
# num = int(input('请输入一个整数:'))
# res = fzbo()
# for i in range(num+1):
#     print(next(res),end=',')
#
# def fzbo(sum):
#     a,b,i = 0,1,0
#     while i < sum:
#         print(a,end=',')
#         a,b = b,a+b
#         i += 1
# fzbo(7)
