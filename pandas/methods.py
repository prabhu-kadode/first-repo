import pandas as pd 

data = {
    "country":["india","InDia","SA","sa","africa","west"],
    "name":["a","a","b","c",'s',"d"],
    "age":[30,18,19,20,21,None]
}
df = pd.DataFrame(data)

df.query("age.notna()")
print(notnall)

second = df['age'].nlargest(4)

values = df['name'].value_counts()
print(values)
print(second.min())

df = df.query('age < 20 and country == "SA"')
print(df)
