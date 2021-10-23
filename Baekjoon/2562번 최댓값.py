res=0
cnt=0
a=[]

for i in range(9):
    a.append(int(input()))
    if a[i]>res:
        res=a[i]

print(res,i, sep='\n')