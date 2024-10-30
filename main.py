
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  

    def authenticate(self, username, password):
        return self.username == username and self.password == password

# Product Class
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

users = [
    User("jia", "jia498627", "Admin"),
    User("javeriaamjad", "javeriaamjad", "User")
]


products = {}

# Functions
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users:
        if user.authenticate(username, password):
            print(f"Welcome {username}!")
            return user
    print("Invalid credentials")
    return None

def add_product(admin_user):
    if admin_user.role != "Admin":
        print("Permission denied!")
        return
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    category = input("Enter category: ")
    price = safe_input("Enter price: ", float)
    stock_quantity = safe_input("Enter stock quantity: ")
    products[product_id] = Product(product_id, name, category, price, stock_quantity)
    print(f"Product {name} added successfully.")

def view_products():
    if not products:
        print("No products available.")
    else:
        for product in products.values():
            print(f"{product.product_id}: {product.name} ({product.category}) - ${product.price}, Stock: {product.stock_quantity}")

def delete_product(admin_user, product_id):
    if admin_user.role != "Admin":
        print("Permission denied!")
        return
    if product_id in products:
        del products[product_id]
        print("Product deleted.")
    else:
        print("Product not found.")

def check_stock():
    for product in products.values():
        if product.stock_quantity < 10:
            print(f"Low stock alert: {product.name}")

def adjust_stock(admin_user, product_id, quantity_change):
    if admin_user.role != "Admin":
        print("Permission denied!")
        return
    if product_id in products:
        products[product_id].stock_quantity += quantity_change
        print(f"Stock updated. New quantity: {products[product_id].stock_quantity}")
    else:
        print("Product not found.")

def safe_input(prompt, cast_func=int):
    while True:
        try:
            return cast_func(input(prompt))
        except ValueError:
            print("Invalid input, please try again.")

# Main Loop
def main():
    print("Welcome to the Inventory Management System!")
    user = login()
    if not user:
        return

    while True:
        print("\nOptions:")
        print("1. Add Product (Admin Only)")
        print("2. View Products")
        print("3. Delete Product (Admin Only)")
        print("4. Adjust Stock (Admin Only)")
        print("5. Check Stock Levels")
        print("6. Exit")

        choice = safe_input("Choose an option: ")

        if choice == 1:
            add_product(user)
        elif choice == 2:
            view_products()
        elif choice == 3:
            product_id = input("Enter product ID to delete: ")
            delete_product(user, product_id)
        elif choice == 4:
            product_id = input("Enter product ID to adjust stock: ")
            quantity_change = safe_input("Enter quantity to add/remove: ")
            adjust_stock(user, product_id, quantity_change)
        elif choice == 5:
            check_stock()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
