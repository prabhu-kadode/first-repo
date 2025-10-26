# lambda params: expression
# def add(a,b):
#     print(a+b)
# add(10,20)
# lambda function is ananymous function which is defined with lambda keyword
res = lambda a,b: a+b
mul = lambda x: x**2
nameUpper = lambda name: name.upper()
print(res(10,20))
print(mul(10))
print(nameUpper('abcdef'))

# Zip is the function which combines two or more iterators 
names = ['a','b','c']
marks = [10,20,30]
print(list(zip(names,marks)))
for name, mark in zip(names,marks):
    print(name,mark)

evenList = []
for i in [1,2,3,4,5,6,7,9,10]:
    if i%2==0:
        print(i)
        evenList.append(i)
print(evenList)
# List comprehension is easy way to create newlist based on filter or condtion by avoiding explicit loop
l1 = [1,2,3,4,5,6,7,9,10]
filteredList = [i for i in l1 if i%2==0]
print(filteredList)
   

