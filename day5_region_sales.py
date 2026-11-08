import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

region_sales = data.groupby("Region")["Sales"].sum()

plt.figure(figsize=(7, 7))

plt.pie(
    region_sales.values,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales by Region")

plt.show()