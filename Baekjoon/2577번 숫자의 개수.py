A=int(input())
B=int(input())
C=int(input())

D = list(str(A*B*C))
numbers = [0,1,2,3,4,5,6,7,8,9]
cnt = [0]*10

for i in D:
    for j in numbers:
        if int(i) == j:
            cnt[j]+=1
for i in cnt:
    print(i)