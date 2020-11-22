# fp = open('./1.txt','w',encoding='utf-8')
# print(fp,type(fp))
#
# fp.write('hello world')
# fp.close()
# fp = open('./1.txt','r',encoding='utf-8')
#
# res = fp.read()
# print(res)
# fp.close()

# fp = open('./1.txt','a')
# fp.write('\n你好啊')
# fp.close()
#
# fp = open('./1.txt','r')
# res = fp.read()
# fp.close()
# print(res)
# with open('./1.txt','r+',encoding='utf-8') as fp:
#     fp.seek(20)
#     fp.write('cc')
#     fp.seek(0)
#     res = fp.read()
#     print(res)


# vars = 5211  # int类型无法写入
# vars = ['hello','world','1','2']
# # vars = {'name':'zs','age':'22'}
# with open('./2.txt','w',encoding='utf-8') as fp:
#     fp.writelines(vars)


# with open('./2.txt','r',encoding='utf-8') as fp:
    # fp.seek(3)
    # res = fp.read()
    # res = fp.read(3)
    # res = fp.readline()
    # print(res)
    # res = fp.readline(3)
    # res = fp.readlines()
    # res = fp.readlines(6)
    # print(res)

# with open('./2.txt','r+',encoding='utf-8') as fp:
#     # fp.seek(10)
#     # fp.seek(0,2)
#     fp.write('\n0000')
#     res = fp.read()
#     print(res)

# with open('./2.txt','r+',encoding='utf-8') as fp:
#     fp.write('helloksdjfaksjdfa')
#     res = fp.truncate(5)
#     print(res)

# str = 'hello1\nhello2\nhello3\nhello4\n'
# with open('./3.txt','a+',encoding='utf-8') as fp:
#     # fp.write(str)
#     fp.seek(0)
#     res = fp.readlines()
#     print(res,type(res))
#
# with open('./1.txt','w+',encoding='utf-8') as fp:
#     fp.write('你好啊\n我不好!')
# with open('./1.txt','r+',encoding='utf-8') as fp:
#     fp.seek(20)
#     fp.write('cc')
#     fp.seek(0)
#     res = fp.read()
#     print(res)

# vars = ['hello','world','1','2']
# # vars = {'name':'zs','age':'22'}
# with open('./4.txt','w',encoding='utf-8') as fp:
#     fp.writelines(vars)

# with open('./4.txt', 'r+',encoding='utf-8') as fp:
#     # fp.seek(3)
#     # res =fp.read()
#     # fp.readline()
#     # res = fp.readline()
#     # print(res)
#     fp.seek(0,2)
#     res = fp.read()
#     print(res)

with open('4.txt', 'r+', encoding='utf-8') as fp:
    res = fp.truncate(5)
    print(res)
    res1 = fp.read()
    print(res1)