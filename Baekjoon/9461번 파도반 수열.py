N = int(input())
arr = [0 for _ in range(101)]
arr[1] =1
arr[2] =1
arr[3] =1
for i in range(1,98):
    arr[i+3] = arr[i] + arr[i+1]

for i in range(N):
    a = int(input())
    print(arr[a])