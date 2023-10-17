import random
import matplotlib.pyplot as plt

# Параметри для обчислювального експерименту
N = 10000  # Змініть це значення на бажане

# Функція для підкидання кубика та підрахунку результатів
def roll_dice(N):
    outcomes = [random.randint(1, 6) for _ in range(N)]
    return outcomes

# Виконання експерименту
dice_rolls = roll_dice(N)

# Побудова гістограми розподілу результатів
plt.hist(dice_rolls, bins=range(1, 8), align='left', rwidth=0.8, alpha=0.75, edgecolor='black')
plt.xticks(range(1, 7))
plt.xlabel('Випадковий результат')
plt.ylabel('Кількість випадків')
plt.title('Гістограма розподілу результатів підкидання кубика')
plt.show()

# Очікувані результати для кожного можливого результату від 1 до 6
expected_results = [N / 6] * 6  # Очікувана кількість кожного результату

# Фактичні результати
actual_results = [dice_rolls.count(i) for i in range(1, 7)]

# Виведення очікуваних і фактичних результатів в консоль
for i in range(6):
    print(f"Очікувана кількість {i + 1}: {expected_results[i]}")
    print(f"Фактична кількість {i + 1}: {actual_results[i]}")
