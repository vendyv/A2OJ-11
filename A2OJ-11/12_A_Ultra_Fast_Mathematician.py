"""
12 Ultra Fast Mathematician - https://codeforces.com/problemset/problem/61/A    
"""
n1 = input()
n2 = input()
sum = []
for i in range(len(n1)):
    if n1[i] == '1' and n2[i] == '1' or n1[i] == '0' and n2[i] == '0':
        sum.append('0')
    else:
        sum.append('1')
 
print(''.join(sum))