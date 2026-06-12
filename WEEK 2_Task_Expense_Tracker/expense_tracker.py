print("===== Expense Tracker =====")

total = 0

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    total += float(expense)

print("\nTotal Spent: ₹", total)
