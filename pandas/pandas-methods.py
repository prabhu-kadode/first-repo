import pandas as pd

users = {
    "id":[1,None,2,3,4,5,5,None],
    "name":['a',None,'b','c','d','e','e',None]
}

usersdf = pd.DataFrame(users)
# updated = usersdf.fillna("hello")
# print(updated)
usersdf['age']= [20,19,18,17,16,15,14,13]

nullValues = usersdf.isna()
print(nullValues)

usersdf = usersdf.dropna()
usersdf['lname']= usersdf['name'].apply(lambda name: len(name))
usersdf['updatedAge']= usersdf['age'].apply(lambda age: age+1)
usersdf['name']= usersdf['name'].apply(lambda name: name.upper())
usersdf = usersdf.drop_duplicates()

usersdf['id'] = usersdf['id'].astype("int")
print(usersdf)

