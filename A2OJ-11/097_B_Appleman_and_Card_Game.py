"""
97 Appleman and Card Game - https://codeforces.com/problemset/problem/462/B
"""
def main():
    n, k = map(int, input().split())
    cards = list(input())
    c = 0
    d = {}

    for i in range(n):
        letter = cards[i]
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1

    d = sorted(d.items(), key = lambda x: x[1], reverse=True)

    for key, value in d:
        if k > 0:
            if value > k:
                c += k ** 2
                break
            elif value == k:
                c += k ** 2
                break
            else:
                c += value ** 2 
                k -= value

    return(c)

print(main())