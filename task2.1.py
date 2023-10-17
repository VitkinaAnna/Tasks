def guess_number(user_number, A, B):
    # Початкові межі пошуку
    left = A
    right = B
    attempts = 0  # Лічильник спроб
    while left <= right:
        mid = (left + right) // 2  # Середина поточного діапазону
        attempts += 1
        print(f"Чи це число більше, менше або дорівнює {mid}? (більше/менше/дорівнює): ")
        user_input = input()
        if mid == user_number:
            return mid, attempts  # Комп'ютер вгадав число
        elif user_input == "більше":
            left = mid + 1  # Зсуваємо ліву межу діапазону
        elif user_input == "менше":
            right = mid - 1  # Зсуваємо праву межу діапазону
        else:
            print("Будь ласка, введіть 'більше', 'менше' або 'дорівнює'.")
    return None, attempts  # Задумане число не було знайдено

# Визначте межі для вашого завдання
A = 1
B = 100
print("Загадайте число від", A, "до", B)
# Отримання числа від користувача
user_number = int(input("Введіть ваше число: "))
# Виконання алгоритму відгадування
found_number, attempts = guess_number(user_number, A, B)
if found_number is not None:
    print(f"Комп'ютер вгадав ваше число {found_number} за {attempts} спроб.")
else:
    print(f"Комп'ютер не зміг вгадати ваше число за {attempts} спроб.")
