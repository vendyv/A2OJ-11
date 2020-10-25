"""
82 Pythagorean Theorem II - https://codeforces.com/problemset/problem/304/A
"""
import math
 
l = int(input())
 
ans = 0
for n in range(1, 10000):
    for m in range(n + 1, 10000):
        if m > l:
            break
 
        if math.gcd(n, m) != 1 or (n%2 and m%2):
            continue
 
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
 
        if c > l or b > l:
            break
 
        for k in range(1, 10000):
            y = k * b
            z = k * c
            if y > l or z > l:
                break
            ans += 1
 
print(ans)
 