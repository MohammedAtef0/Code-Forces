n = int(input())
l = list(map(int,input().split()))
if l == l[::-1]:
    print('YES')
else:
    print('NO')
