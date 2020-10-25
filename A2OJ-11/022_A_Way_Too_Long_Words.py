"""
22 Way Too Long Words - https://codeforces.com/problemset/problem/71/A
"""
for _ in range(int(input())):
    word = input()
    l = len(word)
    if l > 10:
        print(word[0] + str(l-2) + word[-1])
    else:
        print(word)
