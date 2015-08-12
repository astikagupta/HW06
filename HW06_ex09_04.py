#!/usr/bin/env python
# HW06_ex09_04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports

# Body

def uses_only(word,letters):
	count=0
	flag=False
	
	for i in word:
		if i in letters:
			flag=True
		else:
			flag=False
			break


	if flag==True:
		return True


##############################################################################
def main():
	fo=open("words.txt","r")
	count = 0
	for line in fo:
		word=line.strip()
		if uses_only(word,"acefhlo"):
			count+= 1
			print "the word is {0}".format(word)
	print count
   
    

if __name__ == '__main__':
    main()
