"""
Given a string s consisting only of lowercase English letters, and a list of character queries q, determine how many times each character in q appears in the string s. Print the frequency of each queried character in the order it appears in q.

Input:

s = "azyxyyzaaaa"

q = ["d", "a", "y", "x"]

Output:

d -> 0
a -> 5
y -> 3
x -> 1
"""

s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

hash_map = [0] * 26

for ch in s:
    ascii_val = ord(ch)
    indx = ascii_val - 97
    hash_map[indx] += 1

for ch in q:
    ascii_val = ord(ch)
    indx = ascii_val - 97
    print(f"{ch} -> {hash_map[indx]}")