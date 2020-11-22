# n = 1
# # ☆
# while n <= 100:
#     print("★",end=" ")
#     if n % 10 == 0 :
#         print()
#     n += 1
# n = 0
# while n < 100:
#     print("☆",end=" ")
#     if n % 10 == 9:
#         print()
#     n += 1


# n = 0
# while n < 100:
#     if n % 2 == 0:
#         print("★",end=" ")
#     else:
#         print("☆",end=" ")
#     if n % 10 == 9:
#         print()
#
#     n += 1
n = 0
while n < 100:
    if n // 10 % 2 == 0:
        print("★",end=" ")
    else:
        print("☆",end=" ")
    if n % 10 == 9:
        print()
    n += 1
# print(15//2)