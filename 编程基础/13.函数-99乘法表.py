def igfa(n=0):
    if n == 0:
        rs = range(1,10)
    else:
        rs = range(9,0,-1)
    for x in rs:
        for y in range(1,x+1):
            print(f'{x}*{y}={x*y}',end='  ')
        print()
igfa(1)