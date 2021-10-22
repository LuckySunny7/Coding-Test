s=input()
res=0
for x in s:
    if x.isdecimal():
        #isdecimal() : 숫자만 찾아줌
        res= res*10+int(x)
print(res)