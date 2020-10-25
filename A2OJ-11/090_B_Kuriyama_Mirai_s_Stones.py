"""
90 Kuriyama Mirai's Stones - https://codeforces.com/problemset/problem/433/B
"""
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    s_arr = sorted(arr)

    cum_arr1, cum_arr2 = [], []
    sum1, sum2 = 0, 0

    for i in range(1, n):
        arr[i] += arr[i-1]
        s_arr[i] += s_arr[i-1]
    arr.insert(0,0)
    s_arr.insert(0,0)

    m = int(input())
    for _ in range(m):
        t, l, r = map(int, input().split())
        if t == 1:
            print(arr[r] - arr[l-1])
        elif t == 2:
            print(s_arr[r] - s_arr[l-1])
            # print(sum(s_arr[l-1:r]))

main()