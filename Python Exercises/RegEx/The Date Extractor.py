import re
document = "Contract signed on 15-08-2025. Review scheduled for 15/08/2025. Ignore invalid format 15.08.2025."
result = re.findall(r"(\d{2}[-/]\d{2}[-/]\d{4})", document)
print(result)
