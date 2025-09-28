fruits = ["apple","orange","banana","graphes"]
fruits[0]="abcd"
print(fruits[0])


#Getting index of an item
print(fruits.index("graphes"))

# add new item at end
fruits.append("watermelon")
fruits.insert(0,"xyz")

#remove item from list
#fruits.remove("apple")

#It always removes last item
fruits.pop()
fruits.pop(0)
print(fruits)
print(len(fruits))

#Nested list...
mixed_fruits = [['apple',['a','b']],['nuts','almonds'],['water','juice'],"hi",True]
first_item = mixed_fruits[0]
mixed_fruits[0][1][1]="c"
print(first_item[1])
  



print(mixed_fruits[len(mixed_fruits)-1])

# emp = [1,2]
# emp1 = [1,2]
# emp1.append(3)
# print(emp)


