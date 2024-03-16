# class Inventory:
#     def __init__(self):
#         self.products = {}
#
#     def add_product(self, product_id, name, price, quantity):
#         self.products[product_id] = {'name': name, 'price': price, 'quantity': quantity}
#
#     def remove_product(self, product_id):
#         if product_id in self.products:
#             del self.products[product_id]
#         else:
#             print(f"Product with ID {product_id} not found in inventory.")
#
#     def update_product(self, product_id, name=None, price=None, quantity=None):
#         if product_id in self.products:
#             if name is not None:
#                 self.products[product_id]['name'] = name
#             if price is not None:
#                 self.products[product_id]['price'] = price
#             if quantity is not None:
#                 self.products[product_id]['quantity'] = quantity
#         else:
#             print(f"Product with ID {product_id} not found in inventory.")
#
#     def list_products(self):
#         return [(product_id, details['name'], details['price'], details['quantity'])
#                 for product_id, details in self.products.items()]
#
#
# # Creating an instance of the Inventory class
# inventory = Inventory()
#
# # a) Add a new product
# inventory.add_product("P001", "Laptop", 899.99, 10)
#
# # b) Add another product
# inventory.add_product("P002", "Smartphone", 499.99, 20)
#
# # c) Update the quantity of "Laptop" (product_id "P001") to 15
# inventory.update_product("P001", quantity=15)
#
# # d) Remove the "Smartphone" (product_id "P002") from the inventory
# inventory.remove_product("P002")
#
# # e) List all products currently in the inventory
# products_list = inventory.list_products()
# print("Products in inventory:")
# for product in products_list:
#     print(f"Product ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}")





####################################..........OR..............###############################################


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, quantity):
        if product_id not in self.products:
            self.products[product_id] = {'name': name, 'price': price, 'quantity': quantity}
        else:
            print(f"Product with ID {product_id} already exists in inventory.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print(f"Product with ID {product_id} not found in inventory.")

    def update_product(self, product_id, name=None, price=None, quantity=None):
        if product_id in self.products:
            product = self.products[product_id]
            if name:
                product['name'] = name
            if price:
                product['price'] = price
            if quantity:
                product['quantity'] = quantity
        else:
            print(f"Product with ID {product_id} not found in inventory.")

    def list_products(self):
        return [(product_id, details['name'], details['price'], details['quantity'])
                for product_id, details in self.products.items()]


# Testing the Inventory class
inventory = Inventory()

# Add products
inventory.add_product("P001", "Laptop", 899.99, 10)
inventory.add_product("P002", "Smartphone", 499.99, 20)

# Update product quantity
inventory.update_product("P001", quantity=15)

# Remove a product
inventory.remove_product("P002")

# List all products
products_list = inventory.list_products()
print("Products in inventory:")
for product in products_list:
    print(f"Product ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}")
