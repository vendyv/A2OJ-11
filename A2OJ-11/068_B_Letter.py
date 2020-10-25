"""
68 Letter - https://codeforces.com/problemset/problem/43/B
"""
header = input().replace(" ", "")
text = input().replace(" ", "")

from collections import defaultdict, Counter
c = Counter()
d = Counter()
for i in header:
    c[i] += 1

for i in text:
    d[i] += 1
try:

    for k, v in d.items():
        if v > c[k]:
            print("NO")
            break
    else:
        print("YES")

except KeyError as e:
    print("NO")