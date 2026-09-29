prices = {"Laptop": 15000,
          "Mouse": 500}
print(prices.get("Keyboard", "Not found"))  # "Not found" as a respone if the value not found instead of "None"
print(prices.get("Mouse", "Not found"))