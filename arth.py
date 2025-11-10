
import maths as mt
print(mt.add(20,30))
print(mt.sub(20,30))
# from maths import add
# print(add(10,20))


# Non keyword arguments..
# def hello(*args):
#     print(args)

#hellokey accepts keyword arguments..
# def hellokey(**args):
#     print(args)
# hello(1,2,3,3,4)
# hellokey(name="a")

t = (1,2,10)
a,b,c = t
def hello(a,b,c):
    print(a,b,c)
hello(10,20,3)    
hello(*t)
hello(*t)

names = ['a','b','c']
newnames = names
# This is function which accepts refernece as params..
def helloByRefrence(data):
    data.append("d")
    print(data)
helloByRefrence(names)# calling the function by reference..
print(names,newnames)

def sum_of_all(*args):
    result = 0
    for i in args:
        result = result+i
    print(result)

sum_of_all(1,2,3,4,5)