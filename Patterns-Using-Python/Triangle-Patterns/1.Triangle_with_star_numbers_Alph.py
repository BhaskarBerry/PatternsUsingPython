# Print the Right angle triange with star symbol

n  = int(input("Enter the size of the Triangle:"))

for i in range(n): # n =3 -> 0,1,2
	print("* "*(i+1))

print("-------Print the Right angle triange with fixed number in a row----------")
for i in range(n): # n =3 -> 0,1,2
	print((str(i+1)+' ')*(i+1))

print("-------Print the Right angle triange with fixed Alphabet in a row----------")
for i in range(n): # n =3 -> 0,1,2
	print((chr(65+i)+' ')*(i+1))

print("-------2 way to achieve the same pattern--------")
for i in range(n):# n =3 -> 0,1,2
	for j in range(i+1):
		print(i+1, end = ' ')
	print()

