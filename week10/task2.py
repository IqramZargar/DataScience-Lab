marks = [80, 90, 70]
weights = [0.2, 0.5, 0.3]

weighted_sum = 0

for i in range(len(marks)):
    weighted_sum += marks[i] * weights[i]

print("Weighted average:", weighted_sum)