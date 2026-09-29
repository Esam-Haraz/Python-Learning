# couldn't do it so its ai generated
celsius_temp = int(input("Enter Your temperate in celsius: "))
fahrenheit_temp = int(input("Enter Your temperate in fahrenheit: "))

c_to_f = (celsius_temp * 9 / 5) + 32
f_to_c = (fahrenheit_temp - 32) * 5 / 9

print("{} Celsius is equal to {:.1f} Fahrenheit".format(celsius_temp, c_to_f))
print("{} Fahrenheit is equal to {:.1f} Celsius".format(fahrenheit_temp, f_to_c))