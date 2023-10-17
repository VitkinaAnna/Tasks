import matplotlib.pyplot as plt
import numpy as np

def is_inside_figure(x, y, z):
    return z >= x ** 2 + y ** 2

def estimate_volume(N):
    points_inside = 0

    x_inside = []
    y_inside = []
    z_inside = []
    x_outside = []
    y_outside = []
    z_outside = []

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(0, 2)

        if is_inside_figure(x, y, z):
            points_inside += 1
            x_inside.append(x)
            y_inside.append(y)
            z_inside.append(z)
        else:
            x_outside.append(x)
            y_outside.append(y)
            z_outside.append(z)

    estimated_volume = (points_inside / N) * 8

    return x_inside, y_inside, z_inside, x_outside, y_outside, z_outside, estimated_volume

N = 10000
x_inside, y_inside, z_inside, x_outside, y_outside, z_outside, estimated_volume = estimate_volume(N)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
x, y = np.meshgrid(x, y)
z = x ** 2 + y ** 2

ax.plot_surface(x, y, z, color='red', alpha=0.5)

ax.scatter(x_inside, y_inside, z_inside, c='yellow', s=5, label='Inside the figure')
ax.scatter(x_outside, y_outside, z_outside, c='blue', s=5, label='Outside the figure')

ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f"Estimated Volume: {estimated_volume:.4f}")
plt.show()
