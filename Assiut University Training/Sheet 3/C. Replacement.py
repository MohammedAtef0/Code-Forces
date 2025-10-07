x = int(input())
l = list(map(int,input().split()))
l2 = []
for i in l:
    if i > 0:
        l2.append(1)
    elif i < 0:
        l2.append(2)
    else:
        l2.append(i)
print(*l2)
