
# function with three params   
def calculate(a,b,optype):
    if optype == "add":
        print("addition of two number:")
        print(a+b)
    elif optype == "sub":
        print(a-b)
    elif optype =="mul":
        print(a*b)
    elif optype == "div":
        print(a/b)
    else:
        print("invalid opty")

# calculate(10,20,"mul")
def add(a,b):
    print("a and b = ",a+b)
    print("addition of two number:") 
def sub(a,b):
    print("sub of two number:")
    print(a-b)
def mul(a,b):
    print("multification of two number:")
    print(a*b)
def div(a,b):
    print("division of two number:")
    print(a/b)

# function with default values
def calculate1(a=10,b=20,optype="add"):
    if optype == "add":
        add(a,b)
    elif optype == "sub":
        sub(a,b)
    elif optype =="mul":
        mul(a,b)
    elif optype == "div":
        div(a,b)
    else:
        print("invalid opty")
# calculate1(10,20,"mul")
# calculate1(10,20)
calculate1()

# Local and global scope..
total = 10


def abcd():
   global total
   total = total+30
   print(total)

abcd()







