# define menu of restaurant
menu = {
  'Pizza': 200,
  'Burger': 100,
  'Pasta': 150,
  'French Fries': 50,
  'Sandwich': 80,
  'Coke': 40,
  'Tea': 20,
  'Coffee': 30
}

# check menu
# print(menu)

# Great!
print("Welcome to the Python Restaurant!\n")
print("Here is the menu :")
for item, price in menu.items():
  print(f"{item} - {price}")  # f-string

# store the order
order_total = 0

order = input("\nEnter your order (separate items by commas): ").split(',')

# test the order
# print(order)

for item in order:
  item = item.strip()  # Remove any leading/trailing spaces
  if item in menu:  # Check if the item exists in the menu
    order_total += menu[item]  # Add the price for each ordered item
  else:
    print(f"Sorry, we don't have {item} on the menu.")

print(f"Your total order amount is: {order_total}")
print("Thank you for ordering with us!")