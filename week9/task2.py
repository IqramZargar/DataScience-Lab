import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Raj"],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print(df)
print("Average marks:", df["Marks"].mean())