import random

try:
    while True:
        secret_number = random.randint(1, 10)
        while int(input("Угадайте число от 1 до 10: ")) != secret_number:
            print("не угадали")
        print("верно!")
except ValueError:
    print("Ошибка: введите число!")
except Exception as e:
    print(f"Ошибка: {str(e)}")