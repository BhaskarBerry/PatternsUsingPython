# Print Hollow diamond pattern with * symbol.

n = int(input("Enter the size of the Diamond:"))

print("==========Hollow Diamond pattern with stars====")
for i in range(1, n+1):# n = 3 ---> 1,2, 3
	for j in range(1, n-i+1):
		print(" ", end="")
	for j in range(1, 2*i):
		if j==1 or j==2*i-1:
			print("*", end="")
		else:
			print(" ", end="")
	print()

for i in range(n-1,0,-1):
	for j in range(1, n-i+1):
		print(" ", end="")
	for j in range(1, 2*i):
		if j==1 or j==2*i-1:
			print("*", end="")
		else:
			print(" ", end="")
	print()
