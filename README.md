# 🧠 DSA with Python

Welcome to my **Data Structures & Algorithms (DSA) journey using Python**.

This repository documents my progress as I learn, practice, and improve my problem-solving and algorithmic thinking skills.

My goal is not just to solve problems, but to understand **why a solution works, how efficient it is, and how it can be improved**.

---

## 🎯 Goal

Build strong foundations in:

- Data Structures
- Algorithms
- Problem Solving
- Time & Space Complexity
- Algorithmic Thinking
- Optimization

I will primarily use **Python** throughout this journey.

---

## 🐍 Why Python?

Python is my primary programming language and I already have a strong foundation in it.

Rather than learning another language for DSA, I want to focus my energy on:

> **Problem solving → Algorithms → Optimization → Complexity Analysis**

---

# 📚 DSA Roadmap

## Phase 1 — Foundations

- [x] Big-O Time & Space Complexity
- [ ] Arrays / Lists *(In Progress)*
- [ ] Sorting Algorithms *(In Progress)*
- [ ] Searching Algorithms *(In Progress)*
- [ ] Strings
- [ ] Hashing *(In Progress)*
- [ ] Sets
- [ ] Dictionaries *(In Progress)*
- [ ] Two Pointers
- [ ] Sliding Window
- [ ] Prefix Sum

## Phase 2 — Core Data Structures

- [ ] Linked Lists *(In Progress)*
- [ ] Stacks
- [ ] Queues
- [ ] Deques
- [ ] Recursion
- [ ] Binary Search *(In Progress)*

## Phase 3 — Trees

- [ ] Binary Trees
- [ ] Tree Traversals
- [ ] DFS
- [ ] BFS
- [ ] Binary Search Trees
- [ ] Heaps
- [ ] Priority Queues

## Phase 4 — Graphs

- [ ] Graph Representation
- [ ] BFS
- [ ] DFS
- [ ] Connected Components
- [ ] Shortest Path
- [ ] Topological Sorting

## Phase 5 — Advanced Algorithms

- [ ] Greedy Algorithms
- [ ] Backtracking
- [ ] Dynamic Programming
- [ ] Advanced Graph Algorithms

---

# 🧩 Problem-Solving Strategy

For every problem, I will try to follow this process:

```text
Understand the Problem
        ↓
Identify the Pattern
        ↓
Think of Brute Force
        ↓
Analyze Time & Space Complexity
        ↓
Find an Optimization
        ↓
Implement in Python
        ↓
Test the Solution
        ↓
Review & Learn
```

The goal is to **understand the solution**, not simply get an accepted submission.

---

# 📊 Complexity

I will track the complexity of my solutions using:

### Time Complexity

How the running time of an algorithm grows as the input size increases.

Examples:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(2ⁿ)
O(n!)
```

### Space Complexity

How much additional memory an algorithm requires as the input grows.

---

# 📈 Progress Tracker

| Topic               | Status         | Problems Solved |
| ------------------- | -------------- | --------------: |
| Big-O               | ✅ Completed   |              14 |
| Arrays              | 🚀 Started     |               4 |
| Sorting             | 🚀 Started     |               2 |
| Strings             | ⬜ Not Started |               0 |
| Hashing             | 🚀 Started     |               2 |
| Two Pointers        | ⬜ Not Started |               0 |
| Sliding Window      | ⬜ Not Started |               0 |
| Linked Lists        | 🚀 Started     |               3 |
| Stacks              | ⬜ Not Started |               0 |
| Queues              | ⬜ Not Started |               0 |
| Recursion           | ⬜ Not Started |               0 |
| Binary Search       | 🚀 Started     |               1 |
| Trees               | ⬜ Not Started |               0 |
| Heaps               | ⬜ Not Started |               0 |
| Graphs              | ⬜ Not Started |               0 |
| Greedy              | ⬜ Not Started |               0 |
| Backtracking        | ⬜ Not Started |               0 |
| Dynamic Programming | ⬜ Not Started |               0 |
| **Total**           | **🔥 Active**  |          **26** |

---

# 🗂️ Repository Structure & Contents

```text
DSA-With_Python/
├── Big_O/
│   ├── note.md                                    # Comprehensive Big-O notes & complexity guide
│   └── practice.py                                # 14 complexity practice problems with solutions
├── Arrays/
│   ├── Searching_Algos/
│   │   ├── 01_Linear_Search_Algo/
│   │   │   ├── 00_linear_search.py                # Linear Search implementation
│   │   │   ├── 01_find_all_occurrences.py         # Practice 1: Find all indices of target
│   │   │   ├── 02_count_comparisons.py            # Practice 2: Count comparison operations
│   │   │   ├── 03_find_max_element.py             # Practice 3: Find maximum element without max()
│   │   │   └── README.md                          # Detailed Linear Search notes & dry runs
│   │   └── 02_Binary_Search_Algo/
│   │       └── 00_binary_search.py                # Binary Search on sorted array + complexity
│   └── Sorting_Algos/
│       ├── bubble_sort.py                         # Bubble Sort (with early-stopping optimization)
│       ├── selection_sort.py                      # Selection Sort implementation
│       └── insertion_sort.py                      # Insertion Sort (work in progress)
├── Hashing/
│   ├── character_frequency_queries.py             # Character frequency queries using array hashing
│   └── query_frequency_of_elements.py             # Element frequency queries using dictionary hashing
└── Linked_List/
    └── linked_list.py                             # Singly Linked List: Traversal, Length, Sum of nodes
```

### 📌 Current Highlights & Implemented Topics

- **[Big-O Analysis](Big_O/)**: Thorough exploration of asymptotic analysis ($O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$) with comprehensive theory notes ([note.md](Big_O/note.md)) and 14 solved practice problems ([practice.py](Big_O/practice.py)).
- **[Arrays & Searching](Arrays/Searching_Algos/)**:
  - **Linear Search**: Algorithm implementation and 3 practice problems covering multiple occurrences, counting comparison steps, and finding the maximum element ([Linear Search Guide](Arrays/Searching_Algos/01_Linear_Search_Algo/README.md)).
  - **Binary Search**: Logarithmic search ($O(\log n)$) on sorted collections with time & space complexity analysis ([00_binary_search.py](Arrays/Searching_Algos/02_Binary_Search_Algo/00_binary_search.py)).
- **[Sorting Algorithms](Arrays/Sorting_Algos/)**:
  - **Bubble Sort**: Optimized with early termination (`is_swap` flag) for $O(n)$ best-case, supporting ascending and descending orders ([bubble_sort.py](Arrays/Sorting_Algos/bubble_sort.py)).
  - **Selection Sort**: In-place minimum selection sort with $O(n^2)$ comparisons ([selection_sort.py](Arrays/Sorting_Algos/selection_sort.py)).
  - **Insertion Sort**: Implementation in progress ([insertion_sort.py](Arrays/Sorting_Algos/insertion_sort.py)).
- **[Hashing](Hashing/)**:
  - Fixed-size array hashing for lowercase English character frequency queries with $O(1)$ lookup ([character_frequency_queries.py](Hashing/character_frequency_queries.py)).
  - Dictionary / hash map based frequency counting for integer query lookups ([query_frequency_of_elements.py](Hashing/query_frequency_of_elements.py)).
- **[Linked Lists](Linked_List/)**:
  - Singly Linked List `Node` structure, manual chaining, pointer traversal (`print_ll`), node count calculation (`ll_length`), and node value summation (`sum_of_node`) ([linked_list.py](Linked_List/linked_list.py)).

---

# 📌 Rules for Myself

1. Don't memorize solutions blindly.
2. Always understand the problem before coding.
3. Try a solution independently before looking at hints.
4. Understand the time and space complexity.
5. Compare brute-force and optimized solutions.
6. Review mistakes instead of simply moving on.
7. Focus on consistency rather than solving hundreds of problems quickly.

---

# ⚙️ Process to Solve a Problem

1. Analyze the problem. (Think with respect to Input and Output)
2. Break down the problem into smaller sub problem.
3. Recall the concepts already know.
4. Take 2-3 examples
5. Write a Pseudocode on a paper.
6. Dry run it once.
7. Write down the solution (Code).
8. Look for the edge cases or boundary conditions.

---

# 🚀 Long-Term Goal

Become confident enough to solve unfamiliar algorithmic problems using structured reasoning and apply these skills to **software engineering, data science, machine learning, and analytics**.

> **Consistency > Intensity**

---

## 📅 Journey Started

**September 2026**

**Language:** Python 🐍

**Status:** 🚀 In Progress (26 Problems / Solutions)
