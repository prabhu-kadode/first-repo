import pandas as pd
import matplotlib.pyplot as plt

data = {
    "match": [1, 2, 3, 4, 5],
    "Team A": [250, 270, 300, 280, 260],
    "Team B": [240, 260, 310, 290, 270]
}

df = pd.DataFrame(data)


plt.figure(figsize=(8,5))
plt.plot(df['match'],df['Team A'],marker="o",linestyle="-",color="blue",label="Team India")
plt.plot(df['match'],df['Team B'],marker="s",linestyle="--",color="red",label="Team Aus")

plt.xlabel("Matches")
plt.ylabel("Total Runs Scored")
plt.title("India Vs Australia")
plt.legend()
plt.grid(True)
plt.show()


