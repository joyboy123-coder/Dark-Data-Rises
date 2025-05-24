import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

input_file = input('Enter cleaned output file : ').strip('"')
df = pd.read_csv(input_file)

sns.set(style="darkgrid")


# Bar Graph

product_quantity = df.groupby('PRODUCT')['QUANTITY'].sum().reset_index()

fig1 = plt.figure(figsize=(6,6))

sns.barplot(data = product_quantity,x= 'PRODUCT',y='QUANTITY',palette='viridis')
plt.title('Total Quantity Ordered By Product')
plt.xlabel('Product')
plt.ylabel('Total Quantity')
plt.xticks(rotation = 45)
plt.tight_layout()
fig1.savefig("Bar_graph.png", dpi=300, bbox_inches="tight")
plt.show()  # Show bar graph before moving on

# Pie Chart 

status_counts = df['ORDERSTATUS'].value_counts()

fig2 = plt.figure(figsize=(6, 6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Order Distribution by Status')
plt.tight_layout()
fig2.savefig("Pie_chart.png", dpi=300, bbox_inches="tight")
plt.show()
