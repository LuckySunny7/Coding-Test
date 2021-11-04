x = int(input())
an=1
n=1
plus = 6

if x == 1:
    n=0
else:
    while x>1:
        if x <= an+plus:
            break
        else:
            an = an +plus
            n+=1
            plus+=6
print(n+1)