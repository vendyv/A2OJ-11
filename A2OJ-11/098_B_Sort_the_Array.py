"""
98 Sort the Array - https://codeforces.com/problemset/problem/451/B
"""
def main():

    n = int(input())
    arr = list(map(int, input().split()))

    l, r = 0, 0
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            l = i - 1
            break

    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            r = i + 1
            break

    r_arr = arr[l:r+1]

    check1 = arr[:l] + r_arr[::-1] + arr[r+1:]
    check2 = sorted(arr)

    if check1 == check2:
        print("yes")
        print(l+1, r+1)
    else:
        print("no")

main()    