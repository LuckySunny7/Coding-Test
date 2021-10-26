N = int(input())
a = list(map(int, input().split()))
M = 0

for i in range(N):
    a.sort(reverse=True)
    M += a[i]

print((M/a[0])*100/N)