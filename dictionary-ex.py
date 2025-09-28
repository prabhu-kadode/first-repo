name = "shiv" 
age = 20
company ="xyz"
hobbies = ['swimming','singging']
salary = 1000
isMarried = True
person = {
    "name":"shiv",
    "age":20,
    "company":"xyz",
    "hobbies":['swimming','singging'],
    "salary":1000,
    "isMarried":True
 }
print(person['name'],person['age'])

persons = [
    {
    "name":"shiv",
    "age":20,
    "company":"xyz",
    "hobbies":['swimming','singging'],
    "salary":1000,
    "isMarried":True
 },
 {
    "name":"Mahadev",
    "age":20,
    "company":"xyz",
    "hobbies":['swimming','singging'],
    "salary":1000,
    "isMarried":True
 }
]

shivinfo,mahadevinfo = persons
print(mahadevinfo)

