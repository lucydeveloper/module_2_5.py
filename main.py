# module_2_5.py
def get_matrix (n, m, value):
    if n<= 0 or m<= 0: # Проверяем, что размеры матрицы положительные
        return [] # Если размеры некорректные, возвращаем пустой список
    matrix = [] # Создаем пустой список
    for i in range(n): # Проходим по количеству строк
        row = [] # добавляем пустой список
        for j in range(m): # Проходим по количеству столбцов
            row.append(value) # Добавляем значение в строку
        matrix.append(row) # Добавляем строку в матрицу
    return matrix # Возвращаем значение переменной matrix
result1 = get_matrix(2, 2, 10) # n - строка, m - столбцы, value - значение
result2 = get_matrix(3, 5, 42) # n - строка, m - столбцы, value - значение
result3 = get_matrix(4, 2, 13) # n - строка, m - столбцы, value - значение
# Выводим результат
print(result1)
print(result2)
print(result3)

