class Abcd:
    # constructor with params name and email
    def __init__(self,name,email):
        self.hi()
        print("i am constructor")
        self.firstname = name
        #self.firstname is instance variable
        self.email = email
        self.print_all_info()
    def print_all_info(self):
        print("hi",len(self.firstname))
        print(self.email.upper())
        print(self.email[0:1])
        marks = 100
        salary = 1000
        msg = f"my name is {self.firstname} and my salary is {salary} and marks are {marks}"
        print(msg)
    def hi(self):
        print("hi method")

abcd = Abcd("india",'a@a.com')
# abcd.print_all_info()
