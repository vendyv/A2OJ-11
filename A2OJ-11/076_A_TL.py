"""
76 TL - https://codeforces.com/problemset/problem/350/A
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
v = min(a)
p = max(a)
c = min(b)
if max(2*v, p) < c:
    print(max(2*v, p))
else:
    print("-1")