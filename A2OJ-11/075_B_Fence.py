"""
75 Fence - https://codeforces.com/problemset/problem/363/B
"""
def main():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    s = sum(l[:k])
    min = s
    x=0
    for i in range(1,n-k+1):
        s = s - l[i-1] + l[k+i-1]
        # print(sum(l[x:i]))
        if s < min:
            min = s
            x = i
        # temp = sum(l[x:i])
        # if temp < s:
        #     s = temp
        #     a = x + 2
        #     # print(a)
        # x+=1
    # print(s)
    # index = s.index(min(s))
    return x+1
print(main()) 