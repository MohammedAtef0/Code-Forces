n = int(input())
a = 0
b = 1
# Special case for n = 1
if n == 1:
    print(a)
# Special case for n = 2
elif n == 2:
    print(a, b)
else:
    # Print the first two numbers
    print(a, b, end=' ')
    # Generate the rest of the Fibonacci sequence
    for i in range(2, n):
        c = a + b
        print(c, end=' ')
        a, b = b, c
