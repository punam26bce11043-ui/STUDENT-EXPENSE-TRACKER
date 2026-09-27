from datetime import datetime


def validate_amount(amount):
    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False


def validate_date(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True

    except ValueError:
        return False


def validate_category(category):
    categories = [
        "Food",
        "Travel",
        "Education",
        "Shopping",
        "Entertainment",
        "Other"
    ]

    return category.title() in categories
