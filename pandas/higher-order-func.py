#hello is higher order function which will take another function as its input params
# def hello(func):
#     func()
#     print("helo....")
# def hi():
#     print("hi....")
# hello(displau)

def displayName(name="xyz"):
   print(name.upper())
printName = displayName # Assigning displayName function to variable printName.
printName("abcd")

