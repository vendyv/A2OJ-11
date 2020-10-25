"""
77 Increase and Decrease - https://codeforces.com/problemset/problem/246/B
"""
n = int(input())
a = list(map(int, input().split()))
if sum(a) % n == 0:
    print(n)
else:
    print(n-1)