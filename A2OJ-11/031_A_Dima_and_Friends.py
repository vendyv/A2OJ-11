"""
31 Dima and Friends - https://codeforces.com/problemset/problem/272/A
"""
n = int(input())
total = sum([int(i) for i in input().split()])
c = 0
for i in range(1, 6):
    if (total+i) %(n+1) != 1:
        c += 1
print(c)