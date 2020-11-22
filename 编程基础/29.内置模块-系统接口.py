import os
# res = os.getcwd()
# print(res)
# os.chdir('G:\study\青苗代码\\1.编程基础\\14.Python中的内置模块\代码')
# res = os.getcwd()
# print(res)
# res = os.listdir()
# for i in res:
#     print(i)
# print(res)

res = os.path.abspath('../')
res = os.path.basename('/青苗代码/study_fpdu')
res = os.path.join('./a/b/c/','2.jpg')
print(res)

v = 'lovwwwww'
res = v.replace('w','N')
print(res)