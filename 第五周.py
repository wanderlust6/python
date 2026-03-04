a = list(map(int, input().split()))
s1 = 0
s2 = 1
for i in a:
    s1 += i
    s2 *= i
print(s1, s2)


def compare_list(lst1, lst2):
    a = b = 0
    for i in lst1:
        if i not in lst2:
            a = 1
    for i in lst2:
        if i not in lst1:
            b = 1
    if b == 0:
        return lst1
    elif a == 0:
        return lst2
    else:
        return False


lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
print(compare_list(lst1, lst2))

a = []
for i in range(1000, 3001):
    s = str(i)
    if (
        (int(s[0]) % 2 == 1)
        and (int(s[1]) % 2 == 1)
        and (int(s[2]) % 2 == 1)
        and (int(s[3]) % 2 == 1)
    ):
        a.append(s)
print(*a, sep=",")

s = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
a = []
for i in s:
    if i not in a:
        a.append(i)
print(a)

n = input()
if n[0] == "-":
    print("-" + n[:0:-1])
else:
    print(n[::-1])


a = eval(input())
b = eval(input())
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)


def print_star(n):
    for i in range(1, n + 1):
        print("* " * i)
    for i in range(n - 1, 0, -1):
        print("* " * i)


n = int(input())
print_star(n)


def count_digits(a):
    s = [0] * 10
    for i in a:
        s[int(i)] += 1
    return s


a = input()
print(count_digits(a))


def sum_of_two(n):
    s = 0
    for i in range(1, n + 1):
        s += int(str(i * "2"))
    return s


n = int(input())
print(sum_of_two(n))

a = [[i for i in range(1, 11)] for j in range(1, 11)]
print(*a, sep="\n")
b = [[i for j in range(10)] for i in range(1, 11)]
print(*b, sep="\n")


def find_min(lst):
    i = len(lst) - 1
    while i > 0 and lst[i] <= lst[i - 1]:
        i -= 1
    return i


lst = eval(input())
print(find_min(lst))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
print(is_prime(n))
lst = [i for i in range(2, 1000001) if is_prime(i)]
print(lst)
