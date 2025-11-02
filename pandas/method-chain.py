import pandas as pd 

data = {
    "country":["india","InDia","SA","sa","africa","west"],
    "name":["a","a","b","c",'s',"d"],
    "age":[30,18,19,20,21,None]
}
def get_transformed_df(data):
    df = (
        pd.DataFrame(data)
        .query("age.notna()")
        .assign(country=lambda df:df['country'].str.upper())
        .assign(averageage=lambda df:df['age'].mean().astype("int"))
        .assign(countryavergae=lambda df:df.groupby('country')['age'].transform('mean'))
        .sort_values(by=['country'])
        .rename(columns={"age":"user_age","name":"user_name"})

    )
    # print(df)
    return  df
print(get_transformed_df(data))


