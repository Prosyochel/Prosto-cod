import random

print("Добро пожаловать в игру 'Угадай число'!")
print("Сначала выбери диапазон чисел.")

# Выбор диапазона
while True:
    start = input("Начало диапазона: ")
    end = input("Конец диапазона: ")

    if start.replace('.', '', 1).isdigit() and end.replace('.', '', 1).isdigit():
        start = float(start)
        end = float(end)
        if start < end:
            break
        else:
            print("Начало диапазона должно быть меньше конца.")
    else:
        print("Пожалуйста, введите корректные числа.")

# Секретное число с одним знаком после запятой
secret_number = round(random.uniform(start, end), 1)

# Ограничение на количество попыток
max_attempts = 7
attempts = 0
history = []
last_diff = None

print(f"\nЯ загадал число от {start} до {end} (с одним знаком после запятой).")
print(f"У тебя есть {max_attempts} попыток. Удачи!\n")

while attempts < max_attempts:
    guess = input(f"Попытка {attempts + 1}: ")

    try:
        guess = float(guess)
    except ValueError:
        print("Пожалуйста, введи число.")
        continue

    attempts += 1
    history.append(guess)

    diff = abs(secret_number - guess)

    if guess == secret_number:
        print(f"\nПоздравляю! Ты угадал число {secret_number} за {attempts} попыток.")
        break
    else:
        if guess < secret_number:
            print("Слишком мало!")
        else:
            print("Слишком много!")

        # Подсказка "теплее/холоднее"
        if last_diff is not None:
            if diff < last_diff:
                print("Теплее 🔥")
            elif diff > last_diff:
                print("Холоднее ❄️")
            else:
                print("Ничего не изменилось 🤔")
        last_diff = diff

        print(f"Осталось попыток: {max_attempts - attempts}")
        print(f"История попыток: {history}\n")

else:
    print(f"\nК сожалению, ты проиграл. Загаданное число было: {secret_number}")
