
def get_matrix(n, m, value):
    matrix = []
    # Внешний цикл для строк
    for i in range(n):
        # Создаем пустой список для строки
        row = []

        # Внутренний цикл для столбцов
        for j in range(m):
            # Добавляем значение в строку
            row.append(value)

        # Добавляем строку в матрицу
        matrix.append(row)

    # Возвращаем созданную матрицу
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

