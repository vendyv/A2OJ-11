"""
93 Flipping Game - https://codeforces.com/problemset/problem/327/A
"""
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(n):
        k = arr.count(1)
        for j in arr[i:]:
            if j == 1:
                k -= 1
            else:
                k += 1
            count = max(count, k)
    return(count)

print(main())