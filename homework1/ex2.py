import random


def get_numbers_ticket(min_value, max_value, quantity):
    """
    Генерує унікальні випадкові числа для лотереї

    параметри:
    min_value: (int) - мінімальне значення вибірки
    max_value: (int) - максимальне значення вибірки
    quantity: (int) - кількість чисел для вибору


    повертає:
    list: Відсортований список всіх унікальних чисел
    """
    # Перевіряємо на недопустимі умови
    if min_value > max_value or quantity > (max_value-min_value+1):
        return []

    result = set()
    # ітеруємо доти допоки довжина нашого сет не буде рівним quantity
    while len(result) != quantity:
        # Додаємо випадкові числа в заданому діапазоні
        result.add(random.randint(min_value, max_value))
    # повертаємо відсортований масив
    return sorted(list(result))



    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа: {lottery_numbers}")
