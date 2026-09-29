class Cart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart = []
    def add_item(self, item_name):
        # self.item_name = item_name unnecessary
        self.cart.append(item_name)
        return f"{item_name} Added Successfully To The Cart"
    def view_cart(self):
        return f"Hello {self.customer_name}, Your Cart Has {len(self.cart)} items: {self.cart}"

customers = Cart("Esam")
print(customers.add_item("Mouse"))
print(customers.add_item("Keyboard"))
print(customers.view_cart())
