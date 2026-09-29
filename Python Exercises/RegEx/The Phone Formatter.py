import re
phone = "015 596 00-6-71"
result = re.sub(r"\s|-", "", phone) # you can use \D to remove anything that non-digit such as whitespace and -
print(result)
