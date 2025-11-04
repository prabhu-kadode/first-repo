import pandas as pd

try:
    df = pd.read_csv("a1.csv")
    df['average'] = df['age'].mean()
    print(df)
except Exception as e:
    print("issssssuess")
    print(e)
finally:
    print("program running... as suals")

