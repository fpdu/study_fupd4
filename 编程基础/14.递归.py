#1.
# def digv(num):
#     print(num)
#     if num > 0:
#         digv(num-1)
#     print(num)
# digv(3)

#2.
# def jxig(n):
#     if n == 1:
#         return 1
#     else:
#         return n*jxig(n-1)
# print(jxig(7))
#3.
def fzbo(n):
    if n == 1 or n == 2:
        return 1
    else:
        print(n-1,n-2)
        return fzbo(n-1) + fzbo(n-2)
print(fzbo(6))