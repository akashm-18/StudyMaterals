class Item:
    def __init__(self,name,quantity,weight):
        self.name = name
        self.quantity = quantity
        self.weight = weight

class Inventory:
    def __init__(self):
        self.items = []
    
    def add_item(self,name,quantity,weight):
        self.items.append(Item(name,quantity,weight))
    
    def remove_item(self,name):
        self.items = [item for item in self.items if item.name != name]
    
    def total_weight(self):
        return sum(item.weight for item in self.items)

    def is_prime(self,num):
        if num <= 1:
            return False
        for i in range(2,int(num ** 0.5)+1):
            if num % i == 0:
                return False
        
        return True

    def total_quantity(self):
        return sum(item.quantity for item in self.items)
    
    def remaining_weight(self):
        return 500 - self.total_weight()
    
    def add_items_meet_condition(self):
        remaining_weight = self.remaining_weight()
        
        while remaining_weight > 0 or not self.is_prime(self.total_quantity()):
            print('You need to Add Item to Attain the Prime Number or Total Weight be 500')
            
            name = input(f"Enter Name for item {len(self.items) + 1} : ")
            quantity = int(input(f"Enter Quantity for Item {len(self.items) + 1} : "))
            weight = min(int(input(f"Enter Weight for Item {len(self.items) + 1} : ")) , remaining_weight)
            
            if self.total_weight() + weight > 500:
                print("Can't Add this Item ! Exceeds the Limit")
                print(f"You only can Add {remaining_weight} as weight")
                break
            
            self.add_item(name,quantity,weight)
            remaining_weight = self.remaining_weight()
            self.display_items()
            
                
    
    def display_items(self):
        for item in self.items:
            print(vars(item))
    
    def ask_to_remove(self):
        name_to_remove = input("\nEnter the Name of Item to Remove or '0' to Skip")
        
        if name_to_remove.lower() != '0':
            self.remove_item(name_to_remove)
            print(f"\nItem {name_to_remove} Removed !")
            self.display_items()
        
        if self.total_weight() < 500:
            remaining_weight = self.remaining_weight()
            print(f"Weight is less than 500.You Need to add item to match")
            name = input(f"Enter Name for Item {len(self.items)+1} : ")
            self.add_item(name,1,remaining_weight)
            print(f"New Item added with weight {remaining_weight}")
            self.display_items()


inventory = Inventory()

# Adding Items 
for i in range(1,4):
    name = input(f"Enter Name for Item {i} : ")
    quantity = int(input(f"Enter Quantity for Item {i} : "))
    weight = min(int(input(f"Enter Weight for Item {i} : (You only can Add ) {inventory.remaining_weight()} ! "
                       "If You Add more than this . Then it takes remaining Weight : ")),inventory.remaining_weight())
    inventory.add_item(name,quantity,weight)

# inventory.add_items_meet_condition()

# Display Items 
print('\nItems:')
inventory.display_items()



inventory.ask_to_remove()
inventory.add_items_meet_condition()

print('\nAll ok')

# Check Totals
print('\nTotal Weight : ',inventory.total_weight())
print('Total Quantity : ',inventory.total_quantity())