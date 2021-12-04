# Print Inverted Pyramid with Digits and Alphabet in Descending Order
n = int(input("Enter the size of Pyramid : "))

print("----------Numbers in Desc order ----------")
for i in range(n): # when n = 3-> 0,1,2
	print(' '*i, end= '')
	for j in range(n-i):
		print(n-j, end = ' ')
	print()


print("----------Alphabets in Desc order ----------")
for i in range(n): # when n = 3-> 0,1,2
	print(' '*i, end= '')
	for j in range(n-i):
		print(chr(64+n-j), end = ' ')
	print()



