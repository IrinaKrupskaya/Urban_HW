my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0 # Индекс для перебора элементов списка
# Цикл while для перебора элементов списка
while index < len(my_list):
    number = my_list[index]
    # Проверка на отрицательное число
    if number < 0:
        break  # Прерываем цикл при встрече отрицательного числа
    # Пропускаем нули
    if number == 0:
        index += 1
        continue  # Переходим к следующей итерации цикла
    # Выводим положительное число
    print(number)
    # Переходим к следующему элементу списка
    index += 1



