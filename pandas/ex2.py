import pandas as pd
data = {
    "name":['a','a','b','c','d','e','f'],
    "salary":[1000,1000,2000,1000,5000,None,None]
}
df = pd.DataFrame(data)
print(df.isna().sum())
print(df.duplicated().sum())
df1 = df['salary'].fillna(df['salary'].mean()).astype('int')
print(df1)