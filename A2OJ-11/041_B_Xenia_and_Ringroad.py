"""
41 Xenia and Ringroad - https://codeforces.com/problemset/problem/339/B
"""
t = 0
n, m = map(int, input().split())
l = list(map(int, input().split()))
t += l[0] - 1
for i in range(1, len(l)):
    if l[i-1] <= l[i]:
        t += l[i] - l[i-1]
    else:
        t += n - l[i-1] + l[i]
print(t)