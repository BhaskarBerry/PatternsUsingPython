# Print the Right angle triange with numbers and alphabets in ascending order
n  = int(input("Enter the size of the Triangle:"))

print("-------Print the Right angle triange with number in ascending row----------")
for i in range(n): # n =3 -> 0,1,2
	for j in range(i+1):
		print((j+1), end = ' ')
	print()

print("-------Print the Right angle triange with alphabets in ascending row----------")
for i in range(n): # n =3 -> 0,1,2
	for j in range(i+1):
		print(chr(65+j), end = ' ')
	print()


