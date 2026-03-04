import time


def find_prime1(n):
    time_start = time.time()
    number_pn = 0
    for j in range(2, n):
        flag = True
        for i in range(2, j):
            if j % i == 0:
                flag = False
                break
        if flag:
            number_pn += 1
    time_end = time.time()
    return time_end - time_start, number_pn


def find_prime2(n):
    time_start = time.time()
    number_pn = 0
    for j in range(2, n):
        flag = True
        for i in range(2, int(j**0.5) + 1):
            if j % i == 0:
                flag = False
                break
        if flag:
            number_pn += 1
    time_end = time.time()
    return time_end - time_start, number_pn


def find_prime3(n):
    time_start = time.time()
    number_pn = 2
    for j in range(2, n):
        flag = True
        if j % 6 == 1 or j % 6 == 5:
            for i in range(2, int(j**0.5) + 1):
                if j % i == 0:
                    flag = False
                    break
        if flag and (j % 6 == 1 or j % 6 == 5):
            number_pn += 1
    time_end = time.time()
    return time_end - time_start, number_pn


def find_prime4(n):
    time_start = time.time()
    number_pn = 0
    a = [1 for i in range(1000000)]
    for i in range(2, n):
        t = i * 2
        while t < 1000000 and a[i] == 1:
            a[t] = 0
            t += i
    for i in range(2, 1000000):
        if a[i] == 1:
            number_pn += 1
    time_end = time.time()
    return time_end - time_start, number_pn


def find_prime5(n):
    time_start = time.time()
    number_pn = 4
    for i in range(9, n, 2):
        flag = True
        if (i % 6 == 1 or i % 6 == 5) and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            t = i - 1
            s = 0
            while t % 2 == 0:
                t = t // 2
                s += 1
            a = [2, 3]
            for j in a:
                if flag == False or i % j == 0:
                    break
                p = pow(j, t, i)
                if p == 1:
                    continue
                for k in range(s):
                    q = pow(p, 2, i)
                    if q == 1:
                        if p != 1 and p != i - 1:
                            flag = False
                            break
                    p = q
                if q != 1:
                    flag = False
                    break
            if flag:
                number_pn += 1
    time_end = time.time()
    return time_end - time_start, number_pn


print(find_prime2(1000000))
print(find_prime3(1000000))
print(find_prime4(1000000))
print(find_prime5(1000000))
