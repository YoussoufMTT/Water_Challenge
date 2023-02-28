import sys
#from UF import *

def halfup(li) :

	li.pop(0)
	for word in li :
	
		wo = list(word)
			
		for ind in range(0, len(wo), 2) :
			
			wo[ind] = wo[ind].upper()
		
		if word == li[len(li) - 1] :
			
			print("".join(wo), end = "\n")
		
		else : 
			
			print("".join(wo), end = " ")
	
li = sys.argv	
#onlychar(li)

halfup(li)

	
