import time

def runtime(f):
    def inner():
        start = time.perf_counter()
        f()
        end = time.perf_counter() - start
        print(f'函数的调用执行时间为"{end}')
    return inner
@runtime
def func():
    for i in range(5):
        print(i,end=' ')
        time.sleep(1)

func()
