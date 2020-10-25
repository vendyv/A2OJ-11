"""
72 Big Segment - https://codeforces.com/problemset/problem/242/B
"""
n = int(input())
l = []
a, b =10**9+1, 0
c, d =10**9+1, 0

for i in range(n):
    x, y = map(int, input().split())
    c = min(c, x)
    d = max(d, y)
    if x <= a and y >= b:
        a = x
        b = y
        index = i+1
    # d[x] = y
    # a = min(a, x)
    # b = max(b, y)
if c == a and d == b:
    print(index)
else:
    print("-1")