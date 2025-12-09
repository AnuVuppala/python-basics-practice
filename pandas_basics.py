import pandas as pd
import matplotlib.pyplot as plt

data = {
    "id": range(1, 21),
    "value": [12, 45, 22, 33, 44, 55, 23, 20, 30, 34, 41, 39, 28, 26, 50, 48, 31, 29, 35, 40]
}
df = pd.DataFrame(data)
print("Head:\n", df.head())

# Basic stats
print("\nDescribe:\n", df["value"].describe())

# Save CSV
df.to_csv("example_values.csv", index=False)

# Plot
plt.hist(df["value"], bins=6)
plt.xlabel("Value")
plt.ylabel("Count")
plt.title("Value distribution (example)")
plt.savefig("value_histogram.png")
print("Saved value_histogram.png and example_values.csv")
