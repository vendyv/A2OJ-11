"""
27 Petya and Strings - https://codeforces.com/problemset/problem/112/A
"""
one = input().lower()
two = input().lower()
if one < two:
    print("-1")
elif one > two:
    print("1")
else:
    print("0")