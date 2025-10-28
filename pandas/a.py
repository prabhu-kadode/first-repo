import pandas as pd

s = pd.Series([1,2,3,4,4,None])
s=s.isna()
print(s)
s = s.dropna()
print(s.dtype)
s= s.drop_duplicates()
print(s)


# Create sample DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value1': [1, 2, 3, 4]})
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value2': [5, 6, 7, 8]})

# Inner merge (default) - keeps only matching keys in both DataFrames
merged_df_inner = pd.merge(df1, df2, on='key', how='outer')

print("Inner Merge:\n", merged_df_inner)