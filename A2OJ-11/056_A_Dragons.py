"""
56 Dragons - https://codeforces.com/problemset/problem/230/A
"""
s=input().split()
b=[]
for i in range(int(s[1])):
    a=input().split()
    a=list(map(int,a))
    b.append(a)
b.sort()
for i in range(int(s[1])):
    if int(s[0])>b[i][0]:
        s[0]=int(s[0])+b[i][1]
    else:
        print('NO')
        break
    if i ==int(s[1])-1:
        if int(s[0])>b[i][0]:
            print('YES')