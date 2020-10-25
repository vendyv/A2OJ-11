"""
14 Arrival of the General - https://codeforces.com/problemset/problem/144/A
"""
input()
sol=list(map(int,input().split()))
swap=0 
maxm=sol.index(max(sol))

for i  in range(1,len(sol)+1):
    if sol[-i]==min(sol):
        minm=len(sol)-i
        break
if minm>maxm:
    swap=swap+((len(sol)-1)-minm)
    swap=swap+maxm
else:
    swap=swap+((len(sol)-1)-minm)
    swap=swap+(maxm-1)

print(swap)
                