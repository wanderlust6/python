def f(n):
    if n <= 1:
        return 1
    else:
        return f(f(n // 2)) + 1


n = int(input())
print(f(n))

a = [-1] * 1001
a[0] = 1
a[1] = 1
for i in range(2, 1001):
    a[i] = a[i - 1] + a[i - 2]
print(a[1000])


a = [-1] * 1001
a[0] = 1
a[1] = 1
a[2] = 1
for i in range(3, 1001):
    a[i] = a[i - 1] + 2 * a[i - 2] - a[i - 3]
print(a[1000])

a = [-1] * 1001
a[0] = 2
a[1] = 3
for i in range(2, 1001):
    a[i] = a[i - 1] * a[i - 2]
print(a[1000])

a = [[-1] * 101] * 101
for i in range(101):
    a[i][0] = 1
    a[0][i] = 1
for i in range(1, 101):
    for j in range(1, 101):
        a[i][j] = a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]
print(a[100][100])


def list_sum(a):
    s = 0
    for i in a:
        if isinstance(i, list):
            s += list_sum(i)
        else:
            s += i
    return s


a = eval(input())
print(list_sum(a))


def list_sum(a):
    global s
    for i in a:
        if isinstance(i, list):
            list_sum(i)
        else:
            s[i] = s.get(i, 0) + 1
    return s


s = {}
a = eval(input())
print(list_sum(a))


def Hadamard(k):
    if k == 1:
        return [[1]]
    else:
        H1 = Hadamard(k // 2)
        top = [row + row for row in H1]
        bottom = [row + [-x for x in row] for row in H1]
        return top + bottom


k = int(input())
print(Hadamard(k))


def powerset(a):
    global b
    if a not in b:
        b.append(a)
    for i in range(len(a)):
        powerset(a[:i] + a[i + 1 :])
    return b


a = eval(input())
b = []
print(powerset(a))
