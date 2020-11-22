var = 'ii_ll_vv_oo_ee'
# res = var.split('_',1) #列表
res = var.swapcase()
print(res)

var1 =  ['user', 'admin', 'id', '123']
res1 = '_'.join(var1) #字符串
print(res1)

vars3 = '###zhangsan#    '
res2 = vars3.strip('#')
print(res2)

var4 = 'ilove'
res3 = var4.replace('i','I')
print(res3)