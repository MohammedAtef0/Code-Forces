# Taking the first number from the user the count of values 
x = int(input())
# Input the Values as integers, and map them to accept them in on line, finally cast them as a list
l = list(map(int,input().split()))
# Print the Final answer
print(abs(sum(l)))
