import pandas as pd



data = {
    'product': ['Laptop', 'phone', 'table', 'headphones'],
    'price': [1200, 800, 400, 150],
    'stock': [10, 25, 15, 50]
}

df = pd.DataFrame(data)
df.to_csv('product.csv', index=False)

df_read = pd.read_csv('product.csv')
print(df_read)