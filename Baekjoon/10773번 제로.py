K = int(input())
arr=[]

for i in range(K):
    a = int(input())
    arr.append(a)
    if a == 0:
        if len(arr) == 0:
            continue
        else:
            del arr[arr.index(0)-1]
            arr.remove(0)

print(sum(arr))