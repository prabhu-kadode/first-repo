fruits = ['apple','mango','banana']

# Getting index and item using enumerate
for index,item in enumerate(fruits):
    print(index,item,len(item))

#Stopping loop based on condtion and using keyword break
numbers = [1,2,3,4,5]
for z in numbers:
    if z==2:
        print("yes stopped")
        break

    print(z)

# Finding item
searchItem = 2
isFound = False
for num in numbers:
    if searchItem == num:
    #    isFound = True
        print("found")
        break

# if isFound :
#     print("fond")
# else:
#     print("not found")
    
# Stopping loop 
names = ['a','b','c','d']
for char in names:
    print(char)
    if char =='c':
        break

print("Filtering words...")
dirtywords = ['fk','sx','as']
usernames = ['fk','hi','sx','as','hello','bye']
for u in usernames:
    if u not in dirtywords:
       print(u)

 # Printing table of any number      
tablenumupto = 20
tablenum = 20
for n  in range(1,tablenumupto+1):
    print(n*tablenum)

for t in (1,2,2):
    print(t)


    















