"""
59 Airport - https://codeforces.com/problemset/problem/218/B
"""
n, m = map(int, input().split())
space = list(map(int, input().split()))

space_min = space.copy()
space_max = space.copy()
space_min.sort()

min = 0
i,c = 0,0
while c < n:
    min = min + space_min[i]
    space_min[i] = space_min[i] - 1
    c = c + 1
    if space_min[i] == 0:
        i += 1


# space_max.sort(reverse= True)
maxi = 0

while n > 0:
    space_max.sort()
    # print(space_max)
    maxi = maxi + space_max[-1]
    space_max[-1] -= 1
    n = n - 1

print(maxi, min)