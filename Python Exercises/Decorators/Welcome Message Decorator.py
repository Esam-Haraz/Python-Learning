username = input("Enter Your Name: ").title()

def mydecorator(func):

    def welcomemag(username):

        print("Welcome To Our System")
        func(username)
        print("See You Soon")
    return welcomemag

@mydecorator
def userwelcmag(username):

    print(f"User: {username}")

userwelcmag(username)