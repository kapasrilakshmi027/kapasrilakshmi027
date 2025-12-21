#list of items
items = {
    "Rice": 50,
    "Flour":25,
    "Milk": 30,
    "Sugar": 40
}
#items thart are available 
print("Available Items:")
print("Rice - Rs.50")
print("Flour-Rs.25")
print("Milk - RS.30")
print("Sugar -RS.40")
#user input
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
#calculations
price = items[item_name]
total_bill = price*quantity
#billing output
print("\n--- Billing Details ---")
print("Item:",item_name)
print("Price per item: ",price)
print("Quantity:",quantity)
print("Total Bill: ",total_bill)
