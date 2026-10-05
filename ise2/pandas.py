#analyze sales data using pandas and identify the highest selling product and total sales by category
import pandas as pd

df = pd.read_csv("sales.csv")

product_sales = df.groupby("Product")["Sales"].sum()
highest_selling_product = product_sales.idxmax()
highest_sales = product_sales.max()

print("Highest Selling Product:", highest_selling_product)
print("Total Sales:", highest_sales)

category_sales = df.groupby("Category")["Sales"].sum()

print("\nTotal Sales by Category:")
print(category_sales)
