import re
log_data = "Error 404: Page not found at line 150. Retry in 30 seconds"
result = re.findall(r"\d+", log_data)
print(result)
