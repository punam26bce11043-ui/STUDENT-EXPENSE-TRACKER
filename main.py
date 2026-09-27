from expense import add_expense, view_expenses, delete_expense
from budget import budget_analysis
from analysis import category_summary, spending_analysis, highest_category
from report import generate_report


def main():

    while True:

        print("\n======================================")
        print("       STUDENT EXPENSE TRACKER")
        print("======================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Category Summary")
        print("5. Budget Analysis")
        print("6. Spending Analysis")
        print("7. Highest Spending Category")
        print("8. Generate Expense Report")
        print("9. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            budget_analysis()

        elif choice == "6":
            spending_analysis()

        elif choice == "7":
            highest_category()

        elif choice == "8":
            generate_report()

        elif choice == "9":
            print("\nThank you for using Student Expense Tracker!")
            break

        else:
            print("\nInvalid choice! Please select 1-9.")


if __name__ == "__main__":
    main()
