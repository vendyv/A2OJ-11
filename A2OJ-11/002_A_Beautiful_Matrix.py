"""
2 Beautiful Matrix - https://codeforces.com/problemset/problem/263/A
"""
l = []
for i in range(5):
    l.append(list(map(int, input().split())))
# print(l)
for i in range(len(l)):
    for j in range(len(l[0])):
        if l[i][j] == 1:
            x, y = i+1, j+1
            break
print(abs(x - 3) + abs(y - 3))
