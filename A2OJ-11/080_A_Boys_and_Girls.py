"""
80 Boys and Girls - https://codeforces.com/problemset/problem/253/A
"""
from sys import stdin,stdout
stdin=open('input.txt','r')
stdout=open('output.txt','w')
print=stdout.write
input = lambda: stdin.readline().rstrip("\r\n")
from collections import deque as que, defaultdict as vector
from heapq import*
inin = lambda: int(input())
inar = lambda: list(map(int,input().split()))
from types import GeneratorType
'''def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack: break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc'''
 
 
Testcase=1
for _ in range(Testcase):
	n,m=inar()
	if n==m:
		print('BG'*n)
	elif n>m:
		print('BG'*m+'B'*(n-m))
	else:
		print('GB'*n+'G'*(m-n))