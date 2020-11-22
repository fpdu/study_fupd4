vars = {1,2,3,4,5}
vars.update([11,2,333,5555])
print(vars)

vars1 = {1,2,3}
vars2 = {4,5,6}

newlist = {i+j for i in vars1 for j in vars2}
print(newlist)