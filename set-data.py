# Set is unordered and accepts only unique values
names = {"a","b","c","a"}
names.add("e") # Adds item in the set
names.remove("z") # Removes value if exists other wise throw the error
names.discard("z") # Removes value if exists otherwise doesn't throw the error
print(names) 
fruits = ["apple","apple","mango","mango"]
# unique_fruits = set(fruits)
# unique_list_of_furuits = list(unique_fruits)
# print(unique_fruits,unique_list_of_furuits)
# print(list(set(fruits)))
unique_fruits = list(set(fruits)) # Copnverting list to set and set to list back.
print(unique_fruits)

