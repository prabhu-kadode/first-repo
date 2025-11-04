import pandas as pd

users = {
    "id":[20,10,1,None,2,3,4,5,5,None],
    "name":['z','y','a',None,'b','c','d','e','e',None]
}

usersdf = pd.DataFrame(users)
# updated = usersdf.fillna("hello")
# print(updated)
start = 20
skipValue = 2
usersdf['age']= [i for i in range(start,start+len(usersdf))]

usersdf['agedesc']= [i for i in range(start,start-len(usersdf)*skipValue,-skipValue)]

nullValues = usersdf.isna()
print(nullValues)

usersdf = usersdf.dropna()
usersdf['lname']= usersdf['name'].apply(lambda name: len(name))
usersdf['updatedAge']= usersdf['age'].apply(lambda age: age+1)
usersdf['name']= usersdf['name'].apply(lambda name: name.upper())
usersdf = usersdf.drop_duplicates()

usersdf['id'] = usersdf['id'].astype("int")
print(usersdf)


data2 = {
    "name":['a','b','c','f'],
    "marks":[20,50,30,40]
}
marksdf = pd.DataFrame(data2)

marksdf['result']= marksdf['marks'].apply(lambda mark:"falil" if mark < 35 else 'pass')

# marksdf['result']= marksdf['marks'].apply(findResult)

print(marksdf)




lenitem = 6
start = 20
skipval = 3
a = [i for i in range(start,start-(lenitem*skipval),-skipval)]

print(a)

csvdf = pd.read_csv('a.csv')

print(csvdf)






