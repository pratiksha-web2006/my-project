import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

plt.figure(figsize=(8, 5))

plt.scatter(data["Sales"], data["Profit"])

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()