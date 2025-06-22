"""print("--- List Operations ---")
while True:
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        numbers_str = input_str.split()
        my_list = [float(num) for num in numbers_str]
        if not my_list:
            print("The list cannot be empty. Please enter some numbers.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")

print(f"Original list: {my_list}")

if my_list:
    smallest_num = min(my_list)
    print(f"Smallest number in the list: {smallest_num}")
else:
    print("Cannot find smallest number in an empty list.")

unique_sorted_list = sorted(list(set(my_list)))

if len(unique_sorted_list) >= 2:
    second_greatest = unique_sorted_list[-2]
    print(f"Second greatest number in the list: {second_greatest}")
else:
    print("Cannot find the second greatest number (need at least two unique numbers).")

if len(unique_sorted_list) >= 2:
    second_smallest = unique_sorted_list[1]
    print(f"Second smallest number in the list: {second_smallest}")
else:
    print("Cannot find the second smallest number (need at least two unique numbers).")"""






print("--- Simple Billing Program ---")
bill_items = []

while True:
    print("\nOptions:")
    print("1. Create Bill (Add Item)")
    print("2. Display Item Price and Total Bill Amount")
    print("3. Display Grand Total")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item_name = input("Enter item name: ")
        while True:
            try:
                item_price = float(input(f"Enter price for {item_name}: "))
                if item_price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number for the price.")

        while True:
            try:
                item_quantity = int(input(f"Enter quantity for {item_name}: "))
                if item_quantity < 1:
                    print("Quantity must be at least 1. Please enter a valid quantity.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer for the quantity.")

        bill_items.append({'name': item_name, 'price': item_price, 'quantity': item_quantity})
        print(f"'{item_name}' added to the bill.")

    elif choice == '2':
        if not bill_items:
            print("No items in the bill yet. Please add items first.")
            continue

        print("\n--- Current Bill ---")
        sub_total = 0
        print(f"{'Item':<20} {'Price':<10} {'Quantity':<10} {'Subtotal':<10}")
        print("-" * 50)
        for item in bill_items:
            item_subtotal = item['price'] * item['quantity']
            print(f"{item['name']:<20} {item['price']:<10.2f} {item['quantity']:<10} {item_subtotal:<10.2f}")
            sub_total += item_subtotal
        print("-" * 50)
        print(f"{'Total Amount:':<40} {sub_total:<10.2f}")

    elif choice == '3':
        if not bill_items:
            print("No items in the bill yet.")
            grand_total = 0
        else:
            grand_total = sum(item['price'] * item['quantity'] for item in bill_items)

        print(f"\nGrand Total of the bill: {grand_total:.2f}")

    elif choice == '4':
        print("Exiting billing program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")






"""print("--- Factorial Calculator ---")
while True:
    try:
        num = int(input("Enter a non-negative integer to find its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers. Please enter a non-negative integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")"""





"""marks = []
total_marks = 0
num_subjects = 5

for i in range(num_subjects):
    while True:
        try:
            mark = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                total_marks += mark
                break
            else:
                print("Marks should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

percentage = (total_marks / (num_subjects * 100)) * 100

grade = ""
if percentage >= 60:
    grade = 'A'
elif 50 <= percentage < 60:
    grade = 'B'
elif 40 <= percentage < 50:
    grade = 'C'
elif 33 <= percentage < 40:
    grade = 'D'
else:
    grade = 'Fail'

print("\n--- Results ---")
print(f"Marks obtained: {marks}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}") """




