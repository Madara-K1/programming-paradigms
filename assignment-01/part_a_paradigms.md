## Snippet 1
**Paradigm**: Imperative programming

**Explanation**: This snippet is mainly imperative because it executes instructions step by step. It uses a mutable accumulator variable called `total`, which is updated during each iteration of the `for` loop. The code explicitly describes how the result is computed.

## Snippet 2
**Paradigm**: Procedural programming

**Explanation**: This snippet is procedural because the program logic is divided into separate functions, such as `get_total` and `get_by_category`. Each function has a specific responsibility and can be reused with different input data. The code still uses imperative logic internally, but it is organised into procedures.

## Snippet 3
**Paradigm**: Imperative programming with a functional element

**Explanation**: This snippet is mostly imperative because it builds the `totals` dictionary by using a loop and changing its state over time. The dictionary is updated step by step as each expense is processed. However, the use of `lambda` inside the `max()` function introduces a small functional-style element.

## Snippet 4
**Paradigm**: Functional programming elements

**Explanation**: This snippet uses functional-style tools such as `sum`, generator expressions, `map`, `filter`, and `lambda`. Instead of manually updating accumulator variables, the code describes transformations over collections of data. This makes the code closer to a functional programming style.
