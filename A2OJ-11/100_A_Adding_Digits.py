"""
100 Adding Digits - https://codeforces.com/problemset/problem/260/A
"""
a, b, n = map(int, input().split())

for i in range(10):
    a = a*10 + i
    if a % b == 0:
        print(str(a) + "0"*(n-1))
        exit(0)
        break
    a = (a-i)//10 

print("-1")