is_member = True
purchase_amount = 500
has_coupon = False
coupon_code = "SAVE20" 

gets_discount = (is_member == True and purchase_amount >= 1000) or (has_coupon == True and coupon_code == "SAVE20")
print(gets_discount)