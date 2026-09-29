def create_email(first, last):
    return f"Your Email Is {first.strip().lower()}.{last.strip().lower()}@company.com"

print(create_email("Esam", "Haraz"))