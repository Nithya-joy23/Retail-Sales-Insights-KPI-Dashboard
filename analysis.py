import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# convert order date to proper format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# create month column
df["Month"] = df["Order Date"].dt.month


# STEP 2: Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()


# STEP 3: Profit by Region
region_profit = df.groupby("Region")["Profit"].sum()

region_profit.plot(kind="bar")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.show()


# STEP 4: Monthly Sales Trend
monthly_sales = df.groupby("Month")["Sales"].sum()

monthly_sales.plot(kind="line")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()


# STEP 5: Top 5 Products
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head()

top_products.plot(kind="bar")

plt.title("Top 5 Products")
plt.xlabel("Product Name")
plt.ylabel("Sales")

plt.show()