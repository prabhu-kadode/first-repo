import matplotlib.pyplot as plt

fix,axis = plt.subplots(1,2,figsize=(8,5))
colors = ['red','green','blue','skyblue','yellow','black']
axis[1].set_title("line")
axis[1].bar([1,2,3,4,5,6],[2,4,6,8,10,12],color=colors)
axis[1].set_ylabel("Y albesl")
axis[1].set_xlabel("x label")

axis[0].set_title("line")
axis[0].plot([1,2,3,4,5,6],[2,4,6,8,10,12],marker="o",linestyle="-",color="red")
axis[0].set_ylabel("Y albesl")
axis[0].set_xlabel("x label")
plt.show()