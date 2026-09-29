sentence = "Python is amazing"
vowels = "aeiou"
count = 0
for letter in sentence:
    if letter in vowels:
        count += 1
else:
    print(f"Number of Vowels: {count}")
