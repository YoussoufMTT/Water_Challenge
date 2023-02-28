import sys
from UF import *

def str_in_str(word1, word2) :

	ind2 = 0
	count = 0
	
	if len(word2) >= len(word1) :
		
		word2 = input("Enter a shorter word : ")
		
	for ind1 in range(len(word1)) :
		
		
		if ind2 == len(word2) :
			
			if count == ind2:
		
				return True
				
			else :
				
				return False
				
			
		if  word1[ind1] == word2[ind2] :
			
			for  i in range(ind1, len(word2)+ind1) :
					
					if  word1[i] == word2[ind2] :
							
							ind2+=1
							count+=1
																																					
					else :
							ind2 = 0
							count = 0
							
	
		

onlychar(sys.argv)
word1 = list(sys.argv[1])
word2 = list(sys.argv[2])

print(str_in_str(word1, word2))
