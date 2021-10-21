# 회문 문자열 : 앞으로 읽든, 뒤로 읽든 동일한 문자열
N = int(input())
for i in range(N):
    s=input()
    #들어오는 문자열을 전부 대문자로 바꿈
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

# s==s[::1]을 이용하면 더욱 쉽게 코드를 짤 수 있음.