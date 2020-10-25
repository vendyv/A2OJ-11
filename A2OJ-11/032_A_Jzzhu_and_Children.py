"""
32 Jzzhu and Children - https://codeforces.com/problemset/problem/450/A
"""
intt = int
mapp = map

n, m = mapp(intt, input().split())
import math
mc = math.ceil
maxx = max
lenn = len
rangee = range
# lambdaa = lambda
l = list(mapp(lambda x : mc(intt(x)/m), input().split()))
x = maxx(l)
for i in rangee(lenn(l)):
    if l[i] == x:
        temp = i
print(temp+1)