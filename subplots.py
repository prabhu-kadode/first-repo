import matplotlib.pyplot as plt

fig,axis = plt.subplots(2,3,figsize=(8,5))

axis[0,0].set_title("scatter")
age = [1,2,3,4]
salary = [100,200,300,400]
axis[0,0].scatter(age,salary,marker="o",color="green")
axis[0,0].set_xlabel('age')
axis[0,0].set_ylabel('salary')

axis[1,2].set_title("lines...")
age = [1,2,3,4]
salary = [100,200,300,400]
axis[1,2].bar(age,salary,color="blue")
axis[1,2].set_xlabel('age')
axis[1,2].set_ylabel('salary')

plt.show()
fig.savefig("abcd.jpeg")



