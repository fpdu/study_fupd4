# varlist1 = [1,2,3,4]
# varlist2 = ['a','b','c','d']
#
# # res = varlist1 + varlist2 + [11,22,33]
# # res = varlist1 * 3
# varlist2.append('ff')
# varlist2.pop()
# print(varlist2)

# varlist = [1,2,3,4,5,6,7]
# varlist[2:5] = [44,55,66]
# varlist[2:5:2] = ['a','b']
# print(varlist)

# varlist = [1,2,3,4,5,6,7,6,7]

# res = len(varlist)
# res = varlist.count(1)

# varlist.insert(3,'aa')
# varlist.pop(2)

# res = varlist.remove(3)
# res = varlist.index(6)
# res = varlist.index(6,0,10)

# varlist.extend({'123':3})
# varlist.clear()
# varlist.reverse()
# varlist.sort(key=abs)
# print(varlist)

# print(res)

# varlist = ['a','b','c']
# res = varlist.copy()
# del res[2]
# print(res)

# varlist = ['a','b','c',[11,22,33]]
# res = varlist.copy()  #深浅copy
#
# del res[3][1]
#
# print(res)
# print(varlist)
# import copy

# varlist = []
# for i in range(10):
#     varlist.append(i**2)
# print(varlist)

# varlist = list(map(lambda x:x**2,range(10)))
# print(varlist)

# varlist = [i**2 for i in range(10)]
# print(varlist)

# varstr = '1234'
# newlist = [int(i)*2 for i in varstr]

# newlist = [i for i in range(10) if i % 2 == 0]
# print(newlist)

# newlist = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             newlist.append((x,y))
#
# # print(newlist)
# newlist = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(newlist)
# arr = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# newlist = []
# for i in range(4):
#     res = []
#     for row in arr:
#         res.append(row[i])
#     newlist.append(res)
# print(newlist)

# newlist = [[row[i] for row in arr] for i in range(4)]
# print(newlist)

# jqjq = [f'{i}*{j}={i*j}' for i in range(1,10) for j in range(1,i+1)]
# print(jqjq)

# vardict =  {'user':'admin','age':20,'phone':'133'}
# varlist = [i+'='+str(vardict[i]) for i in vardict]
# print(varlist)
#
# res = '&'.join(varlist)
# print(res)
# varlist = ['AAAAA','bbBb','CCCcc']
# newlist = [i.lower() for i in varlist]
# print(newlist)

# newlist = [(x,y) for x in range(6) for y in range(6) if x % 2 == 0 and y%2==1]
# print(newlist)


# M=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# N = [
#     [2,2,2],
#     [3,3,3],
#     [4,4,4]
# ]
# list1 = []
# for x in range(3):
#     newlist = []
#     # newlist1 = []
#     for y in M:
#         newlist.append(y[x]*N[x][0])
#     # newlist.extend(newlist1)
#     list1.append(newlist)
# print(list1)
#
#
# res = [[y[x]*N[x][0] for y in M] for x in range(3)]
#
# print(res)


