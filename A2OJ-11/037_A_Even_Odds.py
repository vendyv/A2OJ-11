"""
37 Even Odds - https://codeforces.com/problemset/problem/318/A
"""
import math
n, k = map(int, input().split())
c = math.ceil(n/2)
if k > c:
    print(2 * (k - c))
else:
    print(2 * k - 1)