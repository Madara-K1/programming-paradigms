# Assignment 1 — Foundations of Programming Paradigms

## Project Description

This project is a Personal Expense Tracker written in Python. The program works with a fixed dataset of expense records, where each record contains a date, category, amount, and description. The goal of the project is to calculate useful statistics such as the total amount spent, the number of records, the total amount per category, the most expensive and least expensive expenses, the average expense amount, and the list of expenses above the average.

The assignment is not only about producing the final output. Its main purpose is to compare different programming paradigms and understand how the same problem can be solved in different styles. For that reason, the same core logic is implemented in an imperative version, a procedural version, and a version using functional programming elements.

## How to Run

To run each Python file from the command line, use the following commands:

```bash
python part_b_imperative.py
python part_c_procedural.py
python part_d_functional.py
```

The Markdown files can be opened directly in a text editor or viewed on GitHub.

## Sample Output

```text
Total expenses: 476.44
Number of records: 12

Category breakdown:
  Entertainment : 99.99
  Food          : 144.45
  Transport     : 67.00
  Utilities     : 165.00

Average expense: 39.70
Expenses above average:
  - Concert ticket (60.00)
  - Electricity bill (120.00)
  - Restaurant dinner (55.20)
  - Internet bill (45.00)
```

## Paradigm Comparison

### Imperative Programming

The imperative version was written using variables, loops, conditionals, and accumulator variables. This style makes the execution process very explicit because each step is visible in the code. It was easy to understand how values such as the total amount and category totals were built, but the code became longer because all logic had to be written manually. If the dataset grew to 100,000 records, the code would still work, but it would become harder to maintain if more features were added.

### Procedural Programming

The procedural version reorganises the same logic into functions. This made the program easier to read because each function has a single responsibility, such as calculating the total, finding the average, or printing the summary. It was easier to test and reuse the code in this version. With 100,000 records, the program would still work, and the structure would be more maintainable than the imperative version.

### Functional Elements

The functional version uses tools such as `sum`, generator expressions, set comprehensions, dictionary comprehensions, `filter`, `map`, and `lambda`. This made some operations shorter and more expressive. For example, calculating the total with `sum` is simpler than manually using an accumulator variable. However, functional code can be harder to read at first, especially when several expressions are combined in one line.

## What I Would Do Differently

If I had to start over, I would first design the functions and decide what each part of the program should return. This would make the transition from the imperative version to the procedural version easier. I would also add more tests to check each function separately before printing the final report.
