"""
5 Beautiful Year - https://codeforces.com/problemset/problem/271/A
"""
for year in range(int(input())+1, 9013):
    modified_year = set(list(str(year)))
    if len(modified_year) == 4:
        print(year)
        break
