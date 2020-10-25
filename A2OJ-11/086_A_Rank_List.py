"""
86 Rank List - https://codeforces.com/problemset/problem/166/A
"""
n, k = map(int, input().split())
l = [0]*n
for i in range(n):
    x, y = map(int, input().split())
    l[i] = 100*x - y
    # l.append([x,y])
    # l[0].append(x)
    # l[1].append(y)
l.sort(reverse=True)
# l = sorted(l, key=lambda x: x[0], reverse= True)
print(l.count(l[k-1]))