import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sales_data.csv')
data['Revenue'] = data['Quantity'] * data['Price']

product_revenue = data.groupby('Product')['Revenue'].sum()

plt.figure()
product_revenue.plot(kind='bar')
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.show()

print(product_revenue)
