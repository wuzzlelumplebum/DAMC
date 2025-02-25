import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read data from csv file
data = pd.read_csv('./data/sales_data.csv')

# calculate total sales
data['TotalSales'] = data['QUANTITYORDERED'] * data['PRICEEACH']

# calculate total sales per DEALSIZE
deal_sales = data.groupby('DEALSIZE')['TotalSales'].sum().sort_values(ascending=False)

# box plot to visualize distribution of total sales per deal size
plt.figure(figsize=(8,6))
sns.boxplot(x="DEALSIZE", y="TotalSales", data=data, order=['Small', 'Medium', 'Large'])

# chart format
plt.title("Distribution of Total Sales by Deal Size", fontsize=14)
plt.xlabel("Deal Size")
plt.ylabel("Total Sales ($)")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# visualize contribution percentage
plt.figure(figsize=(8,8))
colors = ["#ff9999", "#66b3ff", "#99ff99"]
deal_sales.plot(kind="pie", autopct="%1.1f%%", startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})

# chart format
plt.title("Percentage Contribution of Total Sales by Deal Size", fontsize=14)
plt.ylabel("")

plt.tight_layout()
plt.show()