x = int(input())
l = list(map(int,input().split()))
print(min(l), l.index(min(l))+1)
