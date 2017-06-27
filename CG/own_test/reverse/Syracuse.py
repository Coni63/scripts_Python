import time
import sys


def check(n):
    a = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        a.append(n)
    return a


def brute_force(n, l):
    res = []
    for nb in range(1, n+1):
        i = nb
        loop = 1
        while i != 1:
            if i % 2 == 0:
                i = i // 2
                loop += 1
            else:
                i = 3*i+1
                loop += 1
        if loop == l:
            res.append(nb)
    return res


def memory(n, l):
    res = []
    save = {}
    for nb in range(1, n + 1):
        i = nb
        loop = 1
        while True:
            if i == 1:
                save[nb] = loop
                if save[nb] == l:
                    res.append(nb)
                break
            elif i in save.keys():
                save[nb] = save[i] + loop
                if save[nb] == l:
                    res.append(nb)
                break
            else:
                if i % 2 == 0:
                    i = i // 2
                    loop += 1
                else:
                    i = 3 * i + 1
                    loop += 1
    return res


value = 50000
length = 5

'''
start = time.time()
arr = brute_force(value, length)
for each in arr:
    print(each)
print(time.time()-start, file = sys.stderr)
'''

start = time.time()
arr2 = memory(value, length)
for each in arr2:
    print(each)
print(time.time()-start, file = sys.stderr)




