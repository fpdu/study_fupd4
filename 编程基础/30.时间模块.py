import time
# res = time.time()
# res = time.ctime()
res = time.localtime()
# # print(f'{res.tm_year}年{res.tm_mon}月{res.tm_mday}日')
# #
print(res)
# res = time.strftime('%Y-%m-%d %H:%M:%S %w')
# print(res)
#
# print(time.strftime('%Y-%m-%d %H:%M:%S %w'))
# time.sleep(3)
# print(time.strftime('%Y-%m-%d %H:%M:%S %w'))
#
# start = time.perf_counter()
# for i in range(1000000):
#     if 'abc' > 'acd':
#         pass
# end = time.perf_counter()
# print(end-start)

# import calendar
# res = calendar.monthrange(2020,10)
# print(res)
# def showdate(year,month):
#     res = calendar.monthrange(year,month)
#     days = res[1]
#     w = res[0] + 1
#     print(f'====={year}年{month}月的日历信息=====')
#     print('  一  二  三  四  五  六   日  ')
#     print('*' * 28)
#     d = 1
#     while d <= days:
#         for i in range(1,8):
#             if d > days or (i < w and d == 1):
#                 print(' '*4,end='')
#             else:
#                 print('  {:0>2d}'.format(d),end='')
#                 d += 1
#         print()
#     print("*"*28)
#
# showdate(2020,11)
