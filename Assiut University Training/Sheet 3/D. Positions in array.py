n = int(input())
l = list(map(int,input().split()))
for i in range(len(l)) :
    if l[i] <= 10:
        print('A[',i,'] = ',l[i],sep='')
