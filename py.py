
import pandas as pd
import numpy as np
import time


# Завдання 1

df_a = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Department': ['HR', 'Engineering', 'Marketing']
})

df_b = pd.DataFrame({
    'EmployeeID': [4, 5],
    'Name': ['David', 'Eva'],
    'Department': ['Finance', 'IT']
})

result = pd.concat(
    [df_a, df_b],
    keys=['Group_A', 'Group_B']
)

print("Завдання 1:")
print(result)


# Завдання 2

orders_df = pd.DataFrame({
    'OrderID': [1001, 1002, 1003, 1004],
    'CustomerID': [1, 2, 1, 3],
    'ProductID': [501, 502, 503, 504],
    'Quantity': [2, 1, 5, 3]
})

customers_df = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David']
})

result = pd.merge(
    orders_df,
    customers_df,
    on='CustomerID',
    how='inner',
    indicator=True
)

print("\nЗавдання 2:")
print(result)
print(result['_merge'].value_counts())


# Завдання 3

np.random.seed(0)

transactions_df = pd.DataFrame({
    'TransactionID': range(1, 100001),
    'UserID': np.random.randint(1, 1001, size=100000),
    'ProductID': np.random.randint(1, 500, size=100000),
    'Date': pd.date_range(start='2023-01-01', periods=100000, freq='min'),
    'Amount': np.random.uniform(10.0, 1000.0, size=100000)
})

products_df = pd.DataFrame({
    'ProductID': range(1, 500),
    'ProductName': [f'Product_{i}' for i in range(1, 500)],
    'Price': np.random.uniform(10.0, 1000.0, size=499)
})

transactions_df['Amount'] = transactions_df['Amount'].astype('float32')

start = time.perf_counter()
result1 = transactions_df.merge(
    products_df,
    on='ProductID',
    how='left'
)
time1 = time.perf_counter() - start

transactions_indexed = transactions_df.set_index(['UserID', 'ProductID'])

start = time.perf_counter()
result2 = transactions_indexed.merge(
    products_df.set_index('ProductID'),
    left_on='ProductID',
    right_index=True,
    how='left'
)
time2 = time.perf_counter() - start

print("\nЗавдання 3:")
print("Злиття без індексу:", time1)
print("Злиття з індексом:", time2)
print(transactions_indexed.head())
print(result2.head())


# Завдання 4

df_sales = pd.DataFrame({
    'SaleID': [2001, 2002, 2003, 2004, 2005],
    'StoreID': [10, 20, 10, 30, 20],
    'ProductID': [301, 302, 303, 301, 304],
    'UnitsSold': [50, 60, 70, 80, 90]
})

df_suppliers = pd.DataFrame({
    'SupplierID': [401, 402, 403, 404],
    'ProductID': [301, 302, 303, 305],
    'SupplierName': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D']
})

df_sales = df_sales.set_index(['StoreID', 'ProductID'])

result = df_sales.merge(
    df_suppliers,
    left_on='ProductID',
    right_on='ProductID',
    how='left',
    validate='many_to_one',
    suffixes=('_sales', '_suppliers')
)

print("\nЗавдання 4:")
print(result)
