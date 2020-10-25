"""
4 Borze - https://codeforces.com/problemset/problem/32/B
"""
pattern = list(input())
s = ""
i = 0
while i < len(pattern):
    if pattern[i] == ".":
        s += "0"
    elif pattern[i] == "-":
        if pattern[i+1] == "-":
            s += "2"
            i += 1
        elif pattern[i+1] == ".":
            s += "1"
            i += 1
    i += 1
print(s)
