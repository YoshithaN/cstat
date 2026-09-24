import pandas as pd

df = pd.read_csv("Population_Murder_Rate.csv")

print("Mean:")
print(df[["Population", "Murder Rate"]].mean())

print("Median:")
print(df[["Population", "Murder Rate"]].median())

print("Variance:")
print(df[["Population", "Murder Rate"]].var())
