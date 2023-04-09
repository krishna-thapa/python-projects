# Strings: ordered, immutable and text representation

my_string = "Hello world"
print(my_string)

my_string2 = 'I\'m a programmer'
print(my_string2)

my_string3 = "I'm a programmer"
print(my_string3)

my_string4 = """
Hello world \
I am here
"""
print(my_string4)

char = my_string[0]
last_char = my_string[-1]
print(char)

# excludes the last index character
sub_string = my_string[1:5]
print(sub_string)

print(my_string[:5])
print(my_string[3:])
print(my_string[::2])
print(my_string[::-1])

greeting = "Hello"
name = "Tom"
print(greeting + " " + name)

for i in greeting:
    print(i)

if 'e' in greeting:
    print("Yes")
else:
    print("No")

my_string5 = "  Hello world"
new_string = my_string5.strip().upper().lower().capitalize()
print(new_string)

new_string.startswith("H")
new_string.endswith("ld")
new_string.find("o")
new_string.count("o")
new_string.replace("ll", "new")

my_list = new_string.split()  # default is space
print(my_string)

# list to string
list_to_string = " ".join(my_list)
print(list_to_string)

# old string format
var = "Tom"
my_string6 = "the variable is %s" % var
print(my_string6)

var = 28
my_string7 = "the variable is %d" % var
print(my_string7)

var = 28.56
my_string8 = "the variable is %.2f" % var
print(my_string8)

var = 28.56
my_string9 = "the variable is {:.2f}".format(var)
print(my_string9)

# new string format
var1 = "Tom"
age = 28
my_string10 = f"the variable for {var1} with age is {age}, solve {1 + 1}"
print(my_string10)
