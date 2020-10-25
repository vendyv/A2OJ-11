"""
10 Stones on the Table - https://codeforces.com/problemset/problem/266/A
"""
num = int(input())
colors = list(input())
a = 0
for i in range(1, num):
    if colors[i] == colors[i-1]:
        a += 1
print(a)