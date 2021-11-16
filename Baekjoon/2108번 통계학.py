import sys

N = int(sys.stdin.readline())
a=[]
d=[]

def most_cnt(x):
    e = set(x)
    if len(x) == 1:
        return(x[0])
    else:
        if len(x) == len(e):
            return(x[1])
        elif len(x) > len(e):
            for j in x:
                if j in e:
                    e.remove(j)
                else:
                    d.append(j)
            if len(d)>=2:
                return d[1]
            elif len(d) == 1:
                return d[0]

for i in range(N):
    b= int(input())
    if abs(b)>=4000:
        a.append(b)
        break
    else:
        a.append(b)

c = sorted(a)

print(round(sum(c)/len(c)))
print(c[N//2])
print(most_cnt(c))
print(max(c)-min(c))

