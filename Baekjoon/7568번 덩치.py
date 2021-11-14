N = int(input())
cnt = [1]*(N)
a = [0]*(N)
b = [0]*(N)

for i in range(N):
    a[i], b[i] = list(map(int, input().split()))

for j in range(N):
    for k in range(0,N):
        if a[j] > a[k] and b[j] > b[k]:
            cnt[k]+=1
        else:
            continue

for z in range(len(cnt)):
    print(cnt[z], end=' ')