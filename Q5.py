
n = int(input("Enter number of grocery items: "))
prices = {}
quantities = {}

for _ in range(n):
    item = input("Enter item name: ")
    price = float(input(f"Enter price of {item}: "))
    qty = float(input(f"Enter quantity of {item}: "))
    
    prices[item] = price
    quantities[item] = qty

total_bill = 0
for item in prices:
    if item in quantities:
        total_bill += prices[item] * quantities[item]

print("Total bill: Rs.", total_bill)
