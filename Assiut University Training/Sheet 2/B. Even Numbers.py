# =======================================================================================================================
# First Solution just one line python code 
# input() reads the integer N.
# range(2, N + 1, 2) generates all even numbers between 2 and N (inclusive).
# str(i) converts each even number to a string for printing.
# '\n'.join(...) joins all the even numbers with a newline between them.
# or -1 ensures that if there are no even numbers (i.e., when N is less than 2), it will print -1.
print('\n'.join(str(i) for i in range(2, int(input()) + 1, 2)) or -1)
# =======================================================================================================================
# Second Solution 
n = int(input())
if n > 1 :
    for i in range(1,n+1):
        if i % 2 == 0:
            print(i)
else:
    print(-1)
# =======================================================================================================================
# Third Solution 
n = int(input())
if n > 1:
    for i in range(2,n+1,2):
        print(i)
else:
    print(-1)
# =======================================================================================================================
