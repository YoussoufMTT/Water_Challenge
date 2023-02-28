import sys
#from UF import *

def minmax(a, b) :

	if a < b :
	
		for num in range(a+1, b) :
				
			print(num, end = " ")
	
	elif a > b :
	
		for num in range(b+1, a) :
			
			print(num, end = " ")
	
	else :
	
		print("Error, a and b equals !")


li = sys.argv		
#onlynum(li)
a = int(li[2])
b = int(li[3])

minmax(a, b)
