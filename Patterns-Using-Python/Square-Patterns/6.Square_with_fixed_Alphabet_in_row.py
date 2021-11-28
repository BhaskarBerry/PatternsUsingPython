#Print Square pattern with Alphabet symbols

n = int(input("Enter the size of the Square:"))

for i in range(n):
	print((chr(65+i)+" ")* n)

