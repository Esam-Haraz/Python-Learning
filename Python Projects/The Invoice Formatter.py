product_1_name = "Magical Mouse"
product_1_price = 50.5
product_2_name = "Super Keyboard"
product_2_price = 120.0
product_3_name = "HDMI Cable"
product_3_price = 15.5
discount_percentage = 10

total = product_1_price + product_2_price + product_3_price

discount_amount = (total * discount_percentage) / 100
final_price = total - discount_amount

print("Product".ljust(20), "Price")
print("-" * 30)
print("{} {}".format(product_1_name.ljust(20), product_1_price))
print("{} {}".format(product_2_name.ljust(20), product_2_price))
print("{} {}".format(product_3_name.ljust(20), product_3_price))
# print("{:<20} {:>10}".format(product_1_name, product_1_price)) AI Suggestion
print("-" * 30)
print("Total Price: {}".format(str(total).rjust(13)))
print("Discount: {}".format(str(discount_amount).rjust(15)))
print("Final Price: {}".format(str(final_price).rjust(13)))
