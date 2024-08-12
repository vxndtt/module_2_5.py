def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


n = int(input('Введите исло строк: '))
m = int(input('Введите исло столбцов: '))
value = int(input('Введите значение матрицы: '))
matrix = get_matrix(n, m, value)
print(matrix)