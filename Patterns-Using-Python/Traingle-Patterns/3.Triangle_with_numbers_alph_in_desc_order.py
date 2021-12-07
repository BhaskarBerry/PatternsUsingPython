# Print the Right angle triangle with numbers and alphabets in descending order
n  = int(input("Enter the size of the Triangle:"))

print("-------Print the Right angle triangle with number in descending order----------")
for i in range(n): # n =3 -> 0,1,2
	for j in range(i+1):
		print((n-j), end = ' ')
	print()

print("-------Print the Right angle triangle with alphabets in descending order----------")
for i in range(n): # n =3 -> 0,1,2
	for j in range(i+1):
		print(chr(64+n-j), end = ' ')
	print()


