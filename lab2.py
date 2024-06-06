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
            if item.get_name() == name:
                print(f"Item {name} already exists.")
                return None
        new_item = Item(name, price, quantity)
        self.items.append(new_item)
        print(f"Item added: {name}.")
        return True

    def remove_item(self, name):
        for item in self.items:
            if item.get_name() == name:
                self.items.remove(item)
                print(f"Item removed: {name}")
                return True
        print("Item not found.")
        return None

    def update_item(self, name, new_price=None, new_quantity=None):
        for existing_item in self.items:
            if existing_item.get_name() == name:
                existing_item.set_quantity(new_quantity)
                existing_item.set_price(new_price)
                print(f"Item updated: {name}.\nNew quantity: {new_quantity}\nNew price: ${new_price}")
                return True
        print("Item not found")
        return False
    
    def display_items(self):
        for item in self.items:
            print(f"Item name: {item.get_name()}\n\nItem price: {item.get_price()}\nItem quantity: {item.get_quantity()}")

            
    
# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

bread_section = InventoryManager()
bread_section.add_item('baguette' , 30, 60)
bread_section.remove_item('baguette')
bread_section.display_items()

milk_section = InventoryManager()
milk_section.add_item('cream', 20, 1)
milk_section.update_item('cream', 15, 12)
