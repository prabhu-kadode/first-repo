import pandas as pd 

data = {
    "country":["india","InDia","SA","sa","africa","west"],
    "name":["a","a","b","c",'s',"d"],
    "age":[30,18,19,20,21,22]
}
df = pd.DataFrame(data)

second = df['age'].nlargest(4)

values = df['name'].value_counts()
print(values)
print(second.min())

df = df.query('age < 20 and country == "SA"')
print(df)
