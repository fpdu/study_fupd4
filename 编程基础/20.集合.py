# vars = {123,'abc',False,'love',True,(1,2,3),0,3.1415,'123'}
# for i in vars:
#     print(i,type(i))
# print(vars)
# res = vars.add('def')
# print(vars)

# res = vars.update({1,2,3,4,5})
# print(vars)

# varset = {1,2,3,4}
# newset = {i * 2 for i in varset}
#
# newset = [i<<1 for i in varset if i%2==0]
#
# print(newset)
# vars1 = {1,2,3}
# vars2 = {4,5,6}
# newset = set()
# for i in vars1:
#     for j in vars2:
#         print(i,j)
#         newset.add(i+j)
# print(newset)
#
# newset = {i+j for i in vars1 for j in vars2}
# print(newset)
#
#
# newset = {i+j for i in vars1 for j in vars2 if i%2==0 and j%2==0}
# print(newset)


vars1 = {'郭富城','刘德华','张学友','黎明','都敏俊',1}
vars2 = {'尼古拉斯赵四','刘能','小沈阳','宋小宝','都敏俊',1}

res = vars1 & vars2
res = vars1 | vars2

res = vars1 - vars2
res = vars2 - vars1
res =vars1 ^ vars2

print(res)