age_years = int(input("Enter Your age in years: "))
age_months = age_years * 12
age_weeks = age_months * 4 # الأرقام مش دقيقة لان الشهر مفهوش 4 اسابيع فقط
age_days = age_years * 365
print("Your age in month is: {}, your age in weeks is: {}, and your age in days is: {}".format(age_months, age_weeks, age_days))
