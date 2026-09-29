class Shop:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
    def discount(self, discount_percentage):
        self.product_price -= (discount_percentage / 100) * self.product_price
        return f"The New Price For {self.product_name} After a {discount_percentage}% Discount is: {self.product_price}"

products = Shop("Laptop", 30000)
print(products.discount(15))
