def Multply(arr):
    mult = 1
    for i in arr:
        mult *= i 
    return mult 
l = list(map(int, input().split()))
m = str(Multply(l))
print(m[-2],m[-1],sep='')
