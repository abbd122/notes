import time
from concurrent.futures import ThreadPoolExecutor

list_ = []


def t1(x):
    time.sleep(3)
    return x


def t2(x):
    time.sleep(2)
    return x


def t3(x):
    time.sleep(1)
    return x


func_lst = [t1, t2, t3]
t = ThreadPoolExecutor(3)
start = time.time()
for func in func_lst:
    obj = t.submit(func, func_lst.index(func))
    list_.append(obj)
t.shutdown(wait=True)
end = time.time()
for each in list_:
    print(each.result())
print(end - start)
