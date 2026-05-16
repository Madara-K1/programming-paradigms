expenses = [
    {"date": "2024-01-05", "category": "Food",          "amount": 42.50, "description": "Groceries"},
    {"date": "2024-01-07", "category": "Transport",     "amount": 15.00, "description": "Bus pass"},
    {"date": "2024-01-09", "category": "Entertainment", "amount": 60.00, "description": "Concert ticket"},
    {"date": "2024-01-10", "category": "Food",          "amount": 8.75,  "description": "Coffee & snack"},
    {"date": "2024-01-12", "category": "Utilities",     "amount": 120.00,"description": "Electricity bill"},
    {"date": "2024-01-14", "category": "Food",          "amount": 55.20, "description": "Restaurant dinner"},
    {"date": "2024-01-15", "category": "Transport",     "amount": 30.00, "description": "Taxi"},
    {"date": "2024-01-17", "category": "Entertainment", "amount": 14.99, "description": "Streaming subscription"},
    {"date": "2024-01-20", "category": "Food",          "amount": 38.00, "description": "Groceries"},
    {"date": "2024-01-22", "category": "Utilities",     "amount": 45.00, "description": "Internet bill"},
    {"date": "2024-01-25", "category": "Transport",     "amount": 22.00, "description": "Train ticket"},
    {"date": "2024-01-28", "category": "Entertainment", "amount": 25.00, "description": "Book"},
]


def get_total(expense_list):
    """
    Calculate the total amount of all expenses.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        float: Sum of all 'amount' values.
    """
    total = 0
    for expense in expense_list:
        total += expense["amount"]
    return total


def get_count(expense_list):
    """
    Count the number of expense records.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        int: Number of expense records.
    """
    count = 0
    for expense in expense_list:
        count += 1
    return count


def get_category_totals(expense_list):
    """
    Build a mapping from category names to their total amounts.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        dict: Dictionary in the format {category: total_amount}.
    """
    category_totals = {}

    for expense in expense_list:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals


def get_most_expensive(expense_list):
    """
    Find the expense record with the highest amount.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        dict: Expense dictionary with the highest amount.
    """
    most_expensive = expense_list[0]

    for expense in expense_list:
        if expense["amount"] > most_expensive["amount"]:
            most_expensive = expense

    return most_expensive


def get_least_expensive(expense_list):
    """
    Find the expense record with the lowest amount.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        dict: Expense dictionary with the lowest amount.
    """
    least_expensive = expense_list[0]

    for expense in expense_list:
        if expense["amount"] < least_expensive["amount"]:
            least_expensive = expense

    return least_expensive


def get_average(expense_list):
    """
    Calculate the average expense amount.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        float: Average value of the expense amounts.
    """
    total = get_total(expense_list)
    count = get_count(expense_list)
    return total / count


def get_above_average(expense_list):
    """
    Return a list of expenses whose amount is strictly above the average.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        list: Expense dictionaries above the average amount.
    """
    average = get_average(expense_list)
    above_average = []

    for expense in expense_list:
        if expense["amount"] > average:
            above_average.append(expense)

    return above_average


def print_summary(expense_list):
    """
    Print a full summary report using the helper functions above.

    Parameters:
        expense_list (list): List of expense dictionaries.

    Returns:
        None
    """
    total = get_total(expense_list)
    count = get_count(expense_list)
    category_totals = get_category_totals(expense_list)
    most_expensive = get_most_expensive(expense_list)
    least_expensive = get_least_expensive(expense_list)
    average = get_average(expense_list)
    above_average = get_above_average(expense_list)

    print(f"Total expenses: {total:.2f}")
    print(f"Number of records: {count}")

    print("\nCategory breakdown:")
    for category in sorted(category_totals):
        print(f"  {category:<14}: {category_totals[category]:.2f}")

    print(f"\nMost expensive : {most_expensive['description']} ({most_expensive['category']}) — {most_expensive['amount']:.2f}")
    print(f"Least expensive: {least_expensive['description']} ({least_expensive['category']}) — {least_expensive['amount']:.2f}")

    print(f"\nAverage expense: {average:.2f}")
    print("Expenses above average:")
    for expense in above_average:
        print(f"  - {expense['description']} ({expense['amount']:.2f})")


if __name__ == "__main__":
    print_summary(expenses)
