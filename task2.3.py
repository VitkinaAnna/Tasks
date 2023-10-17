import random

def play_game():
    options = ["камінь", "ножиці", "папір"]

    while True:
        user_choice = input("оберіть ваш варіант (камінь, ножиці, папір) або введіть 'вийти': ").lower()

        if user_choice == "вийти":
            print("гра завершена.")
            break
        elif user_choice in options:
            computer_choice = random.choice(options)
            print(f"комп'ютер обрав: {computer_choice}")

            if user_choice == computer_choice:
                print("нічия")
            elif (
                    (user_choice == "ножиці" and computer_choice == "папір") or
                    (user_choice == "камінь" and computer_choice == "ножиці") or
                    (user_choice == "папір" and computer_choice == "камінь")
            ):
                print("ви перемогли")
            else:
                print("комп'ютер переміг.")
        else:
            print("невірний вибір. спробуйте ще раз.")

if __name__ == "__main__":
    print("Гра 'камінь, ножиці, папір'")
    play_game()
