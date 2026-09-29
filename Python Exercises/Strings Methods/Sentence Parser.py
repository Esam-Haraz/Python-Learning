user_request = input("Enter Your Paragraph: ")
words = user_request.split()

print("Number of Words:", len(words))
print("Number of Characters (no space):", len(user_request.replace(" ", "")))
print("Longest Word:", max(words, key=len))
print("Shortest word:", min(words, key=len))
