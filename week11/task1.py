import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)

plt.plot(x, y)
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.show()