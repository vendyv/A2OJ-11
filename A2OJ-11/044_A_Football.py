"""
44 Football - https://codeforces.com/problemset/problem/43/A
"""
from collections import Counter
n = int(input())
l = Counter()
for _ in range(n):
    x = input()
    l[x] += 1
    
    # if l[x] is not None:
    #     l[x] += 1
    # else:
    #     l[x] = 1

print(max(l, key=l.get))