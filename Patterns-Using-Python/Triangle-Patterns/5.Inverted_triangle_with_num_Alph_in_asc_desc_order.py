# Print the Inverted Right angle triangle with numbers and alphabets in asc and desc order
n  = int(input("Enter the size of the Triangle:"))

print("==========Inverted Right Angle Triangle with numbers in Asc order=========")
for i in range(n):# when n = 3 -> 0,1,2
	for j in range(n-i):
		print((j+1), end= ' ')
	print()

print("==========Inverted Right Angle Triangle with numbers in DESC order=========")
for i in range(n):# when n = 3 -> 0,1,2
	for j in range(n-i):
		print((n-j), end= ' ')
	print()

print("==========Inverted Right Angle Triangle with alphabet in Asc order=========")
for i in range(n):# when n = 3 -> 0,1,2
	for j in range(n-i):
		print(chr(65+j), end= ' ')
	print()

print("==========Inverted Right Angle Triangle with alphabet in DESC order=========")
for i in range(n):# when n = 3 -> 0,1,2
	for j in range(n-i):
		print(chr(64+n-j), end= ' ')
	print()