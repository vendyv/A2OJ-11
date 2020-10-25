"""
50 k-String - https://codeforces.com/problemset/problem/219/A
"""
k = int(input())
string = input()
from collections import Counter
letters = Counter()
for s in string:
    letters[s] += 1
# print(dict(letters))
for keys in letters:
    if letters[keys] % k != 0:
        print("-1")
        exit(0)
b = ""
for keys in letters:
    b = b + keys*(letters[keys]//k)
print(b*k)