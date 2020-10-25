"""
53 String Task - https://codeforces.com/problemset/problem/118/A
"""string = input()
string = string.lower()
for i in string:
    if i == "a" or i =="e" or i == "i" or i =="o" or i == "u" or i == "y":
        # print(i)
        string = string.replace(i, "")
print("." + ".".join(string))