import json

def menu():
    print("--------MENU---------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")

def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
           data = json.load(file)
        return data
    except FileNotFoundError: 
        print("Warning: inventory.json not found. Returning empty inventory.")
        return {}

print("============================")
print("INVENTORY MANAGEMENT SYSTEM")
print("============================")

print(load_inventory())