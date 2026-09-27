from storage import get_expenses


def generate_report():
    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    total = 0
    categories = {}

    for expense in expenses:
        category = expense[1]
        amount = float(expense[2])

        total += amount
        categories[category] = categories.get(category, 0) + amount

    print("\n================================")
    print("       EXPENSE REPORT")
    print("================================")

    print(f"Total Expenses: ₹{total:.2f}")

    print("\nCategory-wise Spending:")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")

    highest = max(categories, key=categories.get)

    print("\nHighest Spending Category:")
    print(f"{highest}: ₹{categories[highest]:.2f}")

    print("================================")
