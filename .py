
# Inventory List Analyzer

items = []

print("Welcome to Inventory List Analyzer!")

while True:
    name = input("\nEnter item name: ").strip().title()
    category = input("Enter category: ").strip().lower()

    quantity = int(input("Enter quantity: "))

    item = {
        "name": chocolate,
        "category": sweets 
        "quantity": 10
    }

    items.append(item)

    choice = input("\nDo you want to add more items? (y/n): ").lower()

    if choice != "y":
        break

# Inventory Summary
print("\n========== INVENTORY SUMMARY ==========")

total_items = len(items)
total_quantity = sum(item["quantity"] for item in items)
average = total_quantity / total_items

most_stocked = max(items, key=lambda item: item["quantity"])
least_stocked = min(items, key=lambda item: item["quantity"])

print(f"\nTotal Different Items: {total_items}")
print("Explanation: You entered", total_items, "different items:",
      ", ".join(item["name"] for item in items) + ".")

print(f"\nTotal Quantity in Stock: {total_quantity}")
print("Explanation: Sum of all quantities:",
      " + ".join(str(item["quantity"]) for item in items),
      "=", total_quantity)

print(f"\nAverage Quantity per Item: {average:.2f}")
print(f"Explanation: Average = {total_quantity} total / {total_items} items")

print(f"\nMost Stocked Item: {most_stocked['name']} "
      f"({most_stocked['quantity']} units)")
print(f"Explanation: {most_stocked['name']} has the highest quantity.")

print(f"\nLeast Stocked Item: {least_stocked['name']} "
      f"({least_stocked['quantity']} units)")
print(f"Explanation: {least_stocked['name']} has the lowest quantity.")

# Unique Categories using Set
categories = sorted(set(item["category"] for item in items))

print("\nUnique Categories in Inventory:", categories)
print("Explanation: Categories are converted to lowercase.")
print("No duplicate categories are shown.")

# Sort Items by Quantity (High to Low)
print("\n========================================")
print("📦 Items Sorted by Quantity (High to Low):")

sorted_items = sorted(
    items, key=lambda item: item["quantity"], reverse=True
)

for index, item in enumerate(sorted_items, start=1):
    print(f"{index}. {item['name']} - {item['quantity']} units")

# Sort Categories Alphabetically
print("\n========================================")
print("📁 Categories in Alphabetical Order:")

for index, category in enumerate(categories, start=1):
    print(f"{index}. {category}")

print("\n========== END OF REPORT ==========")
