import pandas as pd
data = {
    "country":["india","india","SA","africa","west"],
    "name":["a","a","b","c","d"],
    "age":[30,18,19,20,22]
}
df = pd.DataFrame(data)

# print(df)
df= df.groupby('country').min() # Gives you minimum age of emp by country
df= df.groupby('country').agg({
    "age":['min','max','mean','median']
})
print(df)







