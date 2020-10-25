"""
7 Word - https://codeforces.com/problemset/problem/59/A
"""
upper, lower = 0, 0
s = input()
for i in s:
    if i.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(s.upper())
else:
    print(s.lower())
