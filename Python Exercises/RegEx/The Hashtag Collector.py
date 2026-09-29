import re
post = "Loving the new #Python features in 2026! #coding #developer_life"
result = re.findall(r"#\w+", post) # \w already include underscore _
print(result)
