# For Loop on list

for i in [1,2,3,4,5]:
    print(i)
 

# For loop on tuple    
for i in (1,2,3,4):
    print(i)
    

# For loop on string
for i in "hello":
    print(i)

# For loop on set

# For loop on dictionary
family = {
    "name":"a",
    "fname":"fa",
    "mname":"ma"
}

for fam in family:
    print(fam, family[fam])

familyList = [
    {
        "name":"a",
        "fname":"fa",
        "mname":"ma"
    },
    {
        "name":"a1",
        "fname":"fa1",
        "mname":"ma"
    },
    {
        "name":"a2",
        "fname":"fa2",
        "mname":"ma2"
    }
]

for flist in familyList:
    print(flist['name'])
    if flist['name']=='a':
        continue
    flist.update({"country":"india"})
    print(flist)


print("list:",familyList)

# Range 

for i in range(1,10):
    print(i)

# Continue and Break

vowels = ['a','i','e','o','u']

countryname = "iandia"

for  char in countryname:
    if char in vowels:
        continue
    print(char)

for char in countryname:
    if char =='a':
        break
    print(char)

print("i am outside")

