# =========================================================
# First Solution optimized
n = int(input())
a = list(map(int,input().split()))
print(*a[::-1])
# =========================================================
# Second Solution using built-in method "reverse"
x = int(input())
l = list(map(int,input().split()))
l.reverse()
print(*l)
# =========================================================
# Third Solution without using built-in methods
n = int(input())
a = list(map(int,input().split()))
for i in range(len(a)-1,-1,-1):
    print(a[i],end=' ')
# =========================================================
