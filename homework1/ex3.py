import re



def normalize_phone(phone_number):
    
    """
    Нормалізує телефонний номер до формату +380XXXXXXXXX
    """

    # Залишаємо лише цифри та плюс
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    # Якщо вже у форматі +38XXXXXXXXX
    if re.match(r"^\+38\d+$", cleaned):
        return cleaned

    # Якщо без плюса, але з 38 на початку
    if re.match(r"^38\d+$", cleaned):
        return "+" + cleaned

    # Якщо просто цифри (050, 097 тощо)
    return "+38" + cleaned



# Приклади
phones = [
    "38050-111-22-22",
    "    +38(050)123-32-34",
    "0503451234",
    "(050)8889900",
    "38050 111 22 11   "
]

for phone in phones:
    print(normalize_phone(phone))