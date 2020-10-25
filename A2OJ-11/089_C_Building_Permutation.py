"""
89 Building Permutation - https://codeforces.com/problemset/problem/285/C
"""
n = int(input())
l = list(map(int, input().split()))
l.sort()
moves = 0
for i in range(n):
    if l[i] != i+1:
        moves += abs(l[i] - i - 1)
print(moves)