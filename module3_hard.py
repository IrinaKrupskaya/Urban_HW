def calculate_structure_sum(structure):
    total_sum = 0

    # Рекурсивная функция для обработки различных типов данных
    def process_element(element):
        nonlocal total_sum

        if isinstance(element, int):
            total_sum += element
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, list) or isinstance(element, tuple) or isinstance(element, set):
            for item in element:
                process_element(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                process_element(key)
                process_element(value)
        else:
            print(f'Неизвестный тип {type(element)}')

    # Обработка входного аргумента
    if isinstance(structure, list) or isinstance(structure, tuple) or isinstance(structure, set):
        for item in structure:
            process_element(item)
    else:
        raise ValueError("Неверный тип входных данных")

    return total_sum


# Входные данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вызов функции
result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99