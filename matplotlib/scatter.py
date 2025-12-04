import matplotlib.pyplot as plt

fig,axis = plt.subplots(2,2,figsize=(8,5))

salary = [100,200,150,300]
age =[20,21,25,25]
axis[0,0].set_title("scatter")
axis[0,0].scatter(age,salary,marker="o",color="green")
axis[0,0].set_ylabel("salary")
axis[0,0].set_xlabel("age")

plt.show()