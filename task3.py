import random
import matplotlib.pyplot as plt
import numpy as np

def is_inside_heart(x, y):
    return (x ** 2 + (y - np.sqrt(abs(x))) ** 2) <= 1

def estimate_area(N):
    points_inside = 0

    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(N):
        x = random.uniform(-1.5, 1.5)
        y = random.uniform(-1, 1.7)

        if is_inside_heart(x, y):
            points_inside += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    estimated_area = (points_inside / N) * 8.1

    return x_inside, y_inside, x_outside, y_outside, estimated_area

N = 10000
x_inside, y_inside, x_outside, y_outside, estimated_area = estimate_area(N)
plt.figure(figsize=(6, 6))

t = np.linspace(-1, 1, 400)
x_heart = t
y_heart = np.sqrt(abs(t)) - np.sqrt(-t * t + 1)
plt.plot(x_heart, y_heart, color='red')

t = np.linspace(-1, 1, 400)
x_heart_top = t
y_heart_top = np.sqrt(abs(t)) + np.sqrt(-t * t + 1)
plt.plot(x_heart_top, y_heart_top, color='red', linewidth=2)

plt.scatter(x_inside, y_inside, color='yellow', s=5)
plt.scatter(x_outside, y_outside, color='blue', s=5)

plt.axis('equal')
plt.title(f"Приблизна площа: {estimated_area:.4f}")

plt.show()