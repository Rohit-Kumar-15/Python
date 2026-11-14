# 05 - Getter and Setter Methods
# A getter reads a value. A setter validates/updates a value.
# geetr == .get 
# seter == .set 
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = 0
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price < 0:
            print("Price cannot be negative.")
            return
        self._price = new_price

item = Product("Keyboard", 1500)
print("Initial price:", item.get_price())

item.set_price(1800)
print("Updated price:", item.get_price())

item.set_price(-100)  # Rejected by validation
print("Final price:", item.get_price())
