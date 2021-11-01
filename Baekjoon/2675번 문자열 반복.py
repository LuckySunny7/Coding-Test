a = int(input())

for i in range(a):
    num, x = input().split()
    for j in x:
        print(j*int(num), end='')
    print()