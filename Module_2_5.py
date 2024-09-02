# # def say_hello(name):
# #     print('Hello', name)
#
# # say_hello('denis')
# # say_hello('maxx')
# # say_hello('anton')
#
# # import random
# # def lottery(mon,tue):
# #     tickets = [1,2,3,4,5,6,7,8,9,10]
# #     win1 = random.choice(tickets)
# #     tickets.remove(win1)
# #     win2 = random.choice(tickets)
# #     print(mon,tue)
# #     return win1, win2
# # win1, win2 = lottery('mon', 'tue')
# # print(win1,win2)
#
# # import random
# # def lottery(*args,**kwargs):
# #     tickets = [1,2,3,4,5,6,7,8,9,10]
# #     win1 = random.choice(tickets)
# #     tickets.remove(win1)
# #     win2 = random.choice(tickets)
# #     print(*args)
# #     return win1, win2
# # win1, win2 = lottery('mon', 'tue')
# # print(win1,win2)
#
# def test(a=2, b=True):
#     print(a, b)
# #
# # test(False, 'OK')
# test(*[1,2])
#

#
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

# Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
# В первом цикле добавляйте пустой список в список matrix.
# Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
# Во втором цикле пополняйте ранее добавленный пустой список значениями value.
# После всех циклов верните значение переменной matrix.
# Выведите на экран(консоль) результат работы функции get_matrix.
#
# Пример результата выполнения функции:
# Исходный код:
# result1 = get_matrix(2, 2, 10)
# result2 = get_matrix(3, 5, 42)
# result3 = get_matrix(4, 2, 13)
# print(result1)
# print(result2)
# print(result3)
# Вывод на консоль:
# [[10, 10], [10, 10]]
# [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
# [[13, 13], [13, 13], [13, 13], [13, 13]]
# Примечания:
# Вложенный список - это строка матрицы, элементы вложенных списков(глубже) - это столбцы матрицы.
# В случае передачи аргумента со значением 0 или меньше, будет возвращаться пустой список.