inventory = { 'Apple', 'Banana' }
new_shipment = ['Orange', 'Banana', 'Grape']
returns = { 'Apple', 'Mango' }
inventory.update(new_shipment, returns)
print(inventory)