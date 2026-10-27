import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 6])

model = LinearRegression()
model.fit(x, y)

predicted = model.predict(x)
residuals = y - predicted

print("Predicted values:", predicted)
print("Residuals:", residuals)

plt.scatter(x, residuals)
plt.axhline(y=0, color="red")
plt.xlabel("X")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()