a, b = map(int, input().split())
s = input()
if len(s) != a + b + 1:
    print("No")
elif s[a] != '-':
    print("No")
else:
    # Check left and right parts
    left = s[:a]
    right = s[a+1:]
    if left.isdigit() and right.isdigit():
        print("Yes")
    else:
        print("No")
