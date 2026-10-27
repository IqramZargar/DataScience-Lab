from sklearn.naive_bayes import GaussianNB

# Features: study hours and attendance
X = [
    [1, 40],
    [2, 50],
    [3, 60],
    [7, 80],
    [8, 90],
    [9, 95]
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

model = GaussianNB()
model.fit(X, y)

result = model.predict([[8, 85]])

if result[0] == 1:
    print("Result: Pass")
else:
    print("Result: Fail")