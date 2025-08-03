from datetime import datetime 

def get_days_from_today(date: str) -> int:
    """
    Обчислює кількість днів від заданої дати до сьогоднішньої.

    параметри:
    date: (str)

    повертає:
    int: Кількість днів від заданої дати до поточної.
    
    """
    # блок try для відловлення неправильного формату вхідних даних
    try:
        # беремо поточну дату
        time_now = datetime.today()
        # повертаєо різницю між теперішньою датою та заданій
        return (time_now.date() - datetime.strptime(date, "%Y-%m-%d").date()).days
    
    except ValueError:
        return "Неправильний формат дати. Використовуйте РРРР-ММ-ДД."


# виклик функції
test = get_days_from_today("2020-10-09")
print(test)
