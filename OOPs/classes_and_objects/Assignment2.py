class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        try:
            if quantity <= 0:
                raise ValueError("quantity must be positive.")
            if item_name in self.items:
                self.items[item_name] += quantity
            else:
                self.items[item_name] = quantity
            print(f"{quantity} units of {item_name} added to inventory.")
        except ValueError as e:
            print(e)

    def remove_item(self, item_name, quantity):
        try:
            if quantity <= 0:
                raise ValueError("quantity must be positive.")
            if item_name not in self.items:
                raise ValueError(f"{item_name} not found in inventory.")
            if self.items[item_name] < quantity:
                raise ValueError(f"insufficient stock of {item_name}.")
            self.items[item_name] -= quantity
            print(f"{quantity} units of {item_name} removed from inventory.")
        except ValueError as e:
            print(e)

    def check_stock(self, item_name):
        if item_name in self.items:
            print(f"stock level of {item_name}: {self.items[item_name]}")
        else:
            print(f"{item_name} not found in inventory.")

if __name__ == "__main__":
    inventory = Inventory()

    inventory.add_item("apple", 50)
    inventory.add_item("banana", 30)
    inventory.check_stock("apple")
    inventory.remove_item("apple", 20)
    inventory.remove_item("apple", 40) 
    inventory.check_stock("apple")
    inventory.check_stock("orange")  
