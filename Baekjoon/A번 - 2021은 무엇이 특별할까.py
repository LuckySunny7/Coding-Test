import math
import sys

def is_prime_number(n):
    array = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]

N = int(sys.stdin.readline())
if N==1 or N==2:
    print(6)
else:
    arr = is_prime_number(N)
    ans = 0

    for k in range(len(is_prime_number(N))):
        if (N- arr[k] * arr[k + 1]) < 0:
            ans = arr[k] * arr[k+1]
            break

    print(ans)