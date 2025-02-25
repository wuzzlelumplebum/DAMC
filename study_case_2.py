import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# read data from csv file
data = pd.read_csv('sales_data.csv')

# convert ORDERDATE data type to datetime
data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'])

# calculate total sales
data['TotalSales'] = data['QUANTITYORDERED'] * data['PRICEEACH']

# group sales per month
data['YearMonth'] = data['ORDERDATE'].dt.to_period("M")
monthly_sales = data.groupby('YearMonth')["TotalSales"].sum()

# visualize monthly sales data
plt.figure(figsize=(12, 6))
ax = monthly_sales.plot(marker="o")

# chart format
plt.title('Monthly Sales Graph', fontsize=14)
plt.xlabel('Time (Year Month)')
plt.ylabel('Total Sales')
plt.xticks(rotation=15)  # rotate month labels if necessary
plt.grid(axis='y', linestyle='--', alpha=0.7)  # add a grid for easy reading

# number format for y axis
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))

plt.tight_layout()
plt.show()

# calculate the percentage change in monthly sales
percentage_changes = monthly_sales.pct_change() * 100

# visualize percentage changes
plt.figure(figsize=(12, 6))
ax = percentage_changes.plot(kind='bar', color='skyblue') # save axes to add labels

# chart format
plt.title('Monthly Sales Percentage Change', fontsize=14)
plt.xlabel('Time (Year-Month)')
plt.ylabel('Percentage Change')
plt.xticks(rotation=30)  # rotate month labels if necessary
plt.grid(axis='y', linestyle='--', alpha=0.7)

# add labels to bars
for p in ax.patches:
    ax.annotate(f"{p.get_height():,.0f}%", (p.get_x() + p.get_width()/2, p.get_height()),
                ha="center", va="bottom", fontsize=10, color="black", xytext=(0, 5),
                textcoords="offset points")

plt.tight_layout()
plt.show()

# identify pattern in sales trends
highest_sales_month = monthly_sales.idxmax().strftime('%B %Y')
lowest_sales_month = monthly_sales.idxmin().strftime('%B %Y')
avg_sales = f'${monthly_sales.mean():,.0f}'
med_sales = f'${monthly_sales.median():,.0f}'
ovr_trend = "Increasing" if monthly_sales.iloc[-1] > monthly_sales.iloc[0] else "Decreasing"

# print analysis results
print("\n====== Monthly Sales Analysis ======")
print(f"Highest Sales Month     : {highest_sales_month}")
print(f"Lowest Sales Month      : {lowest_sales_month}")
print(f"Average Sales           : {avg_sales}")
print(f"Median Sales            : {med_sales}")
print(f"Overall Trend           : {ovr_trend}")
print("====================================\n")