def even_generator():
    even_num = 0
    while True:
        even_num += 2
        yield even_num

even_number = even_generator()
for number in even_number:
    if number <= 20:
        print(number)
    else:
        break
