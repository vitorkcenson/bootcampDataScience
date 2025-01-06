"""
This code calculates the total stock value of coffee items in a cafe. 

It utilizes three dictionaries:
    - `menu`: Stores the menu items with their corresponding IDs.
    - `stock`: Stores the available stock quantity for each item.
    - `price`: Stores the selling price for each item.

The code iterates through the `menu`, calculates the value of each item 
(stock quantity multiplied by price), and accumulates the total stock value. 
Finally, it prints the value of each item and the total stock value.
"""

menu = [(1, "Espresso"), 
        (2, "Americano"), 
        (3, "Latte"), 
        (4, "Mocha"), 
        (5, "Cappuccino")]

stock = {'Espresso': 150, 
         'Americano': 135, 
         'Latte': 120, 
         'Mocha': 200, 
         'Cappuccino': 300}

price = {'Espresso': 1.50, 
         'Americano': 2.45, 
         'Latte': 3.25, 
         'Mocha': 3.95, 
         'Cappuccino': 3.65}

total_stock = 0

for id, item in menu: 
    # Calculate the value of the current item
    item_value = stock[item] * price[item]
    # Print the value of the current item
    print(f"Item value: ${item_value:.2f}")  
    # Add the item value to the total stock value
    total_stock += item_value 

# Print the total stock value
print(f"Total stock value: ${total_stock:.2f}")