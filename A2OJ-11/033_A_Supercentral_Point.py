"""
33 Supercentral Point - https://codeforces.com/problemset/problem/165/A
"""
l = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    l.append((x, y))
c = 0
for i in range(n):
    up, right, left, down = 0, 0, 0, 0
    for j in range(n):
        if i!=j:
            x1, y1 = l[i]
            x2, y2 = l[j]
            if x1 > x2 and y1==y2:
                up+=1
            elif y1 > y2 and x1==x2:
                right+=1
            elif x2 > x1 and y1==y2:
                down+=1
            elif y2 > y1 and x1 == x2:
                left += 1
    if up >= 1 and down >= 1 and right >= 1 and left >=1:
        c+=1
print(c)