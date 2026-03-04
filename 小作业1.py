def hanoi_plus(n, x, y, z):
    if n == 1:
        print(f"{x}->{y}")
        print(f"{y}->{z}")
    else:
        hanoi_plus(n - 1, x, y, z)
        print(f"{x}->{y}")
        hanoi_plus(n - 1, z, y, x)
        print(f"{y}->{z}")
        hanoi_plus(n - 1, x, y, z)


n = int(input())
hanoi_plus(n, "A", "B", "C")

n = int(input())
s = [i for i in range(1, n + 1)]
i = 0
j = 1
while len(s) > 1:
    if j % 2 == 0:
        s.pop(i)
        i %= len(s)
    else:
        i = (i + 1) % len(s)
    j += 1
print(s[0])


def T(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * T(n // 2) - 1
    else:
        return 2 * T(n // 2) + 1


print(T(n))
i = 1
while i <= n:
    i *= 2
print(2 * (n - i // 2) + 1)


def cover(k, i, j):
    global s
    if k == 1:
        if i % 2 == 0 and j % 2 == 0:
            s[i + 1][j] = 4
            s[i][j + 1] = 4
            s[i + 1][j + 1] = 4
        elif i % 2 == 0 and j % 2 == 1:
            s[i][j - 1] = 3
            s[i + 1][j - 1] = 3
            s[i + 1][j] = 3
        elif i % 2 == 1 and j % 2 == 0:
            s[i - 1][j] = 2
            s[i - 1][j + 1] = 2
            s[i][j + 1] = 2
        else:
            s[i - 1][j - 1] = 1
            s[i - 1][j] = 1
            s[i][j - 1] = 1
    else:
        t = 2 ** (k - 1)
        if i < t and j < t:
            cover(k - 1, i, j)
            s[t - 1][t] = 4
            s[t][t - 1] = 4
            s[t][t] = 4
            cover(k - 1, t - 1, t)
            cover(k - 1, t, t - 1)
            cover(k - 1, t, t)
        elif i < t and j >= t:
            cover(k - 1, i, j)
            s[t - 1][t - 1] = 3
            s[t][t - 1] = 3
            s[t][t] = 3
            cover(k - 1, t - 1, t - 1)
            cover(k - 1, t, t - 1)
            cover(k - 1, t, t)
        elif i >= t and j < t:
            cover(k - 1, i, j)
            s[t - 1][t - 1] = 2
            s[t - 1][t] = 2
            s[t][t] = 2
            cover(k - 1, t - 1, t - 1)
            cover(k - 1, t - 1, t)
            cover(k - 1, t, t)
        else:
            cover(k - 1, i, j)
            s[t - 1][t - 1] = 1
            s[t - 1][t] = 1
            s[t][t - 1] = 1
            cover(k - 1, t - 1, t - 1)
            cover(k - 1, t - 1, t)
            cover(k - 1, t, t - 1)


k, i, j = map(int, input().split())
s = [[0] * 2**k for _ in range(2**k)]
cover(k, i - 1, j - 1)
print(*s, sep="\n")
