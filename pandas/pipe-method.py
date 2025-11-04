import pandas as pd 
import logging

logging.basicConfig(level=logging.INFO)
data = {
    "country":["india","InDia","SA","sa","africa","west"],
    "name":["a","a","b","c",'s',"d"],
    "age":[30,18,19,20,21,None]
}
LOGOFF = False
def loggingData(df,msg,showdf=True):
    if LOGOFF:
        return df
    logging.info(msg)
    if showdf:
        logging.info(df)
    return df


def get_transformed_df(data):
    df = (
        pd.DataFrame(data)
        .pipe(loggingData,"creating datat frame",False)
        .query("age.notna()")
        .pipe(loggingData,"Filtering not null",False)
        .assign(country=lambda df:df['country'].str.upper())
        .assign(averageage=lambda df:df['age'].mean().astype("int"))
        .assign(countryavergae=lambda df:df.groupby('country')['age'].transform('mean'))
        .sort_values(by=['country'])
        .rename(columns={"age":"user_age","name":"user_name"})
        .pipe(loggingData,"Final Output")
    )
    # print(df)
    return  df
print(get_transformed_df(data))


