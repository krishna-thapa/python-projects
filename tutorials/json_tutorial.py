# In Python, you have the built-in json module for encoding and decoding JSON data.
"""Some advantages of JSON:

    - JSON exists as a "sequence of bytes" which is very useful in the case we need to transmit (stream) data over a network.
    - Compared to XML, JSON is much smaller, translating into faster data transfers, and better experiences.
    - JSON is extremely human-friendly since it is textual, and simultaneously machine-friendly.
"""

import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person)

# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
print(person_json)
print(person_json2)

# convert Python objects into JSON objects and save them into a file with the json.dump() method.
with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)  # you can also specify indent etc...

# FROM JSON to Python (Deserialization, Decode)

person_json = """
{
    "age": 30, 
    "city": "New York",
    "hasChildren": false, 
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""

person = json.loads(person_json)
print(person)

# load data from a file and convert it to a Python object with the json.load() method.
with open('person.json', 'r') as f:
    person = json.load(f)
    print(person)

# Working with Custom Objects
z = 5 + 9j


def encode_complex(z):
    if isinstance(z, complex):
        # just the key of the class name is important, the value can be arbitrary.
        return {z.__class__.__name__: True, "real": z.real, "imag": z.imag}
    else:
        raise TypeError(f"object of type '{z.__class__.__name__}' is not JSON serializable")


zJSON = json.dumps(z, default=encode_complex)
print(zJSON)

# will decode into a dictionary
zDict = json.loads(zJSON)
print(zDict)


# decode function that will take a dictionary as input, and creates your custom object
# if it can find the object class name in the dictionary.

def decode_complex(dct):
    if complex.__name__ in dct:
        return complex(dct["real"], dct["imag"])
    return dct


# Now the object is of type complex after decoding
z = json.loads(zJSON, object_hook=decode_complex)
print(type(z))
print(z)


# Template encode and decode functions
# This works for all custom classes if all instance variables are given in the __init__ method.

class User:
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.friends = friends


def encode_obj(obj):
    """
    Takes in a custom object and returns a dictionary representation of the object.
    This dict representation also includes the object's module and class names.
    """
    #  Populate the dictionary with object meta data
    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }

    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)
    return obj_dict


def decode_dict(dict):
    """
    Takes in a dict and returns a custom object associated with the dict.
    It makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    """
    if "__class__" in dict:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = dict.pop("__class__")

        # Get the module name from the dict and import it
        module_name = dict.pop("__module__")

        # We use the built in __import__ function since the module name is not yet known at runtime
        module = __import__(module_name)

        # Get the class from the module
        class_ = getattr(module, class_name)

        # Use dictionary unpacking to initialize the object
        # Note: This only works if all __init__() arguments of the class are exactly the dict keys
        obj = class_(**dict)
    else:
        obj = dict
    return obj


# User class works with our encoding and decoding methods
user = User(name="John", age=28, friends=["Jane", "Tom"], balance=20.70, active=True)

userJSON = json.dumps(user, default=encode_obj, indent=4, sort_keys=True)
print(userJSON)

user_decoded = json.loads(userJSON, object_hook=decode_dict)
print(type(user_decoded))
print(user_decoded)