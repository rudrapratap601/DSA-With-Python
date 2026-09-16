# Big-O Time & Space Complexity

Big-O notation is used to describe how the **time or memory requirements of an algorithm grow as the input size increases**.

It helps us compare algorithms and understand which solution will scale better for large inputs.

---

## 1. Why Big-O Matters

Suppose we have two solutions that solve the same problem.

- Solution A takes 1 second for 1,000 inputs.
- Solution B takes 10 seconds for 1,000 inputs.

For small inputs, both may work fine.

But as the input grows, the difference can become very large.

Big-O helps us understand this growth without depending on a specific computer or exact execution time.

---

# 2. Time Complexity

**Time Complexity** describes how the number of operations performed by an algorithm grows with the input size `n`.

Common complexities:

| Complexity | Name | Example |
|---|---|---|
| `O(1)` | Constant | Accessing a list element |
| `O(log n)` | Logarithmic | Binary Search |
| `O(n)` | Linear | Traversing a list |
| `O(n log n)` | Linearithmic | Efficient sorting algorithms |
| `O(n²)` | Quadratic | Nested loops |
| `O(2ⁿ)` | Exponential | Some recursive problems |

---

# 3. O(1) — Constant Time

The number of operations does not depend on the size of the input.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])

 ```
Whether the list contains 5 elements or 5 million elements, accessing an element by index takes constant time.

**Time Complexity**

``` 
O(1)

```
# 4. O(n) — Linear Time

The number of operations grows proportionally with the input size.

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)

```

If the input contains n elements, the loop runs approximately n times.

**Time Complexity**
```
O(n)

```

**Example**

``` 
n = 5       → 5 operations
n = 100     → 100 operations
n = 10,000  → 10,000 operations

```

# 5. O(n²) — Quadratic Time

Usually occurs when we have a loop inside another loop.

```
numbers = [1, 2, 3, 4, 5]

for i in numbers:
    for j in numbers:
        print(i, j)
```

For every element, we iterate through all elements again.

If there are ```n``` elements:

`n × n = n²`

**Time Complexity**
```O(n²)```

Nested loops do not automatically mean O(n²), but when both loops depend on the same input size, it commonly results in O(n²).

# 6. O(log n) — Logarithmic Time

In a logarithmic algorithm, the problem size is reduced significantly at each step.

A classic example is Binary Search.

For a sorted list, binary search repeatedly divides the search space in half.

```
100 elements
    ↓
50
    ↓
25
    ↓
12
    ↓
6
    ↓
3
    ↓
1
```

**Time Complexity**
```
O(log n)
```

This is much more efficient than checking every element one by one for large inputs.

# 7. O(n log n) — Linearithmic Time

This commonly appears in efficient sorting algorithms such as:

- Merge Sort
- Heap Sort
- Average-case Quick Sort

A common pattern is:

```
Divide the problem → O(log n)
Process elements → O(n)
```

Therefore:

```
O(n log n)
```
# 8. O(2ⁿ) — Exponential Time

The number of operations can roughly double as the input increases.

This commonly appears in some recursive solutions, especially when a problem branches into multiple recursive calls.

Example:

```python
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```

The naive recursive Fibonacci solution has exponential time complexity.

**Time Complexity**
```
O(2ⁿ)
```

Such algorithms become impractical very quickly as n increases.

# 9. Space Complexity

Space Complexity describes how much additional memory an algorithm requires as the input size grows.

For example:

```python
numbers = []

for i in range(n):
    numbers.append(i)
```

The additional list grows with `n`.

**Space Complexity**
```
O(n)
```

### O(1) Space

If an algorithm uses only a fixed number of variables:

```python
total = 0

for number in numbers:
    total += number
```

The input may contain millions of elements, but we only use a few extra variables.

**Space Complexity**
```
O(1)
```

# 10. Drop Constants

Big-O focuses on the growth rate, so constants are ignored.

For example:

```python
for i in range(n):
    print(i)

for i in range(n):
    print(i)
```

This performs approximately:
```
2n operations
```
But we write:
```
O(n)
```
not:
```
O(2n)
```

# 11. Drop Lower-Order Terms

Suppose an algorithm performs:
```
n² + n + 10 operations
```

As `n` becomes very large, the `n²` term dominates.

Therefore:
```
O(n² + n + 10)
```
becomes:
```
O(n²)
```

# 12. Multiple Parts of an Algorithm

Consider:

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

The first loop is:
```
O(n)
```

The second loop is:
```
O(n)
```

Together:
```
O(n) + O(n)
= O(2n)
= O(n)
```

So the overall complexity is:
```
O(n)
```

# 13. Nested Loops

Consider:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The outer loop runs `n` times.

For every outer iteration, the inner loop also runs `n` times.

Therefore:
```
n × n = n²
```

#### Time Complexity
```
O(n²)
```

# 14. Complexity Hierarchy

From generally more scalable to less scalable:
```
O(1)
   ↓
O(log n)
   ↓
O(n)
   ↓
O(n log n)
   ↓
O(n²)
   ↓
O(2ⁿ)
```

As input size increases, algorithms with faster-growing complexity become increasingly expensive.

---

# 15. Best, Average and Worst Case

An algorithm can behave differently depending on the input.

**Best Case**

The most favorable input.

**Average Case**

Typical expected behavior across inputs.

**Worst Case**

The least favorable input.

When discussing Big-O, we commonly focus on the worst-case growth unless otherwise specified.

---

# 16. Important Python Operations

Understanding the complexity of Python's built-in data structures is important for DSA.

**List**
```python
numbers[index]
```

Access by index:
```
O(1)
```

Searching for a value:
```
x in numbers
```

Generally:
```
O(n)
```

Appending to the end:
```
numbers.append(x)
```

Amortized:
```
O(1)
```

**Dictionary**
```
student["name"]
```
Average-case lookup:
```
O(1)
```
**Set**
```
x in my_set
```

Average-case membership checking:
```
O(1)
```
---

# 17. Key Takeaways
- Big-O describes how an algorithm scales with input size.
- It does not represent exact execution time.
- Constants are ignored.
- Lower-order terms are ignored.
- O(1) is constant time.
- O(log n) is logarithmic.
- O(n) is linear.
- O(n log n) is common in efficient sorting.
- O(n²) commonly appears with nested loops.
- O(2ⁿ) grows extremely quickly.
- Space complexity measures additional memory usage.
- Understanding complexity helps us choose between different solutions.

---

# 🧠 Problem-Solving Habit

For every DSA problem, I should ask:

```
1. What is my approach?
        ↓
2. How many times does each operation run?
        ↓
3. What is the Time Complexity?
        ↓
4. How much extra memory am I using?
        ↓
5. What is the Space Complexity?
        ↓
6. Can I optimize the solution?
```