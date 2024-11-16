
row = int(input("Enter the number of rows for your Number Floyd Triangle: "))
num = 1
for i in range(row): 
    for j in range(i + 1):
        print(num, end = "")
        num = num + 1
    print()