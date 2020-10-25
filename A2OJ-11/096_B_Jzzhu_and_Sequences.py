"""
96 Jzzhu and Sequences - https://codeforces.com/problemset/problem/450/B
"""
import math
 
mo= 10e8+7
#print(mo)
f1,f2 = map(int,input().split(' '))
n = int(input())
li = [f1,f2,f2-f1,-f1,-f2,f1-f2]
#print(li)
n = math.trunc((n-1) % 6)
res = li[n] % mo
print(math.trunc(res))