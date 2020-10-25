"""
60 DZY Loves Chessboard - https://codeforces.com/problemset/problem/445/A
"""
n,m=map(int,input().split())
j=0
for _ in range(n):
    a=list(input())
    j+=1
    for i in range(len(a)):
        if j%2==1 and i%2==0 and a[i]==".":
            a[i]="B"
        if j%2==0 and i%2==0 and a[i]==".":
            a[i]="W"
        if j%2==1 and i%2==1 and a[i]==".":
            a[i]="W"
        if j%2==0 and i%2==1 and a[i]==".":
            a[i]="B"
    print("".join(a))
