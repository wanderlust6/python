import minimatrix as mm

a = mm.narray([4, 3])
print("矩阵 a:")
print(a)

print("矩阵 a 的形状:")
print(a.shape())

print("重塑矩阵 a 为 2x6:")
print(a.reshape([2, 6]))

print("创建一个 2x3 的零矩阵:")
print(mm.zeros([2, 3]))

print("与矩阵 a 相同大小的零矩阵:")
print(mm.zeros_like(a))

b = mm.narray([4, 3], init_value=2)
print("矩阵 b (初始化为 2):")
print(b)

print("矩阵 a 与矩阵 b 的和:")
print(a + b)

print("矩阵 a 与矩阵 b 的差:")
print(a - b)

print("矩阵 a 与矩阵 b 的元素相乘:")
print(a * b)

print("矩阵 a 的转置:")
print(a.T())

print("矩阵 a 所有元素的和:")
print(a.sum())

print("矩阵 a 按列求和:")
print(a.sum(axis=0))

print("矩阵 a 按行求和:")
print(a.sum(axis=1))

if a.dim[0] == a.dim[1]:
    print("矩阵 a 的行列式:")
    print(a.det())
else:
    print(f"矩阵 a 不是方阵，无法计算行列式。")

print("矩阵 a 的逆矩阵:")
try:
    print(a.inverse())
except ValueError as e:
    print(f"错误: {e}")

print("矩阵 a 的秩:")
print(a.rank())

I_matrix = mm.I(3)
print("单位矩阵 I:")
print(I_matrix)

print("矩阵 a 与单位矩阵 I 相乘:")
print(a.dot(I_matrix))

c = mm.narray([2, 2], init_value=3)
print("矩阵 c:")
print(c)

print("矩阵 a 与矩阵 c 的 Kronecker 积:")
print(a.Kronecker_product(c))

print("矩阵 a 的前两行:")
print(a[:2, :])

print("矩阵 a 的前两列:")
print(a[:2, :2])

d = mm.narray([3, 2], init_value=1)
print("矩阵 d:")
print(d)

print("矩阵 a 与矩阵 d 的矩阵乘法 (a.dot(d)):")
print(a.dot(d))

print("矩阵 a 的副本:")
a_copy = a.copy()
print(a_copy)

print("矩阵 a 的平方 (a^2):")
print(a**2)

print("矩阵 a 的第一个元素:")
print(a[0, 0])

print("修改矩阵 a 的第一个元素为 100:")
a[0, 0] = 100
print(a)

print("创建一个 3x3 的单位矩阵:")
I_matrix_3x3 = mm.I(3)
print(I_matrix_3x3)

print("使用 arange 创建一个矩阵:")
print(mm.arange(1, 10, 2))

print("创建一个随机矩阵:")
print(mm.nrandom([3, 3]))

print("创建一个与矩阵 a 大小相同的随机矩阵:")
print(mm.nrandom_like(a))

print("创建一个与矩阵 a 大小相同的全 1 矩阵:")
print(mm.ones_like(a))

print("拼接两个矩阵 a 和 b 沿轴 0 (行拼接):")
concat_axis_0 = mm.concatenate([a, b], axis=0)
print(concat_axis_0)

print("拼接两个矩阵 a 和 b 沿轴 1 (列拼接):")
concat_axis_1 = mm.concatenate([a, b], axis=1)
print(concat_axis_1)

print("使用 vectorize 将平方函数应用到矩阵 a 的每个元素:")
square_func = mm.vectorize(lambda x: x**2)
result = square_func(a)
print(result)
