from storage import get_expenses


def calculate_total():
    expenses = get_expenses()
    total = 0

    for expense in expenses:
        total += float(expense[2])

    return total


def budget_analysis():
    print("\n--- BUDGET ANALYSIS ---")

    try:
        budget = float(input("Enter your monthly budget: ₹"))

        if budget <= 0:
            print("Budget must be greater than zero.")
            return

        spent = calculate_total()
        remaining = budget - spent

        print(f"\nMonthly Budget : ₹{budget:.2f}")
        print(f"Total Spent    : ₹{spent:.2f}")
        print(f"Remaining      : ₹{remaining:.2f}")

        if remaining > 0:
            print("Status: You are within your budget.")

        elif remaining == 0:
            print("Status: You have used your complete budget.")

        else:
            print(f"Status: Budget exceeded by ₹{-remaining:.2f}")

    except ValueError:
        print("Please enter a valid amount.")
