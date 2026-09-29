class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    @classmethod
    def from_dict(cls, data_dict):
        brand = data_dict["brand"]
        price = data_dict["price"]
        return cls(brand, price)

laptop_data = {"brand": "Dell", "price": 1500}
my_laptop = Laptop.from_dict(laptop_data)
print(f"Laptop Brand is: {my_laptop.brand}, And The Price is: {my_laptop.price}")