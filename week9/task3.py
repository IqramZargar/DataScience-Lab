import matplotlib.pyplot as plt

tests = [1, 2, 3]
marks = [60, 75, 90]

plt.plot(tests, marks, marker="o")
plt.xlabel("Test Number")
plt.ylabel("Marks")
plt.title("Student Performance")
plt.show()