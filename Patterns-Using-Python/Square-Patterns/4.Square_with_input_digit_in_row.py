#Print Square pattern with input number fixed for every row

n = int(input("Enter the size of the Square:"))

for i in range(n): #0,1,2
	print((str(i+1)+' ') * n)
