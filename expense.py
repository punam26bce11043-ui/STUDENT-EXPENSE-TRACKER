from storage import save_expense, get_expenses, update_expenses
from validation import validate_amount, validate_date, validate_category


def add_expense():
    print("\n--- ADD EXPENSE ---")

    date = input("Enter date (DD-MM-YYYY): ")

    if not validate_date(date):
        print("Invalid date format!")
        return

    category = input(
        "Enter category (Food/Travel/Education/Shopping/"
        "Entertainment/Other): "
    ).title()

    if not validate_category(category):
        print("Invalid category!")
        return

    amount = input("Enter amount: ₹")

    if not validate_amount(amount):
        print("Invalid amount!")
        return

    description = input("Enter description: ")

    expense = [
        date,
        category,
        float(amount),
        description
    ]

    save_expense(expense)

    print("Expense added successfully!")


def view_expenses():
    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n--------------- EXPENSES ---------------")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. Date: {expense[0]} | "
            f"Category: {expense[1]} | "
            f"Amount: ₹{float(expense[2]):.2f} | "
            f"Description: {expense[3]}"
        )


def delete_expense():
    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number!")
            return

        deleted = expenses.pop(number - 1)

        update_expenses(expenses)

        print(
            f"Expense of ₹{deleted[2]} "
            f"deleted successfully!"
        )

    except ValueError:
        print("Please enter a valid number.")
