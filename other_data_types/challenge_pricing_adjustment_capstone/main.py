#1
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
#2
price_eggs = grocery_inventory["Eggs"][1]
if price_eggs > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    price_eggs_reduced = price_eggs-1
    grocery_inventory.update({"Eggs": ("Dairy", price_eggs_reduced, 30)})
else: 
    print("The price of Eggs is reasonable.")
#3
grocery_inventory.update({"Tomatoes":("Produce", 1.2, 30)})
print("Inventory after adding Tomatoes:",grocery_inventory)
#4
stock_milk = grocery_inventory["Milk"][2]
if stock_milk < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    stock_milk_restocked = stock_milk+20
    grocery_inventory.update({"Milk": ("Dairy", 3.50, stock_milk_restocked)})
else:
    print("Milk has sufficient stock.")
#5
if grocery_inventory["Apples"][1] > 2:
    print("Apples removed from inventory due to high price.")
    grocery_inventory.pop("Apples")
#6
print("Updated inventory:", grocery_inventory)
    