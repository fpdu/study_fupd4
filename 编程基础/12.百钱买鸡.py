num = 1
for gj in range(1,34):
    for mj in range(1,101):
        for xj in range(1,202):
            if gj + mj + xj == 100 and gj * 3 + mj *1 + xj * 0.5 == 100:
                print(f'公鸡{gj}只,母鸡{mj}只,小鸡{xj}只')
                num += 1
print(num)