
# WEEK 3 - DAY 4
# Project: Sales Data Analysis
# Topic: Analyze Sales

import pandas as pd

# Step 1: Load cleaned sales data
df = pd.read_csv("cleaned_sales_data.csv")

print("====================================")
print("       SALES DATA ANALYSIS")
print("====================================")

# Step 2: Calculate total revenue
total_revenue = df["Total_Sales"].sum()

# Step 3: Calculate total quantity sold
total_quantity = df["Quantity"].sum()

# Step 4: Calculate average sales
average_sales = df["Total_Sales"].mean()

# Step 5: Find highest sales
highest_sales = df["Total_Sales"].max()

# Step 6: Find lowest sales
lowest_sales = df["Total_Sales"].min()

# Step 7: Find best selling product
product_sales = df.groupby("Product")["Quantity"].sum()

best_product = product_sales.idxmax()

# Step 8: Display sales analysis
print("\nTotal Revenue:")
print("Rs.", total_revenue)

print("\nTotal Quantity Sold:")
print(total_quantity)

print("\nAverage Sales:")
print("Rs.", round(average_sales, 2))

print("\nHighest Sales:")
print("Rs.", highest_sales)

print("\nLowest Sales:")
print("Rs.", lowest_sales)

print("\nBest Selling Product:")
print(best_product)

# Step 9: Display product wise sales
print("\nProduct Wise Sales:")
print(product_sales)

print("\n====================================")
print("     ANALYSIS COMPLETED!")
print("====================================")
