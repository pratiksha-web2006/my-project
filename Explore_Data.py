
# WEEK 3 - DAY 2
# Explore Sales Data

import pandas as pd

df = pd.read_csv("sales_data.csv")

# Display number of rows and columns
print("Dataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

print("\nData Exploration Completed!")
