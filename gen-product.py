import pandas as pd
import random

randomUsers = [
    100,101,102,103,104,105,106,107,108,109
]
randomTitles = [
    "Dell","HP",'Oneplus',"Iphone",
    "Headphone","Nokia","Charger",
    "Bag","Waterbottle"
]
randomPrices = [
    100,200,300,400,500,600,700,800,900,1000
]
productData = {
    "id":[],
    "title":[],
    "price":[],
    "ownerid":[]
}
start = 2000
totalNums = 10000
for i in range(start,start+totalNums):
    productData['id'].append(i)
    productData['title'].append(random.choices(randomTitles)[0])
    productData['price'].append(random.choices(randomPrices)[0])
    productData['ownerid'].append(random.choices(randomUsers)[0])

data = pd.DataFrame(productData)
data.to_csv(f"products-{totalNums}.csv",index=False)
print(data)
