a = 10
name = "abcd"
isvalid = True
price = 10.50

if a == int("10"):
    print("yes")
else:
    print("no")

if int(price) == 10:
    print("yes")
else:
    print("no")

config = ("user","root","password")
print(config[2])

a,b,c = config
print(a,b,c)

frutis = ['apple','mango']
ap,ma = frutis

print(ap,ma)

company = {
    "name":"xyz",
    "revenue":1000,
    "address":{
        "name":"xyz",
        "pincode":1234,
        "housenumer":'#38373'
    },
    "isProductBased":False,
    "directors":['a','b'],
    "description":""
}
print(company['name'])
print(company.get('ceo','damn'))

if company['isProductBased']:
    company.update({"description":"This is product based"})
else:
    company.update({"description":"This is not product based"})

print(company['description'])

nums = [1,2,3,4,5,6,7,10,20,30]
totalNums = 0
for num in nums:
    print(num)
    # totalNums = totalNums+num
    totalNums += num

# print(totalNums)
even_values=[]
odd_values =[]

for n in nums:
   if n%2==0:
       print(n,"even")
       even_values.append(n)
   else:
       print(n,"odd")
       odd_values.append(n)

print(odd_values,even_values)

print(3//2)















   




