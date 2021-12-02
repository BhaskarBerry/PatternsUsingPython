# Print the pyramid with star symbol
n = int(input("Enter the size of Pyramid : "))

for i in range(n): #0,1,2,3 for n=4
	print((' '*(n-i-1))+('* ')*(i+1))