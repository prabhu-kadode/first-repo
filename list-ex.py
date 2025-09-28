names = ['a','b','c',['e','f']]
print(names[-1][-2])

#slicing....
fruits = ['apple','banana','mango']
print(fruits[0:2])# apple and banana
print(fruits[:2])# apple and banana
print(fruits[:10])#apple , banana, mango
print(fruits[1:])#banana and mango

list1 = [1,2,3]
list2 = [1,2,3] 
list3 = list1

print(list1 == list2) # compares values
print(list1 is list2) # compares the address
print(list3 is list1)


countNums = [1,2,3,3,3,3,4,4]

print(countNums)

print(countNums.count(4))

if 2 in countNums:
    print("yes")
else:
    print("no")


allowedCountries = ['ind','ban','sri','uk','xyz',10,True]
newCountry = 20
if newCountry in allowedCountries:
    print("allow")
else:
    print("not allowed")


