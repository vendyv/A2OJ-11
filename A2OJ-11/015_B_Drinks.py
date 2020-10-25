"""
15 Drinks - https://codeforces.com/problemset/problem/200/B
"""
n = int(input())
props = sum(list(map(int, input().split())))
print(props/(n))
