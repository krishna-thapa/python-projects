# Dictionary: key-value pairs, Unordered and Mutable

mydict = {
    "name": "John",
    "age": 38,
    "isMale": True
}

print(mydict)

mydict2 = dict(name="Hero", age=28, isMale=False)
print(mydict2)

value = mydict["name"]
print(value)
print(mydict["age"])

# Dictionary is mutable
mydict["email"] = "abc@com"
print(mydict)

# To remove/delete
del mydict["age"]
mydict.pop("name")
mydict.popitem()  # removes last inserted item
print(mydict)

if "name" in mydict2:
    print("Yes")
else:
    print("No")

try:
    print(mydict["wrong"])
except:
    print("Not found")

for key in mydict2.keys():
    print(key)

for value in mydict2.values():
    print(value)

for key, value in mydict2.items():
    print(key, value)

# NOTE: If you modify the copied, then original also get modified
mydict_cp = mydict

# To copy, use:
mydict_cp1 = mydict.copy()
mydict_cp2 = dict(mydict)

my_dict = {"name": "Hero", "age": 28, "email": "abc@com"}
my_dict2 = dict(name="Marry", age=18, city="London")
my_dict.update(my_dict2)
print(my_dict)

# Key can be any type
my_dict3 = {3: 9, 6: 36, 9: 81}
print(my_dict3)

value = my_dict3[3]
print(value)

# Key can be tuple
mytuple = (1, 2)
mydicttuple = {mytuple: 89}
print(mydicttuple)

# NOT possilbe with list as list is mutable
# mydiclist = {mylist: 89}