"""
18 I_love_%username% - https://codeforces.com/problemset/problem/155/A
"""
n = int(input())
scores = list(map(int, input().split()))
max_score, min_score = scores[0], scores[0]
c = 0
for score in range(1, n):
    # if scores[score] < scores[score - 1]
    if scores[score] > max_score:
        max_score = scores[score]
        c += 1
    elif scores[score] < min_score:
        min_score = scores[score]
        c += 1
print(c)

