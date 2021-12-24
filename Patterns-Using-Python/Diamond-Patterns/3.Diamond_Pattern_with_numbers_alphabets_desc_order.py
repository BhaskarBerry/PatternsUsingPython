# Print diamond pattern with digits and alphabets in descending order

n = int(input("Enter the size of the diamond:"))
print("========== Diamond pattern with numbers in descending order ====")
for i in range(n):# n = 3 ---> 0,1,2
	print(" "*(n-1-i), end = " ")
	for j in range(i+1):
		print((n-j), end = ' ')
	print()
for i in range(n-1):# 2--> 0,1
	print(" "*(i+1) , end = " ")
	for j in range(n-1-i):
		print((n-j), end = ' ')
	print()

print("========== Diamond pattern with Alphabets in descending order ====")
for i in range(n):# n = 3 ---> 0,1,2
	print(" "*(n-1-i), end = " ")
	for j in range(i+1):
		print(chr(64+n-j), end = ' ')
	print()
for i in range(n-1):# 2--> 0,1
	print(" "*(i+1) , end = " ")
	for j in range(n-1-i):
		print(chr(64+n - j), end = ' ')
	print()