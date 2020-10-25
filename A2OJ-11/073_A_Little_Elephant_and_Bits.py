"""
73 Little Elephant and Bits - https://codeforces.com/problemset/problem/258/A
"""
n = input()
for i in range(len(n)):
    if n[i] == '0':
        break
print(n[:i] + n[i+1:])