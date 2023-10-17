import random

# Параметри для обчислювального експерименту
N = 100000

# Функція для підкидання монети та підрахунку кількості Орлів і Решок
def flip_coin(N):
    outcomes = [random.choice(['Орел', 'Решка']) for _ in range(N)]
    heads_count = outcomes.count('Орел')
    tails_count = outcomes.count('Решка')
    return heads_count, tails_count

# Виконання експерименту
heads_count, tails_count = flip_coin(N)

# Очікувана кількість Орлів і Решок
p = 0.5  # Ймовірність випадіння Орла або Решки в одному підкиданні
expected_heads = N * p
expected_tails = N * (1 - p)

# Виведення кількості підкидань та очікуваних факторів
print("Кількість підкидань: ", N)
print("Очікувана кількість Орлів:", expected_heads)
print("Фактична кількість Орлів:", heads_count)
print("Очікувана кількість Решок:", expected_tails)
print("Фактична кількість Решок:", tails_count)
