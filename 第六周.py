# a = eval(input())
# b = {}
# for i in a:
#     if i not in b:
#         b[i] = 1
# print(b)
# c = []
# for i in b:
#     c.append(i)
# c.sort(reverse=True)
# print(c)

# a = input()
# print(a.upper())


# def merge(a, b):
#     for i in b:
#         a.append(i)
#     a.sort()
#     return a


# a = eval(input())
# b = eval(input())
# print(merge(a, b))

# a = input()
# even = 0
# odd = 0
# for i in a:
#     if int(i) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f"偶数个数为：{even} 奇数个数为：{odd}")


# def is_vaild(s):
#     if len(s) < 6 or len(s) > 16:
#         return False
#     a1 = False
#     a2 = False
#     a3 = False
#     a4 = False
#     for i in s:
#         if i.isdigit():
#             a1 = True
#         if ord(i) >= 65 and ord(i) <= 90:
#             a2 = True
#         if ord(i) >= 97 and ord(i) <= 122:
#             a3 = True
#         if i in "$#@":
#             a4 = True
#     if a1 and a2 and a3 and a4:
#         return True
#     return False


# s = input()
# print(is_vaild(s))

# a = input()
# if a in "aeiouAEIOU":
#     print("是元音字母")
# else:
#     print("是辅音字母")

# dic = {
#     "Janaruy": 31,
#     "February": 28,
#     "March": 31,
#     "April": 30,
#     "May": 31,
#     "June": 30,
#     "July": 31,
#     "August": 31,
#     "September": 30,
#     "October": 31,
#     "November": 30,
#     "December": 31,
# }
# month = input()
# print(dic[month])

# a = input()
# try:
#     num = float(a)
#     if num.is_integer():
#         print("是整数")
#     else:
#         print("不是整数")
# except ValueError:
#     print("不是整数")

# a = ["spring", "summer", "autumn", "winter"]
# b = list(map(int, input().split()))
# print(a[(b[0] - 1) // 3])

# a = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
# b = int(input())
# print(a[(b - 4) % 12])

# a = list(map(int, input().split("-")))
# if a[0] % 4 == 0 and a[0] % 100 != 0 or a[0] % 400 == 0:
#     if a[1] == 2 and a[2] == 28:
#         print(f"{a[0]}-{a[1]}-29")
#     elif a[1] == 2 and a[2] == 29:
#         print(f"{a[0]}-3-1")
#     elif a[1] in [1, 3, 5, 7, 8, 10] and a[2] == 31:
#         print(f"{a[0]}-{a[1]+1}-1")
#     elif a[1] in [4, 6, 9, 11] and a[2] == 30:
#         print(f"{a[0]}-{a[1]+1}-1")
#     elif a[1] == 12 and a[2] == 31:
#         print(f"{a[0]+1}-1-1")
#     else:
#         print(f"{a[0]}-{a[1]}-{a[2]+1}")
# else:
#     if a[1] == 2 and a[2] == 28:
#         print(f"{a[0]}-3-1")
#     elif a[1] in [1, 3, 5, 7, 8, 10] and a[2] == 31:
#         print(f"{a[0]}-{a[1]+1}-1")
#     elif a[1] in [4, 6, 9, 11] and a[2] == 30:
#         print(f"{a[0]}-{a[1]+1}-1")
#     elif a[1] == 12 and a[2] == 31:
#         print(f"{a[0]+1}-1-1")
#     else:
#         print(f"{a[0]}-{a[1]}-{a[2]+1}")


from collections import Counter
import re

a = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.

Abraham Lincoln
November 19, 1863
"""
for i in a:
    if i in "--.,":
        a = a.replace(i, " ")
a = a.lower()
letter = Counter(re.findall(r"[a-z]", a))
word = Counter(re.findall(r"[a-z]+", a))
word = dict(sorted(word.items()))
letter = dict(sorted(letter.items()))
print(f"{word}\n{letter}")
