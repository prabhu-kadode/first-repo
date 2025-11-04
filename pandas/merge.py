import pandas as pd
userdata = {
    "username":['ramesh','suresh','satish'],
    "email":["ramesh@","suresh@","satish@"]
}

productdata = {
    "name":["satish","satish","suresh","robin",'sachin'],
    "productsname":["mobile","bat",'fan',"laptop","bike"]
}

userdf = pd.DataFrame(userdata)
proddf = pd.DataFrame(productdata)
mergedDf = pd.merge(userdf,proddf,on="username",how="outer")
print(userdf)
print("\n",proddf)
print("\n",mergedDf)


