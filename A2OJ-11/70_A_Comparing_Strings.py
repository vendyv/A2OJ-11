"""
70 Comparing Strings - https://codeforces.com/problemset/problem/186/A
"""
string1 = list(input())
string2 = list(input())
one = len(string1)
two = len(string2)
if one != two:
    print("NO")
else:
    c = 0
    l = []
    for i in range(one):
        if string1[i] != string2[i]:
            c += 1
            l.append(i)

    if c != 2:
        print("NO")
    else:
        # print(string1)
        string1[l[0]], string1[l[1]] = string1[l[1]], string1[l[0]]
        # print(string1)
        # string1[l[1]] = string1[l[0]]
        # print(l)
        # string1 = string1.replace(l[0], l[1],1)
        # print(string1)
        # string1 = string1.replace(l[1], l[0],1)
        # print(string1)
        if "".join(string1) == "".join(string2):
            print("YES")
        else:
            print("NO")
