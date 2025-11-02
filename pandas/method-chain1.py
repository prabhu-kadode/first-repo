import pandas as pd 
data = {
    "country":["india","InDia","SA","sa","africa","west"],
    "name":["a","a","b","c",'s',"d"],
    "age":[30,18,19,20,21,None]
}
data1 = {
    "country":["india","InDia","SA","sa","africa","west"],
    "name":["a","a","b","c",'s',"d"],
    "age":[30,18,None,20,21,30]
}
def clean_data(data):
    df= (
        pd.DataFrame(data)
        .query("age.notna()")
        .assign(country=lambda df: df['country'].str.upper())
        .assign(average=lambda df: df['age'].mean().astype("int"))
        .assign(totalAge=lambda df:df.groupby("country")['age'].transform("sum"))
        .sort_values(by=['country'])
        .rename(columns={"country":"c"})
        )
    return df

print(clean_data(data))
print(clean_data(data1))


    


