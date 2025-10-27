import pandas as pd

data = {
    "name":["a","b","c",None],
    "email":["a@a.com","b@b.com","c@c.com",None]
}
df = pd.DataFrame(data)
print(df.isnull())
# df = df.dropna(how="all")

# df = df.fillna("unknow")
#df = df.fillna({"name":"a1","email":"a1@a.com"})
df = df.fillna(method="ffill")

# df = df.drop_duplicates()

# df =df[df.duplicated()]
df['age']= [age for age in range(20,(20-len(df)),-1)]
df['average']= df['age'].mean().astype("int")
df['namelen']= df['name'].apply(lambda name:len(name))




print(df)

