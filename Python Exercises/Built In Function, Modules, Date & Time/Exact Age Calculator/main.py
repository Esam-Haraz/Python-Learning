import calculations

useryear = 0
usermonth = 0
userday = 0

while True:
    print("___Welcome___")
    print("1. Add Your Birthday")
    print("2. Calculate Your Birthday")
    print("3. Quit")
    userinput = input("Enter Your Choose: ").strip()
    
    if userinput == "1":
        useryear_input = input("Enter Your BirthYear: ").strip()
        usermonth_input = input("Enter Your BirthMonth: ").strip()
        userday_input = input("Enter Your BirthDay: ").strip()
        
        if useryear_input.isdigit() and usermonth_input.isdigit() and userday_input.isdigit():
            useryear = int(useryear_input)
            usermonth = int(usermonth_input)
            userday = int(userday_input)
            print("Birthday Saved Successfully!")
        else:
            print("Numbers Only!")
            useryear = 0 
            
    elif userinput == "2":
        if useryear != 0:
            calculations.days_calculation(useryear, usermonth, userday)
            calculations.birthday_count(useryear, usermonth, userday)
        else:
            print("Please add your birthday first!")
            
    elif userinput == "3":
        print("GoodBye")
        break
    else:
        print("Please Enter Your Choose Number!")