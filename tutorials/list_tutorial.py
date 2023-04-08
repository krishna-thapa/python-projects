print("Welcome to Python tutorial for list collection!!")

# Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list()  # empty list

mylist3 = [5, True, "string", "string"]  # duplicates and allow multiple types

first_item = mylist[0]  # first item
last_item = mylist[-1]  # last item
print(last_item)

for i in mylist:
    print(i)

if "lemon" in mylist:
    print("yes")
else:
    print("no")

len(mylist)  # get the length

mylist.append("lemon")
mylist.insert(1, "mango")
mylist.pop()  # returns the last item and remove it
print(mylist)

mylist.remove("cherry")
mylist.clear()  # remove everything from the list

mylist = ["banana", "cherry", "apple"]
mylist.reverse()
print(mylist)

mylist.sort()
new_list = sorted(mylist)  # Create a new sorted list

mylist1 = [0] * 5
print(mylist1)

mylist4 = [1, 2, 3, 4, 5]
new_list1 = mylist1 + mylist4

print(new_list1)

slice_list = mylist4[0:2]  # Last index is excluded
print(slice_list)

start_items = mylist4[:4]
end_items = mylist4[3:]

# step index
step_items = mylist4[0::2]
step_reverse = mylist4[::-1]

# copy
list_org = ["banana", "cherry", "apple"]

list_cpy = list_org

print(list_cpy)
list_cpy.append("mango")
print(list_org)  # NOTE: original list is get modified

# Instead copy like this
list_copy = list_org.copy()
list_copy1 = list(list_org)
list_copy2 = list_org[:]

# Advanced: list comprehension
int_list = [1, 2, 3, 4, 5, 6]
sqr_list = [i * i for i in int_list]
print(sqr_list)
