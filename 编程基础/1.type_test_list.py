var = []
var.extend('123')
print(var)


# varlist = list(map(lambda x:x*2,range(10)))
# print(varlist)

# varlist = [i**2 for i in range(10)]
# print(varlist)
# varstr = '1234'
# newlist = [int(i)*2 for i in varstr]
# print(varstr)
#
#
# newlist1 = [i for i in range(10) if i % 2 == 0 ]
# print(newlist1)
# arr = [
#  [1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9, 10, 11, 12],
# ]
# newlist2 = [[row[i] for row in arr] for i in range(4)]
# print(newlist2)

var = [1,2,3,4]
var[1] = 5
f = str(var)
print(var)
print(f,type(f))