import datetime

def days_calculation(birth_year, birth_month, birth_day):
    today = datetime.date.today()
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    
    days_lived = (today - birth_date).days
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    
    print(f"You are {years} Years and {months} Months old,")
    print(f"And you lived for {days_lived} Days.")

def birthday_count(birth_year, birth_month, birth_day):
    today = datetime.date.today()
    
    next_birthday = datetime.date(today.year, birth_month, birth_day)
    
    if next_birthday < today:
        next_birthday = datetime.date(today.year + 1, birth_month, birth_day)
        
    days_left = (next_birthday - today).days
    print(f"Your Next Birthday is in {days_left} Days.")