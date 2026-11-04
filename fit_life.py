# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
user_name = input("Привет! Напиши своё имя: ")

# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать в число)
user_age = input("Напиши свой возраст: ")
int_user_age = int(user_age)

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
user_weight = input("Напиши свой вес (кг): ")
float_user_weight = float(user_weight)

# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)
user_height = input("Напиши свой рост в (м), с использованием '.': ")
float_user_height = float(user_height)

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = float_user_weight / (float_user_height ** 2)
float_bmi = float(bmi)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_ml = float_user_weight * 30 
# Перевод нормы воды в литры
water_l = water_ml / 1000

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print()
print("Отчёт для пользователя:", user_name, (f"{int_user_age} г.") )
print("Твой Индекс Массы Тела:", round(float_bmi, 1))
print("Рекомендуемая норма воды:", water_l, "л. в день")
print("Расчет окончен. Будьте здоровы!")