def custom_range(start, end, step):
    print(start)
    current_number = start + step
    while current_number <= end:
        yield current_number
        current_number += step

number_range = custom_range(1, 10, 2)
for number in number_range:
    if number <= 10:
        print(number)
    else:
        break
