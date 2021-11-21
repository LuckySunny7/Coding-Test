N = int(input())
arr=[]
arr1=[]

for i in range(N):
    a = input()
    arr.append(a)

arr2=list(set(arr))
for j in arr2:
    if j not in arr1:
        arr1.append([len(j),j])

arr1.sort()
for k in range(len(arr1)):
    print(arr1[k][1])