rows = int(input("Enter the rows of the triangle: "))

for i in range(1, rows + 1): 
    print(" " * (rows - i), end="")
    print("*" * i)
