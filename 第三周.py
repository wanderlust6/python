a, b, c = map(float, input().split())
print(a, b, c)
print(int(a), int(b), int(c))

import math

print(math.pi)
print(math.sin(1.57))
print(math.acos(-1))
a, b, c = map(int, input().split())
p = (a + b + c) / 2
s1 = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(f"三角形面积为：{s1:.3f}")
print(
    f"弧度值为{math.acos((a**2+b**2-c**2)/(2*a*b)):.3f},{math.acos((b**2+c**2-a**2)/(2*b*c)):.3f},{math.acos((c**2+a**2-b**2)/(2*c*a)):.3f}"
)
r = (a * b * c) / (4 * s1)
print(f"外接圆半径为：{r:.3f} 外接圆面积为：{math.pi*r**2:.3f}")
print(f"内切圆半径为：{s1/p:.3f} 内接圆面积为：{math.pi*(s1/p)**2:.3f}")


d = str(input())
print(f"{d} = {eval(d)}")

a, b = map(int, input().split())
a, b = b, a
print(a, b, a - b)

a, b, c = map(int, input().split())
import math


def area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"三角形面积为：{s}")


def angle(a, b, c):
    A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
    print(f"弧度制为：{A},{B},{C}")


def circumradius(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    r = (a * b * c) / (4 * s)
    print(f"外接圆半径为：{r} 外接圆面积为：{math.pi*r**2}")


def inradius(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"内切圆半径为：{s/p} 内接圆面积为：{math.pi*(s/p)**2}")


area(a, b, c)
angle(a, b, c)
circumradius(a, b, c)
inradius(a, b, c)

x1, y1, r1, x2, y2, r2 = map(int, input().split())


def f(x1, y1, r1, x2, y2, r2):
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if d > r1 + r2:
        print("0个交点")
    elif d == r1 + r2 or d == abs(r1 - r2):
        print("1个交点")
    elif abs(r1 - r2) < d < r1 + r2:
        print("2个交点")
    else:
        print("0个交点")


f(x1, y1, r1, x2, y2, r2)
