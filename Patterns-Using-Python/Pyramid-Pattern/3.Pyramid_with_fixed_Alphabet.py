# Print the pyramid with fixed alphabet in every row
n = int(input("Enter the size of Pyramid : "))

for i in range(n): # n=3 -> 0,1,2
	print((' '*(n-i-1)) + (chr(65+i)+' ')*(i+1))
