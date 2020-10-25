"""
51 The number of positions - https://codeforces.com/problemset/problem/124/A
"""
n, a, b = map(int, input().split())
print(n-max(a+1, n-b)+1)