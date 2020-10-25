"""
45 Bicycle Chain - https://codeforces.com/problemset/problem/215/A
"""
n = int(input())

pedal = list(map(int, input().split()))

m = int(input())

rear  = list(map(int, input().split()))


pedal.sort()
rear.sort(reverse= True)

#calculate max ratio
ratio = int(0)
for i in range(m):
    for j in range(n):
        if rear[i] % pedal[j] == 0:
            if rear[i] / pedal[j] > ratio: ratio = int(rear[i] / pedal[j])
            break

count =0
for i in range(m):
    for j in range(n):
        if rear[i] / pedal[j] == ratio: count+=1

print(count)