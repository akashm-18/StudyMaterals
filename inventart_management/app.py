class Item:
    def __init__(self, name, weight, quantity):
        self.name = name
        self.weight = weight
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, weight, quantity):
        self.items.append(Item(name, weight, quantity))

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def total_weight(self):
        return sum(item.weight for item in self.items)

    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def total_quantity(self):
        return sum(item.quantity for item in self.items)

    def remaining_weight(self):
        return max(500 - self.total_weight(), 0)

    def add_items_to_meet_conditions(self):
        remaining_weight = self.remaining_weight()

        while self.total_weight() != 500 or not self.is_prime(self.total_quantity()):
            name = input(f"Enter Name for Item{len(self.items) + 1}: ")
            
            # Prompt user for quantity
            quantity = int(input(f"Enter quantity for {name}: "))
            
            # Prompt user for weight within the remaining limit
            weight = min(int(input(f"Enter weight for {name} (Remaining Weight: {remaining_weight}): ")), remaining_weight)
            
            # if len(self.items) < 3 and self.total_weight() + weight > 500:
            #     print("Cannot add this item. Exceeds total weight limit.")
            #     print(f"Can only add {remaining_weight} weight to meet the conditions.")
            #     break
            
            self.add_item(name, weight, quantity)
            remaining_weight = self.remaining_weight()

# Create an Inventory instance
inventory = Inventory()

# Prompt user to enter a minimum of 3 items with conditions on total weight
for i in range(1, 4):
    name = input(f"Enter name for Item{i}: ")
    quantity = int(input(f"Enter quantity for Item{i}: "))
    weight = min(int(input(f"Enter weight for Item{i} (You can add only : {inventory.remaining_weight()} !" 
                "If you add More than this We automatically take This weight ): ")), 
                 inventory.remaining_weight())
    inventory.add_item(name, weight, quantity)

# Add items to meet conditions
inventory.add_items_to_meet_conditions()

# Display items
print("\nItems:")
for item in inventory.items:
    print(vars(item))

# Check requirements
print("\nTotal Weight:", inventory.total_weight())
print("Total Quantity:", inventory.total_quantity())

if inventory.total_weight() == 500 and inventory.is_prime(inventory.total_quantity()):
    print("Requirements met!")
else:
    print("Requirements not met.")
