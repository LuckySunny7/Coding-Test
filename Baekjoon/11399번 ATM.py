N = int(input())
arr = list(map(int,input().split()))
cnt = [0]*N

arr.sort()
for j in range(N):
    cnt[j] = sum(arr[0:j+1])

print(sum(cnt))