"""
42 Magic Numbers - https://codeforces.com/problemset/problem/320/A
"""
# from itertools import groupby
n = list(map(int, input()))
# print(n)
flag = True
if len(n) == 1:
    if n[0] != 1:
        flag = False
elif n[0] != 1:
    flag = False
elif n[1] in [2,3,5,6,7,8,9,0]:
    flag = False
elif len(n) > 2:
    for i in range(2, len(n)):
        if n[i] == 4 and n[i-1] == 4 and n[i-2] == 4:
            flag = False
            break
        elif n[i] in [2,3,5,6,7,8,9,0]:
            flag = False
            break
if flag:
    print("YES")
else:
    print("NO")