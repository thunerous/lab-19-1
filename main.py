import pandas as pd

df = pd.read_csv('start.csv')

print("Массив для первого города:")
print(df.iloc[:, 0])
print("\nМассив для второго города:")
print(df.iloc[:, 1])
