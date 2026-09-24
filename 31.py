import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("River_Temperature.csv")

swale = df[df["Site Name"] == "Swale at Catterick Bridge"]

print("Mean Temperature:", swale["Temperature"].mean())
print("Median Dissolved Oxygen:", swale["Dissolved Oxygen"].median())

plt.hist(swale["Temperature"], bins=10)
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.title("Temperature Distribution - Swale at Catterick Bridge")
plt.show()
