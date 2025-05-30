product_catalog = {
    "apple": (100, 10),
    "banana":(60, 20),
    "mango":(120, 30),
    "orange":(80, 15),
    "grape":(150, 25),
    "kiwi":(200, 5),
    "watermelon":(300, 8),
    "strawberry":(250, 12),
    "blueberry":(180, 18),
    "peach":(90, 22)
}

def get_product_info(product_name):
    product_name = product_name.lower()
    if product_name in product_catalog:
        price, quantity = product_catalog[product_name]
        return f"{product_name.capitalize()} - Price: ${price}, Quantity: {quantity} available"
    else:
        return "Product not found in the catalog."

def get_all_products():
    product_list = []
    for product_name, (price, quantity) in product_catalog.items():
        product_list.append(f"{product_name.capitalize()} - Price: ${price}, Quantity: {quantity} available")
    return "\n".join(product_list)

def add_or_update_product(product_name, price, quantity):
    product_name = product_name.lower()
    if product_name in product_catalog:
        product_catalog[product_name] = (price, quantity)
        return f"Updated {product_name.capitalize()} - Price: ${price}, Quantity: {quantity} available"
    else:
        product_catalog[product_name] = (price, quantity)
        return f"Added {product_name.capitalize()} - Price: ${price}, Quantity: {quantity} available"
    
def purchase_items(product_name, quantity):
    product_name = product_name.lower()
    if product_name in product_catalog:
        price, available_quantity = product_catalog[product_name]
        if quantity <= available_quantity:
            total_cost = price * quantity
            product_catalog[product_name] = (price, available_quantity - quantity)
            return f"Purchased Successful.  Products: {product_name}  Total Cost: ${total_cost}. Remaining stock: {available_quantity - quantity}"
        else:
            return f"Insufficient stock for {product_name}. Available: {available_quantity}, Requested: {quantity}"
    else:
        return "Product not found in the catalog."

print("Welcome to the Smart Grocery Store Assistant!")
while True:
    print("\nOptions:")
    print("1. View Products Information")
    print("2. List All Products")
    print("3. Add/Update Product")
    print("4. Purchase Items")
    print("5. Exit")
    
    choice = input("Please enter your choice (1-5): ")
    
    if choice == '1':
        product_name = input("Enter the product name: ")
        print(get_product_info(product_name))
    elif choice == '2':
        print(get_all_products())
    elif choice == '3':
        product_name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the product quantity: "))
        print(add_or_update_product(product_name, price, quantity))
    elif choice == '4':
        product_name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity to purchase: "))
        print(purchase_items(product_name, quantity))
    elif choice == '5':
        print("Thank you for using the Smart Grocery Store Assistant. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")