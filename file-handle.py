# fileobj = open("logs.txt","r")
# print(fileobj.readlines())
# fileobj.close()
successCount=0
errorCount=1
with open("logs.txt","r") as fileobject:
    for i in fileobject:
        print(i.lower())
        # if "Error" in i:
        #     print("Error")
        #     errorCount+=1
        # elif "success" in i:
        #     print("success")
        #     successCount+=1
# print(successCount,errorCount)



# with open("logs.txt","w") as fileobject:
#     fileobject.write("i am writting...")

# with open("logs.txt","a") as fileobject:
#     for i in range(100):
#         if i%2==0:
#             fileobject.write("\ni am update.......Error")
#         else:
#             fileobject.write("\n success.,... sjhshshss")