"""
30 Effective Approach - https://codeforces.com/problemset/problem/227/B
"""
n = int(input())
l = list(map(int,input().split()))
m = int(input())
v=list(map(int,input().split()))
a,b=0,0
d = [0]*(n+1)
for i in range(n) :
	d[l[i]] = i
 
for q in v:
	a += d[q]+1
	b += n-d[q]
print(a,b)
 