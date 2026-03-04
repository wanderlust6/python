import time


def str2list(a):
    lst = []
    for i in range(len(a)):
        if a[i] == "-":
            lst.append("-")
        else:
            lst.append(int(a[i]))
    return lst


def list2str(a):
    return "".join(map(str, a))


def add(str1, str2):
    k1 = 1
    k2 = 1
    if str1[0] == "-":
        k1 = -1
        str1 = str1[1::]
    if str2[0] == "-":
        k2 = -1
        str2 = str2[1::]
    str1 = str1[::-1]
    str2 = str2[::-1]
    l1 = len(str1)
    l2 = len(str2)
    if l1 > l2:
        str2 += [0] * (l1 - l2)
    else:
        str1 += [0] * (l2 - l1)
    carry = 0
    str3 = []
    for i in range(max(l1, l2)):
        temp = str1[i] * k1 + str2[i] * k2 + carry
        if temp < 0:
            carry = -1
            temp += 10
        else:
            carry = temp // 10
            temp = temp % 10
        str3.append(temp)
    if carry < 0:
        carry1 = 0
        str3 = []
        for i in range(max(l1, l2)):
            temp = str1[i] * k1 * -1 + str2[i] * k2 * -1 + carry1
            if temp < 0:
                carry1 = -1
                temp += 10
            else:
                carry1 = temp // 10
            temp = temp % 10
            str3.append(temp)
        if carry1 > 0:
            str3.append(carry1)
    if carry > 0:
        str3.append(carry)
    while len(str3) > 1 and str3[-1] == 0:
        str3.pop()
    str3 = str3[::-1]
    if carry < 0:
        return ["-"] + str3
    else:
        return str3


def sub(str1, str2):
    k1 = 1
    k2 = 1
    if str1[0] == "-":
        k1 = -1
        str1 = str1[1::]
    if str2[0] == "-":
        k2 = -1
        str2 = str2[1::]
    str1 = str1[::-1]
    str2 = str2[::-1]
    str4 = [0]
    l1 = len(str1)
    l2 = len(str2)
    for i in range(l1):
        carry = 0
        str3 = [0] * i
        for j in range(l2):
            temp = str1[i] * str2[j] + carry
            carry = temp // 10
            temp = temp % 10
            str3.append(temp)
        if carry > 0:
            str3.append(carry)
        str4 = add(str4, str3[::-1])
    if k1 * k2 == 1:
        return str4
    else:
        return ["-"] + str4


def mul(str1, str2):
    k1 = 1
    k2 = 1
    if str1[0] == "-":
        k1 = -1
        str1 = str1[1::]
    if str2[0] == "-":
        k2 = -1
        str2 = str2[1::]
    l1 = len(str1)
    l2 = len(str2)
    str3 = []
    p = 0
    for i in range(l1 - l2 + 1):
        temp = str1[p : i + l2]
        for j in range(0, 11):
            if add(temp, ["-"] + sub([j], str2))[0] == "-":
                break
        if j == 1:
            str3.append(0)
        else:
            str3.append(j - 1)
            str1[p : i + l2] = [0] * (
                i + l2 - p - len(add(temp, ["-"] + sub([j - 1], str2)))
            ) + add(temp, ["-"] + sub([j - 1], str2))
            while str1[p] == 0 and p < i:
                p += 1
    while len(str3) > 0 and str3[0] == 0:
        str3 = str3[1::]
    if k1 * k2 == 1:
        return str3
    else:
        if str1 == [0] * l1:
            return ["-"] + str3
        else:
            return ["-"] + add(str3, [1])


def div(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    str3 = []
    p = 0
    for i in range(l1 - l2 + 1):
        temp = str1[p : i + l2]
        for j in range(0, 11):
            if add(temp, ["-"] + sub([j], str2))[0] == "-":
                break
        if j == 1:
            str3.append(0)
        else:
            str3.append(j - 1)
            str1[p : i + l2] = [0] * (
                i + l2 - p - len(add(temp, ["-"] + sub([j - 1], str2)))
            ) + add(temp, ["-"] + sub([j - 1], str2))
            while str1[p] == 0 and p < i:
                p += 1
    while len(str1) > 0 and str1[0] == 0:
        str1 = str1[1::]
    while len(str3) > 0 and str3[0] == 0:
        str3 = str3[1::]
    return str3, str1


def pow(str1, n):
    str2 = [1]
    for i in range(n):
        str2 = sub(str2, str1)
    return str2


time_start = time.time()
print(list2str(add(str2list("22222222222222"), str2list("8773849905050505"))))
print(list2str(add(str2list("11111111"), str2list("-9877344555"))))
print(list2str(add(str2list("345676778778"), str2list("-222222"))))
print(list2str(sub(str2list("123456"), str2list("789"))))
print(list2str(mul(str2list("8773849905050505"), str2list("123"))))
print(list2str(pow(str2list("2"), 66)))
print(list2str(add(pow(str2list("2"), 100), pow(str2list("3"), 50))))
print(
    list2str(
        add(
            add(
                sub(str2list("2"), str2list("100")),
                sub(str2list("123456"), str2list("789")),
            ),
            ["-"] + mul(str2list("8773849905050505"), str2list("123")),
        )
    )
)
time_end = time.time()
print("运行时间：", time_end - time_start)
