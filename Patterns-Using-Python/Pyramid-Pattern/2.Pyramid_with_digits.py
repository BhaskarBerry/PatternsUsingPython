# Print the pyramid with numerical digits in every row
n = int(input("Enter the size of Pyramid : "))

for i in range(n): #0,1,2 for n=3
	print((' '*(n-i-1))+(str(i+1)+' ')*(i+1))