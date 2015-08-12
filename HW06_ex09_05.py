#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou:
#   - # of words that use all aeiouy:
##############################################################################
# Imports

# Body
def uses_all(word,letters):

	
	flag=False
	
	for i in letters:
		if i in word:
			flag=True
		else:
			flag=False
			break


	if flag==True:
		return True


##############################################################################
def main():
	fo = open("words.txt","r")
	count = 0
	for line in fo:
		word=line.strip()
		if uses_all(word,"aeiou"):
			count+= 1
			print ("the word is {0}".format(word))
	print count

if __name__ == '__main__':
    main()
