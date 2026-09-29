import re
emails = "contact@gmail.com, support@yahoo.com, admin@hotmail.com"
result = re.findall(r"@(\w+\.\w+)", emails) # put in group to not include @
print(result)
