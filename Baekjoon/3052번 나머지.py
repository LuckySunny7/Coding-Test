b = [0]*42
cnt=0

for i in range(10):
    idx=0
    a = int(input())
    idx = a%42
    b[idx] +=1
for j in range(42):
    if b[j] >= 1:
        cnt+=1
print(cnt)
#set 함수를 쓰면 더 쉽게 찾을 수 있음.
#참고로 set 함수는 .append 해야함