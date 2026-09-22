# Linear Search in Python

This folder contains my implementation of **linear search** and three practice problems that use the same idea: examine array elements one at a time.

## Files

| File | Purpose |
| --- | --- |
| [00_linear_search.py](00_linear_search.py) | Return the index of the first occurrence of a target |
| [01_find_all_occurrences.py](01_find_all_occurrences.py) | Find every index where a target appears |
| [02_count_comparisons.py](02_count_comparisons.py) | Count comparisons until the target is found |
| [03_find_max_element.py](03_find_max_element.py) | Find the largest element using a linear scan |

## What Is Linear Search?

Linear search, also called **sequential search**, checks each element from the beginning until it finds the target or reaches the end.

- It works on both sorted and unsorted arrays.
- It does not require sorting or extra preprocessing.
- A basic search returns the **first matching index**, even if the target appears multiple times.
- Python uses **zero-based indexing**: the first element is at index `0`.
- This implementation returns `-1` when the target is absent.

The examples use `array.array('i', ...)`, which stores signed integers. These functions also work with Python lists containing suitable values.

## Algorithm

1. Start at index `0`.
2. Compare the current element with the target.
3. If they are equal, return the current index immediately.
4. Otherwise, move to the next element.
5. If the entire array has been checked without a match, return `-1`.

### Pseudocode

```text
LINEAR_SEARCH(array, target)
    for each index i from 0 to length(array) - 1
        if array[i] equals target
            return i
    return -1
```

### My Python Implementation

From [00_linear_search.py](00_linear_search.py):

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return -1
```

The `else` belongs to the `for` loop. Python runs a loop's `else` block when the loop finishes normally without a `break`. Here, finding a match exits the entire function with `return`, so the `else` is reached only when no match is found. Placing `return -1` after the loop without an `else` would also work.

### Dry Run

```python
arr = [20, 98, 74, 65, 82, 74]
target = 65
```

| Comparison | Index | Element | Matches `65`? |
| --- | --- | --- | --- |
| 1 | 0 | 20 | No |
| 2 | 1 | 98 | No |
| 3 | 2 | 74 | No |
| 4 | 3 | 65 | Yes: return `3` |

The search stops after **4 comparisons**. The result is index `3`, not position `4` or value `65`.

### Why It Works

Before checking index `i`, every earlier element has already been checked and does not match the target. Therefore, a match at `i` is the first occurrence. If the loop finishes, every element has been checked, so the target is absent.

## Time and Space Complexity

Let `n` be the number of elements. Assume indexing and comparing integer values take constant time.

| Case | Target comparisons | Time |
| --- | --- | --- |
| Best case | `1`, when the target is first | `O(1)` |
| Average successful search | `(n + 1) / 2`, assuming each position is equally likely | `O(n)` |
| Worst case | `n`, when the target is last or absent | `O(n)` |

**Auxiliary space: `O(1)`**. The basic search only needs an index and uses no additional collection that grows with the input.

An empty array requires zero element comparisons and returns `-1`.

## Practice Question 1: Find All Occurrences

**Problem:** Return every index where the target appears.

**Solution:** [01_find_all_occurrences.py](01_find_all_occurrences.py) — `get_trg_indx_lst(arr, target)`.

```python
arr = [20, 74, 98, 74, 65, 74]
target = 74

# Result: [1, 3, 5]
```

### Approach

1. Create an empty integer array to store matching indices.
2. Check every element against the target.
3. Append the index whenever there is a match.
4. Convert the collected indices to a Python list with `.tolist()` and return it.
5. If no matches exist, return `-1`.

Unlike basic linear search, this solution **cannot stop at the first match**, because more matches may appear later.

**Current return behavior:** A list of indices when found, or `-1` when absent, including for an empty input. Returning an empty list instead is another possible design, but the current code uses `-1`.

**Complexity:** `O(n)` time for the full scan and `O(k)` additional space for `k` matching indices, up to `O(n)` in the worst case. Converting to a list also takes `O(k)` time and temporarily stores both collections; the overall bounds remain `O(n)` time and `O(k)` additional space.

**Key learning:** Move `return` outside the loop when the task requires collecting all matches.

## Practice Question 2: Count Comparisons

**Problem:** Count how many element-to-target comparisons occur before finding the target.

**Solution:** [02_count_comparisons.py](02_count_comparisons.py) — `count_comp(arr, target)`.

```python
arr = [20, 98, 74, 65, 82, 74]
target = 65
```

Printed output:

```text
index : 3
Comparisons : 4
```

### Approach

1. Initialize `count_comparisons` to `0`.
2. Increment it immediately before each target comparison.
3. When a match is found, return a formatted string containing the index and count.
4. If the target is absent, return `-1`.

For a first match at index `i`, the number of comparisons is **`i + 1`**. This count includes only checks of `arr[i] == target`, not loop-control operations.

**Current return behavior:** The function returns a string on success. If the target is absent, it performs `n` target comparisons internally but returns only `-1`, so that count is not included in the result. Empty input also returns `-1` after zero comparisons.

**Complexity:** Best-case time `O(1)`, average and worst-case time `O(n)`, and `O(1)` auxiliary space under the usual fixed-size integer model, excluding the returned formatted text.

**Key learning:** An index and a comparison count differ because indexing starts at zero while counting starts at one.

## Practice Question 3: Find the Maximum Element

**Problem:** Find the largest element without using Python's built-in `max()` function.

**Solution:** [03_find_max_element.py](03_find_max_element.py) — `find_max(arr)`.

The executable example in the file uses:

```python
arr = [20, 98, 74, 65, 182, 74]

# Result: 182
```

The problem comment in the script uses `82` instead of `182`; that different input would have maximum `98`.

### Approach

1. Set `max_ele` to the first element, `arr[0]`.
2. Scan from index `1` onward.
3. If the current element is greater than `max_ele`, update `max_ele`.
4. Return `max_ele` after checking all elements.

| Current element | Maximum after checking it |
| --- | --- |
| 20 | 20 (initial value) |
| 98 | 98 |
| 74 | 98 |
| 65 | 98 |
| 182 | 182 |
| 74 | 182 |

After each step, `max_ele` is the largest value seen so far. After the complete scan, it is the largest value in the array.

Initializing from `arr[0]`, rather than `0`, also makes the algorithm work for entirely negative input. For example, `[-8, -3, -10]` returns `-3`.

**Current input requirement:** The array must be nonempty. An empty array raises `IndexError` at `arr[0]`. A single-element array returns that element without any maximum comparisons.

**Complexity:** Exactly `n - 1` value comparisons for nonempty input, `O(n)` time in all cases as input size grows, and `O(1)` auxiliary space.

**Key learning:** Finding a maximum uses a linear scan, but it is not a search for a supplied target. Every element must be considered.

## Edge Cases to Remember

| Situation | Basic search | All occurrences | Count comparisons | Maximum |
| --- | --- | --- | --- | --- |
| Empty input | `-1` | `-1` | `-1` | Raises `IndexError` |
| Target absent | `-1` | `-1` | `-1`; count is not returned | Not applicable |
| Repeated target | First matching index | All matching indices | Stops at first match | Repeated maximum does not change the result |
| Single element | `0` if matched, otherwise `-1` | `[0]` if matched, otherwise `-1` | One comparison; success string or `-1` | Returns the element |
| Negative values | Supported | Supported | Supported | Supported |

Do not use a returned `-1` as an array index without checking it: in Python, `arr[-1]` accesses the last element.

## When to Use Linear Search

- The data is unsorted.
- The collection is small or only needs an occasional search.
- You need all matches or must inspect every element, such as when finding a maximum.
- You want a simple baseline before considering more complex approaches.

For large collections with many repeated searches, another data structure or algorithm may be more suitable.

### Linear Search vs. Binary Search

| Property | Linear search | Binary search on an array |
| --- | --- | --- |
| Input requirement | Sorted or unsorted | Must be sorted |
| Method | Check elements sequentially | Repeatedly halve the search interval |
| Worst-case search time | `O(n)` | `O(log n)` |
| Iterative auxiliary space | `O(1)` | `O(1)` |

Sorting solely for one search generally costs more than a single linear scan: comparison-based sorting typically takes `O(n log n)` time. Binary search becomes useful when the data is already sorted or the sorting cost can be shared across many searches. Finding all matches also requires time to produce those results.

## Run the Examples

From this folder, run:

```powershell
python 00_linear_search.py
python 01_find_all_occurrences.py
python 02_count_comparisons.py
python 03_find_max_element.py
```

Expected outputs, in the same order:

```text
3
[1, 3, 5]
index : 3
Comparisons : 4
182
```

No third-party packages are required; `array` is part of Python's standard library.

## What I Learned

- Traverse an array using indices.
- Return early when only the first match is needed.
- Complete the scan when collecting all matches or finding a maximum.
- Count element comparisons and relate them to time complexity.
- Distinguish constant auxiliary space from space used to collect results.
- Check empty input, duplicate values, missing targets, and negative numbers.
