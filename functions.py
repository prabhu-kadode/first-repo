# Function is block of code which gets executd upon calling with its name
def logMessage():
    fruits = ['apple','mango']
    print(fruits)

#logMessage()

# Function add accepts two params namely x,y  
def add(x,y):
    return x+y

add(1,10)
add(2,10)
print(add(50,50))

def check_even(num):
    if num%2==0:
       return True
    
    return False

data = check_even(23)
print(data)


# def allow_access():
#     if isLoggedIn:
#         if isHeAdmin:
#             print("he hass access")
#         else:
#             print("you are not admin")
#     else:
#         print("please login")

# #allow_access()
isLoggedIn = True
isHeAdmin = True
def allow_access_version1():
    if not isLoggedIn:
        print("please login")
        return 
    
    if not isHeAdmin:
        print("no access")
        return 
    
    print("he has access")


allow_access_version1()

def accept_more_than_zero(num):
    if num==0:
        print("invalid")
    else:
        print("your num is valid")
        for i in range(num):
            print(i)
accept_more_than_zero(1)

def accept_more_than_zero_version2(num):
    
    if num<=1:
        print(num,"is invalid...pleaee provide value more than 1")
        return
    
    for i in range(num):
        print(i)
accept_more_than_zero_version2("ososos")
      









