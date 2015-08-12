#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body

def avoids(y):
	f=open("words.txt","r")
	count = 0
	#uc=y.upper()
	for line in f:
		uc=y.upper()
		for i in y :
			if i not in line and uc not in line:
				count+= 1
		
	print count

def combination():
	pass
##############################################################################
def main():
	#x=raw_input("Enter the string:")
	y=raw_input("Enter a string of forbidden letters:")
	#z=avoids(x,y)
	avoids(y)
	combination()

if __name__ == '__main__':
    main()
