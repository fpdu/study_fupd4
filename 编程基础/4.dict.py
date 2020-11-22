# var1 = {'a': 1, 'b': 2, 'c': 3}
# # for k in var1.keys():
# #     print(k)
# #
# #
# # var1.popitem()
# # print(var1)
# res = var1.get('aa','abc')
#
# # var1.update(a=11,b=22)
# # var1.update(d=4)
# # print(var1)
#
# res = var1.setdefault('d',5)
# print(res)


vardict = {'a':1,'b':2,'c':3}
# newdict = {v:k for v,k in vardict.items()}
# print(newdict)
newdict = dict(vardict.items())
print(newdict)