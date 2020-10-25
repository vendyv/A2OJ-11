"""
79 Unlucky Ticket - https://codeforces.com/problemset/problem/160/B
"""
input()
digits = list(map(int, list(input())))

first_half = digits[:len(digits)//2]
second_half = digits[len(digits)//2:]

first_half = sorted(first_half)
second_half = sorted(second_half)

flag = 0

if first_half[0] > second_half[0]:
    flag = 1
elif first_half[0] < second_half[0]:
    flag = 2
else:
    print("NO")
    exit()

for i in range(1, len(first_half)):
    if flag == 1:
        if first_half[i] <= second_half[i]:
            print("NO")
            exit()
    else:
        if first_half[i] >= second_half[i]:
            print("NO")
            exit()

print("YES")