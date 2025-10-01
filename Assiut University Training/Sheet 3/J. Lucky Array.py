n = int(input())
a = list(map(int,input().split()))
if a.count(min(a)) % 2 != 0 :
    print("Lucky")
else:
    print("Unlucky")
