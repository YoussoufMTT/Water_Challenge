import sys
from UF import *

def firstind(li) :

	target = li[len(li) - 1]
	
	i = 0
	for ind in range(0, len(li) - 1) :
	
		if li[ind] == target :
		
			i+=1
			print(ind)
			exit()
			
	if i == 0: 
	
		print("Error.", "'",target,"'"," not found.")
		
li = sys.argv	

firstind(li)