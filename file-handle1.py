# import random
# randomMessages = [
#     "2025-03-10T14:32:11Z ERROR Error occurred during operation. url=/login status=500",
#     "[2025-03-10 14:32:11] ERROR: An error occurred while processing the request. URL=/api/users/23",
#     "[2025-03-10 14:32:11] INFO: Operation completed successfully. URL=/api/users/23"
# ]

# with open("log-data.txt","w") as file:
#     for _ in range(1000):
#         randValue = random.choices(randomMessages)
#         file.write(f"\n{randValue[0]}\n")
successc=0
errorc=0
with open("log-data.txt","r") as file:
    print(file.read())
    # for log in file:
    #     if "Error" in log:
    #         print("Error found")
    #         errorc+=1
    #     elif "success" in log:
    #         print("success..")
    #         successc+=1
print("success:",successc,"error:",errorc)

