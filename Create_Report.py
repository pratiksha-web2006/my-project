
# WEEK 3 - DAY 5
# Project: Sales Data Analysis
# Topic: Create Sales Report

import pandas as pd

# Step 1: Load cleaned sales data
df = pd.read_csv("cleaned_sales_data.csv")

# Step 2: Calculate total revenue
total_revenue = df["Total_Sales"].sum()

# Step 3: Calculate total quantity
total_quantity = df["Quantity"].sum()

# Step 4: Calculate average sales
average_sales = df["Total_Sales"].mean()

# Step 5: Find highest and lowest sales
highest_sales = df["Total_Sales"].max()
lowest_sales = df["Total_Sales"].min()

# Step 6: Find best selling product
product_sales = df.groupby("Product")["Quantity"].sum()
best_product = product_sales.idxmax()

# Step 7: Create report
report = f"""
========================================
       SALES DATA ANALYSIS REPORT
========================================

PROJECT OVERVIEW:
This project analyzes sales data using Python
and Pandas library.

SALES SUMMARY:

Total Revenue: Rs. {total_revenue:,.2f}

Total Quantity Sold: {total_quantity}

Average Sales: Rs. {average_sales:,.2f}

Highest Sales: Rs. {highest_sales:,.2f}

Lowest Sales: Rs. {lowest_sales:,.2f}

BEST SELLING PRODUCT:
{best_product}

PRODUCT WISE SALES:
{product_sales.to_string()}

INSIGHTS:

1. Total revenue is Rs. {total_revenue:,.2f}.
2. Best selling product is {best_product}.
3. Total {total_quantity} items were sold.
4. Sales data was analyzed successfully.

CONCLUSION:

Sales data analysis helps understand business
performance and identify best selling products.

========================================
          END OF REPORT
========================================
"""

# Step 8: Display report
print(report)

# Step 9: Save report in file
with open("analysis_report.md", "w", encoding="utf-8") as file:
    file.write(report)

print("\nReport Created Successfully!")
print("Day 5 Task Completed!")
print("Week 3 Project Completed!")
