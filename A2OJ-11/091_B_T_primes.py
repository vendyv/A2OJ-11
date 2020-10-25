"""
91 T Primes - https://codeforces.com/problemset/problem/230/B
"""
import math


def sieve(n):
    isPrime = [True]*(n+1)

    # isPrime[0] = False
    isPrime[1] = False
    i = 2
    while(i*i <= n):
        if isPrime[i] == True:
            for j in range(i*i, n + 1, i):
                isPrime[j] = False
        i += 1
    return isPrime

# pri = prime(1000000)

def main():
    n = int(input())
    l = list(map(int, input().split()))
    arr = sieve(1000000)
    for i in range(n):
        number = math.sqrt(l[i])
        if number.is_integer():
            if arr[int(number)]:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")

main()