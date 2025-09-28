# Unpacking list
l1 = ['a','b','c','d']
w,x,y,z = l1 # unpcking all items and adding them in  w,x,y,z respectively
print(w,x,y,z)

config = ('root','1234','https://www.com')
username, password,url = config # unpacking tuple and adding them in respective varibales
print(username,password,url)

config1 = ('root1','1234','https://www.com')
*dummy,url = config1 #last one will be added to url and remaing first 2 will be added to dummy
print(url)

fruits = ['apple','water','juice','hshshs','banana']

fruit1,*liguid,fruitlast = fruits
print(fruit1,liguid,fruitlast)