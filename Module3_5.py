# a=[1, 2, 3]
# print(a is a[:])

# a = int(input('Введите первое число: '))
# b= int(input('Введите второе число: '))
# print('Сумма чисел: ', a + b)
# print('Разность чисел: ',  a - b )
# print('Произведение чисел: ', a * b)
# print('Частное от деления первого числа на второе: ', a%b)

# def count_vowels(text):
#     # Определяем гласные буквы
#     vowels = 'ауеыоэяиюАУЕЫОЭЯИЮ'
#     count = 0
#
#     # Проходим по каждому символу в строке
#     for char in text:
#         if char in vowels:
#             count += 1
#
#     return count
# # Запрашиваем ввод у пользователя
# user_input = input("Введите строку: ")
# vowel_count = count_vowels(user_input)
# # Выводим результат
# print(f"Количество гласных букв: {vowel_count}")

# a =  [1, 2, 3, 4, 5, 6]
# count = 0
# for i in a:
#     if i % 2 == 0:
#         count += i
# print('сумма четных чисел равна:', count)


# a = int(input('Введите  число: '))
# b = []
#
# print('Все делители числа: ', b)
# # Ввод: 18
# # Вывод: 1 2 3 6 9 18
#
# def find_common_substring(word1, word2):
#     min_length = min(len(word1), len(word2))
#     for i in range(min_length, 0, -1):
#         if word1[-i:] == word2[-i:]:
#             return word1[-i:]
#     return ""
#
#
# def find_related_words(words, target_word):
#     target_root = target_word.lower()
#
#     related_words = []
#     for word in words:
#         common_part = find_common_substring(word.lower(), target_root)
#         if common_part:
#             related_words.append(word)
#
#     return related_words
#
#
# # Пример использования
# # words = ['Able', 'Mable', 'Disable', 'Bagel']
# # target_word = 'Disablement'
# #
# # result = find_related_words(words, target_word)
# # print(result)

# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
#
#
# print(summa(5))
# def recursion():
#     recursion()

# recursion()
# stack = []
# stack.append(1)
# print('Добавили элемент' , stack)
# stack.append(2)
# print('Добавили элемент' , stack)
# stack.append(3)
# print('Добавили элемент' , stack)
# print(stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)

def get_multiplied_digits(number):
    str_number = str(number)
    if number == 0:
        return 1

    first = int(str_number[0])
    if len(str_number) > 1:
        if first != 0:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return get_multiplied_digits(int(str_number[1:]))
    else:
        return first if first != 0 else 1

result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)  