numbers = [12, 7, 34, 23, 89, 4, 15]
even_numbers = []
odd_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
else:
    print(f"Evens: {even_numbers}")
    print(f"Odds: {odd_numbers}")
