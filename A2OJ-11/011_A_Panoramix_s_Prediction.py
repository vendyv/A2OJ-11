"""
11 - Panoramix's Prediction
"""
first, second = map(int, input().split())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
if second in primes and primes.index(second) - primes.index(first) == 1:
    print("YES")
else:
    print("NO")
