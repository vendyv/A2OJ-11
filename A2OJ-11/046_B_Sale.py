"""
46 Sale - https://codeforces.com/problemset/problem/34/B
"""
n, m = map(int, input().split())
prices = sorted(list(map(int, filter(lambda x: int(x) <= 0, input().split()))))
prices = prices[:m]
print(-sum(prices))