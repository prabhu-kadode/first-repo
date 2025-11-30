import matplotlib.pyplot as plt
import pandas as pd

# df = pd.DataFrame({
#     "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
#     "age": [25, 30, 22, 35, 28],
#     "salary": [50000, 60000, 45000, 70000, 52000]
# })

df = pd.read_csv('./../users.csv')

plt.figure(figsize=(6,4))
plt.scatter(df['age'], df['salary'], color='purple', s=100)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Scatter Plot: Age vs Salary")
plt.grid(True)
plt.show()
