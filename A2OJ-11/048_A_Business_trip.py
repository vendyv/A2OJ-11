"""
48 Business Trip - https://codeforces.com/problemset/problem/149/A
"""
k=int(input())
m=sorted(map(int,input().split()))[::-1]
for i in range(13):
    if sum(m[:i])>=k:
        print(i)
        exit(0)
print(-1)