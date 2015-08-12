import random
def func1():
	fo = open("text.txt","a")
	for i in range(10):
		x=random.randint(1,25)
		fo.write(str(x)+'\n')
		
	fo.close()
	
def func2():
	fo = open("roster.txt","r")
	f1 = open("result.txt", "a")
	f2 = open("result1.txt","a")
	count=0
	for line in fo:
		if 'e' in line or 'E' in line:
			print line
			f1.write(str(line) + "\n")
			count+= 1
	print ("{0} names contain the letter 'e' or 'E'".format(count))
	f1.write(str(count))
	# other way by copying the contents from 1 file to other
	fo.seek(0)
	old=fo.read()
	print old		 
	f2.write(old)
	
def main():
	func1()
	func2()
	
if __name__ == '__main__':
    main()
