import time
# Decorator is higher order function which modifies the behaviour of other function
def log(func):
    def wrapper():
        print("hello is beingh changed")
        func()
        print("hello is being changed again..")
    return wrapper

def upperCase(func):
    def wrapper(*args,**kargs):
        print(args)
        print("started exeuection",time.time())
        start = time.time()
        result = func(*args,**kargs)
        end = time.time()
        print(end-start)

        return result.upper()
    return wrapper

@log
def hello():
    print("hello")

@log
def hi():
    print("hi")

hello()
hi()

@upperCase
def printName(name):
    time.sleep(2)
    return name

@upperCase
def message(msg):
    return msg

print(printName("prabhu"))

print(message("hi hello i am prabhu"))

def validate(func):
    def wrapper(a,b,*args,**kargs):
        def validate_params(val):
            if not isinstance(val,(int,float)) or isinstance(val,(bool)):
                print(f"'{val}'  must be integer type value")
                return False
            return True
            
        if not validate_params(a) or not validate_params(b):
            return
        func(a,b,*args,*kargs)
    return wrapper
    
@validate
def add(a,b):
    print(a+b)
    
@validate
def sub(a,b):
    print(a-b)

add(10,20)

sub(20,True)

