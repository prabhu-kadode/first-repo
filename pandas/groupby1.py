import pandas as pd
data = {
    "country":["india","InDia","SA","sa","africa","west"],
    "name":["a","a1","b","c",'s',"d"],
    "age":[30,18,19,20,21,22]
}
df = pd.DataFrame(data)
df['country']=df['country'].apply(lambda country: country.upper())
# print(df)
df1= df.groupby('country').agg({
    "age":['mean']
})
# print(df1)
# df['avrg'] = df.groupby('country')['age'].transform('sum')
# print(df)

df['avrg'] = df.groupby('country')['age'].apply(lambda age: age.mean())
print(df)








