"""
95 Polo the Penguin and Matrix - https://codeforces.com/problemset/problem/289/B
"""
n, m, d = map(int, input().split())
arr = []
for _ in range(n):
    arr.extend(list(map(int, input().split())))
arr.sort()

size = n * m
median = arr[size//2]
arr = [abs(i - median) for i in arr]
s = sum(arr)
if s % d == 0:
    print (s // d)
else:
    print("-1")