def factorial(numbers):
    if numbers <= 1:
        return 1
    else:
        return numbers * factorial(numbers - 1)

print(f"Your Factorial is {factorial(5)}")
