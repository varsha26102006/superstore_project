import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('superstore.csv',encoding='latin1')
print(df.head())
print(df.shape)
df.info()
print(df.describe())
df.columns.tolist()
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
print(df.dtypes)
df = df.drop_duplicates()
df.info()
df['City']=df['City'].fillna('Unknown')
# 1. Sales & Profit by Region
region_summary = df.groupby('Region')[['Sales', 'Profit']].sum().sort_values('Profit', ascending=False)
print(region_summary)

# 2. Sales & Profit by Category
category_summary = df.groupby('Category')[['Sales', 'Profit']].sum()
print(category_summary)

# 3. Sub-category profitability (find the losers)
subcat_summary = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values('Profit')
print(subcat_summary)

# 4. Discount vs Profit relationship
discount_profit = df.groupby('Discount')['Profit'].mean()
print(discount_profit)

# 5. Monthly sales trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
print(monthly_sales)

# 6. Top 10 customers by sales
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_customers)

# 7. Sales by Segment
segment_summary = df.groupby('Segment')[['Sales', 'Profit']].sum()
print(segment_summary)

# Set a clean visual style for all charts
sns.set_style('whitegrid')

# Chart 1: Profit by Region
plt.figure(figsize=(8,5))
sns.barplot(x=region_summary.index, y=region_summary['Profit'])
plt.title('Total Profit by Region')
plt.ylabel('Profit ($)')
plt.savefig('chart1_profit_by_region.png')   # saves the image into your project folder
plt.show()

# Chart 2: Monthly Sales Trend
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.ylabel('Sales ($)')
plt.xlabel('Month')
plt.savefig('chart2_monthly_trend.png')
plt.show()

# Chart 3: Discount vs Profit
plt.figure(figsize=(8,5))
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title('Discount vs Profit')
plt.savefig('chart3_discount_vs_profit.png')
plt.show()

# Chart 4: Sales by Category
plt.figure(figsize=(8,5))
sns.barplot(x=category_summary.index, y=category_summary['Sales'])
plt.title('Total Sales by Category')
plt.savefig('chart4_sales_by_category.png')
plt.show()

