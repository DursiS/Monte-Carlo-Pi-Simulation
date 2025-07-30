""" Outside Modules """
import matplotlib.pyplot as plt
import numpy as np


""" Random lengths of the square """
sims = int(input("Number of simulations: "))
while sims <= 0:
    print("Invalid.")
    sims = int(input("Number of simulations: "))
x = np.random.uniform(-1, 1, sims)
y = np.random.uniform(-1, 1, sims)
points = np.column_stack((x, y))


""" How many points in circle """
inside = ( (x**2 + y**2) <= 1 )
points_inside = points[inside]
count_inside = points_inside.shape[0]
count_total = points.shape[0]
print(f"Inside: {count_inside}, Total: {count_total}")


""" Approximates pi """
pi = 4 * (count_inside / count_total )
print(f"Approximate pi: {pi}")


""" Scatters the random points """
fig, ax = plt.subplots()
ax.scatter(x, y, c='red', alpha=0.6, s=1)


""" Plots a circle """
x_axis = np.linspace(-1, 1, 200)
y_axis = np.sqrt(1 - x_axis**2)
ax.plot(x_axis, y_axis, c='white')
ax.plot(x_axis, -y_axis, c='white')


""" Graph Settings """
ax.set_facecolor('#333333')
fig.patch.set_facecolor('#1A1A1A')
ax.axis('scaled')
ax.grid(True)
ax.set_ylim(-1, 1)
ax.set_xlim(-1, 1)
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
plt.title(f"Approximate pi: {pi}", color='white')
plt.show()






