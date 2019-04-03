fruits=["apple","banana","cherry"]
print(fruits)
z=fruits.count("apple")
print(z)
print(type(z))
fruits.append("orange")
print(fruits)
fruits.remove("banana")
print(len(fruits))
fruits.insert(1, "mango")
print(fruits)
for x in fruits:
    print(x)
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")
