# vardict = dict(name='zhangsan',sex='男',age=22)
# print(vardict)

# vardict = dict([['a',1],['b',2],['c',3]])
# print(vardict)
# var1 = [1,2,3,4]
# var2 = ['a','b','c','d']
# vardict = dict(zip(var1,var2))
# print(vardict)


# var1 = {'a': 1, 'b': 2, 'c': 3}
# var2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}


# var1['aa'] = 'AA'
# var1['aa'] = 'aa'
# res = len(var1)

# print(var1)
# print(res)

# res = var1.keys()
# res = var1.values()
# res = var1.items()
# print(res)

# for k,v in var1.items():
#     print(k)
#     print(v)

# vardict = {'a':1,'b':2,'c':3}
# res = vardict.pop('a')
# res = vardict.popitem()
# res = vardict.get('a','b')
# res = vardict.update(a=1,b=2)
# vardict.update({'c':33,'d':44})
# res = vardict.setdefault('f',50)
# print(vardict)
# print(res)


# vardict = {'a':1,'b':2,'c':3}
# newdict = {}
# for k,v in vardict.items():
#     newdict[v] = k
# print(newdict)

# newdict = {v:k for k,v in vardict.items()}
# print(newdict)

# newdict = {v for k,v in vardict.items()}
# print(newdict,type(newdict))

vardict = {'a':1,'b':2,'c':3,'d':4}
# newdict = {}
# for k,v in vardict.items():
#     if v % 2 == 0 :
#         newdict[v] = k
# print(newdict)
newdict = {v:k for k,v in vardict.items() if v % 2 == 0}
print(newdict)

