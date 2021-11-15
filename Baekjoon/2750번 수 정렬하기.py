N = int(input())
a= []
c= []

for i in range(N):
    b=int(input())
    a.append(b)

for j in a:
    if j not in c:
        c.append(j)
d= sorted(c)
for k in range(N):
    print(d[k])