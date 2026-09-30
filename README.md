# Student Expense Tracker

## Project Description
The Student Expense Tracker is a beginner-friendly Python project developed to help students manage and track their daily expenses. It allows users to record expenses, view saved records, calculate total spending, analyze category-wise expenses, and compare spending with a budget.
The project uses Python programming concepts and CSV file handling to store expense records.

## Project Details
* **Student Name:** Punam Sethi
* **Registration Number:** 26BCE11043
* **Course:** Introduction to Problem Solving
* **Faculty:** DR PRIYADARSHINI B
* **Academic Year:** 2026–2030

## Objectives
* To maintain a record of daily expenses.
* To calculate total expenses.
* To organize expenses according to categories.
* To analyze spending habits.
* To compare expenses with a given budget.
* To understand Python programming and file handling.

## Features
1. **Add Expense:** Enter the date, category, amount, and description.
2. **View Expenses:** Display all saved expense records.
3. **Delete Expense:** Remove a selected expense record.
4. **Category-wise Summary:** Calculate spending for each category.
5. **Total Expense:** Calculate the total amount spent.
6. **Budget Analysis:** Compare recorded expenses with a given budget.
7. **Spending Analysis:** Classify spending as Low, Moderate, or High.

## Technologies Used

* **Programming Language:** Python
* **Data Storage:** CSV file
* **Concepts Used:** Functions, loops, conditional statements, dictionaries, lists, file handling, and exception handling.

## Project Structure

```text
Student-Expense-Tracker/
│
├── student_expense_tracker.py
├── expenses.csv
├── README.md
└── images/
    ├── main_menu.png
    ├── add_expense.png
    └── expense_summary.png
```

Note: The `expenses.csv` file is created when the program saves an expense. The images shown above are example filenames; upload your actual screenshots to the `images` folder.

## Requirements

* Python 3 installed on your computer.
* No external Python libraries are required.

## How to Run the Project

1. Download or clone this repository.
2. Open the project folder in your terminal.
3. Run the following command:

```bash
python student_expense_tracker.py
```

If your system uses Python 3 through the `python3` command, run:

```bash
python3 student_expense_tracker.py
```

4. Follow the menu instructions displayed in the terminal.

## Screenshots

### Main Menu

![Main Menu](images/main_menu.png)

### Adding an Expense

![Adding an Expense](images/add_expense.png)

### Expense Summary

![Expense Summary](images/expense_summary.png)

To display these images, upload your screenshots using the same filenames into the `images` folder in your GitHub repository.

## Data Storage
The project stores expense records in a CSV file named `expenses.csv`.
Each expense record contains:

* Date
* Category
* Amount
* Description

The CSV file allows expense records to be saved and accessed when the program runs again.

## Spending Analysis
The program uses fixed spending thresholds:

* **Low:** Total expenses below ₹3,000.
* **Moderate:** Total expenses from ₹3,000 to below ₹7,000.
* **High:** Total expenses of ₹7,000 or more.

These categories are simple classifications used for this project.

## Limitations

* The program runs in the terminal and does not have a graphical user interface.
* Date and amount validation can be improved.
* Budget analysis currently compares the budget with the expenses stored in the file and does not filter records by month.
* Spending categories use fixed thresholds.

## Future Enhancements
* Add monthly and yearly expense reports.
* Improve input validation.
* Add graphical charts for spending analysis.
* Create a graphical user interface.
* Add a separate budget for each month.
* Export expense summaries into reports.

## Learning Outcomes
Through this project, I learned how to:* Write and organize Python functions.
* Use loops and conditional statements.
* Work with lists and dictionaries.
* Read from and write to CSV files.
* Handle basic file-related errors.
* Apply programming concepts to a practical problem.

## Conclusion
The Student Expense Tracker is a simple Python project that helps students record and analyze their expenses. It demonstrates fundamental programming concepts and provides a foundation for developing more advanced expense management applications.

**Punam Sethi**
Registration Number: 26BCE11043

**Course:** Introduction to Problem Solving
**Academic Year:** 2026–2030
