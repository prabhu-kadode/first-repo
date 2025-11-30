import pandas  as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('./../users.csv')
print(df.head())

# plt.barh(df['name'],df['salary'],color="skyblue")
# plt.xlabel('age')
# plt.ylabel('salary')
# plt.title("Salary vs name")
# plt.show()

# plt.plot(df['name'], df['salary'], marker='o', linestyle='-', color='red')
# plt.xlabel("name")
# plt.ylabel("salary")
# plt.title("Age of Users")
# plt.show()

# plt.hist(df['age'], bins=5, color='orange', edgecolor='black')
# plt.xlabel("Age")
# plt.ylabel("Number of Users")
# plt.title("Age Distribution")
# plt.show()


# city_counts = df['city'].value_counts()
# plt.figure(figsize=(6,6))
# plt.pie(
#     city_counts, 
#     labels=city_counts.index, 
#     autopct='%1.1f%%',   # show percentages
#     startangle=90      # start from the top
# )
# plt.title("Users by City")
# plt.show()
agesalary = df.groupby('city')['salary'].mean().reset_index()
plt.figure(figsize=(6,4))
plt.plot(agesalary['city'], agesalary['salary'], marker='o', linestyle='-', color='red')
plt.xlabel("City")
plt.ylabel("salary")
plt.title("Salary Trend by Age")
plt.grid(True)
plt.show()




