"""
78 Two bags of Potatoes - https://codeforces.com/problemset/problem/239/A
"""
y,k,n = map(int,input().split())
f=[]
x=k-y%k
while(x<n-y+1):
	f.append(str(x))
	x+=k
if len(f):
	print(' '.join(f))
else:
	print('-1')