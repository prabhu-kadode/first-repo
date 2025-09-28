emp = {
    "name":"abcd",
    "email":"abcd@gmail.com"
}

name = emp['name']
email = emp['email']
# Accessing values from dictionary 
name1 = emp.get('name')
email1 = emp.get("email")

print(name1,email1)

# Accessing values from dictionary 
mobile = emp.get("mobile","833173814999")
isMaried = emp.get("isMaried",False)
print(mobile)

#Updating dictionary with mobile  and isMarried as key 
emp['mobile'] = '83838****'
emp.update({"isMarried":True})

# Removing isMarried from dictionary and returns its value
value = emp.pop('isMarried')
print(emp)
print(value)




