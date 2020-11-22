def jmce():
    while True:
        year = input('年份:')
        if len(year) != 4:
            print("输入错误,请输入四位数年份")
            continue
        else:
            if year == 1993:
                print("回答正确")
            else:
                print('回答错误')
jmce()