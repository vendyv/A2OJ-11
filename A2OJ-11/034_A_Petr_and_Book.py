"""
34 Petr and Book - https://codeforces.com/problemset/problem/139/A
"""
pages = int(input())
days = list(map(int, input().split()))
i = 0
while pages > 0:
    pages -= days[i%7]
    if pages <= 0:
        print(i%7 +1)
        break
    else:
        i += 1