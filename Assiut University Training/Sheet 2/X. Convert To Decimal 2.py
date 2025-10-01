n = int(input())
# Counter
# c = 0 
x = ''
# Taking the inputs 
for i in range(n): 
    # inputs
    num = int(input())
    # Convert the number 
    # Bin = bin(num)
    for i in bin(num):
        if i == '1':
            # Count the number of 1
            # c+= 1  
            x += i 
    print(int(x,2))
    # c = 0 
    x = ''
# Testing 
# print(Bin)
# print(c)
# print(x)
