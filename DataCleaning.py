import pandas as pd

pd.set_option('display.width', 600)
pd.set_option('display.max_columns', 18)

# Importing the dataset
sales_df = pd.read_csv("C:/Users/acrum/Documents/train.csv")
print()

# Finding if there are null values in any columns of the dataset
print(sales_df.isnull().sum())

# Revealing which rows contain null or 'NaN' values
print(sales_df[sales_df['Postal Code'].isnull()])

# Adding correct postal codes to rows with the missing values
sales_df['Postal Code'] = sales_df['Postal Code'].fillna(5401)

# Checking if problemn was solved
print(sales_df.isnull().sum())

# Creating a new csv containing corrected data
sales_df.to_csv("C:/Users/acrum/Documents/FixedData.csv")