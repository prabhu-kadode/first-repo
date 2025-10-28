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


d1 = pd.DataFrame({
    "id":[1,2,3,3,None],
    "name":["a","b","c","c",None]
})

d1= d1.dropna()
d1 = d1.drop_duplicates()
d1['id'] = d1['id'].astype('int')
d1['age']= [1,2,3]

print(d1)





