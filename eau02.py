import sys

if len(sys.argv) > 1 :
	
	print("Error ! No argument accepted.")
	exit()

for n1 in range(0, 10) :
	
	for n2 in range(0, 10) :
	
		for n3 in range(0, 10) :
			
			for n4 in range(0, 10) :
			
				print(n1,n2, sep = "", end=" ")
				print(n3,n4, sep = "", end=" ; ")