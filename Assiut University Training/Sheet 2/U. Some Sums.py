# =====================================================================================================
N, A, B = map(int, input().split())
total_sum = 0
for i in range(1, N + 1):
    digit_sum = sum(int(digit) for digit in str(i))  # Calculate sum of digits of i
    if A <= digit_sum <= B:  # Check if the sum of digits is between A and B
        total_sum += i
print(total_sum)
# =====================================================================================================
