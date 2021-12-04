# Print the Inverted pyramid with star,digits and alphabet
n = int(input("Enter the size of Pyramid : "))

print("-----------The inverted Pyramid using star symbol-------------")
for i in range(n): # n= 3 -> 0,1,2
	print(' '*i+ '* '*(n-i))

print("-----------The inverted Pyramid using digit symbol-------------")
for i in range(n): # n= 3 -> 0,1,2
	print(' '*i+ (str(i+1)+ ' ')*(n-i))

print("-----------The inverted Pyramid using Alphabet symbol-------------")
for i in range(n): # n= 3 -> 0,1,2
	print(' '*i+ (chr(i+65)+ ' ')*(n-i))