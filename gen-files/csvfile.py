import pandas as pd
randNames = ["prabhu","sunil","sirdhar","shiva","mahadev","hanuman","krishna","vishnu","abcd","Brahma"]

data = {
    "name":[],
    "email":[],
    "age":[],
    "ownerid":[],
    "department":[]
}
start = 100
offset = 20
for i in range(start,(start+offset)):
    index = i%10
    data['name'].append(f"{randNames[index]}{i}")
    data['email'].append(f"{randNames[index]}{i}@gmail.com")

print(data)
