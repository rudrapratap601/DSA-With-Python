"""
Given two integer arrays, nums1 of size N and nums2 of size M, determine how many times each element in nums2 appears in nums1. Print (or return) each element from nums2 alongside its frequency in nums1 in the order they appear in nums2

Input - 

nums1 = [98, 7, 87, 2, 7, 87, 2, 5, 2, 87, 6, 1, 5, 4, 5, 5]
nums2 = [7, 87, 1, 5, 4, 98]

Output -

7 -> 2
87 -> 3
1 -> 1
5 -> 4
4 -> 1
98 -> 1

"""

nums1 = [98, 7, 87, 2, 7, 87, 2, 5, 2, 87, 6, 1, 5, 4, 5, 5]
nums2 = [7, 87, 1, 5, 4, 98]

hash_map = {}

for i in nums1:
    hash_map[i] = hash_map.get(i, 0) + 1

for j in nums2:
    print(f"{j} -> {hash_map.get(j, 0)}")