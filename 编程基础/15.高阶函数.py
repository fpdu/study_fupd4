# def jwfa(x,y):
#     return x+y
# print(jwfa(2,5))

# res = lambda x,y:x + y
# print(res(2,5))

# res = lambda sex:'很man' if sex == '男' else '很漂亮'
# print(res('女'))


# arr = [4,6,1,3,2,-4]
# res = sorted(arr,key=lambda x:x % 2)
# print(res)

# n = ['1','2','3','4']
# # print(list(n))
# res = map(int,n)
# print(list(res))


# varlist = [1,2,3,4,5]
# def myfunc(x):
#     return x ** 2
# res = map(myfunc,varlist)
# print(list(res))
# res = map(lambda x:x ** 2,varlist)
# print(list(res))

# varlist = ['a','b','c','d']
# res = map(ord,varlist)
# res1 = map(lambda x:x - 32,res)
# print(list(res1))
# from functools import reduce
# varlist = [5,2,1,1]
# res = reduce(lambda x,y:x * 10 + y,varlist)
# print(res)

# varlist = [1,2,3,4,5,6,7,8,9]
# res = filter(lambda x:True if x % 2 == 0 else False,varlist)
# print(list(res))


# zip() 与 * 运算符相结合可以用来拆解一个列表:
# x = [1, 2, 3]
# y = [4, 5, 6]
# zipped = zip(x, y)
# print(list(zipped))

# print(zip(x, y)) # 迭代器对象，
# print(*zip(x, y))# 组合好的多个元组数据







