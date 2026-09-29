def mydeco(func):
    def mywrapper(num1, num2):
        if num2 == 0:
            return print("Warning: Cannot divide by zero")
        else:
            func(num1, num2)
    return mywrapper

@mydeco
def calucation(num1, num2):
    result = num1 / num2
    print(result)

calucation(10, 2)
calucation(10, 0)
