# def print_params(**kwargs): #*arg, **kwargs
#     for key, value in kwargs.items():
#         print(key, value)
#
# dict_ = {'a':1, 'b':2, 'd':3}
# print_params(**dict_)

#list_ = [1, 2, 3]
#print_params(list_, 2, 3)
#print_params(*list_)

# def print_params(a = 1, b = 'строка', c = True):
#     print(a, b, c)
# # Вызов функции без аргументов
# print_params()
# # Вызов функции с одним аргументом
# print_params(10)
# # Вызов функции с двумя аргументами
# print_params(10, 'новая строка')
# # Вызов функции с тремя аргументами
# print_params(10, 'новая строка', False)
# # Вызов функции с именованным аргументом
# print_params(b=25)
# # Вызов функции с именованным аргументом
# print_params(c=[1, 2, 3])


def print_params(a, b, c):
    print(a, b, c)

values_list = [1, 'string', [1,2,3]]
values_dict = {'a': 7, 'b': 'Hello', 'c': False}
values_list_2 = [54.32, 'Строка']

print_params(*values_list)
print_params(**values_dict)

print_params(*values_list_2, 42)