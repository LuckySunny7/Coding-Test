a=list(range(21))
for _ in range(10):
    s, e=map(int,input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

print(a[1:21])
#a.pop(0)를 이용하여도 0값을 제거할 수 있다.