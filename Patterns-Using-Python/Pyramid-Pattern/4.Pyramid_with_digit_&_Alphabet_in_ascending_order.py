# Print the pyramid with digits and alphabet in ascending order
n = int(input("Enter the size of Pyramid : "))

for i in range(n): # n=3 -> 0,1,2.
	print((' '* (n-i-1)),end='')
	for j in range(i+1):
		print(j+1, end=' ')
	print()

print("------Alphabets in Ascending order---------")
for i in range(n): # n=3 -> 0,1,2.
	print((' '* (n-i-1)),end='')
	for j in range(i+1):
		print(chr(65+j), end=' ')
	print()


