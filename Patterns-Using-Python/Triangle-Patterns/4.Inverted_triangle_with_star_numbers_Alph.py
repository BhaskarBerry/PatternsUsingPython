# Print the Inverted Right angle triangle with star symbol, numbers and alphabets 
n  = int(input("Enter the size of the Triangle:"))

print("==========Inverted Right Angle Triangle with Star Symbol==========")
for i in range(n):# when n = 3 -> 0,1,2
	print("* "* (n-i))

print("==========Inverted Right Angle Triangle with Numbers==========")
for i in range(n):# when n = 3 -> 0,1,2
	print((str(i+1)+ ' ')* (n-i))

print("==========Inverted Right Angle Triangle with Alphabets==========")
for i in range(n):# when n = 3 -> 0,1,2
	print((chr(65+i)+ ' ')* (n-i))
    