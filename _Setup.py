
# WEEK 4 - DAY 1
# Project: Data Visualization
# Topic: Setup and Load Data

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load sales dataset
df = pd.read_csv("sales_data.csv")

# Step 2: Display project title
print("====================================")
print("     DATA VISUALIZATION PROJECT")
print("====================================")

# Step 3: Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# Step 4: Display complete dataset
print("\nComplete Sales Data:")
print(df)

# Step 5: Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Step 6: Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Step 7: Display data types
print("\nData Types:")
print(df.dtypes)

# Step 8: Display total sales
total_sales = df["Total_Sales"].sum()

print("\nTotal Sales:")
print("Rs.", total_sales)

# Step 9: Display average sales
average_sales = df["Total_Sales"].mean()

print("\nAverage Sales:")
print("Rs.", round(average_sales, 2))

# Step 10: Display success message
print("\nData Loaded Successfully!")
print("Week 4 Day 1 Completed!")
