"""
25 Soft Drinking - https://codeforces.com/problemset/problem/151/A
"""
n, k, l, c, d, p , x, y = map(int, input().split())
print(min((k*l)//(n*x), (c*d)//n, (p)//(n*y)))