import pandas as pd # imporitng pandas as pd

# Pandas Series..
series = pd.Series([1,2,3,4]) # Creation of pandas series using pd.Series
print(series) # prints series....
print(type(series))# It shows type of series..

# Pandas Dataframe...

users = {
    "name":['x','y','z','a','b','c'],
    "email":['x@','y@','z@','a@','b@',"c@"]
}
udf = pd.DataFrame(users)
print(udf)
print(udf.head()) # Prints top 5  items
print(udf.tail()) # Prints last top 5 items





