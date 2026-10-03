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
        print("inventory.json found")
        print("Inventory loaded successfully")
        return data
    except FileNotFoundError: 
        print("Warning: inventory.json not found. Returning empty inventory.")
        return {}

def display_all(inventory):
    print("Current Inventory")
    print("-" * 50)
    inventory_list = inventory["products"]  #Access the list inside 'products'
    for product in inventory_list:
        item_id = product["ID"]
        name = product["Name"]
        price = product["Price"]
        stock = product ["Stock"]
        print(f"ID: {item_id} | Name: {name} | Price: {price} | Stock: {stock} ")
    print("-" * 50)

def add_stock(inventory):
    item_id = input("Product ID: ")
    product_name = input("Product Name")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {
        "ID": item_id,
        "Name": product_name,
        "Price": price,
        "Stock": stock
    }

    inventory["products"].append(new_product)
    print("Product added successfully !")

print("============================")
print("INVENTORY MANAGEMENT SYSTEM")
print("============================")
print()
print(load_inventory())
print()
menu()
inventory = load_inventory()
print()
display_all(inventory)
add_stock(inventory)
