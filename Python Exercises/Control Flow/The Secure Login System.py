saved_user = "Essam"
saved_pass = "1234"
is_admin = True
if saved_user.strip().lower() == input("Enter Your Username: ").strip().lower():
    if saved_pass == input("Enter Your Password: ").strip():
        if is_admin == True:
            print("Welcome Administrator, Access Granted")
        else:
            print("Welcome User, Limited Access")
    else:
        print("Wrong Password")
else:
    print("Username Not Found")