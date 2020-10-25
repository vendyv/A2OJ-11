"""
61 Pashmak and Flowers - https://codeforces.com/problemset/problem/459/B
"""
n = int(input())
import math
l = list(map(int, input().split()))
if max(l) != min(l):
    print(max(l)-min(l), l.count(max(l)) * l.count(min(l)))
else:
    print("0", n*(n-1)//2)