class Transpose:
    def __init__(self):
        self.x, self.y = list(map(int, input('Enter size matrix: ').split()))
        self.a = []
        self.b = []
        print('The result is:')
        for i in range(self.x):
            self.a.append(list(map(float, input().split())))
        for i in range(self.x):
            self.b.append([float(0)] * self.y)

    def main_diagonal(self):
        print('The result is:')
        for j in range(self.y):
            for i in range(self.x):
                self.b[j][i] = self.a[i][j]
                print(self.b[j][i], end=' ')
            print()
        print()

    def side_diagonal(self):
        print('The result is:')
        for i in range(self.x):
            for j in range(self.y):
                self.b[i][j] = self.a[self.x - 1 - j][self.x - 1 - i]
                print(self.b[i][j], end=' ')
            print()
        print()

    def vertical_line(self):
        print('The result is:')
        for i in range(self.x):
            for j in range(self.y):
                self.b[i][j] = self.a[i][self.x - 1 - j]
                print(self.b[i][j], end=' ')
            print()
        print()

    def horizontal_line(self):
        print('The result is:')
        for i in range(self.x):
            for j in range(self.y):
                self.b[i][j] = self.a[self.x - 1 - i][j]
                print(self.b[i][j], end=' ')
            print()
        print()


def get_matrix():
    a_matrix = []
    a_rows, a_cols = list(map(int, input('Enter size of first matrix: ').split()))
    print('Enter first matrix:')
    for i in range(a_rows):
        a_matrix.append(list(map(float, input().split())))

    return a_matrix


def add_multi_matrix(var=None):
    a_matrix = []
    b_matrix = []

    a_rows, a_cols = list(map(int, input('Enter size of first matrix: ').split()))
    print('Enter first matrix:')
    for i in range(a_rows):
        a_matrix.append(list(map(float, input().split())))

    b_rows, b_cols = list(map(int, input('Enter size of second matrix: ').split()))
    print('Enter second matrix:')
    for i in range(b_rows):
        b_matrix.append(list(map(float, input('').split())))

    if var == 'sum':
        if a_rows != b_rows or a_cols != b_cols:
            print('The operation cannot be performed.')
        else:
            print('The result is:')
            for i in range(a_rows):
                for j in range(a_cols):
                    print(a_matrix[i][j] + b_matrix[i][j], end=' ')
                print()
            print()
    else:
        if a_cols != b_rows:
            print('The operation cannot be performed.')
        else:
            print('The result is:')
            for j in range(a_rows):
                for i in range(b_cols):
                    s = 0
                    for k in range(b_rows):
                        s += a_matrix[j][k] * b_matrix[k][i]
                    print(s, end=' ')
                print()
        print()


def multiply_constant():
    a_matrix = []

    a_rows, a_cols = list(map(int, input('Enter size of matrix: ').split()))
    print('Enter matrix:')
    for i in range(a_rows):
        a_matrix.append(list(map(float, input().split())))

    multi = float(input('Enter constant: '))
    print('The result is:')
    for i in range(a_rows):
        for j in range(a_cols):
            print(a_matrix[i][j] * multi, end=' ')
        print()
    print()


def zeros_matrix(rows, cols):
    matrix = []
    while len(matrix) < rows:
        matrix.append([])
        while len(matrix[-1]) < cols:
            matrix[-1].append(0.0)

    return matrix


def copy_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    matrix_c = zeros_matrix(rows, cols)
    for k in range(rows):
        for j in range(cols):
            matrix_c[k][j] = matrix[k][j]

    return matrix_c


def determinant_recursive(matrix_a, total=0):
    indices = list(range(len(matrix_a)))

    if len(matrix_a) == 2 and len(matrix_a[0]) == 2:
        val = matrix_a[0][0] * matrix_a[1][1] - matrix_a[1][0] * matrix_a[0][1]
        return val
    elif len(matrix_a) == 1 and len(matrix_a[0]) == 1:
        return matrix_a[0][0]
    for fc in indices:
        matrix_a_c = copy_matrix(matrix_a)
        matrix_a_c = matrix_a_c[1:]
        height = len(matrix_a_c)
        for p in range(height):
            matrix_a_c[p] = matrix_a_c[p][0:fc] + matrix_a_c[p][fc + 1:]
        sign = (-1) ** (fc % 2)
        sub_det = determinant_recursive(matrix_a_c)
        total += sign * matrix_a[0][fc] * sub_det
    return total


def identity_matrix(n):
    identity = zeros_matrix(n, n)
    for i in range(n):
        identity[i][i] = 1.0

    return identity


def invert_matrix(a_matrix):
    check = 0
    n = len(a_matrix)
    matrix = copy_matrix(a_matrix)
    matrix_i = identity_matrix(n)
    matrix_i_c = copy_matrix(matrix_i)
    indices = list(range(n))
    for fd in range(n):
        if matrix[fd][fd] != 0:
            fd_ = 1.0 / matrix[fd][fd]
        else:
            check += 1
            print("This matrix doesn't have an inverse.")
            print()
            break
        for j in range(n):
            matrix[fd][j] *= fd_
            matrix_i_c[fd][j] *= fd_
        for i in indices[0:fd] + indices[fd + 1:]:
            cr_ = matrix[i][fd]
            for j in range(n):
                matrix[i][j] = matrix[i][j] - cr_ * matrix[fd][j]
                matrix_i_c[i][j] = matrix_i_c[i][j] - cr_ * matrix_i_c[fd][j]
    if check == 0:
        print('The result is:')
        for i1 in range(n):
            for j1 in range(n):
                print(matrix_i_c[i1][j1], end=' ')
            print()
        print()


choice = None

while choice != 0:
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')
    choice = input('Your choice: ')
    if choice == '1':
        add_multi_matrix('sum')
    elif choice == '2':
        multiply_constant()
    elif choice == '3':
        add_multi_matrix()
    elif choice == '4':
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        choice_1 = input('Your choice: ')
        if choice_1 == '1':
            transpose = Transpose()
            transpose.main_diagonal()
        elif choice_1 == '2':
            transpose = Transpose()
            transpose.side_diagonal()
        elif choice_1 == '3':
            transpose = Transpose()
            transpose.vertical_line()
        elif choice_1 == '4':
            transpose = Transpose()
            transpose.horizontal_line()
    elif choice == '5':
        print('The result is:')
        print(determinant_recursive(get_matrix()))
        print()
    elif choice == '6':
        invert_matrix(get_matrix())
    elif choice == '0':
        break
