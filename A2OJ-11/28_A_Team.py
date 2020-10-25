"""
28 Team - https://codeforces.com/problemset/problem/231/A
"""
number = int(input())
c = 0
for n in range(number):
    if (input().split().count("1") > 1):
        c += 1
print(c)