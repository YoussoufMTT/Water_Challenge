import sys
from UF import *


def onlynum(li) :
	
	for n in range(1, len(li)):
	
		if li[n].isdigit() == False :
			
			return False
			exit()
	else :
	
		return True
		
li = sys.argv
print(onlynum(li))