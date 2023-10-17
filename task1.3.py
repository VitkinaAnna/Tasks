import random
import matplotlib.pyplot as plt

# Параметри для обчислювального експерименту
N = 10000
# Функція для підкидання двох кубиків та підрахунку суми результатів
def roll_two_dice(N):
    outcomes = [random.randint(1, 6) + random.randint(1, 6) for _ in range(N)]
    return outcomes
# Виконання експерименту
dice_rolls = roll_two_dice(N)

# Побудова гістограми розподілу результатів
plt.hist(dice_rolls, bins=range(2, 14), align='left', rwidth=0.8, alpha=0.75, edgecolor='black')
plt.xticks(range(2, 13))
plt.xlabel('Випадковий результат')
plt.ylabel('Кількість випадків')
plt.title('Гістограма розподілу результатів підкидання двох кубиків')
plt.show()
# Очікувані результати для кожного можливого результату від 2 до 12
expected_results = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
# Фактичні результати
actual_results = [dice_rolls.count(i) for i in range(2, 13)]
# Фактичні результати
actual_probabilities = [result / N for result in actual_results]

# Виведення очікуваних та фактичних результатів і ймовірностей в консоль
for i in range(2, 13):
    print(f"Сума {i}:")
    print(f"Очікуваний результат: {expected_results[i-2]}")
    print(f"Фактичний результат: {actual_results[i-2]}")
    print(f"Фактичний результат: {actual_probabilities[i-2]:.4f}")
