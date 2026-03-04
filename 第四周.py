def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


a, b, c = map(int, input().split())
print(is_triangle(a, b, c))


def delta(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        return 2
    elif d == 0:
        return 1
    else:
        return 0


a, b, c = map(int, input().split())
print(delta(a, b, c))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
print(is_prime(n))


def is_palindrome_year(year):
    if year == year[::-1]:
        return True
    else:
        return False


year = str(input())
print(is_palindrome_year(year))

import math


def f(x):
    if x < -2:
        return x**4
    elif -2 <= x < 2:
        return math.sin(x)
    else:
        return math.exp(x)


x = int(input())
print(f(x))

a = int(input())
while a != 0:
    if a != -1:
        print(str(a)[::-1])
    a = int(input())

a = input()[::-1]
s = 0
for i in range(len(a)):
    if a[i] == "0":
        s += 1
    else:
        break
print(s)


def Hamming(a, b):
    a = bin(a)[2:][::-1]
    b = bin(b)[2:][::-1]
    s = 0
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            s += 1
    s += abs(len(a) - len(b))
    return s


a, b = map(int, input().split())
print(Hamming(a, b))


def is_valid(n):
    a = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        if n in a:
            return False
        a.append(n)
    return True


n = int(input())
print(is_valid(n))


for i in range(1, 100000):
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        print(i)


def fractal(n):
    s = 1
    while n > 1:
        s *= n
        n -= 1
    return s


def choose(n, k):
    return fractal(n) // (fractal(k) * fractal(n - k))


def pascal(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print(choose(i, j), end=" ")
        print()


n = int(input())
pascal(n)