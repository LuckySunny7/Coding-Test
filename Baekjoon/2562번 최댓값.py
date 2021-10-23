res=0
cnt=0
a=[]

for i in range(9):
    a.append(int(input()))
    if a[i]>res:
        res=a[i]
        cnt = i+1

print(res,cnt, sep='\n')