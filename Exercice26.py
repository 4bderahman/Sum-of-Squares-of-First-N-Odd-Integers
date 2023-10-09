# asking the use to inter the integer
n = int(input("Enter an integer n: "))

# variables
s = 0
Impair = 1

# Loop through the first n odd numbers
for i in range(1, n + 1):
    s = s + Impair ** 2
    Impair = Impair + 2

# Print the result 
print("the sum of the squares of the first", n, "odd integers is:",s)
