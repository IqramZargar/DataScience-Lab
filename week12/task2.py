from sklearn.tree import DecisionTreeClassifier

# 0 = Sunny, 1 = Rainy
X = [[0], [0], [1], [1], [1], [0]]

# 0 = No, 1 = Yes
y = [0, 0, 1, 1, 1, 0]

model = DecisionTreeClassifier(
    criterion="entropy",
    random_state=0
)

model.fit(X, y)

print("Sunny:", model.predict([[0]])[0])
print("Rainy:", model.predict([[1]])[0])