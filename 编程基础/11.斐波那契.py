# num = int(input('你要计算的是第几页:'))
# n1 = 0
# n2 = 1
# count = 2
# if num <= 0 :
#     print("请输入一个正整数")
# elif num == 1:
#     print(f'斐波那契数列:{n1}')
# else:
#     print(f'斐波那契数列:{n1},{n2}',end=",")
#     while count < num:
#         n3 = n1 + n2
#         print(n3,end=",")
#         n1,n2 = n2,n3
#         count += 1
num = int(input('第几项:'))
n1 = 0
n2 = 1
count = 2
if num <= 0 :
    print("请输入一个正整数:")
elif num == 1:
    print(f'斐波那契数列:{n1}')
else:
    print(f'斐波那契数列:{n1},{n2}',end=',')
    while count < num:
        n3 = n1 + n2
        print(n3,end=',')
        n1,n2=n2,n3
        count += 1


