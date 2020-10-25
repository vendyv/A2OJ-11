"""
38 Little Elephant and Rozdil - https://codeforces.com/problemset/problem/205/A
"""
n = int(input())
cities = list(map(int, input().split()))
m = min(cities)
if cities.count(min(cities)) > 1:
    print("Still Rozdil")
else:
    print(cities.index(m)+1)