"""
74 Yaroslav and Permutations - https://codeforces.com/problemset/problem/296/A
"""
n = int(input())
a = [int(i) for i in input().split()]
 
for i in a:
    if a.count(i) * 2 > n + 1:
        print("NO")
        exit(0)
 
print("YES")