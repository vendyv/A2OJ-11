"""
35 Parallelopiped - https://codeforces.com/problemset/problem/224/A
"""
a1, a2, a3 = map(int, input().split())
import math
x = math.sqrt(a1 * a3 / a2)
y = a1/x
z = a3/x

print(int(4*(x + y + z)))