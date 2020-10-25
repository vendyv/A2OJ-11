"""
85 Cinema Line - https://codeforces.com/problemset/problem/349/A
"""
c25,c50=0,0
n=int(input())
flag=0
for i in list(map(int,input().split())):
    if i==25:
        c25+=1
    elif i==50:
        if c25>0:
            c25-=1
            c50+=1
        else:
            flag=1
            break
    else:
        if c25>0 and c50>0:
            c25-=1
            c50-=1
        elif c25>2:
            c25-=3
        else:
            flag=1
            break
if(flag==0):
    print("YES")
else:
    print("NO")