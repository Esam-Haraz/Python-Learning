def mydeco(func):
    def decowrapper(first, last):
        original_mag = func(first, last)
        uppercase_mag = original_mag.upper()
        print(uppercase_mag)
    return decowrapper

@mydeco
def welmag(first, last):
    return f"Hello {first} {last}, Welcome Back"

first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")

welmag(first_name, last_name)