class Car:
    base_price = 50000
    def __init__(self, color):
        self.color = color
    @classmethod
    def update_base_price(cls, new_price):
        cls.base_price = new_price
        return f"The new base price for all cars is {cls.base_price}"

print(Car.base_price)
car_one = Car("Red")
car_two = Car("Blue")
print(Car.update_base_price(55000))
