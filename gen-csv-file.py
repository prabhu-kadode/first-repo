import pandas as pd
import random
randomNames = ['mahadev','shiv','sridhar','sunil','prakash','prabhu','krishna','kumar','bandu','kiran']
randomAges = [20,30,35,49,65,60]
randomDepartment = ['It','finance','hr','sales','advisor','consulting']
salaries = [
    10000,
    15000,
    5000,
    2000,
    50000,
    4000,
    17000,
    30000,
    45000,
    9000,
    2000
    ]
randomCities =[
    'banglore',
    'mumbai',
    'hydrabad',
    'delhi',
    'pune',
    'manglore',
    'chennai',
]
data = {
    "id":[],
    "name":[],
    "email":[],
    "age":[],
    "city":[],
    "department":[],
    "salary":[]
}
start = 100
end = 30
for i in range(start,start+end):
    index = i%10
    data['id'].append(i)
    data['name'].append(f"{randomNames[index]}{i}")
    data['email'].append(f"{randomNames[index]}{i}@gmail.com")
    data['age'].append(random.choices(randomAges)[0])
    data['department'].append(random.choices(randomDepartment)[0])
    data['city'].append(random.choices(randomCities)[0])
    data['salary'].append(random.choices(salaries)[0])

df = pd.DataFrame(data)
print(df)
df['name']= df['name'].apply(lambda name: name.title())
df['department']=df['department'].apply(lambda department: department.upper())
df['city']=df['city'].apply(lambda city: city.upper())
df.to_csv("users.csv",index=False)

  