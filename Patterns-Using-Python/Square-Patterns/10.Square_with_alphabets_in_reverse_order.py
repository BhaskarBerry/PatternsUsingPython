#Print Square pattern with alphabets in reverse order

n = int(input("Enter the size of the Square:"))

for i in range(n):
	print((chr(65+n-i-1)+" ")* n)

print("-------------------------------------------")
for i in range(n):
	for j in range(n):
		print(chr(65+n-j-1), end = " ")
	print()


