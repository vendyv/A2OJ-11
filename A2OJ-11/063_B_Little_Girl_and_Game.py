"""
63 Little Girl and Game - https://codeforces.com/problemset/problem/276/B
"""
string = input()
f = True
i = 0 # if i even, first else second
from collections import Counter
c = Counter()
for s in string:
    c[s] += 1
l = len(list(filter(lambda x: x[1]%2 != 0, c.items())))
if l <= 1 or l%2 != 0:
    print("First")
else:
    print("Second")