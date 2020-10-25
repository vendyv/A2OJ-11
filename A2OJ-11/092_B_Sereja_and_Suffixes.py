"""
92 Sereja and Suffixes - https://codeforces.com/problemset/problem/368/B
"""
n, m = map(int, input().split())
l = list(map(int, input().split()))
ans = [0]*n
count = 0
d = {}
for i in range(n-1, -1, -1):
    if l[i] not in d:
        count += 1
        d[l[i]] = 1
    ans[i] = count
for i in range(m):
    print(ans[int(input())-1])