#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body
def has_no_e():
	f = open("words.txt","r")
	count1 = 0
	count2=0
	for line in f:
		if 'e' not in line:
			count1+= 1
		count2+= 1
	print count1
	print count2
	x=(count1/float(count2))*100.0
	print ("percentage:" + str(x))
##############################################################################
def main():
	
	has_no_e()
	


if __name__ == '__main__':
    main()
