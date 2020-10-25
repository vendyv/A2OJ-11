"""
17 Cupboards - https://codeforces.com/problemset/problem/248/A
"""
n = int(input())
nL, nR = 0, 0
for _ in range(n):
    x, y = map(int, input().split())
    nL += x 
    nR += y
print(min(nL, n - nL) + min(nR, n - nR))
