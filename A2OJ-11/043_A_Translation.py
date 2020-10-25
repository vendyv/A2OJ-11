"""
43 Translation - https://codeforces.com/problemset/problem/41/A
"""
s = input()
s_r = input()
if s_r[::-1] == s:
    print("YES")
else:
    print("NO")