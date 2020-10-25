""" 
54 - Little Elephant and Function - https://codeforces.com/problemset/problem/221/A
"""
l=[int(i) for i in range(1,int(input())+1)]
p=[l[-1]]+l[:-1]
print(*p)