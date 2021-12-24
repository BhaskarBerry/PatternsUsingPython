# Print diamond pattern with * symbol ,fixed numerical and alphabet symbol in every row.

n = int(input("Enter the size of the diamond:"))
print("========== Diamond pattern with stars====")
for i in range(n):# n = 3 ---> 0,1,2
	print(" "*(n-i-1) + "* "*(i+1))
for j in range(n-1): # n = 3 ---> 0,1
	print(" "*(j+1) + "* "*(n-1-j))

print("========== Diamond pattern with numbers====")
for i in range(n):# n = 3 ---> 0,1,2
	print(" "*(n-i-1) + (str(i+1)+" ")*(i+1))
for j in range(n-1): # n = 3 ---> 0,1
	print(" "*(j+1) + (str(n-1-j)+" ")*(n-1-j))

print("========== Diamond pattern with Alphabets====")
for i in range(n):# n = 3 ---> 0,1,2
	print(" "*(n-i-1) + (chr(65+i) +" ")*(i+1))
for j in range(n-1): # n = 3 ---> 0,1
	print(" "*(j+1) + (chr(64+n-1-j)+" ")*(n-1-j))