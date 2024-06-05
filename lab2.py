"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py
from lab1 import Item

# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.
class InventoryManager:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity):
        for item in self.items:
            if item.get_name(self) == name:
                print(f"Item {name} already exists.")
                return
        new_item = Item(name, price, quantity)
        self.items.append(new_item)
        print(f"Item added: {new_item}.")
        return

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"Item removed: {name}")
                return
        print("Item not found.")

    def update_item(self, name, new_price=None, new_quantity=None):
        for item in self.items:
            if item.get_name(self) == name:
                self.item.append(new_price, new_quantity)
                return
        print("Item not found")
    
# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

bread_section = InventoryManager()
bread_section.add_item('baguette' , 30, 60)
