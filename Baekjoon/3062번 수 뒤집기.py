def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

T=int(input())

for i in range(T):
    a = int(input())
    M=reverse(a)
    N=reverse(M+a)
    if N == a+M:
        print("YES", sep='')
    else:
        print("NO", sep='')