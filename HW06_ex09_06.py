#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports

# Body
def is_abecedarian(word):
    for i in range(len(word) - 1):
    	
    	count=0
        if word[i] > word[i + 1]:
            return False
        
    return True

##############################################################################
def main():
 	fo = open("words.txt","r")
	count = 0
	for line in fo:
		word=line.strip()
		if is_abecedarian(word):
			count+= 1
			print ("the word is {0}".format(word))
	print count
if __name__ == '__main__':
    main()
