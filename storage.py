import csv

FILE_NAME = "expenses.csv"


def save_expense(expense):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense)


def get_expenses():
    expenses = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row:
                    expenses.append(row)

    except FileNotFoundError:
        pass

    return expenses


def update_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)
