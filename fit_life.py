# Проект FitLife - MVP версия 1.0

# 1. Знакомство
def meeting():
    '''Приветствует пользователя.

    Функция проверяет введённое значение с клавиатуры
    на предмет пустой строки. Если строка пустая, то 
    предлагает попробовать ввести значение снова. 

    Returns:
    name или выводит надпись: "Имя не может быть пустым. Попробуйте ещё раз."
    '''

    while True:
        name = input("Привет! Напиши своё имя: ").strip()
        if name:
            return name
        print('Имя не может быть пустым. Попробуйте ещё раз.')


def human_age(statement):
    """Проверяет введённый возраст с клавиатуры.

    Функция проверяет введённое значение с клавиатуры
    на предмет пустой строки и целого числа.

    Args:
    statement (str): Строка, которая выводиться при вызове функции.

    Returns:
    value: Целочисленное значение введённого значения с клавиатуры.
    """

    while True:
        user_ans = input(statement).strip()
        try:
            value = int(user_ans)
        except ValueError:
            print('Нужно ввести целое число. Попробуйте ещё раз.')
            continue
        if 1 <= value <= 130:
            return value
        print('Значение должно быть от 1 до 130. Попробуйте ещё раз.')


def human_weight_height(statement):
    """Проверяет введённый вес и рост с клавиатуры.
    
        Функция проверяет введённое значение с клавиатуры
        на предмет пустой строки и попадает ли значение в допустимый диапазон.
    
        Args:
        statement (str): Строка, которая выводиться при вызове функции.
    
        Returns:
        value: Значение с плавающей точкой, введённое с клавиатуры.
        """
    
    while True:
        user_ans = input(statement).strip()
        try:
            value = float(user_ans)
        except ValueError:
            print('Должно быть введено число. Попробуйте ещё раз.')
            continue
        if 1 <= value <= 300:
            return value
        print('Значение должно быть от 1 до 300. Попробуйте ещё раз.')


user_name = meeting()
age = human_age('Напиши свой возраст: ')

# 2. Сбор данных
weight = human_weight_height('Напиши свой вес (кг): ')
height = human_weight_height('Напиши свой рост в (м), с использованием ".": ')

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = weight / (height ** 2)
float_bmi = float(bmi)

# Подсчет воды: вес * 30 мл
# Перевод нормы воды в литры
water_l = (weight * 30) / 1000

# Подбор склонения в зависимости от возраста


def get_word(age_declension):
    if age_declension % 10 == 1 and age_declension % 100 != 11:
        return "год"
    elif 11 <= age_declension % 100 <= 14:
        return "лет"
    elif 2 <= age_declension % 10 <= 4:
        return "года"
    else:
        return "лет"


word = get_word(age)

# 4. Вывод красивого результата
print()
print("Отчёт для пользователя:", user_name, (f"{age}"), word)
print(f"Твой Индекс Массы Тела: {float_bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л в день")
print("Расчет окончен. Будьте здоровы!")
