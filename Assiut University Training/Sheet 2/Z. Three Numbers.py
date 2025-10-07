# =====================================================================================================
K, S = map(int, input().split())  # Read K and S
count = 0
# Loop through possible values of X and Y
for X in range(K + 1):
    for Y in range(K + 1):
        Z = S - X - Y  # Calculate Z directly
        if 0 <= Z <= K:  # Check if Z is within the valid range
            count += 1
print(count)
# =====================================================================================================
