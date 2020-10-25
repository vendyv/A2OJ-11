"""
99 Sereja and Bottles - https://codeforces.com/problemset/problem/315/A
"""
n = int(input())
l = []
# x, y = list(), list()
for i in range(n):
    l.append(list(map(int, input().split())))

c = 0
for i in range(n):
    flag = False
    for j in range(n):
        if l[i][0] == l [j][1] and i != j:
            flag = True
            break
    
    if not flag:
        c += 1

print(c)