inventory = ["Laptop", "Mouse", "Keyboard", "Mouse", "Monitor", "Mouse"]
mouse_count = inventory.count("Mouse")
sold_item = inventory.pop()
inventory.insert(0, "Webcam")
inventory.remove("Keyboard")
print(f"Original Mouse Count: {mouse_count}")
print(f"Item Sold: {sold_item}")
print(f"Inventory After Updates: {inventory}")
print(f"Is Headset available? {"Headset" in inventory}")