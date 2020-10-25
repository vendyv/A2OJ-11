"""
58 Chat Room - https://codeforces.com/problemset/problem/58/A
"""
word = input()
hello = ['h', 'e', 'l', 'l', 'o']
for h in range(len(word)):
    if word[h] == "h":
        for e in range(h+1, len(word)):
            if word[e] == "e":
                for l in range(e+1, len(word)):
                    if word[l] == "l":
                        for l_l in range(l+1, len(word)):
                            if word[l_l] == "l":
                                for o in range(l_l + 1, len(word)):
                                    if word[o] == "o":
                                        print("YES")
                                        exit(0)
print("NO")
                