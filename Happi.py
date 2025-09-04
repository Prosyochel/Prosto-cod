import random

secret_number = random.randint(1, 10)
attempts = 0

print("Я загадал число от 1 до 10. Попробуй угадать!")

while True:
    guess = input("Твой вариант: ")

    if not guess.isdigit():
        print("Пожалуйста, введи число.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Слишком мало!")
    elif guess > secret_number:
        print("Слишком много!")
    else:
        print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток.")
        break
