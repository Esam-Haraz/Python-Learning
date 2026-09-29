class Device:
    def __init__(self, brand):
        self.brand = brand
    def turn_on(self):
        return f"{self.brand} Device Is Now ON"

class Phone(Device):
    def __init__(self, brand, network):
        super().__init__(brand)
        self.network = network
    def call(self):
        return f"Calling Using {self.network}"

device_brand = Device("Samsung")
print(device_brand.turn_on())
phone_brand = Phone("Apple", "5G")
print(phone_brand.turn_on())
print(phone_brand.call())
