"""
19 Tram - https://codeforces.com/problemset/problem/116/A
"""
n = int(input())
l = []
c = 0
for _ in range(n):
    # passengers.extend(list(map(int, input().split())))
    x, y = map(int, input().split())
    c += -x + y
    l.append(c)
print(max(l))