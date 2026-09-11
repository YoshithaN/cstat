import pandas as pd

data = {
    "Dept": ["IT", "HR", "IT", "Finance"],
    "Employee": ["A", "B", "C", "D"],
    "Salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nCross Tabulation:")
print(pd.crosstab(df["Dept"], df["Employee"]))

print("\nPivot Table:")
print(pd.pivot_table(df, values="Salary", index="Dept", aggfunc="sum"))

