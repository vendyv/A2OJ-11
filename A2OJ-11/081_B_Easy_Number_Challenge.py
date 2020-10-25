"""
81 Easy Number Challenge - https://codeforces.com/problemset/problem/236/B
"""

a, b, c = map(int, input().split())

limit = a*b*c + 1
d = [1] * limit
for i in range(2, limit):
    for j in range(i, limit, i):
        d[j] += 1

answer = 0
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            answer += d[i*j*k]

print(answer % 1073741824)