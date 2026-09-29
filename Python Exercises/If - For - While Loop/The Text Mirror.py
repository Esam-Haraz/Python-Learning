original_text = input("Enter Only One Word: ").strip()
reversed_text = ""
for char in original_text:
    reversed_text = char + reversed_text
print(f"Mirrored Text: {reversed_text}")
