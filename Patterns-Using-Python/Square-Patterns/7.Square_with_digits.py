#Print Square pattern with Digits

n = int(input("Enter the size of the Square:"))

for i in range(n): # 0,1,2
	for j in range(n): #0,1,2
		print(str(j+1), end = " ")
	print()



