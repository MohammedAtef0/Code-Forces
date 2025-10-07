x = int(input())
l = list(map(int,input().split()))
pos = int(input())
# print(x,l,pos)
t = 0 
for i in l:
    if pos == i:
        t = l.index(i)
        break 
    else:
        t = -1 
print(t)
        
