# def print_nums(n):
#     for item in range(1,n+1):
#         print(item)
# print_nums(10)

# Recurssion function
start = 1
def print_nums1(num):
    global start
    print(start)
    start +=1
    if start<=num:
        print_nums1(num)

print_nums1(10)

def hello(name):
    print("hello",name)

hello1 = hello

# hello1("abcd")

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
def mod(a,b):
    print("mods of two number:")
    print(a%b)
def square(a,b=None):
    print("square of two number:")
    print(a*a)
def powerof(a,b):
    print("square of two number:")
    print(a**b)


# function with default values
operations_dict = {
    "add":add,
    "sub":sub,
    "mul":mul,
    "div":div,
    "mod":mod,
    "square":square,
    "powerof":powerof
}
def calculate1(a=10,b=20,optype="mul"):
    call_back = operations_dict[optype]
    call_back(a,b)

calculate1(100,100,"add")

def whileLoopfunc(num):
    a = 0
    while a<=num:
        print("while:",a)
        if a%2 == 0:
            print(a)

        a +=1
whileLoopfunc(20)
# whileLoopfunc(10)