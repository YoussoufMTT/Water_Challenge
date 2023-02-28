import sys

if len(sys.argv) > 1 :
	
	print("Error ! No argument required.")
	exit() 
	

for n1 in range(0, 8) :
	
	for n2 in range(0, 9) :
	
		for n3 in range(0, 10) :
		
			if n1 != n2 and n2 != n3 and n1 != n3 :
				
				if n1 == 7 and n2 == 8 and n3 == 9 :
					
					print(n1,n2,n3,sep ="", end="\n")
					
				else :
					print(n1,n2,n3,sep ="", end=" ")