A,B = map(int,input().split())

def Big(A, B):
    while B>0:
        A,B = B , A%B
    return A

def small(A,B):
    return A*B//Big(A,B)

print(Big(A,B))
print(small(A,B))