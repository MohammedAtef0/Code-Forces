def find_intersection(l1, r1, l2, r2):
    start = max(l1, l2)
    end = min(r1, r2)
    
    if start <= end:
        print(start, end)
    else:
        print(-1)
 
# Read input
l1, r1, l2, r2 = map(int, input().split())
 
# Find and print the intersection
find_intersection(l1, r1, l2, r2)
