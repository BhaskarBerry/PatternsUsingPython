# Print the pyramid with digits and alphabet in Descending order
n = int(input("Enter the size of Pyramid : "))

for i in range(n): # n=3 -> 0,1,2.
	print((' '* (n-i-1)),end='')
	for j in range(i+1):
		print(n-j, end=' ')
	print()

print("------Alphabets in Reverse order---------")
for i in range(n): # n=3 -> 0,1,2.
	print((' '* (n-i-1)),end='')
	for j in range(i+1):
		print(chr(64+n-j), end=' ')
	print()


