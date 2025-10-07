# Inputs 
n = int(input())
a = list(map(int,input().split()))
# Find the index of each of the min and max 
Min = a.index(min(a))
Max = a.index(max(a))
# Replacing by declare the new values of the Min, Max in the list by swapping them
a[Min], a[Max] = a[Max], a[Min]
# Output
print(*a)
