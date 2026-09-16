# ============================================================
# BIG-O PRACTICE
# ============================================================


# ------------------------------------------------------------
# Problem 1
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [10, 20, 30, 40, 50]

for i in L:
    print(i)

# Time Complexity = O(n)
# Space Complexity = O(1)


# ------------------------------------------------------------
# Problem 2
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

for i in L:
    print(i)

for j in L:
    print(j)

# Time Complexity = O(n)
# Space Complexity = O(1)


# ------------------------------------------------------------
# Problem 3
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

for i in L:
    for j in L:
        print(i, j)

# Time Complexity = O(n**2)
# Space Complexity = O(1)


# ------------------------------------------------------------
# Problem 4
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

print(L[0])

# Time Complexity = O(1)
# Space Complexity = O(1)


# ------------------------------------------------------------
# Problem 5
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

total = 0

for i in L:
    total += i

# Time Complexity = O(n)
# Space Complexity = O(1)


# ------------------------------------------------------------
# Problem 6
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

new_L = []

for i in L:
    new_L.append(i * 2)

# Time Complexity = O(n)
# Space Complexity = O(n)


# ------------------------------------------------------------
# Problem 7
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

for i in range(len(L)):
    for j in range(2):
        print(L[i], j)

# Time Complexity = O(n)
# Space Complexity = O(1)


# ------------------------------------------------------------
# Problem 8
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

i = 1

while i < len(L):
    print(L[i])
    i = i * 2

# Time Complexity = O(log n)
# Space Complexity = O(1)


# ------------------------------------------------------------
# Problem 9
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

i = len(L)

while i > 0:
    print(i)
    i = i // 2

# Time Complexity = O(log n)
# Space Complexity = O(1)


# ------------------------------------------------------------
# Problem 10
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

for i in L:
    print(i)

    for j in L:
        print(j)

# Time Complexity = O(n**2)
# Space Complexity = O(1)


# ------------------------------------------------------------
# Problem 11
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

result = []

for i in L:
    if i % 2 == 0:
        result.append(i)

# Time Complexity = O(n)
# Space Complexity = O(n)


# ------------------------------------------------------------
# Problem 12
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

for i in range(len(L)):
    print(L[i])

for i in range(len(L)):
    print(L[i] * 2)

for i in range(len(L)):
    print(L[i] * 3)

# Time Complexity = O(n)
# Space Complexity = O(1)


# ------------------------------------------------------------
# Problem 13
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

sum = 0
for i in L :
    sum = sum + i
print(sum)

product = 1
for i in L:
    product = product * i
print(product)

# Time Complexity = O(n)
# Space Complexity = O(1)


# ------------------------------------------------------------
# Problem 14
# ------------------------------------------------------------
# Find the Time and Space Complexity.

L = [1, 2, 3, 4, 5]

for i in L:
    for j in L:
        print(f"{i},{j}")

# Time Complexity = O(n**2)
# Space Complexity = O(1)



