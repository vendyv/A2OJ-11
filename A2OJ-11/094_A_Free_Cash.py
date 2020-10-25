"""
94 Free Cash - https://codeforces.com/problemset/problem/237/A
"""
def main():
    n = int(input())
    d = {}
    for _ in range(n):
        x, y = map(int, input().split())
        if (x,y) not in d:
            d[(x,y)] = 1
        else:
            d[(x,y)] += 1
    dd = sorted(d.items(), key= lambda x: x[1], reverse= True)
    print (dd[0][1])
    
main()