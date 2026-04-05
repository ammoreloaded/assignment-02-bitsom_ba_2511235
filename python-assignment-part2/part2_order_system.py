import copy;

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# Task 1: Print Menu Grouped by Category

# Group Categories in Menu List & Print according to Category
categories = []

for menu_item in menu:
    cat_item = menu[menu_item]["category"]
    #If a new Category is found, append in category list
    if cat_item not in categories:
        categories.append(cat_item)

# print category-wise menu
for cat_item in categories:
    print(f"\n===== {cat_item} =====")

    for item in menu:
        if menu[item]["category"] == cat_item:
            price = menu[item]["price"]
            status = "Available" if menu[item]["available"] else "Unavailable"

            print(f"{item:<15} ₹{price:.2f}   [{status}]")

# 1.1 Menu Insights

# total items
total_items = len(menu)

# total available items
available_count = 0
for item in menu:
    if menu[item]["available"]:
        available_count += 1

# most expensive item
max_price = 0
max_item = ""

for item in menu:
    if menu[item]["price"] > max_price:
        max_price = menu[item]["price"]
        max_item = item


print("\nSummary:")
print("Total number of items on the menu:", total_items)
print("Total number of available items:", available_count)
print("The most expensive item:", max_item, "- ₹", max_price)

# items under 150
print("\nAll items priced under ₹150:")
for item in menu:
    if menu[item]["price"] < 150:
        print(item, "- ₹", menu[item]["price"])


#-------------------------------------------------Task 2----------------------------------------

# cart starts empty
cart_list = []


# Define method to be called on demand to optimize code. Basically picks cart[] List and prints all items in it

def print_cart():
    print("\nYour Cart Contents:")
    if len(cart_list) == 0:
        print("Your Cart is empty")
    else:
        for cart_contents in cart_list:
            print(cart_contents)


# Adding item to cart

def add_to_cart(item_name, qty):
    # check if item exists
    if item_name not in menu:
        print(item_name, "does not exist in menu")
        return

    # check availability
    if not menu[item_name]["available"]:
        print(item_name, "is currently unavailable")
        return

    # check if already in cart
    found = False
    for cart_contents in cart_list:
        if cart_contents["item"] == item_name:
            cart_contents["quantity"] += qty
            found = True
            break

    # if not found, add new entry
    if not found:
        cart_list.append({
            "item": item_name,
            "quantity": qty,
            "price": menu[item_name]["price"]
        })


# -------------------------------
# Remove item
# -------------------------------
def remove_from_cart(item_name):
    found = False

    for cart_contents in cart_list:
        if cart_contents["item"] == item_name:
            cart_list.remove(cart_contents)
            found = True
            break

    if not found:
        print(item_name, "not found in cart")


# Update quantity

def update_quantity(item_name, qty):
    found = False

    for cart_contents in cart_list:
        if cart_contents["item"] == item_name:
            cart_contents["quantity"] = qty
            found = True
            break

    if not found:
        print(item_name, "not found in cart")


# Simulation Steps

# 1
add_to_cart("Paneer Tikka", 2)
print_cart()

# 2
add_to_cart("Gulab Jamun", 1)
print_cart()

# 3
add_to_cart("Paneer Tikka", 1)
print_cart()

# 4
add_to_cart("Mystery Burger", 1)
print_cart()

# 5
add_to_cart("Chicken Wings", 1)
print_cart()

# 6
remove_from_cart("Gulab Jamun")
print_cart()

# Printing Order Summary


print("\n========== Order Summary ==========")

subtotal = 0

for cart_contents in cart_list:
    item_total = cart_contents["quantity"] * cart_contents["price"]
    subtotal += item_total

    print(f"{cart_contents['item']:<18} x{cart_contents['quantity']}    ₹{item_total:.2f}")

print("------------------------------------")

gst = round(subtotal * 0.05, 2)
total = round(subtotal + gst, 2)

print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):                ₹{gst:.2f}")
print(f"Total Payable:           ₹{total:.2f}")
print("====================================")



#-------------------------------------------------Task 3----------------------------------------
# Step 1: Deep Copy Inventory

inventory_backup = copy.deepcopy(inventory)

# Create a backup of inventory
# Manually change source inventory & print both copies
# Restore original inventory with backup to POC deepcopy
inventory["Paneer Tikka"]["stock"] = 5

print("\n\nAfter manual change:")
print("Inventory:", inventory["Paneer Tikka"])
print("Backup   :", inventory_backup["Paneer Tikka"])

# restore original inventory
inventory = copy.deepcopy(inventory_backup)


# Step 2: Deduct stock based on cart

print("\n--- Order Fulfilment ---")

for cart_item in cart_list:
    item = cart_item["item"]
    qty_needed = cart_item["quantity"]

    stock_available = inventory[item]["stock"]

    # check if enough stock is available
    if stock_available >= qty_needed:
        inventory[item]["stock"] -= qty_needed

    else:
        print(f"Warning: Only {stock_available} {item} available, cannot fulfil {qty_needed}")
        inventory[item]["stock"] = 0  # do not go below 0


# Step 3: Reorder Alerts


print("\n--- Reorder Alerts ---")

for item in inventory:
    stock = inventory[item]["stock"]
    reorder = inventory[item]["reorder_level"]

    if stock <= reorder:
        print(f"⚠ Reorder Alert: {item} — Only {stock} unit(s) left (reorder level: {reorder})")


# Step 4: Final Check


print("\n--- Final Inventory ---")
print(inventory)

print("\n--- Backup Inventory (unchanged) ---")
print(inventory_backup)



#-------------------------------------------------Task 4----------------------------------------

# Part 1: Revenue per day


print("---- Revenue Per Day ----")

daily_revenue = {}

#Iterate Sales Log to get date then iterate date list to fetch total object
#Append total value in another variable to calculate total revenue
for date in sales_log:
    total = 0

    for order in sales_log[date]:
        total += order["total"]

    daily_revenue[date] = total
    print(date, "- ₹", total)


# Part 2: Best-selling day
#Iterate daily revenue list declared earlier to compare value in Max revenue that gives best-selling day


max_revenue = 0
best_day = ""

for date in daily_revenue:
    if daily_revenue[date] > max_revenue:
        max_revenue = daily_revenue[date]
        best_day = date

print("\nBest Selling Day:", best_day, "- ₹", max_revenue)


# Part 3: Most ordered item. Calculating item that appears in the greatest number of individual orders across all days


item_count = {}

for date in sales_log:
    for order in sales_log[date]:
        for item in order["items"]:

            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

# find max
max_item = ""
max_count = 0

for item in item_count:
    if item_count[item] > max_count:
        max_count = item_count[item]
        max_item = item

print("\nMost Ordered Item:", max_item, "-", max_count, "times")


# Part 4: Adding a new day with additional orders. This will update the max, best-selling day and other KPIs calculated earlier


sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\n---- Updated Revenue Per Day ----")

daily_revenue = {}

for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]

    daily_revenue[date] = total
    print(date, "- ₹", total)

# recalculate best-selling day
max_revenue = 0
best_day = ""

for date in daily_revenue:
    if daily_revenue[date] > max_revenue:
        max_revenue = daily_revenue[date]
        best_day = date

print("\nUpdated Best Selling Day:", best_day, "- ₹", max_revenue)


# Part 5: Numbered list using enumerate.

#Demo use of Enumerate function to display orders for all dates

print("\n---- All Orders ----")

all_orders = []

# flatten all orders into one list
for date in sales_log:
    for order in sales_log[date]:
        all_orders.append((date, order))

# print using enumerate
for i, entry in enumerate(all_orders, start=1):
    date = entry[0]
    order = entry[1]

    items_str = ", ".join(order["items"])

    print(f"{i}. [{date}] Order #{order['order_id']} — ₹{order['total']:.2f} — Items: {items_str}")
