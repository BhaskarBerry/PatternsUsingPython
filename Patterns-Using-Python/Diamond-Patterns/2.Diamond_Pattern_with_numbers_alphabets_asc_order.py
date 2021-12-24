# Print diamond pattern with digits and alphabets in ascending order

n = int(input("Enter the size of the diamond:"))
print("========== Diamond pattern with numbers in ascending order ====")
for i in range(n):# n = 3 ---> 0,1,2
	print(" "*(n-1-i), end = " ")
	for j in range(i+1):
		print(j+1, end = ' ')
	print()
for i in range(n-1):# 2--> 0,1
	print(" "*(i+1) , end = " ")
	for j in range(n-1-i):
		print(j+1, end = ' ')
	print()

print("========== Diamond pattern with Alphabets in ascending order ====")
for i in range(n):# n = 3 ---> 0,1,2
	print(" "*(n-1-i), end = " ")
	for j in range(i+1):
		print(chr(65+j), end = ' ')
	print()
for i in range(n-1):# 2--> 0,1
	print(" "*(i+1) , end = " ")
	for j in range(n-1-i):
		print(chr(65 + j), end = ' ')
	print()