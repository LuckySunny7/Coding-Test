N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
cnt = 0

for i in range(1,N+1):
    res = arr[-i]
    if K>=res:
        cnt = cnt + K//res
        K = K%res

print(cnt)