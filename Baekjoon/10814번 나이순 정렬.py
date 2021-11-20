N = int(input())
arr=[]

for i in range(N):
    a, b = map(str,input().split())
    arr.append([int(a), i, b])

arr.sort()

for j in range(len(arr)):
    print("%d %s"%(arr[j][0],arr[j][2]))


