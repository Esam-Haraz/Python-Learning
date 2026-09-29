raw_url = "   https://www.elzero.org/courses/python   "
new_list = list(raw_url.strip().replace("https://www.", "").split("/"))
print("Website: {}, And The Section Is: {}".format(new_list[0], new_list[2]))

# replace() alternatives

# Slicing solution
# cleaned_url = raw_url.strip()[12:] 
# ده هيقطع أول 12 حرف ويبقي الباقي

# Method solution
# cleaned_url = raw_url.strip().removeprefix("https://www.")
