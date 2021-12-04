# Print Inverted Pyramid with Digits and Alphabet in Ascending Order
n = int(input("Enter the size of Pyramid : "))

print("-----------The inverted Pyramid using Digits -------------")
for i in range(n): # n= 3 -> 0,1,2
	print(' '*i,end = '')
	for k in range(n-i):
		print(k + 1, end = ' ')
	print()

print("-----------The inverted Pyramid using Alphabets in asc order -------------")
for i in range(n): # n= 3 -> 0,1,2
	print(' '*i,end = '')
	for k in range(n-i):
		print(chr(65+ k), end = ' ')
	print()


