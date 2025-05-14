import pandas as pd
import matplotlib.pyplot as plt

items_df = pd.read_csv('src/data/Items.csv')
customers_df = pd.read_csv('src/data/customers.csv')
orders_df = pd.read_csv('src/data/orders.csv')
order_item_df = pd.read_csv('src/data/order_item.csv')

## section 1

#  1
print(items_df['item_price'].mean())


## section 2

#  1
gender_counts = customers_df.dropna()['gender'].value_counts()
bars = plt.bar(gender_counts.index, gender_counts.values)
plt.title('Distribution of gender')
plt.xlabel('Gender')
plt.ylabel('Amount')
plt.bar_label(bars)
plt.show()

# 2
nationality_counts = customers_df.dropna()['nationallity'].value_counts()
bars = plt.bar(nationality_counts.index, nationality_counts.values)
plt.title('Distribution of nationality')
plt.xlabel('Nationality')
plt.ylabel('Amount')
plt.bar_label(bars)
plt.show()

# 3
plt.hist(customers_df['age'], bins=10, edgecolor='black')
plt.title('Distribution of customer ages')
plt.xlabel('Age')
plt.ylabel('Number of customers')
plt.show()






