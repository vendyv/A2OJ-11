"""
3 Queue at the School - https://codeforces.com/problemset/problem/266/B
"""
n, t = input().split()
intt = int
queue = input()
queue = list(queue)
# print(queue)
for _ in range(intt(t)):
    i = 0
    while i < intt(n)-1:
        if queue[i] == "B" and queue[i+1] == "G":
            queue[i], queue[i+1] = queue[i+1], queue[i] 
            i += 2
        else:
            i += 1
print("".join(queue))
