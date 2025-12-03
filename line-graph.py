import matplotlib.pyplot as plt 


# data = {
#     "India":[10,6,12,8,10,25],
#     "Australia":[5,10,12,5,10,10],
#     "over":[1,2,3,4,5,6]
# }

# plt.figure(figsize=(8,5))
# plt.title("Runs with respect to over")
# plt.plot(data['over'],data['India'],marker="o",linestyle="-",color="blue",label="India")
# plt.plot(data['over'],data['Australia'],marker="o",linestyle="--",color="red",label="Australia")
# plt.xlabel("Overs")
# plt.ylabel("Runs")
# plt.grid(True)
# plt.legend()
# plt.show()

datacities = {
    "cities":['Banglore','Delhi','Mumbai'],
    "population":[2000,1000,5000]
}

plt.figure(figsize=(8,5))
plt.title("Population by cities")
plt.bar(datacities['cities'],datacities['population'],color="green")
plt.xlabel("Cities")
plt.ylabel("Population")
plt.show()






