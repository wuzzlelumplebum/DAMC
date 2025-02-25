import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# read data from csv file
data = pd.read_csv('./data/sales_data.csv')

# calculate total sales
data['TotalSales'] = data['QUANTITYORDERED'] * data['PRICEEACH']

# sales per product line from highest to lowest
sales_ppl = data.groupby('PRODUCTLINE')['TotalSales'].sum().sort_values(ascending=False)

# create chart for highest and lowest product lines
plt.figure(figsize=(10, 6))
ax = sales_ppl.plot(kind='bar', color="skyblue")  # save axes to add labels

# chart format
plt.title("Total Sales per Product Lines", fontsize=14)
plt.xlabel("Product Lines")
plt.ylabel("Total Sales")
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# number format on x
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))

# add a sales total label on each bar
for p in ax.patches:
    ax.annotate(f"${p.get_height():,.0f}", (p.get_x() + p.get_width()/2, p.get_height()),
                ha="center", va="bottom", fontsize=10, color="black", xytext=(0, 5),
                textcoords="offset points")

# adjust layout
plt.tight_layout()

# show chart
plt.show()