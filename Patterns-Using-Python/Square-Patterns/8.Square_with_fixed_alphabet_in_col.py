#Print Square pattern with fixed alphabet symbol in every column

n = int(input("Enter the size of the Square:"))

for i in range(n):
	for j in range(n):
		print((chr(65+j)+" "), end = " ")
	print()


