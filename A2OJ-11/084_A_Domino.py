"""
84 Domino - https://codeforces.com/problemset/problem/353/A
"""
n = int(input())
 
a = []
b = []
 
for i in range(n):
    x, y = list(map(int, input().strip().split()))
    a.append(x)
    b.append(y)
 
top_sum = sum(a)
bottom_sum = sum(b)
 
if top_sum%2 == 0 and bottom_sum%2 == 0:
    print(0)
elif top_sum%2 and bottom_sum%2:
    flag = False
    for i in range(n):
        if (a[i]%2) ^ (b[i]%2):
            print(1)
            flag = True
            break
    if not flag:
        print(-1)
else:
    print(-1)