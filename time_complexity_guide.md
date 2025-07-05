# How to Find the Time Complexity of a Program

Time complexity is a measure of how long a program takes to run as a function of the length of its input. It's a way to describe the efficiency of an algorithm. We usually use Big O notation to express time complexity.

## Big O Notation

Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. In computer science, it is used to classify algorithms according to how their run time or space requirements grow as the input size grows.

Here are some common time complexities, from fastest to slowest:

*   **O(1) - Constant Time:** The running time is constant and does not depend on the input size.
    *   *Example:* Accessing an element in an array by its index.
*   **O(log n) - Logarithmic Time:** The running time grows logarithmically with the input size. This is very efficient.
    *   *Example:* Binary search in a sorted array.
*   **O(n) - Linear Time:** The running time is directly proportional to the input size.
    *   *Example:* Iterating through all elements in an array.
*   **O(n log n) - Linearithmic Time:** The running time is a product of linear and logarithmic time.
    *   *Example:* Efficient sorting algorithms like Merge Sort or Quick Sort.
*   **O(n^2) - Quadratic Time:** The running time is proportional to the square of the input size. This is common with nested loops.
    *   *Example:* Comparing each element of a list to every other element (e.g., Bubble Sort).
*   **O(2^n) - Exponential Time:** The running time doubles with each addition to the input data set. This is very slow.
    *   *Example:* Recursive calculation of Fibonacci numbers without memoization.
*   **O(n!) - Factorial Time:** The running time grows factorially with the input size. This is extremely slow and impractical for even small `n`.
    *   *Example:* Traveling salesman problem solved with a brute-force approach.

## How to Analyze Your Code

To find the time complexity of your program, you can follow these steps:

1.  **Identify the basic operations:** These are the simplest operations in your code, like assignments, comparisons, and arithmetic operations. We assume these take constant time, O(1).

2.  **Analyze loops:**
    *   A single loop that iterates `n` times is O(n).
    *   Nested loops are multiplied. A loop inside another loop that both run `n` times will be O(n * n) = O(n^2).
    *   If a loop's control variable is divided or multiplied by a constant factor in each iteration, it's logarithmic, O(log n).

3.  **Analyze sequential statements:** If you have multiple statements in a row, you add their time complexities. The largest one will dominate.
    *   *Example:* An O(n) loop followed by an O(n^2) loop is O(n + n^2), which simplifies to O(n^2).

4.  **Analyze conditional statements (if/else):** The time complexity is the complexity of the condition plus the complexity of the more expensive branch.
    *   *Example:* `if (condition) { ...O(n)... } else { ...O(1)... }` would be O(n).

5.  **Analyze recursive functions:** For recursive functions, you need to determine the recurrence relation.
    *   *Example:* A function that calls itself once on an input of size `n-1` will likely be O(n). A function that calls itself twice on an input of size `n/2` could be O(n log n).

## Example Analysis

Let's analyze a simple Python function:

```python
def find_sum_and_product(numbers):
    total_sum = 0  # O(1)
    for number in numbers:  # Loop runs n times
        total_sum += number  # O(1)

    product = 1  # O(1)
    for number in numbers:  # Loop runs n times
        product *= number  # O(1)

    return total_sum, product
```

*   The first loop is O(n).
*   The second loop is also O(n).
*   The total time complexity is O(n) + O(n) = O(2n).
*   In Big O notation, we drop the constants, so the final complexity is **O(n)**.

Let's look at another one:

```python
def print_pairs(numbers):
    for i in numbers:  # Outer loop runs n times
        for j in numbers:  # Inner loop runs n times
            print(i, j) # O(1)
```

*   The outer loop runs `n` times.
*   The inner loop runs `n` times for *each* iteration of the outer loop.
*   Total operations: n * n = n^2.
*   The time complexity is **O(n^2)**.
