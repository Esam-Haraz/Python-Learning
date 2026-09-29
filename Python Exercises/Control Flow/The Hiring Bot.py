skill = input("Enter Your Skill: ")
if skill.strip().lower() == "python":
    years_exp = int(input("Enter Your Years Experince: ")) # AI Correction
    if years_exp < 3:
        print("Accepted as Junior Developer")
    elif years_exp > 3:
        print("Accepted as Senior Developer")
else:
    print("Rejected: Must know Python")