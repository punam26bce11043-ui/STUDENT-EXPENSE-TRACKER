from storage import get_expenses


def category_summary():
    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense[1]
        amount = float(expense[2])

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n------- CATEGORY SUMMARY -------")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


def spending_analysis():
    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    total = 0

    for expense in expenses:
        total += float(expense[2])

    print("\n------- SPENDING ANALYSIS -------")
    print(f"Total Spending: ₹{total:.2f}")

    if total < 3000:
        print("Spending Level: Low")
    elif total < 7000:
        print("Spending Level: Moderate")
    else:
        print("Spending Level: High")


def highest_category():
    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense[1]
        amount = float(expense[2])

        categories[category] = categories.get(category, 0) + amount

    highest = max(categories, key=categories.get)

    print("\n------- HIGHEST SPENDING -------")
    print(f"Category: {highest}")
    print(f"Amount: ₹{categories[highest]:.2f}")
