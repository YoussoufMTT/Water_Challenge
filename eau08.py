import sys
from UF import *

def firstup(li) :

	li.pop(0)
	for word in li :
		
		wo = list(word)
		
		wo[0] = wo[0].upper()
		
		for ind in range(1, len(wo)) :
		
			wo[ind] = wo[ind].lower()
		
		if word == li[len(li) - 1] :
			
			print("".join(wo), end = "\n")
		
		else : 
			
			print("".join(wo), end = " ")
			
li = sys.argv	
onlychar(li)

firstup(li)