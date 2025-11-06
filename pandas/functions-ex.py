def some_operation(a,b,showResult):
    if showResult:
        return a+b
    else:
        print(a+b)
print(some_operation(10,20,True))
print(some_operation(30,20,False))

def logger(message,showlog):
    if showlog:
        print(message)
logger("Hi ia m good",False)

def add(a,b,show):
    c= a+b
    if show:
        print(c)
add(10,20,False)
add(200,400,True)

perValue = 100
def get_discount(totalPrice,discount):
    result = (totalPrice/perValue)*discount
    print("discount:",result)
    print("Actaul price after discount",totalPrice-result)

get_discount(2303093,13)

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
    if username==userDatabase['username'] and password==userDatabase['password']:
        print("successs")
    else:
        print("invalid")

login_user("pra@gmaisls.com",29292992)
login_user("india@gmail.com",123456)











