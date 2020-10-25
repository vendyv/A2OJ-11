"""
40 Jeff and Digits - https://codeforces.com/problemset/problem/352/A
"""
n = int(input())
cards = list(map(int, input().split()))
fives = cards.count(5)
zeros = cards.count(0)
if zeros > 0 and fives > 8:
    f = [5]*(fives - fives%9)
    z = [0]*zeros
    # print(z)
    f.extend(z)
    # print(f)
    print('5'*(fives - fives%9) + '0'*(zeros))
    # s = "".join(list(map(int, f)))
    # print(s)
    # print("".join(f))
elif zeros > 0:
    print("0")
else:
    print("-1")