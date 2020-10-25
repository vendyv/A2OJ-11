"""
36 Reconnaisance 2 - https://codeforces.com/problemset/problem/34/A
"""
n = int(input())
l = list(map(int, input().split()))
d = []
d.append(abs(l[0] - l[-1])) 
for i in range(1, len(l)):
    d.append(abs(l[i] - l[i-1]))
m = d.index(min(d))
if m == 0:
    print(1, n)
else:
    print(m, m+1)