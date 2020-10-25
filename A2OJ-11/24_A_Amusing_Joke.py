"""
24 Amusing Joke - https://codeforces.com/problemset/problem/141/A
"""
from collections import Counter
one, two, three = Counter(), Counter(), Counter()
for letters in input():
    one[letters] += 1
for letters in input():
    two[letters] += 1
for letters in input():
    three[letters] += 1
if one + two == three:
    print("YES")
else:
    print("NO")