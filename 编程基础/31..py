import calendar
res = calendar.monthrange(2020,11)
print(res)
days = res[1]
w = res[0] + 1
print(' 一  二   三  四  五   六  日 ')
print('*'*27)
d = 1
while d <= days:
    for i in range(1,8):
        if d > days or (i < w and d == 1):
            print(' '*4,end='')
        else:
            print(' {:0>2d} '.format(d),end="")
            d += 1
    print()
print('*'*27)

