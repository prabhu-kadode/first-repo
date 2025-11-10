# def some_operation(a,b,showResult):
#     if showResult:
#         return a+b
#     else:
#         print(a+b)
# print(some_operation(10,20,True))
# print(some_operation(30,20,False))

# def logger(message,showlog):
#     if showlog:
#         print(message)
# logger("Hi ia m good",False)

# def add(a,b,show):
#     c= a+b
#     if show:
#         print(c)
# add(10,20,False)
# add(200,400,True)

# perValue = 100
# def get_discount(totalPrice,discount):
#     result = (totalPrice/perValue)*discount
#     print("discount:",result)
#     print("Actaul price after discount",totalPrice-result)

# get_discount(2303093,13)

userDatabase = [
    {
        "username":'india@gmail.com',
        "password":123456
    },
    {
        "username":'india1@gmail.com',
        "password":123
    },
    {
        "username":'india2@gmail.com',
        "password":56789
    }
]

def login_user(username,password):
    isValid = False
    for user in userDatabase:
        if username==user['username'] and password==user['password']:
            isValid = True
            break
    result = "success" if isValid else "failed"
    print(result)
    return isValid  
#login_user("pra@gmaisls.com",29292992)
# login_user("india2@gmail.co",56789)

def sign_up(username,password):
    if len(username)==0 or len(password)==0:
        print("lenth of username or password must be greater than 0")
        return 
    
    isPresent = False
    for user in userDatabase:
        if user['username']==username:
            isPresent = True
            break  
    if isPresent:
        print("user already exists")
    else:  
        userdict = {"username":username,"password":password}
        userDatabase.append(userdict)
        print("user has been added: ",username)     
sign_up("asas","as")


















