#Print Square pattern with digits in descending order

n = int(input("Enter the size of the Square:"))

for i in range(n):
	print((str(n-i)+" ")* n)

print("-------------------------------------------")
for i in range(n):
	for j in range(n):
		print(n-j, end = " ")
	print()


