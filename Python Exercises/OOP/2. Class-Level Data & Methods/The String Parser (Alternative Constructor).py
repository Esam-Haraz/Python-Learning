class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, data_string):
        name = data_string.split("-")[0]
        age = int(data_string.split("-")[1])
        # Here we return a new Object
        return cls(name, age)

string_data = "Esam-25"
new_person = Person.from_string(string_data)
print(f"Name: {new_person.name}, Age: {new_person.age}")

# AI Explanation

class Person:
    # The main door (strict format required)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # The side door (Alternative Constructor)
    @classmethod
    def from_string(cls, data_string):
        # 1. Parsing the messy data
        name = data_string.split("-")[0]
        age = int(data_string.split("-")[1])
        
        # 2. Creating and returning the actual Object 
        # This is exactly like typing: return Person(name, age)
        return cls(name, age)

# We have messy data
string_data = "Esam-25"

# We hand it to the side door. 
# It does the cleaning and gives us back a ready-to-use Object.
new_person = Person.from_string(string_data)

# Now new_person is a real object with its own attributes
print(new_person.name)
print(new_person.age)
