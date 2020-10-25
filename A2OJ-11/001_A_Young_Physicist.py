"""
1. Young Physicist - https://codeforces.com/problemset/problem/69/A
"""
x, y, z = 0, 0, 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    x += a
    y += b
    z += c
if x == y == z == 0:
    print("YES")
else:
    print("NO")
