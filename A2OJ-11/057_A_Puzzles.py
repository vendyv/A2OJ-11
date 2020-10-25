"""
57 Puzzles - https://codeforces.com/problemset/problem/337/A
"""
n, m = map(int, input().split())
pieces = list(map(int, input().split()))
pieces.sort()
if n == m:
    print(pieces[-1] - pieces[0])
else:
    b = []
    for i in range(0, m-n+1):
        b.append(pieces[n+i-1] - pieces[i])
    print(min(b))