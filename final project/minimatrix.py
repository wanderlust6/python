import random


class Matrix:
    def __init__(self, data=None, dim=None, init_value=0):
        if data is not None:
            self.dim = (len(data), len(data[0]))
            self.data = data
        else:
            self.dim = dim
            self.data = [[init_value for _ in range(dim[1])] for _ in range(dim[0])]

    def shape(self):
        return self.dim

    def reshape(self, newdim):
        if newdim[0] * newdim[1] != self.dim[0] * self.dim[1]:
            raise ValueError("新维度与原维度不匹配，无法reshape")
        data1 = [
            self.data[i][j] for i in range(self.dim[0]) for j in range(self.dim[1])
        ]
        data2 = [
            [data1[i * newdim[1] + j] for j in range(newdim[1])]
            for i in range(newdim[0])
        ]
        return Matrix(data=data2)

    def dot(self, other):
        data1 = [[0 for _ in range(other.dim[1])] for _ in range(self.dim[0])]
        for i in range(self.dim[0]):
            for j in range(other.dim[1]):
                sum_ij = 0
                for k in range(self.dim[1]):
                    sum_ij += self.data[i][k] * other.data[k][j]
                data1[i][j] = sum_ij
        return Matrix(data=data1)

    def T(self):
        data1 = [[0 for _ in range(self.dim[0])] for _ in range(self.dim[1])]
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                data1[j][i] = self.data[i][j]
        return Matrix(data=data1)

    def sum(self, axis=None):
        if axis == None:
            sum = 0
            for i in range(self.dim[0]):
                for j in range(self.dim[1]):
                    sum += self.data[i][j]
            return Matrix(data=[[sum]])
        elif axis == 0:
            data1 = [0 for _ in range(self.dim[1])]
            for j in range(self.dim[1]):
                sum = 0
                for i in range(self.dim[0]):
                    sum += self.data[i][j]
                data1[j] = sum
            return Matrix(data=[data1])
        else:
            data1 = [0 for _ in range(self.dim[0])]
            for i in range(self.dim[0]):
                sum = 0
                for j in range(self.dim[1]):
                    sum += self.data[i][j]
                data1[i] = sum
            return Matrix(data=[[data1[i]] for i in range(self.dim[0])])

    def copy(self):
        data = [
            [self.data[i][j] for j in range(self.dim[1])] for i in range(self.dim[0])
        ]
        return Matrix(data=data)

    def Kronecker_product(self, other):
        data = [
            [0 for _ in range(self.dim[1] * other.dim[1])]
            for _ in range(self.dim[0] * other.dim[0])
        ]
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                for p in range(other.dim[0]):
                    for q in range(other.dim[1]):
                        data[i * other.dim[0] + p][j * other.dim[1] + q] = (
                            self.data[i][j] * other.data[p][q]
                        )
        return Matrix(data=data)

    def __getitem__(self, key):
        if isinstance(key[0], int) and isinstance(key[1], int):
            return self.data[key[0]][key[1]]
        else:
            s1 = key[0].start if key[0].start is not None else 0
            e1 = key[0].stop if key[0].stop is not None else self.dim[0]
            s2 = key[1].start if key[1].start is not None else 0
            e2 = key[1].stop if key[1].stop is not None else self.dim[1]
            data = [[self.data[i][j] for j in range(s2, e2)] for i in range(s1, e1)]
            return Matrix(data=data)

    def __setitem__(self, key, value):
        if isinstance(key[0], int) and isinstance(key[1], int):
            self.data[key[0]][key[1]] = value
            return Matrix(data=self.data)
        else:
            s1 = key[0].start if key[0].start is not None else 0
            e1 = key[0].stop if key[0].stop is not None else self.dim[0]
            s2 = key[1].start if key[1].start is not None else 0
            e2 = key[1].stop if key[1].stop is not None else self.dim[1]
            for i in range(s1, e1):
                for j in range(s2, e2):
                    self.data[i][j] = value.data[i - s1][j - s2]
            return Matrix(data=self.data)

    def __pow__(self, n):
        for i in range(n - 1):
            if i == 0:
                result = self.dot(self)
            else:
                result = result.dot(self)
        return result

    def __add__(self, other):
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                self.data[i][j] += other.data[i][j]
        return Matrix(data=self.data)

    def __sub__(self, other):
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                self.data[i][j] -= other.data[i][j]
        return Matrix(data=self.data)

    def __mul__(self, other):
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                self.data[i][j] *= other.data[i][j]
        return Matrix(data=self.data)

    def __len__(self):
        return self.dim[0] * self.dim[1]

    def __str__(self):
        return (
            "["
            + "\n".join(
                [
                    "[" + " ".join(f"{float(x):.3f}" for x in row) + "]"
                    for row in self.data
                ]
            )
            + "]"
        )

    def det(self):
        if self.dim[0] != self.dim[1]:
            raise ValueError("不是方阵")
        data = self.copy().data
        n = self.dim[0]
        s = 1
        for i in range(n):
            if data[i][i] == 0:
                flag = False
                for k in range(i + 1, n):
                    if data[k][i] != 0:
                        data[i], data[k] = data[k], data[i]
                        s *= -1
                        flag = True
                        break
                if not flag:
                    return 0
            for j in range(i + 1, n):
                factor = data[j][i] / data[i][i]
                for k in range(n - 1, i - 1, -1):
                    data[j][k] -= factor * data[i][k]
        for i in range(n):
            s *= data[i][i]
        return round(s, 6)

    def inverse(self):
        if self.dim[0] != self.dim[1]:
            raise ValueError("不是方阵")
        n = self.dim[0]
        if n == 1:
            if abs(self.data[0][0]) == 0:
                raise ValueError("矩阵不可逆")
            return Matrix(data=[[1.0 / self.data[0][0]]])
        new_data = []
        for i in range(n):
            new_row = self.data[i][:] + [1 if j == i else 0 for j in range(n)]
            new_data.append(new_row)
        for i in range(n):
            max_row = i
            max_val = abs(new_data[i][i])
            for k in range(i + 1, n):
                if new_data[k][i] > max_val:
                    max_val = abs(new_data[k][i])
                    max_row = k
            if max_val == 0:
                raise ValueError("矩阵不可逆")
            if max_row != i:
                new_data[i], new_data[max_row] = new_data[max_row], new_data[i]
            for j in range(i, 2 * n):
                new_data[i][j] /= new_data[i][i]
            for k in range(n):
                if k != i:
                    factor = new_data[k][i]
                    for j in range(i, 2 * n):
                        new_data[k][j] -= factor * new_data[i][j]
        result_data = []
        for i in range(n):
            result_data.append(new_data[i][n:])
        return Matrix(data=result_data)

    def rank(self):
        m, n = self.dim
        matrix_data = [row[:] for row in self.data]
        rank = 0
        row = 0
        col = 0
        while row < m and col < n:
            main_row = row
            for i in range(row, m):
                if abs(matrix_data[i][col]) > matrix_data[main_row][col]:
                    main_row = i
            if abs(matrix_data[main_row][col]) != 0:
                if main_row != row:
                    matrix_data[row], matrix_data[main_row] = (
                        matrix_data[main_row],
                        matrix_data[row],
                    )
                pivot = matrix_data[row][col]
                for j in range(col, n):
                    matrix_data[row][j] /= pivot
                for i in range(m):
                    if i != row:
                        factor = matrix_data[i][col]
                        for j in range(col, n):
                            matrix_data[i][j] -= factor * matrix_data[row][j]
                rank += 1
                row += 1
            col += 1
        return rank


def I(n):
    data = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return Matrix(data=data)


def narray(dim, init_value=1):
    data = [[init_value for _ in range(dim[1])] for _ in range(dim[0])]
    return Matrix(data=data)


def arange(start, end, step):
    n = len(range(start, end, step))
    data = [[start + i * step for i in range(n)]]
    return Matrix(data=data)


def zeros(dim):
    data = [[0 for _ in range(dim[1])] for _ in range(dim[0])]
    return Matrix(data=data)


def zeros_like(matrix):
    data = [[0 for _ in range(matrix.dim[1])] for _ in range(matrix.dim[0])]
    return Matrix(data=data)


def ones(dim):
    data = [[1 for _ in range(dim[1])] for _ in range(dim[0])]
    return Matrix(data=data)


def ones_like(matrix):
    data = [[1 for _ in range(matrix.dim[1])] for _ in range(matrix.dim[0])]
    return Matrix(data=data)


def nrandom(dim):
    data = [[random.random() for _ in range(dim[1])] for _ in range(dim[0])]
    return Matrix(data=data)


def nrandom_like(matrix):
    dim = (len(matrix.data), len(matrix.data[0]))
    return nrandom(dim)


def concatenate(items, axis=0):
    if axis == 0:
        if len(set([item.dim[1] for item in items])) != 1:
            raise ValueError("矩阵在列数上不对应，无法拼接")
        new_row_count = sum([item.dim[0] for item in items])
        new_col_count = items[0].dim[1]
        data = [[0 for _ in range(new_col_count)] for _ in range(new_row_count)]
        t = 0
        for item in items:
            for i in range(item.dim[0]):
                data[t + i] = item.data[i]
            t += item.dim[0]
        return Matrix(data=data)
    elif axis == 1:
        if len(set([item.dim[0] for item in items])) != 1:
            raise ValueError("矩阵在行数上不对应，无法拼接")
        new_row_count = items[0].dim[0]
        new_col_count = sum([item.dim[1] for item in items])
        data = [[0 for _ in range(new_col_count)] for _ in range(new_row_count)]
        t = 0
        for item in items:
            for i in range(item.dim[0]):
                for j in range(item.dim[1]):
                    data[i][t + j] = item.data[i][j]
            t += item.dim[1]

        return Matrix(data=data)


def vectorize(func):
    def func2(x):
        data = [[func(i) for i in j] for j in x.data]
        return Matrix(data=data)

    return func2


if __name__ == "__main__":
    print("test here")
